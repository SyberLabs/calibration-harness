# P29 Behavior change: no HTML tables

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 5 | P12, P20 | P28 (independent) | L | high (changes output) |

## Goal

Implement the decided direction (project memory: tomd-no-html-tables): tomd never emits
HTML `<table>` in Markdown. This is an intentional output change: it converts the last
`RawBlock` tables to real `Table` elements and re-blesses only the affected goldens.
It is the one task in this plan where parity is NOT the acceptance test.

## Preconditions

- P12 and P20 merged (pipe tables are already real AST). It may land before or after
  P28; coordinate the `RawBlock` deletion (whichever merges second deletes it).
- The human approves the list of affected papers before re-blessing (rebless only
  papers you touched, never `--all`; see `docs/tomd-qa.md`).

## Read first

- Project memory `tomd-no-html-tables`
- `lib/pdf/table.py`: `TableKind`, `TableStrategy`, `_STRATEGY_MAP` (241),
  `_classify_and_annotate`, `_has_multiline_code_cell` and the "any cell contains a newline
  -> force HTML" escape hatch (around lines 3886-4010)
- `lib/pdf/emit.py` `_render_code_comparison` (787; the lossless Tony Table form,
  currently unreachable), `_render_html_table` (862)
- `lib/html/render.py` `_render_mixed_code_table` (1371), `_render_code_table` (1481),
  `_LOSSY_TABLE_MARKER`; `lib/tables.py` (`MIXED_TABLE_MARKER`, `TABLE_OPEN`, ...);
  TABLE_CSS injection in the bridge/emit
- `domain/table.py`, `writers/markdown/tables.py`; the Tony Table fixture
  `tests/fixtures/markdown/sample_documents/tony_table.md` (currently pins the lossy
  `<br>` form)

## Change

1. Domain: add `TableStrategy.CODE_BLOCKS`. Writer: render it as side-by-side fenced
   code blocks with `// <header>` labels exactly as `_render_code_comparison` does;
   update the Tony Table fixture to the new intended form.
2. PDF: `CODE_COMPARISON` -> `CODE_BLOCKS`; `SPEC_TABLE` and `NB_BALLOT` -> `PIPE_TABLE`;
   delete the newline-forces-HTML escape hatch; the PDF adapter (P12) maps `code_blocks`
   to a `Table` with `CODE_BLOCKS` strategy and `CodeCell`s.
3. HTML: mixed and code tables become `Table` (`CODE_BLOCKS` or `PIPE`) in the P20
   handler; delete `_render_mixed_code_table`, `_render_code_table`, and the
   lossy/mixed markers' emission.
4. Delete `lib/tables.py`, `MIXED_TABLE_MARKER`, `TABLE_OPEN/CLOSE`, TABLE_CSS injection,
   and `RawBlock` if P28 already merged (else leave it to P28).
5. Re-bless only the affected goldens/baselines/ideals with the documented tooling; list
   them in the PR with before/after diffs. Update `tests/test_html_render.py`,
   `tests/test_tables.py`, `tests/test_table_analyzer.py` expectations that asserted HTML.
6. Update docs that mention `<table>` output, `MIXED_TABLE_MARKER`, `html_table`.

## Do not

- Re-bless anything not touched. Do not bundle unrelated fixes.

## Tests

Invariant test: no corpus output contains `<table`, `<tr`, `<td`, `<th`, `<style`
(extend the existing `test_paper_document_pure_markdown_table_invariant` idea to real
converted papers). Content-check (`paperflow convert --check-content`) shows no coverage
loss on the touched papers.

## Acceptance

Checklist green; invariant test green; PR lists every re-blessed paper with a reason;
`grep -rn "MIXED_TABLE_MARKER\|html_table\|HTML_TABLE" packages docs` is empty.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Re-blessed papers (list, reason, diff summary):
Content-check results:
Open questions:
```
