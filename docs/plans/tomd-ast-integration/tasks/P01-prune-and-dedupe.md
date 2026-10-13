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
Status: done | blocked
Files changed:
Checklist output (tails):
Fixtures whose bytes changed and why:
Known divergences found:
Open questions:
```
