# The Transformer lineage: from attention (2014) to the LLM era

Our evergreen take on **where today's LLMs come from** — the line that runs from the
attention mechanism through the Transformer to the scaling era. Settled by
[ai-day-transformers](../pieces/INDEX.md) (live 2026-09-01,
[blog](https://tellian.io/2026/09/01/ai-day-transformers/)). Don't re-derive — extend.

## The frame: the adventure of one idea

It's a lineage, not a single "eureka paper". Attention was invented **in 2014**, three years
before the Transformer; the 2017 paper's contribution wasn't attention itself but **removing
recurrence** so the idea could scale. We frame the anniversary as **"AI Day"** — the story of one
idea growing up, not "an underappreciated paper".

## The timeline

- **2014 — attention is born.** Bahdanau, Cho, Bengio ([arXiv:1409.0473](https://arxiv.org/abs/1409.0473))
  add an alignment mechanism to an RNN encoder-decoder for machine translation. It fixes the
  fixed-length-vector bottleneck that choked long sentences. **Honest boundary:** this attention is
  a **bolt-on to an RNN** — it improves quality, but it is *not* the parallelization win.
- **2017 — "Attention Is All You Need".** Vaswani et al. ([arXiv:1706.03762](https://arxiv.org/abs/1706.03762))
  throw out recurrence entirely. Self-attention alone → the sequence is processed **in parallel**,
  not step-by-step → training scales on modern hardware.
- **Scaling laws → the LLM era.** Parallelism made it worth pouring compute in; Kaplan
  ([arXiv:2001.08361](https://arxiv.org/abs/2001.08361)) and Chinchilla
  ([arXiv:2203.15556](https://arxiv.org/abs/2203.15556)) mapped how loss falls with scale, and the
  architecture rode that curve into BERT, GPT and ChatGPT.

## Durable takeaways

- **Attention ≠ the Transformer.** The 2014 idea and the 2017 architecture are different milestones;
  conflating them is the common error. Attention was the insight; **dropping recurrence** was the
  unlock that made it scale.
- **The frontier still runs on attention.** Twelve years on, the leading models are still Transformer
  descendants. Attention did not get replaced — it got **reworked**.
- **Alternatives haven't dethroned it.** State-space models (Mamba,
  [arXiv:2312.00752](https://arxiv.org/abs/2312.00752)) live in **niche hybrids**, not at the frontier.
- **The reworks since 2017 are real but incremental:** pre-norm, RoPE/ALiBi positions, **decoder-only**
  designs, FlashAttention, GQA, MoE. Same backbone, better engineering.

## Sources

Spine sources curated in [`sources/INDEX.md`](../../sources/INDEX.md): `bahdanau-attention`,
`vaswani-transformer`. Also cited in the piece: Cho (arXiv:1406.1078), Luong (arXiv:1508.04025),
Kaplan (arXiv:2001.08361), Chinchilla (arXiv:2203.15556), BERT (arXiv:1810.04805),
Mamba (arXiv:2312.00752), plus the RoPE/ALiBi/FlashAttention/GQA/MoE/pre-norm reworks. Full
reference list in the piece's Sources section.
