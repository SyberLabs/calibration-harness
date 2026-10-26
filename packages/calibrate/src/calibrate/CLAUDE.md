# calibrate

Calibration harness for the paperweight prompt (`crates/paperweight/paperweight.md`). Project-wide rules live in the root `CLAUDE.md`; the design lives in `docs/plans/calibration-harness.md`, and what is real versus simulated lives in `docs/plans/calibration-harness-status.md`.

## Authority

`paperweight.md` is the authority. The harness reads the prompt; it never edits it, and nothing in `crates/` is modified to suit the harness. The harness's measurements read criteria, labels, rules and thresholds from the prompt at run time, never from copies in Python. The simulator's priors are the one exception, and they are synthetic settings.

## Synthetic data

Synthetic data must never be mistaken for real calibration results.

- Synthetic inputs live only under `data/synthetic/` and `tests/fixtures/synthetic/`. `data/golden/` holds only real data from the team.
- Every synthetic file says so: a first line starting with `SYNTHETIC` in markdown and CSV, `"synthetic": true` on every JSONL line and in every run's `meta.json`.
- Everything the shim backend produces is synthetic, whatever set it ran on.
- Any report, summary or comment built from synthetic inputs starts with the word `SYNTHETIC` on its first line.
- A synthetic run is never a baseline for a real one, and the loader refuses to mix synthetic and golden files.
- Never state a synthetic number as a finding about paperweight, in code, docs or commit messages.

## Layout

- `shim.py` - runs the prompt's own Lua blocks under Lua 5.5 (`lupa.lua55`) with stubs for every model turn. Its docstring lists what it does not reproduce.
- `simulate.py` - the shim's vote provider: a seeded grader drawn around a latent truth, with named profiles. Synthetic by construction; its priors are simulation settings, not measurements.
- `synthetic.py` - builds `data/synthetic/`: real tomd fixture papers with simulated reviewers drawn around the same latent truth. Returns bytes; `scripts/make_synthetic_set.py` writes them.
- `marking.py` - the one rule for saying a file is synthetic, shared by every writer and reader.
- `diagnostics.py` - strict parser for `diagnostics.md`, the report's `Weight:` line and the diagnostics appendix. Keeps printed numbers as printed.
- `aggregate.py` - the Assess epilogue's arithmetic for replay, the epilogue tunables (`EpilogueConstants`), `patch_constants` and `unmodelled_changes`.
- `golden.py` - loads and validates a set (`papers.jsonl`, `papers/`, `grades.csv`): schema, sha256 pins, grades in 0..2, completeness, criteria against the prompt's `CRITERIA` both ways, and the synthetic/golden separation.
- `run.py` - full runs: the `shim` and `binary` backends, the diagnostics patch for the binary, run folders, concurrency (papers in parallel, repeats in order) and failure accounting (kept, counted, never retried). `load_run` reads a folder back.
- `replay.py` - the mode chooser (replay only when every changed line is inside the Assess epilogue and only modelled tunables change), parity on a recorded run, and replay into a new run folder with no model calls.
- `metrics.py` - agreement and stability metrics, nearest-rank bootstrap intervals over papers (2,000 resamples, fixed seed), paired differences. Standard library only.

## Invariants

- The shim locates Lua blocks by section and position and raises `PromptStructureError` when the layout changes. Never fall back to a fixed block index.
- Replay parity is load-bearing: `aggregate.py` must reproduce every number the Lua printed, to the character, on every fixture in `tests/fixtures/synthetic/parity/`. Regenerate those with `scripts/make_parity_fixtures.py`, never by hand. When the epilogue changes in a way `aggregate.py` does not model, replay refuses; it never guesses.
- Lua 5.5, the version Runvil links. Lua 5.4 exists only for the cross-check test.
- The binary backend's environment holds the gateway key: it never goes in a repr, a log line, run metadata or a test's environment.
- Seed everything. No test depends on wall-clock time or the network.
- Standard library for statistics. `lupa` is the only runtime dependency.
- Paper markdown, grades and fixtures are compared byte for byte, so `.gitattributes` marks `data/`, `tests/fixtures/` and `examples/` as `-text`. Prompt text is hashed and parsed with CRLF read as LF.
- Lock the workspace with the uv release that wrote `uv.lock` (revision 3); a newer uv rewrites unrelated entries.
