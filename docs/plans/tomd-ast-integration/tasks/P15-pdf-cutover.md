# P15 PDF cutover

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 2 | P09-P14 | W3 | S | high (blast radius, tiny diff) |

## Goal

Switch the production PDF path to parser -> bridge -> writer. This is the first PR
that changes what runs in production, so it is deliberately a few lines plus evidence.

## Preconditions (verify, do not assume)

- All of P09-P14 are `merged` in STATUS.md.
- The PDF ratchet allow-list contains only html-strategy table origin(s).
- **Maintainer corpus parity is clean.** The human runs
  `uv run --package tomd python packages/tomd/scripts/parity_corpus.py --data-dir $WG21_DATA_DIR`
  and pastes the summary into the PR and `STATUS.md` (Parity runs). An agent cannot do
  this step: stop and ask for it if the summary is not provided.

## Read first

- `api.py` `_convert_with_tomd_full` (PDF branch) and `convert_paper_full`
- `lib/pdf/pipeline.py` end of `run_pipeline` (where `emit_markdown` is called)
- `parsers/legacy_bridge.py`, `parsers/pdf/__init__.py`
- Who reads `PipelineResult.md` / `.sections`: `grep -rn "run_pipeline\|\.sections\|result\.md"
  packages` (QA batch, `tomd/cli.py` golden/score paths, tests)

## Change

1. Make `run_pipeline` produce `result.md` through the new path
   (`sections -> document -> bridge`) instead of `emit_markdown`, so every consumer of
   `run_pipeline` gets the AST path, not only `api`. `emit_markdown` stays in the repo
   (deleted in P28) and is still exercised by its own unit tests.
2. Keep `result.sections` populated for QA scoring.
3. No other behavior change.

## Do not

- Edit goldens or baselines. If anything differs, the PR is blocked, not "updated".
- Delete legacy code (P28).

## Tests

Entire tomd suite, including `test_pdf_golden`, `pdf_pins`, QA and gold-standard tests,
unchanged and green. `tests/parity` PDF tests now compare `emit_markdown` (legacy, still
present) to the production path.

## Acceptance

Checklist green; the human-provided corpus parity summary shows zero diffs; PR diff is
small. Rollback plan stated in the PR: revert this commit.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Corpus parity summary (human-provided):
Consumers of run_pipeline checked:
Known divergences found:
Open questions:
```
