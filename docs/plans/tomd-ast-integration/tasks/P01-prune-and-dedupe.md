# P01 Prune and dedupe the domain and writer

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 0 | P00 | none | S-M | low |

## Goal

Remove AST features with no consumer and collapse duplicated definitions, so later
tasks extend a smaller, single-sourced model. No converter changes. No behavior
change for any AST the writer can build today, except the removed features.

## Read first

- `packages/tomd/src/tomd/domain/*.py`, `writers/markdown/*.py`
- `packages/tomd/src/tomd/lib/metadata_yaml/format.py` (`FRONT_MATTER_ORDER`,
  `format_front_matter`, `_yaml_value`): the single source of truth for front matter
- `design.md` gaps G5, G6, G7, G12
- Tests: `tests/domain/test_domain_models.py`, `tests/writers/**`,
  `tests/fixtures/sample_documents.py`, `tests/fixtures/markdown/sample_documents/*.md`,
  `tests/conftest.py`

## Change

1. Delete `ImageElement` (+ `ElementKind.IMAGE`, exports, writer branch in `blocks.py`)
   and `ImageRef` (`domain/image.py`, exports). Keep domain `ExtractedImage` for now
   (P05 replaces it).
2. Delete the `wording_tags` parameter from `write_span(s)`, `write_element`,
   `write_table`, `MarkdownWriter.write`. `StrikethroughSpan` always renders `<del>`;
   `UnderlineSpan` always renders `<ins>` (the former default). Remove the
   `~~`/`<u>` test and its assertions.
3. Delete `Heading.id` (and `from_text(..., id=)`) and the `{#id}` rendering. Remove
   ids from `sample_documents.py` and the expected `.md` fixtures.
4. Delete `Cell.rowspan`, `Cell.colspan`, and `TextCell.from_text` params for them.
5. Delete domain `TableKind`, `Table.kind`, and `TableStrategy.MIXED_HTML`
   (`TableStrategy` keeps `PIPE`; P29 adds `CODE_BLOCKS`). Update the fixtures that
   set `kind=`.
6. `writers/markdown/front_matter.py`: `write_front_matter` builds a dict from
   `PaperMetadata.to_dict()` (or passes a dict through) and delegates to
   `lib.metadata_yaml.format.format_front_matter`. Delete `_yaml_escape`, `_yaml_value`,
   `_YAML_SPECIAL_CHARS` and the duplicate title/intent logic.
7. `domain/metadata.py`: import `FRONT_MATTER_ORDER` from
   `lib.metadata_yaml.format` instead of redefining it; keep it re-exported from
   `domain/__init__.py`. Verify there is no import cycle.
8. One inline-code formatter: make `spans._format_code_span` public as
   `format_code_span` and use it from `tables.py`; delete the copy there.
9. Leave `audience` / `reply_to` as `list[str] | str` (legacy renders a string as a
   scalar and a list as a YAML list; changing it changes bytes).

## Do not

- Touch `api.py`, `lib/`, `cli`, or any golden. Do not add features.
- Change rendered output of any remaining construct. If a fixture's expected bytes
  must change for a reason other than a removed feature, stop and report.

## Tests

- Existing writer tests updated for removals; add one test that
  `write_front_matter(PaperMetadata(...))` equals `format_front_matter(meta.to_dict())`
  for title with `::`, `Info:` intent inference, list `reply-to`, extra keys, and an
  empty metadata (returns `""`).
- `grep -rn "ImageElement\|ImageRef\|wording_tags\|MIXED_HTML\|TableKind\|rowspan\|colspan\|\.id\b" packages/tomd/src/tomd/domain packages/tomd/src/tomd/writers packages/tomd/tests/writers packages/tomd/tests/domain` shows no stale references (note `lib/pdf` has its own `TableKind` and `rowspan` in `emit.py`: those stay).

## Acceptance

README Section 4 checklist green; `git status --short` lists only `domain/`, `writers/`,
`tests/domain`, `tests/writers`, `tests/fixtures/sample_documents.py`,
`tests/fixtures/markdown/sample_documents/`, `tests/conftest.py` (if needed).

## Handoff (fill in at the end)

