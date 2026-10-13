# P18 HTML code blocks

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 3 | P17 | P19, P20, P21 | M | medium |

## Goal

Convert HTML code constructs from `RawBlock` to `CodeBlock`, byte-identical, including
language detection.

## Read first

- `lib/html/render.py`: `_render_pre` (869), `_render_code_block_custom` (878),
  `_detect_code_language` (885) and everything it uses (`_resolve_lang_token`,
  `_resolve_explicit_lang`, `_lang_from_classes`, `_lang_from_content`,
  `_looks_like_shell/json/grammar/diagram`, the `_*_RE` constants, 700-868), the `div`
  branches for `sourceCode` and `code` (`_render_div`, 905), the `code` branch with
  `div.code` and hatemplate `itemdeclcode` in `_render_element`, `<span class="code">`
  paragraphs (handled in P17), eelis synopsis code in `_render_eelis_block` (leave to P21)
- `writers/markdown/blocks.py` `_format_code_block`
- Tests: code cases in `tests/test_html_render.py`, `tests/test_html_generators.py`

## Change

1. `parsers/html/code.py`: handlers for `pre`, `code-block`, `div.sourceCode`,
   `div.code`, and the `code` special cases. The adapter calls the existing
   `_detect_code_language` and text extraction (import; do not fork) and returns
   `CodeBlock(code=text, language=lang)`. Empty language means an unlabeled fence.
2. Verify writer fence selection equals legacy (legacy always uses a three-backtick
   fence; the writer lengthens it when the code contains backtick runs). If a corpus
   input contains triple backticks inside code, report it before choosing.
3. Register; remove the converted `html:pre`, `html:code-block`, and code-`div` origins.

## Do not

- Touch language detection. Do not convert table cells containing `<pre>` (P20).

## Tests

Twin tests: parse snippets (plain `<pre>`, `<pre><code class="language-x">`,
`sourceCode`, neutral classes, classless shell/json/grammar/diagram, `<code-block>`,
`div.code`, hatemplate `itemdeclcode`, leading/trailing newlines) and compare
`write_element(handler(el))` with the legacy renderer. HTML corpus parity.

## Acceptance

Checklist green; ratchet shrank by the code origins only.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Ratchet before -> after:
Known divergences found:
Open questions:
```
