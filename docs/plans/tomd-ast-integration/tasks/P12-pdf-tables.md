# P12 PDF pipe tables

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 2 | P09 | P10, P11, P13 | M | high |

## Goal

Convert PDF tables whose strategy renders as a pipe table (and `skip` false positives)
from `RawBlock` to real `Table` / `Paragraph` elements, byte-identical. Tables with
strategy `html_table` (and the unreachable `code_blocks`) stay `RawBlock` until P29.

## Read first

- `lib/pdf/emit.py`: `_render_cell_spans` (737), `_cell_text` (855), `_flatten_cell`
  (956), `_render_table` (966), `_render_table_as_text` (836), `_render_html_table`
  (862, read-only: it stays), the continuation fold (extracted in P08)
- `lib/pdf/table.py`: `TableKind` (220), `TableStrategy` (233), `_STRATEGY_MAP` (241),
  how `Section.columns` (rows -> cells -> `Span`s), `table_continuation`, and
  `table_strategy` are set (around lines 3886-4010)
- `domain/table.py` (after P01), `writers/markdown/tables.py`
- Tests: `tests/test_tables.py`, `tests/test_table_analyzer.py`, `tests/test_table_passes.py`,
  `tests/pdf_pins/test_p0957r8.py`, `test_p4100r*.py`

## Change

1. `parsers/pdf/tables.py`: adapter for `SectionKind.TABLE`:
   - strategy `pipe_table`: `Table(headers=[...], rows=[...])`. First row is the header
     with bold suppressed (`suppress_bold=True` in legacy); a continuation section (already
     folded by P08) has no header row only if it remains standalone; cells are
     `TextCell(spans=...)` with newlines collapsed exactly like `_flatten_cell`
     (do this in the adapter, not the writer); rows padded to the column count.
   - strategy `skip` (FALSE_POSITIVE): the legacy output is paragraphs joined by blank
     lines; emit `Paragraph` elements, not a `Table`.
   - strategies `html_table` and `code_blocks`: `RawBlock(origin="pdf:table:<strategy>")`
     via the legacy renderer.
2. Writer: verify alignment-delimiter and escaping behavior equals legacy for cells with
   pipes, empty cells, and short rows (legacy delimiter is always `---`; `CellAlign.DEFAULT`
   must give that). Report any difference before changing the writer.
3. Register; remove `pdf:table:pipe_table` and `pdf:table:skip` from the allow-list.

## Do not

- Touch table detection or classification (`table.py`). Do not convert HTML-strategy tables.

## Tests

Twin tests: hand-built TABLE sections (`columns`) for pipe, skip, continuation-merged,
ragged rows, cells with `|`, soft-wrapped cells, bold header; compare to
`emit._render_table`. Corpus parity incl. `p0957r8`, `p4100r*`, `p3978r*` stays byte-equal.

## Acceptance

Checklist green; ratchet keeps only the html-strategy table origin(s).

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Ratchet before -> after:
Known divergences found:
Open questions:
```
