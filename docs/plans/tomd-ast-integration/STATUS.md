# Status board

Single writer: the human, or the orchestrator session, in the main checkout. Task
agents never edit this file.

Status values: `todo` | `in-progress` | `review` (work done, awaiting human review and
commit) | `merged` | `blocked`.
A task is ready when it is `todo` and all its deps are `merged`.

Last updated: 2026-10-13 (plan created, nothing started)

## Board

| ID | Task | Wave | Deps | Status | Branch / PR | Notes |
|----|------|------|------|--------|-------------|-------|
| P00 | Commit the plan docs to `main` (human action; keeps the plan tracked across branches) | 0 | - | merged | 3d4f3b3 | |
| P01 | Prune and dedupe domain and writer | 0 | P00 | review | tomd-ast/P01 | Golden QA test fails only because `.claude/skills/tomd-*` are deleted in the working tree (R1 in the sheet) |
| P02 | Meta redesign: `write(document)`, `MailingRecord`, `resolve_metadata` | 0 | P01 | todo | | |
| P03 | Lists model and writer | 1 | P02 | todo | | |
| P04 | Wording and blockquote model and writer | 1 | P02 | todo | | |
| P05 | Unify types, `Diagnostics`, trailer markers | 1 | P02 | todo | | |
| P06 | Uncertain element, prompts, provenance | 1 | P02 | todo | | |
| P07 | Escaping policy and `RawBlock` | 1 | P02 | todo | | |
| P08 | Parity harness, ratchet, PDF skeleton, bridge | 2 | P05, P06, P07 | todo | | |
| P09 | PDF inline spans, headings, paragraphs | 2 | P08 | todo | | |
| P10 | PDF lists | 2 | P09, P03 | todo | | |
| P11 | PDF code | 2 | P09 | todo | | |
| P12 | PDF pipe tables | 2 | P09 | todo | | |
| P13 | PDF images, captions, wording problems | 2 | P09 | todo | | |
| P14 | PDF wording | 2 | P10, P11, P04 | todo | | |
| P15 | PDF cutover | 2 | P09-P14 | todo | | |
| P16 | HTML skeleton | 3 | P08 | todo | | |
| P17 | HTML inline, headings, paragraphs | 3 | P16, P09 | todo | | |
| P18 | HTML code | 3 | P17 | todo | | |
| P19 | HTML lists | 3 | P17, P03 | todo | | |
| P20 | HTML pipe tables | 3 | P17 | todo | | |
| P21 | HTML wording, blockquote, note blocks, dl | 3 | P17, P04 | todo | | |
| P22 | HTML cutover | 3 | P16-P21 | todo | | |
| P23 | Pass: `dedup_paragraphs` | 4 | P15, P22 | todo | | |
| P24 | Pass: redundant body meta, orphan TOC list | 4 | P23 | todo | | |
| P25 | Pass: emit-level leading H1 strip | 4 | P24 | todo | | |
| P26 | Pass: `resolve_metadata` swap-in, metadata-table strip | 4 | P25 | todo | | |
| P27 | Pass: freeform metadata lines, API-level H1, TOC strip | 4 | P26 | todo | | |
| P28 | Delete legacy emit/render string paths, bridge, `RawBlock`; update docs | 5 | P27 | todo | | |
| P29 | Behavior change: no HTML tables (`CODE_BLOCKS`, delete `lib/tables.py`) | 5 | P12, P20 | todo | | |

## Ratchet (RawBlock origins still emitted)

Mirror of `tests/parity/rawblock_allowlist.py`, updated after each merge.

| Format | Remaining origins |
|--------|-------------------|
| PDF | not yet measured (P08) |
| HTML | not yet measured (P16) |

## Decision log

| Date | Decision | Why |
|------|----------|-----|
| 2026-10-13 | Tables with HTML strategy stay `RawBlock` until P29; integration does not wait for it | Independent work; either order works |
| 2026-10-13 | PDF parser before HTML parser | `Section` is already an IR; HTML needs a rewrite |
| 2026-10-13 | Remove `wording_tags`, `Heading.id`, `rowspan`/`colspan`, domain `TableKind`, `MIXED_HTML`, `ImageElement`, `ImageRef` from the AST | No consumer; reversible |
| 2026-10-13 | `MailingRecord` lives in `tomd/resolve.py`; the API keeps taking a `meta` dict and builds it internally; CLI callers unchanged | Smaller blast radius than changing the public API |
| 2026-10-13 | No env-var switch; dark path plus per-format dispatch flip | See README Section 2 |
| 2026-10-13 | `PaperMetadata.audience` and `reply_to` keep `list[str] | str` | Legacy `format_front_matter` renders a string as a scalar and a list as YAML list; collapsing would change bytes. Deferred as a behavior change |
| 2026-10-13 | AST passes (P23-P27) come after both cutovers, in legacy chain order | Passes must be a prefix of the legacy chain and cannot see `RawBlock` content |
| 2026-10-13 | W4 passes may be retained as a documented polish stage if a byte-identical AST port is not achievable | The legacy passes are text heuristics (plaintext title echo, bare-Abstract promotion, newline collapse); fidelity to bytes may not be provable |
| 2026-10-13 | Canonical `SkipReason`, `ExtractedImage`, `Confidence` move into `tomd.domain`; `lib/pdf` re-exports them | Domain must not import `lib/pdf` |

## Known divergences (legacy quirks preserved for parity)

Add a row whenever a task finds legacy behavior that looks wrong but must be kept
until a behavior PR. Format: ID found in, quirk, where, proposed fix.

| Found in | Quirk | Location | Proposed fix |
|----------|-------|----------|--------------|
| (planning) | Blockquote blank lines render as `> ` with a trailing space in HTML-sourced output | `lib/html/render.py` `_render_blockquote` and the note/example branches | Bare `>`; behavior PR after P28 |
| (planning) | Uncertain-marker line numbers use a running estimate that ignores later string passes | `emit.py` `emit_markdown` | Out of scope; revisit after P28 |

## Parity runs (maintainer corpus)

| Date | Task | Corpus size | Result |
|------|------|-------------|--------|
| | | | |
