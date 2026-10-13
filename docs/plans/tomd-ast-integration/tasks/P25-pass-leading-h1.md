# P25 Pass: emit-level leading H1 strip

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 4 | P24 | none | S-M | medium |

## Goal

Port the emit-level `apply_strip_leading_h1(md, title, max_level)` step (PDF: level 1,
HTML: level 2) to an AST pass using the parser's own `document.metadata.title`.

## Read first

- `lib/shared.py`: `strip_leading_h1` (148), `_titles_match` (202), `apply_strip_leading_h1`
  (211). Behavior to reproduce: first non-blank, non-comment line; an ATX heading with
  depth <= `max_level` is removed when it matches the title (fuzzy: punctuation-stripped,
  case-folded, prefix match) or, for H1 with an empty title, unconditionally; a plaintext
  title echo (no `#`) is removed too; then a bare `Abstract` / `Abstract:` line
  immediately after is promoted to `## Abstract`; leading triple newlines collapse.
- Where the emit-level calls pass the level (`emit_markdown` tail; `convert_html` with 2)
- P23's pass contract

## Change

1. `tomd/passes/leading_h1.py`: `strip_leading_title(document, *, max_level)` over
   `elements`: skip leading non-content elements the legacy skips (HTML comments such as
   `RawBlock`/uncertain markers that are only a comment); if the first content element is a
   `Heading` with `level <= max_level` and a title match (reuse `_titles_match`), remove it;
   if it is a `Paragraph` whose text matches the title, remove it; then promote a first
   remaining `Paragraph` whose text is `abstract`/`abstract:` (case-insensitive) to
   `Heading(2, "Abstract")`.
2. The format decides `max_level`: the PDF parse result uses 1, HTML uses 2 (carry this
   as a parser-level option, not a global).
3. The leading-newline collapse is a string artifact; the AST has no such thing. Confirm
   parity still holds; if not, report (README Section 6).
4. Remove the step from both bridges. Keep the legacy function (still used by the
   API-level step until P27, and as the oracle).

## Do not

- Change `_titles_match`. Do not touch the API-level H1 call (P27).

## Tests

Direct tests vs `apply_strip_leading_h1` on constructed documents: H1 equals title,
H1 differs, no title, H2 with `max_level=2`, plaintext echo, Abstract promotion,
leading comment elements, no front matter. Full parity for both formats.

## Acceptance

Checklist green; parity green; bridges lost the emit-level H1 step.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Known divergences found:
Open questions:
```
