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

## How to use
- The `researcher` checks here before searching the web.
- The `fact-checker` resolves links here when verifying claims.
- Reliability is your judgment of the source, not of any single claim — still verify per-claim.
