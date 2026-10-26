# Calibration harness: status

Oct 26, 2026 · companion to [calibration-harness.md](calibration-harness.md)

The harness is built end to end and tested, but every number it has produced
so far is synthetic. The real calibration set, a model gateway and a real
paperweight run are still missing, so nothing here says anything yet about how
well paperweight agrees with its reviewers.

## What is real, what is simulated

| Part | Status |
| --- | --- |
| paperweight.md's Lua | **Real.** The shim runs the prompt's own seven Lua blocks, unmodified, under Lua 5.5 (`lupa.lua55`). Only the model turns are stubbed. |
| Diagnostics parser, replay arithmetic | **Real.** `aggregate.py` reproduces every number the Lua printed, to the character, on 51 recorded runs and on live shim runs under all four inter-section rules. |
| Metrics, bootstrap, gates, readings, comment | **Real.** Known-answer tests on hand-computed sets; planted truth recovered through the whole pipeline. |
| Runner, `binary` backend | **Real code, exercised only against a fake binary.** A small Python stand-in on `PATH` runs the patched prompt through the shim. No real paperweight run has happened. |
| CI workflow | **Real, partly exercised.** The replay job runs on the fork's draft pull request against the synthetic baseline. The full-run job has only been seen to skip, because no gateway secret is set. |
| Grade votes, triage, Analyze prose | **Simulated.** `simulate.py`, a seeded grader drawn around a latent truth, and two fixed stubs. |
| Reviewer grades | **Simulated.** `data/synthetic/grades.csv`: three simulated reviewers on real tomd fixture papers. |
| Papers | **Real WG21 markdown,** from tomd's golden fixtures. They are not the ten papers the prompt was tuned on. |
| Baseline history | **Synthetic only.** The `calibration` branch of the fork holds one synthetic baseline under `synthetic/`. |
| Example comment | **Synthetic.** `packages/calibrate/examples/synthetic-comment.md`. |

## Where the shim and the real Runvil could differ

The shim module docstring keeps the full list. In short:

- **Engine globals.** Only `store` (read and write), `models`, `tasks.fanout`, `untrusted`, `var`, `args`, `item` and `prose` exist. A prompt that starts using any other Engine global fails in the shim first.
- **Engine limits.** No memory, response or time limits apply, and fanout runs serially in job order instead of up to 8 at a time.
- **`untrusted`.** It returns its input unchanged instead of wrapping it in nonce delimiters, so the prose a model would see differs. No Lua arithmetic depends on it.
- **Templates.** Rendering is plain `{{ var.x }}` substitution, and there is one `var` table per section run.
- **Fanout return value.** It is an empty table, not a host object, so the epilogue's `as_string(replies[i])` fallback never supplies a reply.
- **Harness.** No Harness, gateway, model binding, `models.use` options, recorder or cancellation.
- **Invalid UTF-8.** Lua slices strings by byte, and the shim decodes the store with replacement characters.

## Blocked on data from Vinnie

- The ten calibration papers and the three reviewers' per-criterion grades (milestone 3 with real data, and everything after it).
- The scripts and runs behind the numbers in the prompt's comments. Their diagnostics would be real parity fixtures, and their numbers milestone 5's target.
- The model and gateway the numbers came from, and a budget or a local model for full runs.

## Swapping in the golden set

