# P20 HTML pipe tables

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 3 | P17 | P18, P19, P21 | M | high |

## Goal

Convert HTML tables that legacy renders as pipe tables from `RawBlock` to `Table`,
byte-identical. Mixed and code tables (`_render_mixed_code_table`, `_render_code_table`)
stay `RawBlock` until P29.

## Read first

- `lib/html/render.py`: `_render_table` (1419; routing order), `_has_spans`,
  `_has_br_multiline_cells`, `_needs_flat_reconstruction`, `_cell_own_text`,
  `_denormalize_table` (1177), `_render_denormalized_table` (1245), `_render_table_flat`
  (1266), `_is_pure_code_table`, `_render_mixed_code_table` (1371; read-only),
  `_render_code_table` (1481; read-only), `_BOLD_WRAP_RE`, `_COLLAPSE_WS_RE`
- `lib/tables.py` (shared markup, stays until P29), `domain/table.py`,
  `writers/markdown/tables.py`
- Tests: table cases in `tests/test_html_render.py`, `tests/test_html_golden.py`
  (`handwritten_table_sample`)

## Change

1. `parsers/html/tables.py`: handler for `table` that mirrors `_render_table`'s routing
   with the same predicates (import them). Routes: code/mixed tables ->
   `RawBlock(legacy, origin="html:table:mixed|code")`; flat, denormalized
   (rowspan/colspan expanded by the existing `_denormalize_table` logic), and simple
   tables -> `Table` with `TextCell`s whose spans come from `inline_to_spans`; the header
   row has one leading full-bold wrap removed (`_BOLD_WRAP_RE`); cell text collapses
   whitespace and escapes pipes via the writer escape module; rows padded to the column
   count; empty table -> nothing.
2. Where legacy builds cell strings (`_cell_own_text`, denormalization), reuse its
   cell-extraction logic and convert its output to spans; do not reimplement the span
   expansion.
3. Register; remove `html:table:*` origins except the mixed/code ones.

## Do not

- Convert mixed/code tables; do not touch `lib/tables.py`; do not change routing.

## Tests

Twin tests with parsed snippets: simple, with thead/tbody/tfoot, rowspan, colspan,
both, ragged, pipes in cells, bold header, `<br>` cells (routes to mixed: stays
`RawBlock`), misnested cells repaired by `prepare_body`, empty. Compare to
`render._render_table`. HTML corpus parity.

## Acceptance

Checklist green; HTML allow-list keeps only the mixed/code table origins among tables.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Ratchet before -> after:
Known divergences found:
Open questions:
```
