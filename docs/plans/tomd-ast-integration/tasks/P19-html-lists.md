# P19 HTML lists

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 3 | P17, P03 | P18, P20, P21 | M | high |

## Goal

Convert `ul`/`ol` from `RawBlock` to `ListBlock` trees with continuation children,
byte-identical.

## Read first

- `lib/html/render.py`: `_LIST_ITEM_BLOCK_TAGS`, `_indent` (1000), `_render_list_item`
  (1011; label vs trailing blocks, tight nested lists, label-less items), `_render_list`
  (1078; non-`<li>` children as continuations, only `<li>` advances the counter),
  `_fix_misnested_list_items` (106, already applied by `prepare_body`)
- P03's model and writer; `parsers/html/dispatch.py` (nested content must go back
  through `to_elements` so nested lists/code/paragraphs become real children, and fall
  back to `RawBlock` for unconverted families)
- Tests: list cases in `tests/test_html_render.py`; markdown-it nesting tests

## Change

1. `parsers/html/lists.py`: handlers for `ul` and `ol`. Each `<li>` becomes a
   `ListItem` whose label spans come from `inline_to_spans` over the leading inline run
   (a leading `<p>` is part of the label) and whose `children` come from `to_elements`
   over the trailing nodes; inline text interleaved after the first block becomes its own
   `Paragraph` child (not merged into the label, not dropped). Non-`<li>` direct children
   become continuation children of the preceding item (or standalone elements before the
   first item). Ordered lists number only `<li>` children.
2. Register; remove `html:ul` and `html:ol` from the allow-list. A list nested in a
   still-unconverted family is fine: it renders as part of that `RawBlock`.

## Do not

- Change `_render_list*` or the DOM repair passes.

## Tests

Twin tests with parsed snippets: flat, nested, mixed `ul`/`ol` nesting, item with
paragraph, code, nested list, label-less item with block, loose text between items,
`<p>` inside `<li>`, empty items. Compare `write_element(handler(el))` with
`render._render_list_item`/`_render_list`. HTML corpus parity.

## Acceptance

Checklist green; ratchet shrank by the list origins only.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Ratchet before -> after:
Known divergences found:
Open questions:
```
