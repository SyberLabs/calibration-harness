# tomd: integrating the AST domain and Writer into the converters

Status: draft for review. Nothing here is implemented.

## 1. Where we are

#459 (domain AST), #460 (Markdown writer), #461 (writer tests) are merged. Nothing
in `api.py`, `lib/pdf`, or `lib/html` imports `tomd.domain` or `tomd.writers`. Both
converters still produce Markdown directly:

```
PDF : pages -> ... -> list[lib.pdf.types.Section] -> emit_markdown() -> str
HTML: soup  -> render.py (DOM -> str, no IR)                          -> str
both: str -> api.py regex passes (front matter, TOC, H1, metadata tables) -> str
```

Target:

```
source -> Parser(PDF|HTML) -> PaperDocument -> AST passes -> Writer -> str
                                                        \-> prompts / diagnostics
```

The PDF side already has an IR (`Section`), so its parser is an adapter plus an
`emit` split. The HTML side has none, so `render.py` must be rewritten to build
elements instead of strings. That asymmetry drives the sequencing in section 5.

## 2. Gap analysis

Each gap is something a real converter produces today that the merged model
cannot represent, or represents in a way that contradicts current behavior.

### Blocking (parser output cannot be expressed)

**G1. Lists are flat.** `ListBlock.items: list[ListItem]`, item = spans only.
Real output has nesting (`Section.indent_level`, HTML nested `<ul>/<ol>`),
per-item continuation blocks (HTML `_render_list_item`: code, paragraphs,
sub-lists under an item), preserved ordinal markers (`b)`, `(a)`, PDF keeps them),
and non-1 start numbers. Fix: `ListItem.children: list[BlockElement]` for
continuation blocks, nested `ListBlock` as a child, `ListItem.marker: str | None`
for preserved ordinals, `ListBlock.start: int = 1`.

**G2. Wording is a string.** `WordingBlock.content: str` discards the
`ins`/`del` roles the whole wording feature exists to carry. PDF wording has three
shapes (`wording_emit.py`): wholesale fenced code, a fenced code diff with inline
`<ins>/<del>` inside the fence, and prose with inline tags. Also the
uniform-role cleanup (`wording_cleanup.strip_redundant_tags`, shared policy in
`wording_policy.py`) needs the role on the block. Fix: `WordingBlock(role,
children: list[BlockElement])`, and a `CodeBlock` that can carry spans (or a
`CodeDiffBlock`) so a code diff keeps its roles. `strip_redundant_tags` becomes an
AST pass that unwraps spans when the block role already implies them.

**G3. Blockquote is a string.** HTML `example-block/note-block/bug-block` and
`<blockquote>` hold multiple blocks (paragraphs, code, lists). Fix:
`Blockquote.children: list[BlockElement]`.

**G4. Uncertain regions lose their data.** `UncertainElement(prompt, raw_content)`
cannot reproduce current behavior: the PDF emits the MuPDF text, and the reconcile
prompt needs both `mupdf_text` and `spatial_text`, the page number, and the
neighboring confident sections (`emit_prompts`). The merged writer also emits
`<!-- tomd:uncertain prompt="..." -->`, but the real marker is
`<!-- tomd:uncertain:L{start}-L{end} -->` with line numbers that only the writer
can compute at write time. Fix: `UncertainElement(mupdf_text, spatial_text,
page)`; the writer computes line spans; `emit_prompts` becomes a function over the
AST (`build_reconcile_prompts(doc)`); wording/HTML problem prompts live on
`PaperDocument.diagnostics`.

**G5. Images.** The writer emits `![alt](file)` for `ImageElement`. #408 forbids
image syntax in Markdown: the PDF renders an image as an italic caption only when
`caption_body_dropped`, otherwise as nothing; HTML drops `<img>`. Domain
`ExtractedImage` lacks `page`, `index_on_page`, `ext`, `bbox`, `xref`,
`sub_captions`, `caption_body_dropped`, and `ImageRef` is unused. Fix: delete
`ImageElement` and `ImageRef`; the converter keeps sidecar records on
`PaperDocument.images` (one `ExtractedImage`, superset of today's fields, shared
by PDF and HTML) and emits captions as ordinary `Paragraph(Emphasis(...))`
elements. The sub-caption and caption-escape rules (`_escape_italic_text`) move to
the writer's escaping policy (G9).

**G6. Tables.** Several mismatches:
- `TableStrategy.MIXED_HTML` contradicts the decision that tomd never emits HTML
  tables (see memory: tomd-no-html-tables). The writer ignores the strategy and
  always writes a pipe table, and a test asserts `<table` never appears.