```
Status: done (one pre-existing failure outside the sheet, see Open questions 1)
Files changed:
  domain/{__init__,elements,image,metadata,table}.py
  writers/markdown/{blocks,front_matter,spans,tables,writer}.py
  tests/domain/test_domain_models.py
  tests/writers/markdown/{test_blocks,test_front_matter,test_markdown_writer,
    test_paper_document,test_spans,test_tables}.py
  tests/fixtures/sample_documents.py
  tests/fixtures/markdown/sample_documents/*.md (6 files)
  (conftest.py not needed)
Checklist output (tails):
  tomd pytest:    1 failed, 2517 passed, 7 skipped, 1 xfailed
                  (failed: test_golden_qa.py::test_review_ideal_embeds_committed_skill_contract)
  ruff:           All checks passed!
  pyright:        0 errors, 0 warnings (changed files)
  stale grep:     no matches
  other packages (per package, as CI runs them): all passed
  git status:     only the sheet's files, plus STATUS.md and this sheet
Fixtures whose bytes changed and why:
  All six sample_documents/*.md lost the `{#id}` heading suffix (Heading.id removed). Nothing else.
Known divergences found:
  Old vs new write_front_matter differential (189 inputs, old writer taken from HEAD):
  3 remaining diffs, all requiring a blank, 0 or False `intent` together with an `Info:`/`Ask:`
  title. The old writer omitted `intent`; the new one infers it (or renders 0/False). Not a real
  input (`PaperMetadata.intent` is a str); fixing it needs a change in lib/, which is out of scope.
  Blank list items, whitespace-only scalars and tuples (R2) are now filtered as before.
Open questions:
  1. Failing golden QA test: it reads the committed .claude/skills/tomd-review/SKILL.md, which is
     deleted in the working tree (the three .claude/skills/tomd-* deletions predate P01 and are
     not part of it). Restore them or move the deletion to its own change.
  2. `uv run pytest -q` at the repo root stops with 11 collection errors (conftest module-name
     clash, packages/pipeline/tests vs packages/tomd/tests). Confirmed identical on a clean
     export of main, so pre-existing. CI runs per package, so the README checklist command
     needs adjusting.
```

---

# Review follow-ups

Adversarial review of the P01 working tree (2026-10-13). The core refactor is clean: stale-reference grep is empty, ruff and pyright are clean, fixture diffs are only `{#id}` removals, front-matter bytes are unchanged for every realistic input. The items below must be resolved before P01 is reported done. Items are ordered by severity.

## R1. Restore or separate the `.claude/skills` deletions (blocker)

`git status` shows these deleted, which is outside the acceptance file list:

- `.claude/skills/tomd-review/SKILL.md`
- `.claude/skills/tomd-surgical-edits/SKILL.md`
- `.claude/skills/tomd-surgical-edits/architecture.md`

This breaks `packages/tomd/tests/test_golden_qa.py::test_review_ideal_embeds_committed_skill_contract` (`'# tomd Review' not in prompt`).

Fix: `git restore .claude/skills`. If the deletion was intentional, move it to its own change and update or remove that test there. It must not ride along with P01.

Done when: `git status --short` lists only the acceptance paths and the golden QA test passes.

## R2. Preserve blank-value filtering in `write_front_matter` (medium)

The old writer's `_yaml_value` dropped blank content. `format_front_matter` does not, and `write_front_matter` only filters `None`, `""` and `[]` before delegating. A differential test of the old writer (from `HEAD`) against the new one found these divergences:

| Input | Old output | New output |
|-------|------------|------------|
| `reply_to=[""]` or `["a", ""]` | blank item dropped | `  - ""` emitted |
| whitespace-only scalar, e.g. `intent="  "` | omitted | `intent:   ` (trailing spaces) |
| tuple value in `extra` | YAML list | `k: "('a', 'b')"` |

The plan says to stop and report any byte change beyond the removed features. Delegation itself was prescribed (step 6), so the divergence should have been reported.

Fix: in `writers/markdown/front_matter.py`, extend the pre-delegation filter to drop whitespace-only strings and blank items inside list values, and normalize tuples to lists. Do not edit `lib/` (the plan forbids it). If any divergence is deliberately kept, record it under "Known divergences found" in the Handoff.

Done when: the old-vs-new differential on blank items, whitespace-only values, and tuples shows no diffs (or each remaining diff is listed in the Handoff).

## R3. Replace the tautological front-matter test with real coverage (medium)

`test_write_front_matter_matches_format_front_matter` compares `write_front_matter(m)` with `format_front_matter(m.to_dict())`, which is exactly what the implementation does. It cannot catch a regression in either function, never exercises the wrapper's own filter, and never exercises the dict-input path. The `empty` parametrize case and `test_write_front_matter_empty_metadata_is_empty_string` assert nearly the same thing.

Fix in `tests/writers/markdown/test_front_matter.py`:

- Keep the plan-required equivalence test, but add literal expected-bytes cases for: title containing `::`, `Info:` intent inference, list `reply-to`, extra keys, empty metadata.
- Add cases for the R2 blank-value inputs (blank list item, whitespace-only scalar, tuple) through both `PaperMetadata` and plain-dict input.
- Remove the redundant empty-metadata assertion.

Done when: reverting the R2 filter makes at least one new test fail.

## R4. Clean up vacuous test names and redundant setup (low)

- `tests/writers/markdown/test_tables.py::test_write_table_never_emits_html_even_for_tony_table_strategy` now sets the default `TableStrategy.PIPE`, so the name no longer describes anything. Rename it (for example `test_write_table_never_emits_html`) or fold it into the neighboring pipe-table tests.
- Drop the explicit `strategy=TableStrategy.PIPE` (the default) where it was only left over from `MIXED_HTML`: `test_markdown_writer.py`, `test_tables.py`, `test_domain_models.py`. Keep it only where the test is about the strategy itself.

Done when: no test name or argument refers to behavior that no longer exists.

## R5. Finish the process items (low)

- Update `STATUS.md`: P01 row from `todo` to the correct state, with branch name.
- Fill in the Handoff block above (files changed, checklist tails, fixture bytes changed and why, known divergences from R2, open questions).
- Resolve the checklist's last step. `uv run pytest -q` currently stops with 11 collection errors: `ImportError: cannot import name 'make_block' / 'make_section' / 'make_span' from 'conftest'`, a `conftest` module-name clash between `packages/pipeline/tests` and `packages/tomd/tests`. It looks unrelated to P01 (no conftest touched) but is unverified on a clean `main`. Confirm on `main`; if pre-existing, list it under "Open questions" in the Handoff rather than fixing it here.

Done when: STATUS and Handoff are filled in, and the `uv run pytest -q` result is either green or explained as pre-existing.

## R6. Optional nit

`domain/metadata.py` gained `__all__` only to keep the `FRONT_MATTER_ORDER` re-export lint-clean, and no other domain module has one. Either leave it or use `from ... import FRONT_MATTER_ORDER as FRONT_MATTER_ORDER` for consistency. Note for later tasks: `domain` now imports from `lib`, so P02 onward must not add a `lib` import of `domain` (that would create a cycle).

## Resolution log

| Item | Outcome |
|------|---------|
| R1 | Not changed. The deletions predate P01 and belong to the working tree owner. Needs a decision: `git restore .claude/skills`, or move the deletion (and the golden QA test) to its own change. |
| R2 | Done. `write_front_matter` drops blank scalars and blank list items and normalizes tuples before delegating. Three pathological diffs remain, listed in the Handoff. |
| R3 | Done. Literal expected-bytes tests plus blank-value cases through `PaperMetadata` and dict input. Reverting the filter fails 15 tests. |
| R4 | Done. Renamed `test_write_table_never_emits_html`; dropped leftover `strategy=TableStrategy.PIPE` in `test_markdown_writer.py`, `test_tables.py`, `test_domain_models.py` and the Tony table fixture. |
| R5 | Done. STATUS and Handoff filled in. The root-level `pytest` collection errors are confirmed pre-existing on `main`. |
| R6 | Done. `domain/metadata.py` uses `import ... as FRONT_MATTER_ORDER` instead of `__all__`. |
