# P17 HTML inline spans, headings, paragraphs

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 3 | P16, P09 | W2 tasks | L | high |

## Goal

Convert headings, paragraphs, `hr`, and the inline span builder for HTML from
`RawBlock` to real nodes, byte-identical. This is the foundation for P18-P21.

## Read first

- `lib/html/render.py`: `_inline_text_nodes` (1577, the whole inline algorithm),
  `_inline_text`, `_render_heading` (643), `_HEADING_*_CLASSES`, `_BOLD_WRAP_RE`,
  `_render_paragraph` (681), `_is_code_paragraph`, `_collapse_whitespace` (690),
  the `hr`/`section`/`figure`/... pass-through branches of `_render_element`
- `lib/shared.py` `strip_format_chars`; `ALLOWED_LINK_SCHEMES`
- `writers/markdown/spans.py` and `escape.py`; `parsers/pdf/inline.py` (P09) for naming
  conventions (do not share code unless it is truly format-neutral)

## Legacy quirks the span builder must reproduce

- Emphasis/strong/code render `**` + `stripped` + `**`: whitespace inside the tag is
  DROPPED, whereas the writer keeps edge whitespace outside the delimiters. Strip
  inside the adapter and keep the surrounding text nodes' own spaces.
- `<code>` renders `` `stripped` `` with no backtick-fence handling; the writer's
  `format_code_span` extends the fence for embedded backticks. If any corpus input
  contains a backtick inside `<code>`, report it (Known divergence) and reproduce
  legacy with a model that yields the same bytes.
- Links: fragment-only hrefs and non-allowlisted schemes drop to bare text; `br` is a
  literal `\n`; `ins`/`del` use `wording_tag_open`; `sub`/`sup` are raw tags; `svg`,
  `img`, `style`, `script` are skipped; unknown tags pass their inner text through.
- Headings: `\n` -> space, double spaces collapsed, a full `**...**` wrap removed,
  empty-after-stripping headings dropped, section-number and self-link spans skipped.

## Change

1. `parsers/html/inline.py`: `inline_to_spans(nodes, skip_classes=frozenset()) ->
   list[Span]`, producing domain spans so that the writer's output equals
   `_inline_text_nodes`. Include a whitespace-normalization step equivalent to
   `_collapse_whitespace` applied at paragraph level.
2. `parsers/html/blocks.py`: handlers for `h1`-`h6` (`Heading`), `p` (`Paragraph`; the
   code-paragraph case becomes a `CodeBlock` with language `cpp`), `hr`
   (`ThematicBreak`), and the transparent containers (`section`, `main`, `article`,
   `figure`, ... which return the concatenation of their children's elements). Register in `HANDLERS`.
3. Remove the corresponding `html:*` origins from the allow-list.

## Do not

- Convert lists, code blocks, tables, wording, blockquote, dl. Do not change legacy
  `render.py` behavior.

## Tests

Twin tests in `tests/parity/test_inline_html.py`: parse an HTML snippet with
BeautifulSoup and assert `write_spans(inline_to_spans(children)) ==
render._inline_text(el)` for the quirk list above and a table of real-world snippets
(nested inline, links with each scheme, `<br>`, entities, format characters, `<svg>`).
Headings and paragraphs: compare `write_element(handler(el))` with
`render._render_heading` / `_render_paragraph`. Plus HTML corpus parity.

## Acceptance

Checklist green; ratchet shrank by the converted origins only.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Ratchet before -> after:
Quirks reproduced / any not reproducible:
Known divergences found:
Open questions:
```
