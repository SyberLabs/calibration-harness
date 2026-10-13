# P05 Unify shared types, add `Diagnostics`, render trailer markers

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 1 | P02 | P03, P04, P06, P07 | M | medium |

## Goal

One definition each of `SkipReason`, `ExtractedImage`, and the per-paper diagnostics.
Give `PaperDocument` a typed `diagnostics` field and let the writer render the trailing
HTML-comment markers that `emit_markdown` appends today.

## Read first

- `lib/pdf/types.py` `SkipReason` (values `"empty pdf"`, `"slide deck"`, ...), domain
  `SkipReason` (different names and values), `cli/jobs.py` `_SKIP_REASON_MAP`,
  `cli/models.py:77`, `tests/test_pipeline_skip_contract.py`
- `lib/pdf/images.py`: `ExtractedImage` (line 139), `ImageSource`,
  `TRUNCATION_MARKER_TEMPLATE`, `VectorUncertaintyStats`
- `lib/pdf/vector_images.py`: `format_uncertainty_marker`, `should_emit_marker`
- `lib/pdf/glyphs.py`: `GlyphPassStats`, `GLYPH_PLACEHOLDER_MARKER_TEMPLATE`,
  `UNKNOWN_GLYPH`
- `lib/pdf/emit.py` `emit_markdown` tail (images_truncated marker, vector marker,
  glyph marker computed from the finished body)
- `api.py` `ConvertedPaper` (the real result type)
- `domain/document.py`, `domain/image.py`

## Change

1. Canonical `SkipReason` moves to `domain/document.py` with the legacy member names
   and values (`EMPTY_PDF = "empty pdf"`, ...). `lib/pdf/types.py` re-exports it. The
   old domain members and `ConvertedPaper` (unused) are deleted; `api.ConvertedPaper`
   stays the result type.
2. Canonical `ExtractedImage` moves to `domain/image.py`: the legacy 13-field frozen
   dataclass including `source`, `sub_captions`, `caption_body_dropped`. `lib/pdf/images.py`
   re-exports it (same import path keeps working). Move `ImageSource` with it.
3. Move `VectorUncertaintyStats` and `GlyphPassStats` into a new `domain/diagnostics.py`
   (frozen dataclasses, unchanged fields); re-export from their old modules. Add
   `Diagnostics(images_truncated: bool, source_image_count: int,
   vector_uncertainty: VectorUncertaintyStats | None, glyph_stats: GlyphPassStats | None,
   extra_prompts: tuple[str, ...])`. `extra_prompts` holds already-formatted prompt
   strings (the parser owns the preamble: PDF wording problems, HTML problems).
   `PaperDocument.diagnostics: Diagnostics = Diagnostics()`.
4. `writers/markdown/markers.py` (new): functions that render the three markers by
   calling the existing template/format helpers in `lib/` (do not copy them). The writer
   appends markers after the last element in the legacy order: truncation, vector
   uncertainty, then (last) glyph placeholders. The glyph count must be taken from the
   finished body the same way `emit_markdown` does (`md.count(UNKNOWN_GLYPH)`).
   Write the function so the bridge in P08 can call "body" and "trailer" separately.
5. Update `cli/jobs.py`/`cli/models.py` only if imports break; behavior unchanged.

## Do not

- Change any marker text, the closed reason-key set, or when a marker fires.
- Edit `emit_markdown` (it keeps working through the re-exports).

## Tests

- Skip-contract and image tests still pass unchanged (`test_pipeline_skip_contract.py`,
  `test_images.py`, `test_glyphs.py`).
- Twin tests: for each marker, render with the writer and compare to the string
  `emit_markdown` produces for a one-paragraph section list with the same stats:
  truncated images; vector uncertainty (fires and does not fire per
  `should_emit_marker`); glyph placeholders with and without skipped counts; all three
  together (order).

## Acceptance

Checklist green; `python -c "import tomd.domain, tomd.lib.pdf"` shows no import cycle;
`git diff --stat` shows `lib/` changes only in the re-export lines.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Import-cycle check:
Known divergences found:
Open questions:
```
