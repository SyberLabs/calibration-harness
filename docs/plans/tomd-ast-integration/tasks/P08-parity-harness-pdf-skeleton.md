# P08 Parity harness, ratchet, PDF skeleton, bridge

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 2 | P05, P06, P07 | none (W3 starts after this) | L | high |

## Goal

Stand up the machinery every later task relies on: the oracle that diffs legacy vs AST
output, the RawBlock ratchet, the parser protocol, a PDF adapter that maps every
section to a `RawBlock`, and the bridge that re-applies the legacy string passes. After
this PR the dark PDF path already matches legacy byte for byte, with all content as
`RawBlock`. If it is too big, split into P08a (harness + emit pre-pass extraction) and
P08b (adapter + bridge) and report.

## Read first

- `lib/pdf/pipeline.py`: `run_pipeline` end (line 2663-2692: `drop_leaked_toc_entries`,
  `emit_markdown`, `emit_prompts`, `PipelineResult`), `PipelineResult` (1773)
- `lib/pdf/emit.py` `emit_markdown` in full (line 1176): the pre-passes
  (`_assign_emdash_nesting`, the cross-page table fold), the section loop, the string
  pipeline (`dedup_paragraphs`, `strip_redundant_body_meta`, `strip_orphan_toc_list`,
  TABLE_CSS injection, `apply_strip_leading_h1`, glyph marker), and what it mutates
- `tests/test_pdf_golden.py` and `tests/test_html_golden.py` (how the corpus is
  discovered: `fixtures/golden/stems/*.txt`, `sources/` vs flat layout, `_GOLDEN_STEMS`)
- `api.py` `convert_paper_full` (the API-level pipeline: `_normalize_front_matter`,
  `_strip_body_metadata_text`, `strip_freeform_metadata_lines`, H1, `_strip_toc`)
- `README.md` Section 2 of this plan

## Change

1. **Pre-pass extraction.** `emit_markdown` mutates its input: `_assign_emdash_nesting`
   sets `indent_level`; the table fold does `prev.columns.extend(...)` and drops the
   continuation only from a local list. Because `PipelineResult.sections` is the
   original list, a second fold double-counts rows. Extract
   `fold_table_continuations(sections) -> list[Section]` and make
   `assign_emdash_nesting` public; make both idempotent; call them from `run_pipeline`
   before `emit_markdown` and store the folded list in `result.sections`; keep
   `emit_markdown` calling them (idempotent, so tests that call it directly still
   work). Verify by running the full golden suite: output must not change.
2. **Parser protocol.** `tomd/parsers/__init__.py` (re-exports only),
   `parsers/base.py`: `DocumentParser` Protocol
   (`parse(path: Path, options) -> PaperDocument`).
3. **PDF adapter.** `parsers/pdf/adapter.py`: `sections_to_document(result:
   PipelineResult) -> PaperDocument`. Dispatch table `ADAPTERS: dict[SectionKind,
   Callable]` whose default maps a section to
   `RawBlock(legacy_render_section(sec), origin=f"pdf:{kind}[:{strategy}]")` using the
   existing `emit._render_section_md` (and the same skip rules as `emit_markdown`:
   empty renders and bare-`#` headings are dropped). UNCERTAIN sections are the one
   exception: map them to `UncertainElement` (P06) filling `mupdf_text`, `spatial_text`,
   `page`, `text`, and the 200-character `context_before`/`context_after` exactly as
   `emit_prompts` derives them, so the writer computes the marker line numbers.
   Metadata comes from `result.metadata` via `PaperMetadata.from_dict`;
   images, skip state, and `Diagnostics` come from `result` (P05 types).
4. **Bridge.** `parsers/legacy_bridge.py`: `render_pdf(document) -> str` =
   `MarkdownWriter` body, then the legacy string chain in the exact `emit_markdown` order
   (`dedup_paragraphs`, `strip_redundant_body_meta`, `strip_orphan_toc_list`, TABLE_CSS
   injection, `apply_strip_leading_h1(md, title)`), then the P05 trailer markers (glyph
   marker last). Isolate the chain in one list of named steps so each pass PR in W4
   removes one entry. The writer (P06) computes uncertain-marker line numbers from the
   pre-pass body, as `emit_markdown` does.
5. **Entry point.** `tomd/parsers/pdf/__init__.py` exports `convert_pdf_dark(path) ->
   str` (run `run_pipeline`, adapt, bridge). Not wired into `api`.
6. **Parity tests** `tests/parity/` (`__init__.py`, `conftest.py`, `corpus.py`,
   `test_pdf_parity.py`): corpus = the PDF stems used by `test_pdf_golden.py` plus the
   synth fixtures and `p2583r3-gold-standard.pdf`; reuse the discovery logic, do not
   copy the stem list. Two assertions per paper: converter level
   (`run_pipeline(path).md == convert_pdf_dark(path)`) and API level (feed both through
   the API-level legacy chain with a fixed `meta`). On failure print a unified diff head.
7. **Ratchet.** `tests/parity/rawblock_allowlist.py` (a `frozenset` of origins) and
   `test_rawblock_ratchet.py` asserting the set of origins emitted over the corpus equals
   the allow-list exactly. Seed it with whatever the skeleton emits.
8. **Corpus script.** `packages/tomd/scripts/parity_corpus.py`:
   takes `--data-dir` (default `$WG21_DATA_DIR`), runs the same two assertions over every
   staged paper, writes a summary and the first diff per failure. Uses `logging`, writes
   output as the existing scripts in `packages/tomd/scripts/` do (`print` is banned
   inside packages, not necessarily in scripts; match the neighbors).

## Do not

- Change any golden or snapshot. Output of `run_pipeline` must be byte-unchanged.
- Convert any family to real nodes (later tasks). Do not wire the dark path into `api`.

## Tests

The parity tests are the tests. Plus: unit tests for `fold_table_continuations` and
`assign_emdash_nesting` idempotence (calling twice equals once).

## Acceptance

Checklist green including `tests/parity`; `tests/test_pdf_golden.py` unchanged and green;
ratchet test passes with the seeded allow-list.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Corpus size (papers) at converter level / API level:
Initial ratchet allow-list (paste):
Anything in emit_markdown that mutates input besides the two pre-passes:
Known divergences found:
Open questions:
```
