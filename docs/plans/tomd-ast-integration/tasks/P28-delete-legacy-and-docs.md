# P28 Delete legacy string paths, bridge, `RawBlock`; update docs

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 5 | P27 | P29 | L (mostly deletions) | medium |

## Goal

Remove everything the migration kept alive for parity, update the documentation, and
leave the repo describing one architecture.

## Preconditions

- P27 merged. Both formats run parse -> passes -> writer in production.
- If P29 has not landed, HTML-strategy tables are still `RawBlock`: delete `RawBlock`
  only after P29, otherwise leave exactly that one element and its writer branch and say
  so in the Handoff.

## Read first

- `grep -rn "emit_markdown\|_render_section_md\|render_body\|legacy_bridge\|RawBlock\|dedup_paragraphs\|strip_redundant_body_meta\|strip_orphan_toc_list\|strip_freeform_metadata_lines\|apply_strip_leading_h1\|_normalize_front_matter\|_strip_toc\|_strip_body_metadata_text" packages docs`
- `tests/parity/` (the oracle tests), `STATUS.md` Known divergences

## Change

1. Delete: `lib/pdf/emit.py` section renderers and `emit_markdown` (keep anything the
   parsers import for real: code-grid/format helpers live elsewhere; move any still-needed
   helper into `parsers/`), `lib/html/render.py` string renderers superseded by
   `parsers/html` (keep `prepare_body` and the DOM repair passes, relocating if clearer),
   `parsers/legacy_bridge.py`, the markdown-string normalizers in `lib/shared.py` and
   `api.py`, `PaperDocument.body` remnants, `rawblock_allowlist.py`, the ratchet test,
   and the legacy-vs-AST parity tests (their job is done; keep the corpus-level golden
   tests, which now test production).
2. Keep `scripts/parity_corpus.py` only if it still has a purpose; otherwise delete.
3. Docs, same pass (rename-and-grep discipline): root `CLAUDE.md` package/flow text;
   `packages/tomd/src/tomd/CLAUDE.md` (Architecture step 17, File Map entries for
   `emit.py`, `render.py`, `api.py`, new `parsers/`, `passes/`, `writers/`, `domain/`,
   `resolve.py`), `PDF_ARCH.md`, `HTML_ARCH.md`, `lib/pdf/ARCHITECTURE.md`,
   `lib/html/ARCHITECTURE.md`, `docs/tomd-qa.md` if it references moved paths.
4. Resolve the Known divergences table: each row either fixed here, scheduled, or
   explicitly accepted.

## Do not

- Change any output. Goldens stay byte-identical (except those P29 re-blessed, if
  P29 landed first).

## Tests

Full workspace suite; `grep` for each deleted symbol returns nothing in `packages`,
`tests`, `docs`; `uv run pytest` and `uv run ruff check packages tests` green.

## Acceptance

Checklist green; the Section 7 definition of done in README is satisfied.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed (deleted / modified counts):
Checklist output (tails):
Symbols deleted and grep proof:
Docs updated:
Remaining RawBlock (if any) and why:
Open questions:
```