- The target strategy `CODE_BLOCKS` (side-by-side fenced blocks, today
  `_render_code_comparison`, currently unreachable) does not exist in the domain.
  The merged writer renders a `CodeCell` as `` `line`<br>`line` `` inside a pipe
  cell, which is the lossy form that decision rejects. The Tony Table fixture
  (`tony_table.md`) locks in that form.
- Domain `TableKind` (STANDARD, TONY_TABLE, POLL_TABLE, ...) does not match
  `lib/pdf/table.py` (CLEAN_MATRIX, INLINE_GRID, PROSE_TABLE, CODE_COMPARISON,
  SPEC_TABLE, KEY_VALUE, BIBLIOGRAPHY, NB_BALLOT, FALSE_POSITIVE). `FALSE_POSITIVE`
  / strategy `SKIP` is not a table at all: the parser should emit paragraphs.
- `rowspan`/`colspan` exist on `Cell` but a pipe table cannot express them; HTML
  denormalizes them (`_denormalize_table`). Decide: the parser denormalizes, and the
  AST drops span attributes (YAGNI) or keeps them only for a future writer.
- Cross-page `table_continuation` is folded in `emit_markdown`; it must be folded
  in the parser.
- Header-cell bold suppression and `_flatten_cell` (soft-wrap collapse) are
  conversion rules, not writer rules.

### Cross-cutting (will cause drift, byte diffs, or duplicated logic)

**G7. Duplicated definitions.** `FRONT_MATTER_ORDER` now exists in
`lib/metadata_yaml/format.py` (declared the single source of truth),
`domain/metadata.py`, and is re-used by `writers/markdown/front_matter.py`, which
re-implements `format_front_matter` (`_yaml_escape`, `_yaml_value`, intent
inference). Also duplicated: `SkipReason` (domain values `empty_content`,... vs
`lib/pdf/types.py` values `"empty pdf"`,... which `cli/jobs.py` maps), the
`ExtractedImage` dataclass (two shapes), `ConvertedPaper` (domain vs `api.py`, with
different fields: the api one carries `prompts`, `intent`, counts, truncation),
the TOC and metadata-table normalizers (`api.py` and `writers/markdown/
normalizers.py`, near-copy), and `_format_code_span` (`spans.py` and `tables.py`).
Fix: one definition of each; the writer calls `format_front_matter`.

**G8. Document-level diagnostics have no home.** Trailing markers appended by
`emit_markdown`: image truncation, vector-extraction-uncertain, glyph
placeholders (count taken from the finished body). Plus `intent`, `source_image_count`,
raster/vector counts, `prompts`. Fix: a typed `PaperDocument.diagnostics`
(dataclass, not a dict) and writer-owned marker rendering.

**G9. Escaping is not in the writer.** `TextSpan` is written raw. Today escaping is
scattered: `escape_leading_atx` and `normalize_whitespace` (PDF cleanup),
`_escape_italic_text`, pipe escaping in cells (HTML), `_escape_wording_text`. The
writer must be the single escaping point (it knows the context: heading, list
item, italic wrapper, cell, code), but parsers must hand it unescaped text. Needs
characterization tests against real papers; this is the likeliest source of byte
drift.

**G10. Markdown-string normalizers have no AST form.** `dedup_paragraphs`,
`strip_redundant_body_meta`, `strip_orphan_toc_list`, `strip_freeform_metadata_lines`,
`strip_toc`, `strip_body_metadata_text`, `apply_strip_leading_h1`. The merged writer
only runs them in the "hybrid body string" branch (`PaperDocument.body`). That
branch is a bridge, not a destination. Each pass becomes
`def pass(doc: PaperDocument) -> PaperDocument` operating on elements. `dedup_paragraphs`
compares rendered text, so it needs a stable text projection (`BlockElement.text`
exists; verify it matches).

**G11. Provenance.** `Section` carries `page_num`, `confidence`, `font_size` and the
CLAUDE.md rule is "discard nothing". Used by `annotate=True` highlight preview and
by structure debugging. Fix: optional `provenance: Provenance | None` on
`BlockElement` (page, confidence). Writers ignore it; a debug writer can use it.

**G12. Smaller items.**
- `Heading.id` renders `{#id}`; neither converter emits anchors today. Either parsers
  start producing them (output change) or drop the field until needed.
- `wording_tags` option (`<u>`, `~~` alternative). No converter uses it. Remove
  unless a consumer exists (YAGNI); if kept, make it a constructor argument.
- `PaperMetadata.audience` / `reply_to` are `list[str] | str`. Keep: legacy renders a string as a scalar and a list as a YAML list, so collapsing changes bytes. Revisit as a behavior change.
- PDF merges consecutive monospace spans into one code span; the AST should have a
  span-normalization step (merge adjacent same-type spans) so parsers and writer
  agree.
