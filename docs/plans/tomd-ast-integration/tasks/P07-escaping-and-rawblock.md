# P07 Writer escaping policy and `RawBlock`

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 1 | P02 | P03, P04, P05, P06 | M | high (byte drift) |

## Goal

(a) Add the temporary `RawBlock(markdown, origin)` element that makes the incremental
migration possible. (b) Give the writer one module that owns the escaping the legacy
converters apply today, in exactly the contexts where they apply it. This task adds NO
new escaping: plain `TextSpan` text is still written verbatim except where a legacy
renderer escapes.

## Read first

- `lib/pdf/cleanup.py`: `escape_leading_atx`, `normalize_whitespace`
- `lib/pdf/emit.py`: `_escape_italic_text` (line 1018) and its `_LEADING_*` constants;
  `_render_paragraph_spans` (172) and `_render_heading_spans` (200) to see where
  `escape_leading_atx` is applied; `_flatten_cell` (956)
- `lib/pdf/wording_emit.py` `_escape_wording_text`
- `lib/html/render.py`: pipe escaping in `_render_table` (`replace("|", "\\|")`),
  `_inline_text_nodes` (what is and is not escaped), `_collapse_whitespace`
- `writers/markdown/spans.py`, `tables.py` (current ad hoc pipe escape)

## Change

1. `domain/elements.py`: `RawBlock(markdown: str, origin: str)` with a docstring that
   states it is migration scaffolding deleted in P28/P29. `origin` is a stable key such
   as `"pdf:table:html_table"`, `"html:ul"`. `text` returns the markdown.
2. `writers/markdown/blocks.py`: `write_element` emits `RawBlock.markdown` verbatim.
3. `writers/markdown/escape.py` (new): named functions, each documented with the legacy
   function it mirrors and the context it applies to:
   `escape_leading_atx`, `escape_italic_wrapper`, `escape_pipe_in_cell`,
   `escape_wording_angle_brackets`. Re-export or reuse legacy implementations by
   import where they are pure (do not fork logic that can drift); where the legacy code
   is inlined, extract it into the escape module and have the legacy call site import
   it, in a behavior-preserving refactor limited to those call sites.
4. Wire the writer's paragraph, heading, italic-caption, and table-cell paths through
   these functions. Keep text outside those contexts untouched.

## Do not

- Add escaping for characters the legacy code does not escape (for example `*`, `_`,
  `<` in plain prose).
- Change legacy behavior. If extraction requires touching a legacy function, add a test
  that pins its current output first.

## Tests

- `tests/writers/markdown/test_escape.py`: each function against the legacy function on
  a table of inputs (leading `#`, `-`, `+`, `>`, `1.`, backslashes, backticks,
  pipes, empty, whitespace-only). Use the legacy function as the oracle.
- Writer tests proving plain prose containing `*`, `_`, `<` is unchanged.
- `RawBlock` round-trips bytes including blank lines and trailing spaces.

## Acceptance

Checklist green; `git diff --stat` for `lib/` is only the extraction call sites, each
with a pinning test.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Legacy functions extracted (name, file):
Known divergences found:
Open questions:
```
