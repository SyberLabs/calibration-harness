# P21 HTML wording, blockquote, note blocks, dl

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 3 | P17, P04 | P18, P19, P20 | M | medium |

## Goal

Convert the remaining HTML block constructs from `RawBlock` to AST, so the HTML
allow-list ends at the mixed/code table origins only.

## Read first

- `lib/html/render.py`: `_render_wording_div` (940), `_render_eelis_block` (961),
  `_render_blockquote` (1500), the `note|example|advisement` branch in `_render_div` and
  the `example-block|note-block|bug-block` / `abstract-block` branches in
  `_render_element`, `_render_dl` (1510), `_normalize_eelis_wording` (328, read-only)
- `lib/wording_cleanup.py`, `lib/wording_policy.py`; P04's `WordingBlock` and
  `strip_redundant_roles`
- Tests: `tests/test_html_render.py`, `tests/test_html_generators.py` (hatemplate)

## Change

1. `parsers/html/special.py`: handlers for
   - wording divs (`wording`, `wording-add`, `wording-remove`) -> `WordingBlock(role,
     children)` with children from `to_elements`; apply `strip_redundant_roles` at the
     same decision point as legacy;
   - `blockquote`, `div.note|example|advisement`, `example-block`, `note-block`,
     `bug-block` -> `Blockquote(children=...)`. Legacy quotes every line with `"> "`
     including blank lines (trailing space); P04's writer reproduces that;
   - `abstract-block` -> `Heading(2, "Abstract")` followed by its children;
   - eelis blocks (`para`/`texpara`/`sentence`): synopsis -> `CodeBlock(cpp)`, sentences
     flowed into one `Paragraph`;
   - `dl` -> `Paragraph` elements, one per entry, where lines within an entry are joined
     by a soft newline (`TextSpan("\n")`), `dt` as `StrongSpan`, `dd` as `: text`;
     code children of a `dd` become separate `CodeBlock`s emitted after the entry text as
     legacy does. Document the soft-newline convention in the model docstring.
2. Register; remove the converted origins. After this PR the HTML allow-list should
   contain only the mixed/code table origins. Paste it in the Handoff.

## Do not

- Change `_normalize_eelis_wording` or DOM repair. Do not alter blockquote bytes.

## Tests

Twin tests with parsed snippets for each handler (wording with each role and uniform
vs mixed inline tags; blockquote with multiple blocks and blank lines; note/example/
bug blocks; abstract-block; eelis synopsis and sentences; dl with dt/dd/code/loose text),
each compared to the legacy renderer. HTML corpus parity incl. hatemplate and
`p3953r0`.

## Acceptance

Checklist green; HTML allow-list reduced as stated.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Final HTML allow-list:
Known divergences found:
Open questions:
```
