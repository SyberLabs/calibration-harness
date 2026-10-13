# P10 PDF lists

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 2 | P09, P03 | P11, P12, P13 | M | medium |

## Goal

Convert PDF `LIST` sections from `RawBlock` to real `ListBlock` trees (nesting from
`indent_level`, preserved ordinals, em/en-dash bullets), byte-identical.

## Read first

- `lib/pdf/emit.py`: `LIST_BULLET`, `_EMDASH_*` (118-170), `_normalize_bullets`,
  `_is_numbered_item`, `_reads_unfinished`, `_is_list_item_start`, `_format_list_item`,
  `_render_list_spans` (285-392), `_assign_emdash_nesting` (1106-1160; already extracted
  public in P08)
- `lib/pdf/structure.py:1918` `_assign_list_nesting`
- `lib/pdf/types.py` `BULLET_CHARS`, `BULLET_RE`, `NUMBERED_LIST_RE`
- P03's model (`ListItem.children`, `marker`, `ListBlock.start`) and `parsers/pdf/inline.py` (P09)
- Tests: `tests/test_position_lists.py`, list cases in `tests/test_emit.py`

## Change

1. `parsers/pdf/lists.py`: adapter for `SectionKind.LIST`. A LIST section is one
   (possibly wrapped) item or several bullet lines; reuse the legacy item-start
   predicates (import them; do not fork) to split lines into items and join wrapped
   continuations. Bullet glyph or `*` marker -> unordered item; ordinal marker (`1.`,
   `b)`, `(a)`) -> `ListItem.marker` preserved verbatim. `indent_level` -> nesting:
   consecutive list sections form one tree; a deeper `indent_level` becomes a nested
   `ListBlock` child of the previous item. Item labels use `lines_to_spans`.
2. Decide how adjacent LIST sections at the same level merge into one `ListBlock`
   versus separate blocks, by matching how legacy separates them (legacy emits each
   section as its own block joined by blank lines; do not merge if that changes bytes).
   Document the rule.
3. Register in `ADAPTERS`; remove the `pdf:list` origin from the allow-list.

## Do not

- Change the em-dash detection or nesting thresholds. Do not touch `structure.py`.

## Tests

Twin tests: for hand-built LIST `Section`s (bullet glyphs, `*`, ordinals, em-dash
items with the dash on its own line, wrapped items, three nesting levels, empty lines)
compare `write_element(adapt(sec))` with `emit._render_list_spans(sec)`. Corpus parity
must stay byte-equal.

## Acceptance

Checklist green; ratchet shrank by `pdf:list` only.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Ratchet before -> after:
Merge rule for adjacent list sections:
Known divergences found:
Open questions:
```