- `LineBreakSpan` writes `<br>`; HTML inline uses `\n`. Define the rule.
- `Link` scheme allowlist (`ALLOWED_LINK_SCHEMES`) is a parser rule; the writer
  should not trust that and should also refuse non-allowlisted URLs.
- Name clash: `lib.pdf.types.Span` (font run) vs `domain.span.Span` (semantic node).
  Keep both; import with qualified names in the adapter.
- Merged files carry the license header but not the author-attributed copyright line
  required for new files.

## 3. The `meta` argument

Confirmed: the parameter is overloaded and the two uses speak different dialects.

- Structured branch: `meta` **replaces** `document.metadata` outright (no merge).
- Body-string branch: `meta` is a **fallback source** in the mailing-row dialect
  (`paper_id`, `document_date`, `subgroup`, `target_group`, `authors`), with `document`
  authoritative over the source (SD-7 D-number rule), and a bare-name `reply-to`
  not blocking fallback.
- Callers cannot tell which applies, and the Protocol hides both.

Decision (recommended):

1. `DocumentWriter.write(document: PaperDocument) -> str`. The writer renders exactly
   `document.metadata`. No `meta`.
2. Mailing fallback becomes a pure resolve step before writing:
   `resolve_metadata(parsed: PaperMetadata, mailing: MailingRecord) -> PaperMetadata`,
   living in the api layer (the only layer that knows about the mailing row). It
   owns the mapping table (`_FALLBACK_KEY_MAP`), the override set (`document`),
   `sanitize_metadata`, and intent inference from `Info:` / `Ask:` titles (moved out of
   the writer).
3. `MailingRecord` is a small typed dataclass built once inside the API from the
   existing `meta` dict (the public signature and the CLI are unchanged).
4. `PaperDocument.paper_id` is the mailing id; `metadata.document` is the
   resolved front-matter value. Make the relationship explicit in the resolve step.

Rejected: keep `meta` but type it (still two meanings); push fallback into
`PaperMetadata.from_dict` (domain would learn the mailing schema).

## 4. Target architecture

```
tomd/domain/        pure data: PaperDocument, elements, spans, tables, metadata
tomd/parsers/       DocumentParser protocol; pdf/ (adapter over lib.pdf), html/
tomd/passes/        AST transforms (toc, h1, dedup, metadata tables, wording cleanup)
tomd/writers/       DocumentWriter protocol; markdown/ (escaping, markers, front matter)
tomd/api.py         convert_paper_full = parse -> resolve_metadata -> passes -> write
```

`lib/pdf` and `lib/html` keep their extraction and classification logic; only their
final stage changes. `PipelineResult` gains `document: PaperDocument` and keeps
`sections` for QA scoring during the transition.

## 5. Migration plan

Superseded by `README.md` (mechanism, graph, session recipes) and `tasks/`. In short:
dark path per format, a temporary `RawBlock` element so every PR is byte-identical, a
ratchet test, a parity gate, per-format cutover PRs, then ordered AST passes, then
deletion of the legacy paths.

## 6. Risks

- Escaping parity (G9) and `dedup_paragraphs` semantics: highest byte-drift risk.
- Uncertain-marker line numbers must match the old running `line_num` arithmetic.
- HTML rewrite size; mitigate with the Phase 0 oracle and per-function migration.
- Concurrent in-flight PRs (whisker #474, golden-ideal PRs) read Markdown output; the
  byte-identical gate protects them.
- `lib/pdf/types.py::SkipReason` values are matched in `cli/jobs.py`; unify with care.

## 7. Decisions (made)

1. **Table sequencing: independent.** Integration does not wait for no-HTML-tables.
   Tables whose strategy is `HTML_TABLE` stay opaque `RawBlock` elements through the
   integration. The no-HTML-tables PR converts them to real `Table` elements
   (strategy `PIPE` or `CODE_BLOCKS`) and deletes the last `RawBlock`s. Whichever
   lands first, the other adapts; there is no ordering constraint.
2. **PDF first, then HTML.** `Section` is already an IR; HTML needs a rewrite.
3. **Removed from the AST:** `wording_tags`, `Heading.id`, `rowspan`/`colspan`,
   `TableKind` (classification is a parser concern; the writer needs only the
   strategy), `TableStrategy.MIXED_HTML`, `ImageElement`, `ImageRef`. Each is
   reversible when a real consumer exists.
4. **`MailingRecord` lives in `tomd`** (`tomd/resolve.py`, next to
   `resolve_metadata`). The API keeps taking a `meta` dict and builds it internally.
5. **No env-var switch.** See the PR plan: the new path is dark, exercised by a
   parity test, and enabled per format by a one-line dispatch change.

How the work is split into PRs: `README.md` and `tasks/`.
