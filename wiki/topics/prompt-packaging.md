# Prompt packaging: language, format, placement

Our evergreen take on **how to package a prompt** — the language you write it in, the data
format you wrap it in, and where you put the important parts. Settled by
[language-format-placement](../pieces/INDEX.md) (live 2026-06-21,
[blog](https://tellian.io/2026/06/21/language-format-placement/)). Don't re-derive — extend.

## The frame: two budgets

Every prompt spends two finite resources, and almost every technique is about spending them wisely:

- **Token budget** (money + space) — the tokenizer cuts text unevenly across languages and formats;
  you pay per token and tokens fill the context window.
- **Attention budget** (quality) — even when everything fits, the model reads unevenly: attention
  goes to the edges, the middle sags, and the effect grows with prompt length.

Cost of error varies by task type — **chat** (cheap, one-off) vs **production prompt** vs
**agent harness** (huge, long-lived, costliest) vs **data** (its own packing rules).

## Durable takeaways

- **Language is a cost/quality lever, not compression.** Switching languages won't shrink a prompt.
  On Western models an **English instruction core** is usually cheaper *and* more accurate — but you
  can still address the model in any language and it works. Caveat: for small post-trained models
  (7–9B) native language can be no worse.
- **Placement follows a U-shape.** Put the key information *and* the question at the **edges**
  (start/end), not buried in the middle. Give the output-language command on its **own line at a
  pole**, never woven into the middle.
- **Simple Markdown beats heavy formats** for the instruction itself. Clean Markdown packs tighter
  than the same meaning in JSON; trendy token-oriented formats (e.g. TOON) are a **data-shape /
  baseline tradeoff**, not a universal win — they help for some data shapes, hurt for others.
- **Caveman / brevity saves ~15–20%, not −75%.** The dramatic compression numbers don't hold up;
  modest savings are real, sometimes eaten by caching/quality losses.
- **Effective context < spec window.** The advertised window is not the usable budget — what fills
  it, and where, decides whether the model notices it.

## Anti-myths (see [anti-patterns](anti-patterns.md))

"Chinese prompts are cheaper", "Russian is more compact", "emoji/box-glyphs save space",
"caveman gives −75%", "a trendy format is always better" — all debunked by this piece.

## Sources

Spine sources curated in [`sources/INDEX.md`](../../sources/INDEX.md): `lost-in-the-middle`,
`tokenizer-tax`, `petrov-tokenizer`, `toon-benchmark`, `toon-matveev`, `caveman-hakim`,
`language-confusion`, `chinese-mythbuster`, `anthropic-context-engineering`. Full reference list
in the piece's Sources section.
