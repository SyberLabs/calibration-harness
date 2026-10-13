# P14 PDF wording

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 2 | P10, P11, P04 | none | M | high |

## Goal

Convert `WORDING`, `WORDING_ADD`, `WORDING_REMOVE` sections from `RawBlock` to
`WordingBlock` trees using P04's model, byte-identical across the three shapes
(wholesale code, code diff, prose).

## Read first

- `lib/pdf/wording_emit.py` (all): `_render_wording_section`, shape selection constants
  (`_MONO_DOMINANT_THRESHOLD`, `_CODE_PROMOTION_MIN_LINES`, `_MAX_CODE_DIFF_INDENT`),
  `_group_wording_spans`, `_escape_wording_text`
- `lib/wording_cleanup.py`, `lib/wording_policy.py`; P04's `strip_redundant_roles`
- `lib/pdf/wording.py` (how `Span.wording_role` is assigned: read only)
- `parsers/pdf/inline.py` (P09) and `parsers/pdf/code.py` (P11, for the wholesale-code shape)
- Tests: `tests/test_wording*.py`, `tests/pdf_pins/` with wording (`test_p4098r1.py`,
  `test_p3978r*.py`), wording cases in `tests/test_emit.py`

## Change

1. `parsers/pdf/wording.py`: adapter that reproduces the shape decision (import the
   existing predicates and constants; do not fork) and builds `WordingBlock(role,
   children)`: wholesale code -> `CodeBlock`; code diff -> P04's diff model with
   `UnderlineSpan`/`StrikethroughSpan` line spans; prose -> `Paragraph` with ins/del spans
   from `Span.wording_role`.
2. Apply `strip_redundant_roles` at the point legacy applies `strip_redundant_tags`
   (read where `_render_wording_section` calls it) so the unwrapping decision is made
   once, identically.
3. Register; remove `pdf:wording*` origins from the allow-list. At this point the PDF
   allow-list should contain only the html-strategy table origin(s).

## Do not

- Change wording detection (`wording.py`), thresholds, or the cleanup policy.

## Tests

Twin tests per shape and per role, plus threshold edges (just below and above
`UNIFORM_ROLE_THRESHOLD`, monospace dominance 0.80, one-line vs two-line code
promotion), indent clamp, angle brackets inside diffs. Compare to
`wording_emit._render_wording_section`. Corpus parity incl. wording-heavy papers stays
byte-equal.

## Acceptance

Checklist green; PDF ratchet allow-list reduced to the html-table origin(s) only.
Paste the final list in the Handoff.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Final PDF allow-list:
Known divergences found:
Open questions:
```
