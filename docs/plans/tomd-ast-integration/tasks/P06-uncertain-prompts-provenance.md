# P06 Uncertain element, reconcile prompts, provenance

| Wave | Deps | Parallel with | Size | Risk |
|------|------|---------------|------|------|
| 1 | P02 | P03, P04, P05, P07 | M | medium |

## Goal

Make uncertain regions round-trip: the element carries both extractions and its
neighbor context, the writer reproduces the `<!-- tomd:uncertain:L{a}-L{b} -->` marker
with legacy line arithmetic, and reconcile prompts are built from the AST. Add optional
provenance (page, confidence) to blocks.

## Read first

- `lib/pdf/emit.py`: `emit_markdown` (the `line_num` arithmetic at the top of the loop
  and in the UNCERTAIN branch), `emit_prompts` (line 1344)
- `lib/pdf/types.py`: `Confidence`, `Section` fields `mupdf_text`, `spatial_text`,
  `page_num`, `confidence`
- `domain/elements.py` `UncertainElement`, `writers/markdown/blocks.py`,
  `writers/markdown/writer.py`
- Tests: `tests/test_emit.py` uncertain and prompts cases; golden prompts files
  (`tests/fixtures/golden/*.prompts.json`)

## Change

1. Move `Confidence` into `domain/` (for example `domain/provenance.py`); `lib/pdf/types.py`
   re-exports it. Add `Provenance(page: int, confidence: Confidence)`.
2. `BlockElement` gains `provenance: Provenance | None = field(default=None, kw_only=True)`.
   Writers ignore it.
3. `UncertainElement(mupdf_text: str, spatial_text: str, page: int, text: str,
   context_before: str = "", context_after: str = "")`. `text` is what is emitted (the
   MuPDF version). `context_*` are the at-most-200-character neighbor snippets that
   `emit_prompts` computes today; the adapter fills them, so the AST never has to
   reproduce `Section.text` projections.
4. Writer: a render context tracks `line_num` with exactly the legacy arithmetic:
   start `fm.count("\n") + 3` if front matter was emitted else `1`; after a normal block
   `+= rendered.count("\n") + 2`; for an uncertain block
   `text_start = line_num + 2`, `+= text_lines + 3`, marker
   `<!-- tomd:uncertain:L{text_start}-L{text_start + text_lines - 1} -->`. Blocks that
   render to empty strings are skipped exactly as in `emit_markdown`.
5. `tomd/prompts.py` (new): `build_reconcile_prompts(document) -> list[str] | None`, a
   port of `emit_prompts` using `UncertainElement` fields. Prompt text must be
   byte-identical; keep the strings as module constants.

## Do not

- Change marker format or prompt wording. Do not touch `emit.py`.
- Compute context from neighboring elements; it is data on the element.

## Tests

Twin tests: build `Section` lists with uncertain sections at the start, middle, end,
adjacent to each other, and after empty-rendering sections; build the equivalent AST;
assert writer output equals `emit_markdown(...)` and `build_reconcile_prompts` equals
`emit_prompts`. Include a case with and without front matter (line offset).

## Acceptance

Checklist green; twin tests byte-equal.

## Handoff (fill in at the end)

```
Status: done | blocked
Files changed:
Checklist output (tails):
Known divergences found:
Open questions:
```
