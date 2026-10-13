# P09 PDF inline spans, headings, paragraphs

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 2 | P08 | W3 may start P16 | M-L | high |

## Goal

Convert `TITLE`, `HEADING`, and `PARAGRAPH` sections from `RawBlock` to real
`Heading` / `Paragraph` elements, and build the inline span builder every later PDF
family (lists, tables, wording) reuses. Output stays byte-identical.

## Read first

- `lib/pdf/emit.py`: `_render_span` (41), `_render_line_spans` (76; note the grouping of
  consecutive monospace spans into one backtick pair), `_render_paragraph_spans` (172),
  `_render_heading_spans` (200), `_decode_dingbats` (701), `_HEADING_SAME_ROW_FONT_FRACTION`
- `lib/pdf/cleanup.py`: `escape_leading_atx`, `normalize_whitespace`
- `lib/pdf/types.py`: `Span` (font run: bold, italic, monospace, link_url, wording_role),
  `Line`, `Section`
- `writers/markdown/spans.py` and `escape.py` (P07)
- The adapter dispatch from P08 (`parsers/pdf/adapter.py`)

## Change

1. `parsers/pdf/inline.py`: `lines_to_spans(lines, *, suppress_bold=False) ->
   list[domain Span]`. Maps font runs to `TextSpan`, `StrongSpan`, `EmphasisSpan`,
   `CodeSpan`, `LinkSpan`; merges consecutive monospace runs into one `CodeSpan`;
   keeps whitespace outside delimiters (the writer's `_wrap_delimiters` does the same);
   applies `_decode_dingbats`. Provide a span-normalization step that merges adjacent
   spans of the same type so the writer never emits `**a****b**`. Name the nesting order
   (bold+italic+link) once, as legacy does (`***[text](url)***`).
2. `parsers/pdf/blocks.py`: adapters for `TITLE`, `HEADING` (depth from
   `heading_level`, same-row joining and bare-prefix dropping as legacy), `PARAGRAPH`
   (unwrapped single line, leading-ATX escape through the writer's escape module). Register them in
   `ADAPTERS`. Fill `provenance` (page, confidence).
3. Writer: only if a legacy behavior cannot be expressed (report first).
4. Update `rawblock_allowlist.py`: remove the `pdf:title`, `pdf:heading`,
   `pdf:paragraph` entries.

## Do not

- Convert other kinds. Do not change legacy `emit.py` renderers.
- Alter whitespace handling; if the writer and legacy differ on a corpus paper, fix the
  adapter, never the golden.

## Tests

Twin tests in `tests/parity/test_inline_pdf.py`: for hand-built `Line`/`Span` inputs
(plain, bold, italic, bold+italic, link, link+bold, monospace runs, mixed, leading and
trailing spaces inside a styled run, empty spans, dingbat glyphs) assert
`write_spans(lines_to_spans(lines)) == emit._render_line_spans(...)`. Headings: levels,
same-row join, absorbed second line. Plus the corpus parity suite.

## Acceptance

Checklist green; parity unchanged; ratchet allow-list shrank by exactly the three
origins above.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Ratchet before -> after:
Span-normalization rules implemented:
Known divergences found:
Open questions:
```
