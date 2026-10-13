# P26 Pass: `resolve_metadata` swap-in and metadata-table strip

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 4 | P25 | none | M | high |

## Goal

Replace the first two API-level steps (`_normalize_front_matter`,
`_strip_body_metadata_text`) with AST equivalents. `resolve_metadata` (built and
oracle-tested in P02) becomes part of the production pipeline.

## Read first

- `api.py`: `_normalize_front_matter`, `_strip_body_metadata_text`,
  `_METADATA_TABLE_LINE_RE`, `_METADATA_TABLE_SCAN_DEPTH`, `_MIN_LABEL_ROWS_FOR_TABLE_STRIP`,
  `convert_paper_full` ordering
- `tomd/resolve.py` and `tests/test_resolve.py` (P02)
- `lib/metadata_yaml/format.py` (`parse_front_matter` round-trips only the shapes
  `format_front_matter` emits: a value with unusual characters can change when the legacy
  path re-parses its own output)
- P23's pass contract

## Change

1. Build `MailingRecord.from_meta(meta)` inside the new pipeline entry point (the
   public `convert_paper_full(paper_id, path, meta: dict)` signature is unchanged) and
   run `resolve_metadata(document.metadata, mailing)` as an AST step between the P25 pass
   and the remaining P27 steps. Not a `PASSES` entry if it needs the mailing record: give
   the pipeline an explicit stage.
2. `tomd/passes/metadata_table.py`: scan the leading elements (the legacy scan covers the
   first `_METADATA_TABLE_SCAN_DEPTH` body lines and stops at the first `#` heading); remove
   any `Table` in that region with at least `_MIN_LABEL_ROWS_FOR_TABLE_STRIP` rows whose
   first cell matches `_METADATA_TABLE_LINE_RE`. Reuse the regex constants.
3. Remove both string steps from the bridges. Keep `api._normalize_front_matter` and
   `_strip_body_metadata_text` until P28 as oracles.

## Do not

- Change `resolve_metadata` rules (P02 pinned them). Do not change the public API.

## Tests

Full API-level parity for both formats with a realistic `meta` (the parity harness
already supplies a fixed one; add cases that exercise each fallback: missing date,
missing audience, D-number override, name-only reply-to). A direct test of the table
strip against the legacy function on constructed documents (with and without front
matter, table after a heading, one metadata row only).

## Acceptance

Checklist green; API-level parity green for both formats.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Cases where front-matter round trip changed bytes:
Known divergences found:
Open questions:
```
