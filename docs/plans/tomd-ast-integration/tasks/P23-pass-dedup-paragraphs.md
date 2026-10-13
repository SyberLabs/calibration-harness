# P23 Pass: `dedup_paragraphs`

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 4 | P15, P22 | none (W4 is sequential, legacy chain order) | M | high |

## Goal

Replace the first step of the legacy emit-level chain, `dedup_paragraphs`
(`lib/shared.py:77`), with an AST pass that runs before the writer, for both formats.
This task also establishes the shape every W4 pass follows.

## Read first

- `lib/shared.py` `dedup_paragraphs`, `_MIN_DEDUP_LENGTH`, `_MAX_PARAGRAPH_OCCURRENCES`
  (the string version works on `md.split("\n\n")` chunks, front matter included as
  chunk 0, never drops headings or code fences)
- `parsers/legacy_bridge.py` (the named-step chain from P08/P16) and the parity harness
- `writers/markdown/blocks.py` `write_element` (the text projection)

## Pass contract (applies to P23-P27)

- Lives in `tomd/passes/<name>.py`, signature `def <name>(document: PaperDocument) ->
  PaperDocument`, pure (returns a new document or the same one unchanged), registered in a
  single ordered `PASSES` list in `tomd/passes/__init__.py`-adjacent module (not in
  `__init__.py`, which holds re-exports only).
- The bridge removes the corresponding string step in the same PR; the AST pass takes
  its place in the pipeline: `parse -> PASSES -> writer -> remaining string steps`.
- Ported passes must be a **prefix** of the legacy chain, because AST passes run before
  the writer. That is why W4 is sequential.
- Equivalence is proven on the corpus by the existing parity gate (and the maintainer
  corpus script), plus a direct test that runs the legacy string function and the new
  pass on the same inputs.
- **If byte equality cannot be reached after a good-faith port, stop and report.** The
  options are (1) keep the string step in the bridge as an explicitly documented "polish"
  stage and record the decision in STATUS.md, or (2) propose an intended behavior change
  as a separate re-bless PR. Never weaken the oracle and never edit goldens.

## Change

1. `tomd/passes/dedup.py`: `dedup_paragraphs(document)`: (a) drop an element whose
   rendered text equals the previous element's (compare stripped rendered text via
   `write_element`); (b) cap repeats at `_MAX_PARAGRAPH_OCCURRENCES` for non-heading,
   non-code elements whose stripped rendered text is at least `_MIN_DEDUP_LENGTH`. Import
   the two constants from `lib/shared.py`; do not copy them.
2. Elements that render with internal blank lines (multi-paragraph quotes, lists with
   continuation blocks, `RawBlock`) were separate chunks in the string version. Decide
   and document how the pass treats them; the corpus decides whether element-level and
   chunk-level agree.
3. Remove the `dedup_paragraphs` step from both bridge chains; keep the legacy function
   in `lib/shared.py` (deleted in P28) as the test oracle.

## Do not

- Change the thresholds or the headings/code exemption. Do not touch other passes.

## Tests

`tests/passes/test_dedup.py`: table of inputs (consecutive duplicates, 10 vs 11
repeats, short repeated lines, repeated headings, repeated code fences, duplicate
list blocks) asserting `write(dedup(doc))` equals `dedup_paragraphs(write(doc))`; plus
the full parity gate for both formats.

## Acceptance

Checklist green; parity green for PDF and HTML; bridge lost exactly one step.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
How multi-chunk elements are treated:
Any corpus paper where element-level and chunk-level differ:
Known divergences found:
Open questions:
```
