# Sources — curated reading list

Durable, reusable sources worth citing again. Track the **manifest here**, not the binaries
(PDFs/epubs live in `sources/files/` and are gitignored). Add a row when the `researcher` finds
a source worth keeping.

| Source | Type | Topic(s) | Link / ID | Reliability | Notes |
|--------|------|----------|-----------|-------------|-------|
| <a id="lost-in-the-middle"></a>Lost in the Middle (Liu et al., 2023) | primary | context-engineering, placement | [arXiv:2307.03172](https://arxiv.org/abs/2307.03172) | high | U-shaped position effect: models attend to the edges of the context, the middle sags. |
| <a id="tokenizer-tax"></a>Tokenizer Tax across 25 European languages (2026) | primary | tokenization | [arXiv:2605.24718](https://arxiv.org/abs/2605.24718) | high | First controlled comparison on parallel texts; Slavic languages most expensive, English cheapest. |
| <a id="petrov-tokenizer"></a>Petrov et al., Language Model Tokenizers (2023) | primary | tokenization | [arXiv:2305.15425](https://arxiv.org/abs/2305.15425) | high | >4× token gap for some language pairs; English carries the smallest markup. |
| <a id="toon-benchmark"></a>TOON format + benchmark | secondary | prompt-packaging, formats | [github.com/toon-format/toon](https://github.com/toon-format/toon) | medium | Token-oriented format vs JSON; data-shape/baseline tradeoff, not always a win. |
| <a id="toon-matveev"></a>Matveev, independent TOON measurement (2026) | primary | prompt-packaging, formats | [arXiv:2603.03306](https://arxiv.org/abs/2603.03306) | high | Independent check on TOON token/accuracy claims. |
| <a id="caveman-hakim"></a>Hakim, Brevity Constraints (2026) | primary | prompt-packaging, brevity | [arXiv:2604.00025](https://arxiv.org/abs/2604.00025) | high | Brevity / caveman-prompt savings are modest (~15–20%), not −75%. |
| <a id="language-confusion"></a>Language Confusion (EMNLP 2024) | primary | language, placement | [arXiv:2406.20052](https://arxiv.org/abs/2406.20052) | high | Isolated language instruction confuses less than an integrated one; one example ≈80% correct-language. |
| <a id="chinese-mythbuster"></a>Mythbuster: Chinese is not more efficient (2026) | primary | tokenization, language | [arXiv:2604.14210](https://arxiv.org/abs/2604.14210) | medium | Preprint; the Chinese-saves-tokens claim is unconfirmed and model-dependent. |
| <a id="anthropic-context-engineering"></a>Anthropic — effective context engineering | secondary | context-engineering | [anthropic.com](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | high | Effective context < spec window; what fills the budget matters. |
| <a id="bahdanau-attention"></a>Bahdanau, Cho, Bengio — Neural MT by Jointly Learning to Align and Translate (2014) | primary | transformers, attention, machine-translation | [arXiv:1409.0473](https://arxiv.org/abs/1409.0473) | high | Origin of the attention mechanism; a bolt-on to an RNN encoder-decoder, fixed the fixed-vector bottleneck on long sentences. Not yet the parallelization win. |
| <a id="vaswani-transformer"></a>Vaswani et al. — Attention Is All You Need (2017) | primary | transformers, attention | [arXiv:1706.03762](https://arxiv.org/abs/1706.03762) | high | Removed recurrence → parallelism → scaling → the LLM era. The architecture the frontier still runs on. |
| <a id="coding-agents-converged"></a>Coding Agents Have Converged (2026) | primary | coding-agents, benchmarking, scaffolding | [arXiv:2609.17394](https://arxiv.org/html/2609.17394v1) | high | Same model (Claude 3.5 Sonnet), different scaffolding on SWE-bench spreads 29.8 pp (168–317 solved); the entire top-30 leaderboard, across different models, spreads only 8.8 pp. |
| <a id="same-model-different-harness"></a>Same Model, Different Harness: Different Coding-Agent Results (2026) | primary | coding-agents, benchmarking, scaffolding | [arXiv:2608.26218](https://arxiv.org/abs/2608.26218) | high | Model and task held fixed, only scaffolding changes: fully-solved share goes 25%→43% (43→72 of 169). |
| <a id="agent-runtime-instruments"></a>workain/agent-runtime-instruments (open tooling) | primary | coding-agents, measurement-tooling | [github.com/workain/agent-runtime-instruments](https://github.com/workain/agent-runtime-instruments) | high | Apache-2.0 open tooling for honestly measuring AI-agent session cost (vs. unreliable self-report); built for the harness-agents-pt1 experiment. |
| <a id="workain-research-results-harness-agents"></a>workain/research-results — 2026-11 harness-agents dataset | primary | coding-agents, benchmarking | [github.com/workain/research-results/tree/main/2026-11_harness-agents](https://github.com/workain/research-results/tree/main/2026-11_harness-agents) | high | CC BY 4.0. Full open dataset behind harness-agents-pt1: all 54 raw measurements (incl. what didn't make the piece), the 9-task list, and the price-recalculation methodology. |

## How to use
- The `researcher` checks here before searching the web.
- The `fact-checker` resolves links here when verifying claims.
- Reliability is your judgment of the source, not of any single claim — still verify per-claim.