1. Put each paper's exact markdown, the bytes the reviewers graded, in `packages/calibrate/data/golden/papers/<paper>.md`. Line endings are kept as committed (`-text`), so commit them exactly.
2. Write `packages/calibrate/data/golden/papers.jsonl`, one line per paper: `{"paper": "P3643R3", "markdown_sha256": "<sha256 of the file>", "tomd_version": "<version>", "split": "calibration"}`. Leave out the `synthetic` field. Papers graded later go in as `"split": "holdout"`.
3. Write `packages/calibrate/data/golden/grades.csv`: the header `paper,reviewer,criterion,grade`, then one row per paper, reviewer and criterion, using the prompt's `short` names.
4. Add provenance, reviewer names or initials, and the labeling rules to `data/golden/README.md`. Keep its first line free of the word SYNTHETIC.
5. Run `uv run calibrate check-set`. It must report a golden set, ten calibration papers and 210 grades, and that the criteria match the prompt.
6. On the repository: set the variable `CALIBRATE_MODEL` to the gateway model id, and add the secrets `RUNVIL_GATEWAY_URL` and `RUNVIL_GATEWAY_API_KEY`.
7. Make the first real baseline. One way is a manual dispatch of the `calibrate` workflow. The other is local:
   ```bash
   uv run calibrate full --backend binary --model <id>
   uv run calibrate record <run> --history <calibration branch checkout>
   ```
   Commit and push that checkout to `calibration`.
8. Milestone 5: compare that run's `summary.md` with the bias, MAE and correlation in the prompt's comments, and explain any gap in writing.

The synthetic set stays: the tests use it, and the replay job falls back to it only while no real baseline exists for `CALIBRATE_MODEL`. Real lookups never read the synthetic history.

## Readings of the spec, taken conservatively

Where the spec was silent or ambiguous, I took the reading below and wrote it down here.

- **Lua version.** The brief said to use `lupa.lua54` to match Runvil's Lua 5.4. The vendored Runvil links Lua 5.5 (mlua `lua55`, `lua-src` 550.1.1), so the shim uses 5.5. A test runs a paper under 5.4 and gets the same store for this prompt.
- **When replay is allowed.** It is stricter than the spec. Every changed line must sit inside the Assess epilogue, *and* the epilogues may differ only in `INTER_RULE`, `CORROBORATION`, `STRONG`, `ACCUM_FULL`, `EDGE_WINDOW`, `BINARY` and `LABELS`. Anything else needs a full run: an edit to a comment on one of those lines, a change to `QUOTE_WORDS`, or a change to the arithmetic or to `band_span` itself.
- **A paper's total.** The mean of its completed (status ok) repeats. Metrics read the numbers as printed, to two decimals, so a full run and a replay of it score identically.
- **Bands.** Both paperweight's and the reviewers' bands are `label_for(round half up(total))`, under the run's own `LABELS`, as the verdict line does it.
- **Grade-2 rate.** It counts judgements at exactly 2, one per completed repeat. Under `top2` a grade can be 1.83, which is not full marks.
- **Sigma.** The sample standard deviation of a paper's totals across repeats, averaged over papers with at least two completed repeats.
- **Bootstrap.** Nearest-rank 2.5% and 97.5% of 2,000 resamples over papers, with seed 20261026. A resample on which a statistic is undefined is dropped and counted.
- **Bias reading.** "Better" means a smaller absolute bias, so the reading uses the paired difference of |bias|. The table shows the signed difference, as the spec's example does.
- **Failed and incomplete runs.** They are kept and counted, fail gates 1 and 2, and are left out of the agreement metrics. NOT_PROPOSAL papers are left out of agreement and counted.
- **Comparisons refused.** A synthetic run is never compared with a real one, in either direction. Runs on different models are not compared, since the spec gives each model its own baseline.
- **Baselines.** Only full, non-partial runs can be baselines, because replay needs recorded votes. Replays are still recorded in the history, for drift.
- **Recording on merge.** The record job runs on a push to `master` that changes the prompt, not on the pull request closing, because a fork's pull request gets a read-only token.
- **Full runs without real grades.** The full-run job skips, with a notice, while the golden set is absent, rather than spend model calls on synthetic grades.
- **Shim output.** A shim run's `report.md` and `diagnostics.md` start with a SYNTHETIC line. The `Weight:` gate reads the line after it, and only in a run whose metadata says synthetic.
- **Unmarked synthetic papers.** The papers in `data/synthetic/papers/` carry no SYNTHETIC line, because a line would change what the prompt reads. The README and every `papers.jsonl` line mark the set.
- **Paths and hashes.** Prompts are hashed and parsed with CRLF read as LF. `data/`, `tests/fixtures/` and `examples/` are `-text`, so hashes agree across platforms.
- **`tomd_version`.** In the synthetic set it is the workspace tomd version when the set was built. The version that produced the fixtures is not recorded anywhere.
- **Model calls.** Counted as 2 + criteria × sections × samples per proposal, which is the spec's formula. Tokens are not recorded, because paperweight's command line does not report usage.
- **Extra verbs.** Besides the four in the spec, the CLI has `choose`, `record`, `baseline` and `check-set`, which CI and set maintenance need.

