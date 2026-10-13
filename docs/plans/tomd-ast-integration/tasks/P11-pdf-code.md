# P11 PDF code blocks

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 2 | P09 | P10, P12, P13 | M | medium |

## Goal

Convert PDF `CODE` sections from `RawBlock` to `CodeBlock`, byte-identical, including
gutter-number stripping, grid alignment, kerning cleanup, and the diagram guard.

## Read first

- `lib/pdf/emit.py`: `_ROW_Y_TOLERANCE` .. `_MAX_GUTTER_CODE_INDENT` (395-420),
  `_group_code_rows`, `_gutter_line_value`, `_detect_code_gutter` (478),
  `_section_span_text_lines` (547), `_render_code_block` (551),
  `_render_code_block_with_gutter` (612)
- `lib/pdf/code_grid.py` (`CodeGrid`), `lib/pdf/code_format.py`
  (`normalize_code_line`, `maybe_normalize_code_line`, `is_diagram_block`)
- `Section.fence_lang`, `domain/elements.py` `CodeBlock`, `writers/markdown/blocks.py`
  `_format_code_block` (fence length from backtick runs; compare with legacy fence rule)
- Tests: `tests/test_emit.py` code cases, `tests/test_code_format.py`,
  `tests/test_code_grid.py`, `tests/pdf_pins/test_p4012r0*`

## Change

1. `parsers/pdf/code.py`: adapter for `SectionKind.CODE` producing
   `CodeBlock(code=..., language=sec.fence_lang)`. The adapter owns gutter detection,
   grid layout and per-line normalization by calling the existing helpers (import,
   do not copy). The rendered code string must equal what `_render_code_block` puts
   between the fences.
2. Verify the writer's fence selection equals legacy for code containing backtick runs
   and for empty language. If they differ, report before changing either side.
3. Register; remove `pdf:code` from the allow-list.

## Do not

- Change code normalization, thresholds, or `code_grid`/`code_format`.

## Tests

Twin tests with hand-built CODE sections: plain, with line-number gutter, indented,
kerning artifacts, diagram block (box-drawing), tabs, fence-containing text, language
`""`. Compare `write_element(adapt(sec))` to `emit._render_code_block(sec)`. Corpus
parity (`p4012r0-codeblock`, `p4012r0-page-*`, pins) stays byte-equal.

## Acceptance

Checklist green; ratchet shrank by `pdf:code` only.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Ratchet before -> after:
Known divergences found:
Open questions:
```
