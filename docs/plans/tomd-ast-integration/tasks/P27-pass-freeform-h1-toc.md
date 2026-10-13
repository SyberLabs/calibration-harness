# P27 Pass: freeform metadata lines, API-level H1, TOC strip

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 4 | P26 | none | L | high |

## Goal

Port the remaining API-level steps and delete the bridge's string chain: 
`strip_freeform_metadata_lines(md, metadata=meta)`, the second `apply_strip_leading_h1`
(using the resolved title), and `_strip_toc`. If over the README Section 6 size limit,
split into P27a (freeform) and P27b (H1 + TOC) and report.

## Read first

- `lib/shared.py`: `strip_freeform_metadata_lines` (575) and `_strip_freeform_metadata_lines`
  (287-450; content-aware when `metadata` is given: structural lines carrying metadata,
  bare author+email lines), the `_FREEFORM_*`, `_HEADING_META_LABEL_RE`,
  `_LIST_META_LABEL_RE`, `_HEADING_BARE_DATE_RE`, `_STRUCTURAL_LINE_RE`,
  `_FREEFORM_SCAN_DEPTH` constants
- `api.py`: `_strip_toc`, `_TOC_RE`, `_TOC_MAX_LINES`, `_strip_toc_replace`; and the
  `convert_paper_full` call order (freeform -> H1 -> TOC)
- `lib/pdf/structure.py` `drop_leaked_toc_entries`, `lib/toc.py` (sibling logic that stays)
- P23 pass contract, P25's `strip_leading_title`

## Change

1. `tomd/passes/freeform_meta.py`: operate on the leading non-heading paragraph and list
   elements within the scan depth; remove those matching the label regexes (use the same
   constants), and with `metadata` (the resolved `PaperMetadata`) the structural and
   author+email cases. Keep the exact stop conditions of the legacy scan (read it end to
   end before porting; it is the subtlest function in the chain).
2. API-level H1: call P25's `strip_leading_title` with the resolved title and the legacy
   default `max_level` (1), after the freeform pass.
3. `tomd/passes/toc.py`: remove a heading or paragraph labeled `Contents` / `Table of
   Contents` and the entries beneath it up to the next heading of any level, leaving the
   next heading; skip if the span exceeds `_TOC_MAX_LINES` rendered lines (so the pass
   needs the writer's line count of the span; compute from `write_element`).
4. Delete the bridge's string chain entirely; the pipeline is now parse -> passes ->
   resolve -> passes -> writer, with only TABLE_CSS injection left in the bridge (P29
   deletes it). Keep legacy functions in `lib/shared.py` and `api.py` as oracles until P28.

## Do not

- Change label lists, scan depth, or thresholds. Do not delete legacy code (P28).

## Tests

Direct legacy-vs-pass tests on constructed documents for each function (label forms
with and without colons/bold, heading and list meta lines, bare date headings,
author+email lines with and without `metadata`, structural-line guard, scan-depth
boundary, TOC with and without label, TOC over the line cap, TOC directly before the first
real heading). Full API-level parity for both formats, plus a maintainer corpus run
(the human pastes the summary; same rule as P15/P22).

## Acceptance

Checklist green; parity green; maintainer corpus summary shows zero diffs.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Corpus parity summary (human-provided):
Cases where a faithful port was not possible:
Known divergences found:
Open questions:
```
