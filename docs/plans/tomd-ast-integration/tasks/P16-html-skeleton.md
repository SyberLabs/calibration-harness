# P16 HTML skeleton

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 3 | P08 | W2 tasks | M | high |

## Goal

Create the dark HTML path with the same structure as the PDF skeleton: every top-level
DOM node becomes a `RawBlock` holding the legacy-rendered string, the metadata and
diagnostics plumbing is real, and the parity test on HTML is green. Fallback to
`RawBlock` must work at any nesting level so later tasks convert families one at a time.

## Read first

- `lib/html/convert.py` (`convert_html`, whole file): metadata extraction, DOCUMENT
  number override from filename, boilerplate stripping, problems -> prompts, body
  render, truncation marker, title fallback from the first `##` heading, leading `---`
  stripping, the string chain (`dedup_paragraphs`, `strip_redundant_body_meta`,
  `strip_orphan_toc_list`, `apply_strip_leading_h1(md, title, 2)`)
- `lib/html/render.py`: `render_body` (468; it also runs the DOM repair passes and
  mutates the soup), `_render_children` (514), `_render_element` (532)
- `lib/html/images.py` (`HtmlImagesResult`)
- `tests/test_html_golden.py` (stems, `golden/sources/*.html`, `golden/snapshots/*.md`),
  `tests/test_html_integration.py`
- `parsers/` from P08 (protocol, bridge, parity harness, ratchet)

## Change

1. Refactor `lib/html/render.py` `render_body` into two steps with no output change:
   `prepare_body(soup, generator) -> Tag` (the DOM repair passes and heading
   normalization) and the existing string rendering over that tag. `render_body` calls
   both. The AST path calls `prepare_body` then its own dispatcher.
2. `parsers/html/dispatch.py`: `to_elements(node, generator) -> list[BlockElement]`.
   Mirrors `_render_children`: text nodes, comments/PI skipped as legacy; each Tag goes
   to a registry `HANDLERS: dict[str, Callable]` consulted by tag name; the default is
   `RawBlock(legacy _render_element(tag, generator), origin=f"html:{tag.name}")` and
   skips `None` results. The registry is empty in this PR.
3. `parsers/html/parser.py`: `parse_html(path, *, html_images_result) -> PaperDocument`
   reproducing `convert_html` up to the render step: metadata (`PaperMetadata.from_dict`),
   `Diagnostics` (`images_truncated`, `source_image_count`, `extra_prompts` built from
   `problems` with the legacy preamble), images from `html_images_result`.
4. `parsers/legacy_bridge.py`: add `render_html(document)`: writer body, then
   `convert_html`'s tail in order (leading `---` strip loop, title fallback from the
   first `##` heading regex, truncation marker as in legacy, string chain with H1 level 2,
   trailing newline). Share the named-step list mechanism with the PDF bridge.
5. `tests/parity/test_html_parity.py`: corpus = the HTML stems from `test_html_golden.py`
   plus `tests/fixtures/html/*.html`. Converter-level (`convert_html(path)` vs dark path)
   and API-level assertions. Seed `HTML_ALLOWLIST` in `rawblock_allowlist.py` and extend
   the ratchet test to cover it.

## Do not

- Change any HTML output or golden. Do not convert any family. Do not wire into `api`.

## Tests

The HTML parity suite is the test. Plus a unit test that `prepare_body` followed by the
legacy string render equals `render_body` on every fixture.

## Acceptance

Checklist green incl. `tests/parity`; `tests/test_html_golden.py` unchanged.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Corpus size / initial HTML allow-list (paste):
Known divergences found:
Open questions:
```
