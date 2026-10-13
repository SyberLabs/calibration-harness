# P24 Pass: redundant body metadata and orphan TOC list

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 4 | P23 | none | M | high |

## Goal

Port the next two steps of the emit-level chain: `strip_redundant_body_meta` and
`strip_orphan_toc_list`. Follow the pass contract in P23. If the size exceeds the
README Section 6 limit, split into P24a (redundant meta) and P24b (orphan TOC) and report.

## Read first

- `lib/shared.py`: `strip_redundant_body_meta` (453) with `_REDUNDANT_META_RE` and
  `_strip_metadata_table` (636) / `_is_metadata_table` (599) / `_META_TABLE_LABELS`;
  `strip_orphan_toc_list` (478) with `_ORPHAN_*` constants
- P23's pass contract and `tomd/passes/`
- `lib/pdf/structure.py` `drop_leaked_toc_entries` and `lib/toc.py` (sibling TOC logic
  that stays in the PDF parser; do not merge)

## Change

1. `tomd/passes/redundant_meta.py`: remove paragraphs/lines matching
   `Document number:`-style lines (the regex is line-based and may hit a line inside a
   multi-line paragraph; handle by operating on paragraph text lines and rebuilding the
   paragraph), and a leading metadata `Table` right after front matter whose label cells
   are all in `_META_TABLE_LABELS`, plus the following `ThematicBreak` as legacy does
   (read `_strip_metadata_table` for the exact conditions).
2. `tomd/passes/orphan_toc.py`: between the front matter and the first `Heading`
   (level >= 2), if there are at least `_ORPHAN_MIN_BULLETS` bullet items and at least
   `_ORPHAN_MATCH_RATIO` of their normalized texts match later headings (normalization:
   lowercase, strip section number, strip inline markdown/links), with no substantive
   non-bullet element between the first and last bullet, remove the list, an
   immediately preceding "Contents"-style label paragraph, and nothing else. Import the
   constants and normalizing regexes from `lib/shared.py`.
3. Remove both steps from the bridges; keep the legacy functions as test oracles until P28.
4. TABLE_CSS injection stays in the bridge (P29 deletes it).

## Do not

- Alter heuristics or thresholds. Do not touch the PDF-side TOC logic.

## Tests

Direct legacy-vs-pass tests on constructed documents (metadata table with and
without HR; stray `Document number:` line; bullet TOC with and without label; TOC
below the match ratio; fewer than 3 bullets; non-bullet content between bullets; no
heading) plus full parity for both formats.

## Acceptance

Checklist green; parity green; bridge lost exactly these steps.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Cases where a faithful port was not possible:
Known divergences found:
Open questions:
```
