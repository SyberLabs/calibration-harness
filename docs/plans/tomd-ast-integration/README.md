# tomd AST integration: execution kit

Goal: make `tomd` convert PDF and HTML through `PaperDocument` (the AST merged in
#459) and `MarkdownWriter` (#460/#461), with byte-identical Markdown output, in 29
small PRs that each leave `main` green.

Read order for a new session: this file, then `STATUS.md`, then your task sheet.

| File | Purpose |
|------|---------|
| `README.md` | Rules, mechanism, dependency graph, session prompts (this file) |
| `STATUS.md` | Progress board, decision log, known divergences. Single writer. |
| `design.md` | Gap analysis and rationale (why the tasks look the way they do) |
| `tasks/Pxx-*.md` | One self-contained task sheet per PR |

## 1. Rules (apply to every task)

Repo rules (from the root and `packages/tomd/src/tomd/CLAUDE.md`):
- Never commit, merge, push, or touch `CHANGELOG.md`. Leave verified changes in the
  working tree; the human commits.
- No lazy imports in production code. `__init__.py` files hold only re-exports,
  `__all__`, `__version__`. Use `logging`, never `print()`. Tunable thresholds are
  named module-level constants. No em dashes anywhere (code, comments, docs).
- New `.py` files carry the BSL-1.0 header; copy it from
  `packages/tomd/src/tomd/writers/base.py`.
- No comments that restate code. Comment only non-obvious domain constraints.
- Evidence before assertions: do not say "done" without running the Section 4
  checklist and pasting its output.

Plan rules:
- **Parity is the law.** Until the two cutover PRs (P15, P22) and the pass PRs, the
  new path must produce byte-identical Markdown to the legacy path. Never edit a
  golden, snapshot, or baseline to make parity pass. Do not fix legacy bugs in a
  parity PR; record them in `STATUS.md` under Known divergences and keep the quirk.
- **One family per PR.** Touch only the files the task sheet lists. If you believe
  another file must change, stop and report (Section 6).
- **Single writer for `STATUS.md`.** In a sequential workflow (one branch at a time)
  the human, or the session at the human's request, updates it. In a parallel wave,
  task agents never edit it (separate worktrees would conflict) and the orchestrator
  or human updates it in the main checkout.
- **Twin tests.** New writer and adapter code is tested against the legacy
  renderer as an oracle: build the legacy input (a `Section`, a DOM fragment) and the
  AST for the same content and assert equal output. Hand-written expected strings
  are allowed only when copied from a legacy test or a golden.

## 2. Mechanism: why `main` never breaks

1. **Dark path.** The AST converter is a separate entry point under
   `tomd/parsers/<fmt>/`, called only by `tests/parity/` until the cutover PR for that
   format. `api.convert_paper_full` keeps calling legacy code. Cutover is a one-line
   dispatch change; rollback is a revert.
2. **`RawBlock`.** One temporary element, `RawBlock(markdown, origin)`, which the
   writer emits verbatim. The skeleton PR maps every legacy section or DOM node to a
   `RawBlock` holding the legacy-rendered string, so output is identical on day one.
   Each later PR converts one family from `RawBlock` to real nodes. Output never
   changes. `RawBlock` is deleted in P28/P29.
3. **Ratchet.** `tests/parity/test_rawblock_ratchet.py` asserts that the set of
   `RawBlock.origin` values emitted over the corpus equals an allow-list in
   `tests/parity/rawblock_allowlist.py`. Converting a family means deleting its entry;
   adding one fails review.
4. **Parity gate.** `tests/parity/` compares legacy and AST output byte for byte on
   the committed corpus at two levels: converter output (`run_pipeline(path).md`,
   `convert_html(path)`) and API output (`convert_paper_full` with a fixed `meta`).
   `scripts/parity_corpus.py` (added in P08) does the same over `$WG21_DATA_DIR`;
   run it before P15 and P22.
5. **Bridge.** `parsers/legacy_bridge.py` re-applies the legacy markdown-string
   passes after the writer. Pass PRs (P23-P27) move them into AST passes one at a time
   in legacy order; P28 deletes the bridge.

An env var is deliberately not used: it would be a second runtime configuration that
nothing exercises, and parity needs both paths in one process.

## 3. Dependency graph

```
W0  P01 -> P02
W1  P02 -> { P03 lists | P04 wording+quote | P05 types+diagnostics | P06 uncertain+prompts | P07 escaping+RawBlock }
W2  (P05,P06,P07) -> P08 skeleton -> P09 inline/heading/para -> { P10 lists | P11 code | P12 tables | P13 images+captions } -> P14 wording -> P15 PDF cutover
W3  P08 -> P16 HTML skeleton -> P17 inline/heading/para -> { P18 code | P19 lists | P20 tables | P21 wording+quote+dl } -> P22 HTML cutover
W4  (P15,P22) -> P23 -> P24 -> P25 -> P26 -> P27      (sequential: legacy chain order)
W5  (P27) -> P28 delete legacy        P29 no-HTML-tables (independent after P12,P20)
```

Detailed edges are in each sheet's `Deps`. A task is **ready** when its status is
`todo` and every dep is `merged` in `STATUS.md`. W2 and W3 run in parallel. Tasks
sharing a bracket `{...}` CAN run in parallel (separate worktrees) but need not: running them one after another on plain branches is fine. Expected parallel conflicts
are limited to export lists and the adapter dispatch table.

Why W4 is sequential and after both cutovers: the legacy string passes run in a
fixed order (emit-level: `dedup_paragraphs`, `strip_redundant_body_meta`,
`strip_orphan_toc_list`, TABLE_CSS, H1; API-level: front-matter normalize,
metadata-table strip, freeform metadata lines, H1, `strip_toc`). An AST pass runs
before the writer, so ported passes must be a prefix of that chain, and a pass cannot
act on content that is still a `RawBlock`.

## 4. Standard checklist (every task)

Run from the repo root, on the task's branch (or worktree). Paste the tail of each output.

```bash
uv sync --all-packages --group dev          # first time in a checkout
uv run --package tomd pytest packages/tomd/tests -q
uv run --package tomd pytest packages/tomd/tests/parity -q    # once P08 exists
uv run ruff check packages tests
uv run pyright <files you changed>          # CI treats pyright as advisory; keep changed files clean
uv run pytest -q                            # full workspace, before reporting done
git status --short                          # confirm only the sheet's files changed
```

## 5. Session recipes

### 0. First step (human)

Commit this directory to `main` (P00) so the plan is tracked and survives branch
switches (untracked files do survive a plain `git switch`, but a plan that is not in git
is easy to lose). Worktrees additionally require it, since they only see committed
files. Then set P00 to `merged` in `STATUS.md`.

Default workflow is sequential on plain branches, one task at a time:
`git switch main && git pull && git switch -c tomd-ast/P03`. Cut each branch from
up-to-date `main` after the previous PR merges; if you want to keep going before the
review lands, stack the next branch on the previous one and rebase after it merges.
Use worktrees only for the parallel wave recipe (B).

### A. Execute one task (human-driven, single agent)

```
Execute docs/plans/tomd-ast-integration/tasks/P03-lists.md.
First read docs/plans/tomd-ast-integration/README.md sections 1, 2, 4 and 6.
Confirm every dep in the sheet is `merged` in STATUS.md; if not, stop.
Work on branch tomd-ast/P03 (already checked out; do not create worktrees).
Follow the sheet exactly. Do not commit. Finish with the Section 4 checklist
output and the sheet's Handoff block filled in.
```

### B. Orchestrate a wave (parallel agents)

```
You are the orchestrator for the tomd AST integration.
Read docs/plans/tomd-ast-integration/README.md and STATUS.md.
1. List ready tasks (status todo, all deps merged).
2. For each ready task that the README graph allows in parallel, spawn one Agent
   with isolation "worktree" (parallel waves only) and this prompt: "Execute
   docs/plans/tomd-ast-integration/tasks/<sheet>. Read README.md sections 1, 2, 4,
   6 first. Do not edit STATUS.md. Do not commit. Report with the sheet's Handoff
   block."
3. When each agent returns, do not trust its summary: in its worktree rerun the
   Section 4 checklist and inspect `git diff --stat` against the sheet's file list.
4. Update STATUS.md in the main checkout: `review`, branch, notes, any Known
   divergence. Report a table of results and anything that needs a human decision.
Never commit or push. Never start a task whose deps are not `merged`.
Cap parallelism at 4 agents.
```

### C. Review a finished task

```
Review the working tree in ../wg21-paperflow-P03 against
docs/plans/tomd-ast-integration/tasks/P03-lists.md. Check: only listed files
changed; no golden/snapshot edits; ratchet moved as the sheet says; twin tests
exist; Do-not list respected; Handoff block honest. Then run /code-review.
```

### D. Resume or recover

If a session died mid-task, start recipe A on the same branch and add: "The
branch already has partial work. Run `git status` and `git diff`, compare with
the sheet, finish or revert, then continue." If parity fails and the cause is a
legacy quirk, follow Section 6.

## 6. Stop and report (do not improvise)

Stop, leave the tree as is, and report when:
- a dep is not `merged`, or the sheet's "Read" references no longer exist;
- parity differs and the cause is a legacy bug or order dependence you cannot
  reproduce faithfully (never "fix" the legacy side, never weaken the oracle);
- the task needs a file outside the sheet's list, or a domain change another task owns;
- a W4 pass cannot reach byte equality after a good-faith port (see P23 "Pass
  contract": keep it as a documented polish step, or propose a behavior change);
- the diff would exceed about 600 changed lines excluding fixtures (the PR is too big;
  propose a split).

The report format is the sheet's Handoff block with `Status: blocked` and the evidence.

## 7. Definition of done for the program

- `api.convert_paper_full` runs parser -> passes -> writer for both formats.
- `RawBlock`, `legacy_bridge.py`, `PaperDocument.body`, and the markdown-string
  normalizers in `api.py` and `emit.py` are gone, or any normalizer that could not be
  ported faithfully is retained as an explicitly documented polish stage with the
  decision recorded in `STATUS.md`.
- Golden snapshots and baselines are unchanged except those P29 intentionally
  re-blessed.
- Root and package `CLAUDE.md` files, `PDF_ARCH.md`, `HTML_ARCH.md`, and
  `lib/*/ARCHITECTURE.md` describe the new flow.