## What in the spec turned out wrong or incomplete

- Runvil runs **Lua 5.5**, not 5.4. The prompt's comment "Lua 5.4 makes the loop variable const" describes 5.5 behaviour; 5.4 allows the assignment.
- **"Replay can evaluate the band-span rule"** holds only for `band_span` as it is written today, through `LABELS`. A change to the function itself is a code change replay does not model, so it needs a full run.
- **Tokens.** The spec says to print tokens when the gateway reports usage. paperweight's command line does not pass usage on, so only calls and wall time are recorded.
- **`tests.yml` runs on `push` to `main`, but the default branch is `master`.** Pushes to `master` never build the `paperweight-linux-x86_64` artifact; only pull request runs do. The full-run job therefore finds a binary for a pull request's head commit, but a dispatch on a `master` commit may find none.
- **The repository-wide `uv run pytest` that CLAUDE.md lists fails at collection on a clean checkout.** Eleven tomd test modules do `from conftest import make_block` and get pipeline's `conftest.py`. CI runs each package separately, and that way all tests pass. This was recorded before any work here and left alone.
- **The root `.gitignore` ignores every `data/` directory.** The spec's `packages/calibrate/data/` needs a negation, which was added the way assay's is.
- **`uv lock` with a current uv (0.13) rewrites `uv.lock`** (revision 3 to 5) and drops platform markers from torch's CUDA dependencies. The lock was regenerated with uv 0.9.5, so the diff adds only `calibrate` and `lupa`.

## Open questions for Vinnie

- [ ] Can the ten papers and the three reviewers' per-criterion grades be checked in, and can the reviewers be named or should they be initials? The loader, the schema and `check-set` are ready for them (see "Swapping in the golden set").
- [ ] Are the scripts and runs behind the numbers in the prompt's comments available? Their `diagnostics.md` files would replace the synthetic parity fixtures as milestone 1's evidence. The parser reads the format the current prompt prints; older runs from before the switch to section means would need checking.
- [ ] Which model and gateway setup produced those numbers? The harness needs that id as `CALIBRATE_MODEL`, and its baselines are per model.
- [ ] Would you accept the small Analyze-epilogue change in [calibration-harness-upstream.md](calibration-harness-upstream.md), which appends diagnostics only under `--args diagnostics`? A test applies it as written and shows that reports are byte for byte unchanged without the argument.
- [ ] Is there a monthly budget for full runs, or a local model behind the gateway? A full run of ten papers × three repeats is about 3,000 to 7,000 calls (the spec's table), and the shim's call count matches the spec's formula.
- [ ] Should this stay in wg21-paperflow as `packages/calibrate`, or become a Runvil prompt or Host? The shim already runs the prompt's own Lua outside Runvil. The scripted Host from the Attest CLI runner spec would let replay run through Runvil itself and retire both the shim and the Python copy of the arithmetic.
- [ ] New: the `tests.yml` `push` trigger names `main`, not `master`. Is that intended? The full-run job depends on that workflow's binary artifact.
- [ ] New: should the triage stub's rule match how the store is actually triaged? The shim calls a paper a proposal unless its id is not a P-number or its front matter says `intent: info`. P4020R0, a position paper, counts as a proposal under that rule.
