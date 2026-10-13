# P13 PDF images, captions, wording problems

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 2 | P09 | P10, P11, P12 | S-M | medium |

## Goal

Convert `IMAGE` and `FIGURE` sections and the surrounding image bookkeeping from
`RawBlock` to AST: no image syntax ever (#408), captions as italic paragraphs, sidecar
image records on the document, and the PDF wording-problem prompts on `Diagnostics`.

## Read first

- `lib/pdf/emit.py`: `_render_image` (1047), `_escape_italic_text` (1018; now in the
  writer escape module from P07), the FIGURE branch of `_render_section_md`
- `lib/pdf/pipeline.py`: `_filter_sections_inside_vector_images` (1465; it already turns
  sub-captions into PARAGRAPH sections `*<escaped>*`), the `wording_problems` prompt block
  near line 2675
- `lib/pdf/images.py` (`ExtractedImage`, `caption_body_dropped`, `TRUNCATION_MARKER_TEMPLATE`)
- CLAUDE.md "Stability commitment for `SectionKind.IMAGE`" in `packages/tomd/src/tomd/CLAUDE.md`
- Tests: `tests/test_images.py`, `tests/test_figures.py`, `tests/pdf_pins/test_p0957r8.py`

## Change

1. `parsers/pdf/images.py`: adapter for `IMAGE`: emit
   `Paragraph([EmphasisSpan(TextSpan(caption))])` (with the writer's italic-wrapper
   escaping) only when `image_ref.suggested_alt` is non-empty and
   `image_ref.caption_body_dropped`; otherwise emit nothing. `FIGURE` emits nothing.
   Images themselves live on `PaperDocument.images` (already populated by P08), not in
   `elements`.
2. Check that an `EmphasisSpan` paragraph renders byte-equal to `"*" +
   _escape_italic_text(alt) + "*"`, including the leading-block-character cases
   (`-`, `*`, `+`, `>`, `#`, `1.`). Escape in the adapter or writer, whichever P07 settled.
3. Wording-problem prompts: the adapter copies the existing formatted prompt strings
   into `Diagnostics.extra_prompts` in the order `run_pipeline` appends them after the
   uncertain prompts.
4. Remove the `pdf:image` and `pdf:figure` origins from the allow-list.

## Do not

- Emit `![]()` anywhere. Change caption attribution or the caption-band predicates.

## Tests

Twin tests: IMAGE with alt + `caption_body_dropped`, with alt but gate-kept body, without
alt, FIGURE; compare to `emit._render_section_md`. Corpus parity incl. the synth
sub-figure fixture and `p0957r8` stays byte-equal. Prompts order test.

## Acceptance

Checklist green; ratchet shrank by `pdf:image`, `pdf:figure`.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Ratchet before -> after:
Known divergences found:
Open questions:
```
