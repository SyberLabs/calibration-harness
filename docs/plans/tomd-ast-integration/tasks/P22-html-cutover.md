# P22 HTML cutover

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 3 | P16-P21 | P15 | S | high (blast radius, tiny diff) |

## Goal

Switch the production HTML path to parser -> bridge -> writer.

## Preconditions (verify, do not assume)

- P16-P21 are `merged` in STATUS.md; the HTML allow-list contains only the mixed/code
  table origins.
- **Maintainer corpus parity is clean** for HTML papers: the human runs
  `uv run --package tomd python packages/tomd/scripts/parity_corpus.py --data-dir $WG21_DATA_DIR`
  and pastes the summary. An agent cannot do this; stop and ask if it is missing.

## Read first

- `api.py` `_convert_with_tomd_full` HTML branch; `lib/html/__init__.py`
  (`convert_html` is imported by tests and by `api`)
- `lib/html/convert.py`, `parsers/html/parser.py`, `parsers/legacy_bridge.py`
- `grep -rn "convert_html" packages` for every consumer

## Change

1. Make `convert_html(path, *, html_images_result=None)` run `parse_html` then
   `render_html` (bridge) so every consumer, not only `api`, gets the AST path. Keep its
   signature and return type `(markdown, prompts | None)`; prompts come from
   `Diagnostics.extra_prompts`.
2. Keep the legacy body renderer (`render_body`, `_render_element`) reachable for the
   remaining `RawBlock` (mixed/code tables) and for `tests/parity`, which now compares
   `render_body` string output against the production path.

## Do not

- Edit goldens or snapshots. A diff blocks the PR. Delete no legacy code (P28).

## Tests

Entire tomd suite unchanged and green, in particular `test_html_golden`,
`test_html_integration`, `test_html_generators`, `test_html_render`.

## Acceptance

Checklist green; human-provided corpus parity summary shows zero diffs. Rollback plan in
the PR: revert this commit.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Corpus parity summary (human-provided):
Consumers of convert_html checked:
Known divergences found:
Open questions:
```
