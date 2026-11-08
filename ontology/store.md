# Ontology store

Structural links between pieces, topics and sources. Appended by the `librarian` on each SHIP.
See `README.md` for the model. One row per link.

| Piece (slug) | Link | Target | Notes |
|--------------|------|--------|-------|
| language-format-placement | covers | prompt-engineering | |
| language-format-placement | covers | prompt-packaging | data format / structure of the prompt |
| language-format-placement | covers | tokenization | tokenizer tax across languages |
| language-format-placement | covers | context-engineering | placement / lost-in-the-middle |
| language-format-placement | cites | sources/INDEX.md#lost-in-the-middle | Lost in the Middle (Liu et al.) — position effect |
| language-format-placement | cites | sources/INDEX.md#tokenizer-tax | Tokenizer Tax (Petrov et al.) — 25 European languages |
| language-format-placement | cites | sources/INDEX.md#toon-benchmark | TOON format vs JSON token/accuracy benchmark |
| language-format-placement | hasStatus | published | SHIP; live 2026-06-21 (issue #3). Blog https://tellian.io/2026/06/21/language-format-placement/ (RU+EN); LinkedIn https://www.linkedin.com/posts/maximlevko_activity-7474523958642479106-gp3l; Telegram posted (URL n/a) |
| ai-day-transformers | covers | transformer-lineage | attention 2014 → Transformer 2017 → scaling → LLM era |
| ai-day-transformers | covers | attention | origin (Bahdanau 2014) and the parallelization win (Vaswani 2017) |
| ai-day-transformers | cites | sources/INDEX.md#bahdanau-attention | Bahdanau/Cho/Bengio (2014) — attention invented for MT |
| ai-day-transformers | cites | sources/INDEX.md#vaswani-transformer | Vaswani et al. (2017) — "Attention Is All You Need" |
| ai-day-transformers | hasStatus | published | SHIP; live 2026-09-01 (issue #26). Blog https://tellian.io/2026/09/01/ai-day-transformers/ (RU+EN, WP post 309); Telegram posted (URL n/a); LinkedIn draft |
| harness-agents-pt1 | covers | agent-harness-effect | Part 1 of a series; no final harness yes/no verdict — see topic page's "Open, for Part 2" |
| harness-agents-pt1 | cites | sources/INDEX.md#coding-agents-converged | Same model, different scaffolding on SWE-bench — 29.8pp spread vs. 8.8pp across top-30 models |
| harness-agents-pt1 | cites | sources/INDEX.md#same-model-different-harness | Model+task fixed, scaffolding only change — solved share 25%→43% |
| harness-agents-pt1 | cites | sources/INDEX.md#agent-runtime-instruments | Open measurement tooling used for all 54 runs |
| harness-agents-pt1 | cites | sources/INDEX.md#workain-research-results-harness-agents | Open dataset: all 54 measurements, task list, methodology |
| harness-agents-pt1 | hasStatus | published | Blog live 2026-11-08 (WP post 362), https://tellian.io/2026/11/08/harness-agents-pt1/ (RU+EN); LinkedIn 5-card series drafted (not yet posted); Telegram not yet drafted. **Note:** issue #42, branch `piece-harness-agents-pt1`, PR #43 — PR not yet merged to `main` as of this entry; flagged for a follow-up ontology/RAG check once it merges |
