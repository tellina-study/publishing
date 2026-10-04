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
| ai-delivery-gap | covers | ai-delivery-gap | local dev metrics up, shipped output flat; bottleneck moved into review/gates |
| ai-delivery-gap | covers | defect-seeding | a gate never fed a deliberate defect counts as broken until proven otherwise |
| ai-delivery-gap | covers | anti-patterns | "green gate = fine"; "coverage = detection" |
| ai-delivery-gap | cites | sources/INDEX.md#chen-stratton-bottlenecks | Harvard, 718 firms: +30% LoC, shipped output insignificant, review +49% |
| ai-delivery-gap | cites | sources/INDEX.md#nber-writing-vs-shipping | NBER WP 35275 — writing code vs shipping code |
| ai-delivery-gap | cites | sources/INDEX.md#dora-2024 | −1.5% throughput / −7.2% stability per +25% AI adoption |
| ai-delivery-gap | cites | sources/INDEX.md#dora-2025 | throughput sign reversal; instrument changed |
| ai-delivery-gap | cites | sources/INDEX.md#dora-2019 | external approval → 2.6× more low performers |
| ai-delivery-gap | cites | sources/INDEX.md#meta-radar | 60.31% auto-approve; reverts 1/3, incidents 1/50 |
| ai-delivery-gap | cites | sources/INDEX.md#anthropic-auto-mode | classifier misses 17% of dangerous actions (n=52) |
| ai-delivery-gap | cites | sources/INDEX.md#google-mutation-icse2021 | 70% coupling; covered code still shipped the bug |
| ai-delivery-gap | cites | sources/INDEX.md#google-mutation-tse2021 | 16.9M mutants; six years of suppression rules; mutation score rejected |
| ai-delivery-gap | cites | sources/INDEX.md#tricorder | ≥10% probation / >25% off; nine-week silent breakage |
| ai-delivery-gap | cites | sources/INDEX.md#mills-bebugging | bebugging, 1972 — origin of seeding (artefact, not detector) |
| ai-delivery-gap | cites | sources/INDEX.md#martin-xie-coverage | 98.6% coverage at 47% mutants killed |
| ai-delivery-gap | cites | sources/INDEX.md#just-mutants-faults | 17% of real faults not coupled to any mutant |
| ai-delivery-gap | cites | sources/INDEX.md#meta-ach | 49% of mutant-killing tests add no coverage |
| ai-delivery-gap | cites | sources/INDEX.md#porter-votta-basili | inspections 24–57%; deliberately unseeded faults |
| ai-delivery-gap | cites | sources/INDEX.md#eicar-testfile | known-bad artefact as the detector self-test |
| ai-delivery-gap | cites | sources/INDEX.md#sre-workbook-alerting | the alert that could never fire |
| ai-delivery-gap | cites | sources/INDEX.md#architecture-conformance | comparative measurements of architecture checks (2008/2016) |
| ai-delivery-gap | hasStatus | published | SHIP; live 2026-09-25 (issue #37). Blog https://tellian.io/2026/09/25/ai-delivery-gap/ (RU+EN, WP post 326). Sources still on branch `hc/sdlc-83361639` (PR #40) — not yet merged to `main`. No Telegram/LinkedIn derivatives |
