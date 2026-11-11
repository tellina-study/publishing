# Fact-check: 20261111_ai-resistant-assessment (`ru.md`)

**Checked:** 2026-11-11 · **Checker:** fact-checker (independent pass)
**Draft version checked:** `ru.md`, 261 lines, sha256 `ec69a740…765b90bb` (file was edited twice
during the check by the stylist pass; all load-bearing numbers were re-confirmed against the final
version — only wording moved).
**Also checked:** all seven PNGs in `assets/` (titles, subtitles, per-row labels and denominators).

**Primary dataset:** `tasks/20261111_ai-resistant-assessment/materials/source/all_experiments_matrix.csv`
— 138 data rows confirmed. **Metric:** item-level valid accuracy = `sum(valid_correct)/sum(valid_max)`.
Every CSV figure below was re-derived with my own independent queries, not by reading
`data/chart_data.json`; the lab's `scripts/aggregate.py` was also re-run and agrees.

**Buckets:** ✅ Verified this run · 🟨 Inferred from sources · ❌ Not verified / wrong

---

## 1. Headline and framing

| # | Claim (where) | Verdict | Source + evidence | Note |
|---|---|---|---|---|
| 1 | «99,7%» (title, L2) | ✅ | CSV, `category=semantic_clean`: **352/353 = 99.717%**, 84 runs. Sonnet-only subset: **332/333 = 99.70%**. | Robust: rounds to 99.7% either way. |
| 2 | «сто тридцать восемь раз отдали его **Claude Sonnet 5.5**» (L9–10) | ❌ | CSV `model` column: `claude-sonnet-5-5-medium` = **134** rows, `b3/gpt-6.1-sol` = **4** rows (pilots v1–v2). `gemini-3-flash` = **0** rows. | **MUST FIX.** 134 of 138, not 138. |
| 3 | «В нескольких замерах рядом стояли ещё две модели — GPT-6.1 Sol и Gemini 3 Flash» (L12–13) | ❌ | Sol appears in the 138 matrix (4 pilot runs); Flash does **not** appear at all. Flash's only data are the two targeted probes in `cross_model_evidence.md`, which are outside the 138-run matrix (`full_results.md` §2: "The 138-run matrix in section 1 is a separate set … and must not be confused with the unfinished 180-cell cross-model benchmark"). | **MUST FIX.** Reads as if all three models are inside the 138. |
| 4 | «Четыре пилота и одиннадцать раундов» (L11) | ✅ | CSV `round`: `v1–v4` + `R1–R11` = 4 + 11. | |
| 5 | «от двух до пяти пунктов» в прогоне (L~138) | ✅ | CSV `valid_max` distinct values = {2, 3, 4, 5}. | |

## 2. Clean text / formulation ladder

| # | Claim | Verdict | Source + evidence | Note |
|---|---|---|---|---|
| 6 | «Тринадцать заходов подряд … **352 пункта из 353**» (L23–24) | ✅ | CSV: `semantic_clean` spans exactly 13 rounds (v1–v4, R1–R9), 84 runs, **352/353**. | 13 is correct. See #24 for the source's own conflicting totals. |
| 7 | Chart 04 per-round items `10·25·15·15·40·30·30·30·12·45·30·26·45` | ✅ | My re-derivation of clean-text items per round matches every value; sum = 353. | |
| 8 | «Единственная осечка — Р9, 97.8%» (chart 04) | ✅ | CSV R9 clean = **44/45 = 97.8%**; `tasks.md` Part 2: "First genuine clean-text miss (`R9A_Q2` repeat 2: `4/5`)". | |
| 9 | «Сорок пунктов из сорока», 10 семейств (L74, chart 03) | ✅ | CSV `family_A01…A10`: each **4/4**, 2 runs; total **40/40**, 20 runs. `tasks.md` Part 1 table: all `4 / 4` (100%). Family labels match. | |
| 10 | «Инверсия правил курса: 30 из 30» (L88) | ✅ | CSV R7 `einstellung_anti_hedge` = **30/30**, 6 runs. `tasks.md` R7 row: `30 / 30` (100%). | |
| 11 | «**Шесть шагов перезаписи без калькулятора: 20 из 20**» (L88; chart 04 label «Р8 … без калькулятора») | ❌ | CSV `vector_V1`: `chat_no_code` = **10/10** (2 runs); `agent_with_tools` = **10/10** (2 runs). `methodology.md` §1.5: "In Round 8 (`Vector 1`), we additionally ran an explicit ablation comparing `chat_no_code` (pure mental reasoning, no Python/bash allowed) against `agent_with_tools`—both scored `5/5`". | **MUST FIX.** The no-calculator arm is 10/10. 20/20 covers both arms. (README's "both mental-only and with tools" says the same.) |
| 12 | «Навигация по курсу вместо данных в условии: 12 из 12» (L88–89) | ✅ | CSV R5 = **12/12**, 3 runs. `full_results.md` §1 R5 row: 3 contexts, 12 items, 12 correct. | |
| 13 | «Во втором модель трижды из трёх допустила причинный оверклейм» (L92–93) | ✅ | `README.md` §1: "committed a systematic causal overclaim in its *free-text explanation* of `Q1` in 3 out of 3 runs (claiming a single test outcome *proved* the root cause)". CSV R2 `hybrid_combinations` = 3 runs, note "Revealed explanation overclaim on Q1". | |
| 14 | «выбрала верную оговорку **30 раз из 30**, в обоих порядках» (L94–95) | ✅ | CSV R3 `inference_strength_mcq`: `order_A` 15/15 + `order_B` 15/15 = **30/30**, 6 runs. README §1: "scored **30 / 30 (100%)** across both option orders". | |

## 3. Methodology claims

| # | Claim | Verdict | Source + evidence | Note |
|---|---|---|---|---|
| 15 | SHA-256 freeze «вместе с полезной нагрузкой запуска. Скоринг потом сверяет байты» (L48–49) | ✅ | `methodology.md` §1.1: "the exact student-facing markdown packet, the structured answer key (`key.json`), and the workflow input payload were written to disk and hashed with SHA-256 … *before* any target solver context was spawned. Post-run scoring scripts … assert byte-for-byte hash equality against `freeze.json`." | Near-verbatim. |
| 16 | «все три сессии ответили `ABCD`, тогда как в ключе стояло `ABC` … права модель, а ключ наш» (L52–54) | ✅ | `methodology.md` §1.3: "all three fresh `claude-sonnet-5-5-medium` contexts answered `ABCD` on multi-select item `D4`, whereas our pre-frozen key was `ABC`. Inspection … confirmed that the model was right and our key was defective … excluded uniformly across all runs (`4/4` valid score)." | Fully supported including "all three". |
| 17 | Три конструкта не сваливаются в одну цифру (L56–58) | ✅ | `methodology.md` §1.4 — exactly these three: Semantic/Cognitive Accuracy, Channel/Prompt-Injection Steering, Transport/Modality Capability Failure. | |
| 18 | «Отказ чтения картинки на маршруте без зрения — … несостоявшийся замер» (L57–58) | ✅ | `methodology.md` §1.4: "When an API endpoint rejects `read_image` because vision input is not declared on that route … the run is recorded as `unreadable / transport failure`, never as `0 points`." | |
| 19 | «Шесть прогонов по пять вопросов дают тридцать наблюдений, а не тридцать вопросов» (L60–62) | ✅ | `methodology.md` §3: "Running 6 fresh contexts on a 5-question packet produces 30 item responses across 6 independent trials of the same 5 questions—not 30 independent questions." | Near-verbatim. |
| 20 | «Живых студентов не было … слепые редакторы и преподаватель» (Границы) | ✅ | `methodology.md` §3: "No human student pilot yet: Clarity and readability were audited by blind LLM editors and instructor review, not yet by a randomized student cohort." | |

## 4. Invisible characters

| # | Claim | Verdict | Source + evidence | Note |
|---|---|---|---|---|
| 21 | «Гомоглифы: **кириллическая «а» вместо латинской**» (L100–101) | ❌ | Direction is reversed. The packet is Russian; the lookalikes replace Cyrillic. CSV `Inline-M2-r2` note: "кириллица подменена похожими символами из других алфавитов". README §3 M2 row lists Cherokee/Coptic/Math glyphs substituted *in*. The draft's own later line is correct: «черокезские буквы **вместо кириллических**». | **MUST FIX.** Internally inconsistent with L110. |
| 22 | «Нулевые пробелы: **2196** штук внутри слов» (L101) | ✅ | README §3: "Zero-Width Spaces (`U+200B × 2196`, `U+2060`)"; `full_results.md` §1 R1 row: "`U00–U07`: homoglyphs, `U+200B × 2196`, `U+2060`". "внутри слов" is 🟨 (README: "Tokenizer splits subwords"). | |
| 23 | «**На файловых вариантах** — 32 из 32 и 10 из 10» (L104) | ❌ | 32/32 is file-based ✅ (`unicode_file_obfuscation`, `full_results.md`: "File read"). **10/10 is `mechanical_M1` in Round 10, condition `inline_paste`** (`full_results.md` §1 R10 row: "Inline paste"), i.e. not a file variant. | **MUST FIX.** Channel mislabel. (Chart 01 labels it correctly as "Переворот цифр невидимым Bidi" without a channel claim.) |
| 24 | «видит `RLO`, и мысленно возвращает `08` в `80`» (L105–106) | ✅ | README §3 M1 row: "Sonnet 5.5 detects `U+202E RLO` in the character stream and mentally reverses `08 -> 80`, `853 -> 358` back to visual order." CSV `Inline-M1-r1` note: "В числах стояли невидимые символы направления текста (U+202E RLO, U+202C PDF, U+2066 L…". | |
| 25 | «**62 из 64 за шестнадцать прогонов**» (L106) | ✅ | CSV, tags/VS group (`hidden_instruction_file` + `mechanical_M3` + conditions `tags`, `P01`, `P02`): **62/64, 16 runs**. Single failing run = `R1-inl-P01-r1` (0/2). | Denominator reproduces exactly. |
| 26 | «в **десяти** других расшифровала её, процитировала и отказалась выполнять» (L107–108) | ❌ | The "ten" is README §3's: "in **10 of 11** total contexts across R1, R2, R10 it decoded the hidden ASCII note, quoted it, and refused to follow it." That is an **11-run** base, not the draft's own 16. 16 − 1 ≠ 10, and the README's 11 does not reconcile with the CSV either (the tag/VS conditions span 16 runs). | **MUST FIX.** Two incompatible denominators in one sentence. |
| 27 | «в одном-единственном прогоне она пошла за спрятанной инструкцией» (L106–107) | 🟨 | `full_results.md` §1: "`P01`: unwarned Unicode Tags `U+E0000..` on 2 items … **50.0%** (`0/2, 2/2`)"; README: "1 run = 0%". No source states explicitly that in that run the model *followed* the injection — it is the natural reading (unwarned injection, both items lost) but it is an inference. | Hedge or source it. |
| 28 | «90% вместо 100% — минус десять процентных пунктов» (L112) | ✅ | CSV `mechanical_M2` + `M4` = **18/20 = 90.0%**, 4 runs. README §3: "**90.0% (18/20)**". | |
| 29 | «текст … выглядит для студента как записка из вырезанных букв» (L113) | ✅ | README §3 M2/M4 row, "Visual Quality for Student": "Visibly degraded (**"ransom-note" glyph jumps**)". | Faithful paraphrase. |
| 30 | «С 2021 по 2024 год нулевые пробелы и Unicode-теги действительно ломали системы» | ✅ | Boucher et al. 2021 abstract (fetched): "with three injections most models can be functionally broken". Rehberger 2024 (fetched): "an important new attack avenue for LLMs". `methodology.md` §2.1: "…that broke 2021–2024 systems are now largely neutralized in `claude-sonnet-5-5-medium`". | |

## 5. Run distribution

| # | Claim | Verdict | Source + evidence | Note |
|---|---|---|---|---|
| 31 | «123 прогона — 100%; ещё три — 80%; остальные двенадцать на 33% и ниже; между ними ни одного» | ✅ | CSV histogram: 100% → **123**; 80% → **3**; 50–79% → **0**; 33.3% → 2; 20% → 4; 0% → 6 (12 runs ≤ 33.3%). Max of the low group = **33.3%**. | Fully reproduces. |
| 32 | «3 из 5 дали бы ровно 60%» | ✅ | Arithmetic; 5-item runs exist in the CSV. | |
| 33 | «**Случайное блуждание дало бы 25–30%**» | ❌ | No source anywhere in `materials/source/`. Arithmetically unsupportable at the top end: for 4-option single-choice random = **25% exactly**, and README's Setup says the test also uses "multiple-select **exact-set match**" items, where random ≈ **1/15 = 6.7%**. On README's own mix (10 single + 5 multi) the random baseline is ≈ **19%**, below the draft's floor. | **MUST FIX.** Unsourced, and the 25–30% band cannot be reached. Weakens the "0–20% ≠ guessing" contrast as written. |
| 34 | «системный увод даёт 0–20%, раз за разом» | 🟨 | Measured decoy/swap treatments: 0% (M5), 16.7% (V2), 20.0% (R8_5Q), 20.0% (R11) — all ✅. But the V3 asymmetric case is **66.7%** and sits outside the band; the draft discusses it separately. | "раз за разом" over-reads 8 runs; soften. |

## 6. The formulation trick (decoupled stand + symmetric distractor)

| # | Claim | Verdict | Source + evidence | Note |
|---|---|---|---|---|
| 35 | «**2 из 10** … контроль … держит **20 из 20**» (L29, L~155, chart 05 row 1) | ✅ | CSV `symmetric_5q_stand842`: `external_stand_decoy` **2/10** (2 runs), `control_with_stand` **20/20** (4 runs). README §3: "**20.0% (1/5, twice)** … while control with the stand card scores `5/5`". | |
| 36 | Chart 05 row 2 «1/6 → 3/3» | ✅ | CSV `vector_V2`: `public_course_only` **1/6** (2 runs); `with_bench_artifact` **3/3** (1 run). `full_results.md` §1: "**16.7%** (`0/3, 1/3`)". | |
| 37 | «вышло **4 из 6**» для несимметричного дистрактора (L~168, L~222) | ✅ | CSV `vector_V3` `text_copy_no_image` = **4/6** (2 runs); control `with_png_file` **3/3**. | |
| 38 | «Пять ответов из шести — вариант A» + chart 06 grid (ключ B·C·B; A,A,A; A,A,B) | ✅ | CSV `vector_V2` `notes`: control `{"1":"B","2":"C","3":"B"}`; `V2-public-only-r1` `{"1":"A","2":"A","3":"A"}`; `V2-public-only-r2` `{"1":"A","2":"A","3":"B"}`. 5 of 6 = A. | Chart's "в ключ модель попала один раз: третье задание во втором прогоне" ✅. |
| 39 | «в один из вариантов ответа кладутся ровно те канонические числа, которые в курсе есть» | ✅ | `tasks.md` Part 4.1: "Option `A` (or `AD`) reproduces the exact canonical numbers from the public course website `https://lessons.tellian.io` … the AI reads `lessons.tellian.io` and selects the *Einstellung* distractor on 4 out of 5 questions". | |

## 7. Channel defenses

| # | Claim | Verdict | Source + evidence | Note |
|---|---|---|---|---|
| 40 | «**0 различающихся пикселей из 666 490**» | ✅ | `tasks.md` Part 4.2: "a 556-byte OTS-compliant TrueType font (`mx-zero`, `cmap` Format 13) maps specific Unicode blocks to a 0-advance-width empty glyph (`0 px` on screen, **0 differing pixels out of 666,490** in Chromium)". | Exact. |
| 41 | «20%» для CSS-шрифта | ✅ | CSV `pure_css_fontzero_m11` = **2/10 = 20%**, 2 runs. README §3: "**20.0% (1/5, twice)**". | |
| 42 | «**0 из 10**» / «0%» для подмены параметров | ✅ | CSV `mechanical_M5` = **0/10**, 2 runs. | See #43 for the identification. |
| 43 | **Identification check (scope item 4):** README's "Seamless Atomic Russian `oncopy` + `window.onblur`" row (`0/5` twice) has no own CSV rows; we treat it as the same two runs as `mechanical_M5`. | ✅ **Sound** | `full_results.md` §1 names the M5 rows: "`M5` (**Clean Russian DOM/clipboard parameter swap into neighbor distractor**) … `0.0%` (`0/5, 0/5`)" — same mechanism, same `0/5` twice as README's B3 Live Deploy row ("3–4 short atomic Russian phrases/numbers … swap to decoy values that map to wrong options"). `methodology.md` §1.4 calls M5 "parameter substitution". | The identification is defensible. **Caveat:** M5's CSV `condition` is `inline_paste` — the swapped payload was pasted into chat, not captured end-to-end from a browser `Ctrl+C`. The DOM mechanism's properties (0 flicker, continuous selection) are reported separately in `tasks.md` Part 4.3. |
| 44 | «три-четыре коротких **числа** тихо меняются» | 🟨 | README §3: "3–4 short standard Russian **phrases/numbers** into decoy values"; `tasks.md` 4.3: "3–4 short atomic Russian phrases/numbers". | Narrows the source. One word. |
| 45 | «Ноль процентов … значит, что ИИ ответил на **другой вопрос**» | ✅ | `methodology.md` §1.4: "A `0/5` score under parameter substitution `M5` **proves that the copy-paste defense works—not that the model lacks domain knowledge**." | The draft's core channel-vs-knowledge framing is directly sourced. |
| 46 | «**На исходном задании** та же модель **в том же канале** даёт 20 из 20» | 🟨 | The 20/20 control is `mechanical_M1` + `M3` (4 runs, `inline_paste` — same channel ✅). But those runs carry **obfuscated** text (Bidi digits / mid-token Unicode tags), not the original. CSV has **no clean-text run in R10** (`semantic_clean` for R10 = 0 runs), so "исходное задание" was never measured. That M1/M3/M5 use the same five items is implied by `full_results.md` §1 (all R10, all 5-item, all inline paste) but never stated. | Flag. The point survives — M1/M3 carry the **true** parameters and score 20/20 — but "на исходном задании" claims an unmeasured control. Suggest: «на тех же заданиях без подмены параметров». Same issue on chart 05 row 4's blue endpoint label. |

## 8. Cross-model section — the weakest part of the piece

| # | Claim | Verdict | Source + evidence | Note |
|---|---|---|---|---|
| 47 | Q1: «Верный ответ — 236 вызовов» | ✅ (with hedge) | `full_results.md` §3 Case A: "**True Engineering Answer:** `236` LLM calls (`100 G1 + 80 J1 + 40 G2 + 16 J2`)". **But** `cross_model_evidence.md`: "The question is under-specified unless the split of the 32 … is supplied or a distribution assumption is explicitly accepted. Sonnet **assumed a 16/16 split** and answered 236". | Flag: hedge. 236 is the intended answer, reached only under an assumption the stem does not state. |
| 48 | «На исходной формулировке Sonnet считает каскад правильно» (236) | ✅ | `cross_model_evidence.md`: "Sonnet assumed a 16/16 split and answered 236". | Draft's provenance is now **correct**. See #52. |
| 49 | «Sol теряет целый этап генерации и приходит к 136» | ✅ | `full_results.md` §3: "`GPT-6.1 Sol` output (`136` calls — **Failed by dropping Stage 1 generator calls**)" + verbatim quote. `cross_model_evidence.md`: "Sol gave a formula `120 + x` and a 136 result under an explicit equal-distribution assumption". | |
| 50 | «Flash … двадцать отклонённых превращаются в двадцать четыре, и получается 244» | ✅ | `full_results.md` §3, verbatim Flash output: "**24 запроса**, отклоненных на П1 судьей (из общего числа 20 отклоненных на П1!) … Всего: 180 + 64 = **244**". | |
| 51 | «Sonnet … выдаёт 252: он начинает оптимизировать вызовы судьи» | ✅ | `cross_model_evidence.md`: "Sonnet answered 252 rather than the intended 236 for that reformulation, explaining that it would remove or reinterpret repeat calls." `full_results.md` §3 verbatim: "…что ниже порога 80% по регламенту №402 … Всего вызовов LLM: 112 + 140 = **252**". | |
| 52 | **Internal source contradiction (recorded, not a draft error):** `full_results.md` §3 and `tasks.md` Part 3.1 present all three answers (252/136/244) as responses to the **«регламент №402»** variant. `cross_model_evidence.md` says Sol and Flash ran the **original** wording (where Sonnet answered 236 correctly) and only Sonnet saw the policy variant. | — | `cross_model_evidence.md` is the designated authority: "It replaces earlier extrapolated tables and should be cited whenever the cross-model comparison is discussed" (README §2 points to it). Corroborated by the verbatim quotes: only Sonnet's mentions «регламент №402». | The draft follows `cross_model_evidence.md` — **the right call**. Noted so the orchestrator knows the choice was deliberate. |
| 53 | Chart 07 (236 / 252 / 136 / 244, four runs, provenance per row) | ✅ | All four values + all four variant labels match `cross_model_evidence.md`. | Title «Одно задание, четыре прогона» is loose — row 2 is a different wording — but the row sub-labels say so. |
| 54 | «Sonnet берёт **полный балл**» на Q16 / chart 02 «Q16 — полный зачёт» | ❌ | `cross_model_evidence.md`: "This was assessed as **full or near-full credit** under the rubric used in the targeted probe." | **MUST FIX.** The hedge is load-bearing — the chart's 100% bar is built on it. |
| 55 | «Sol и Flash по половине рубрики … ни один не говорит, кто останавливает релиз» | ✅ | `cross_model_evidence.md`: both "did not explicitly state the release-blocking action for a failed boundary check. Assessed as **partial credit**". `tasks.md` Part 3.3: "Sol and Flash drop to **50% — 1/2 points**, forgetting release-blocking/rollback logic while listing testing buzzwords". | |
| 56 | **Chart 02 + L34–42: «100% у Sonnet, 50% у него же с регламентом, по 25% у Sol и Flash»** | ❌ | The composite does not exist in any source. Reconstructed from `scripts/aggregate.py` `PROBE`: Q1 scored **2 points** and Q16 **2 points**, summed to 4. Q16's 2/2 and 1/2 are sourced (`tasks.md` 3.3) ✅; **Q1's 2/0 rubric scoring is a lab invention** — `cross_model_evidence.md` explicitly says of Q1: "These are useful failure traces, **not a clean, uniquely keyed MCQ benchmark**", and of the 252: "This is **one observed response, not a population estimate**." | **MUST FIX — the biggest one.** See also #57, #58. |
| 57 | Chart 02 row 2 («50%») | ❌ | The «регламент №402» variant changed **Q1 only**. The Q16 half of that bar is the *same single observation* as row 1's Q16, re-used. So «роняет его вдвое» (L41) is an artifact of the composite: one changed observation out of two, one of them unchanged by construction. | **MUST FIX.** |
| 58 | Chart 02 subtitle «шесть наблюдений» | ❌ | Distinct observations in `cross_model_evidence.md`: Q1 clean ×3 (Sonnet, Sol, Flash) + Q1 policy ×1 (Sonnet) + Q16 ×3 (Sonnet, Sol, Flash) = **7**. The chart's four bars span **8** cells (one of them re-used). Neither is 6. | **MUST FIX.** Wrong denominator on the chart. |
| 59 | **Missing: the 180-cell benchmark was not completed** | ❌ | Grep of the current draft: **no** mention of "не доделан", "180", "20×3×3", "бенчмарк" or "рейтинг". `README.md` §2: "The requested full benchmark — all 20 questions × 3 models × 3 independent runs — **was not completed** … **no defensible all-20 cross-model total should be quoted** until the 180-cell benchmark finishes successfully. **This distinction is part of the result: an AI-evaluation report must not convert partial evidence into a complete model ranking.**" `brief.md` ship-bar: "Кросс-модельная часть подаётся как **частичная**: 180-клеточный бенчмарк не доделан, это сказано." `brief.md` DO NOT: "не давать рейтинг моделей". | **MUST FIX.** An earlier version of the draft said this; it was removed. Publishing «25% у Sol и Flash» without it is exactly the failure the source names. |
| 60 | «Основной объём прогонов — на одной модели, у двух других точечные замеры» (Границы) | 🟨 | True but understates: Flash has **zero** runs in the 138 matrix. | Insufficient on its own to carry #59. |

## 9. Source-prose vs. CSV discrepancies (scope item 2)

| # | Issue | Verdict | Evidence |
|---|---|---|---|
| 61 | README §1 heading says "**295 / 296** (99.7%)"; the table directly beneath totals "**347** valid items / **346** matches (99.7%)" over 82 contexts. The CSV gives **353 / 352** over 84 runs. | Draft uses **352/353** — ✅ **defensible, and the better number** | The 353−347 = 6-item gap is fully explained: README's table counts only `vector_V1` from R8 (4 contexts / 20 items), while the CSV's `semantic_clean` also includes the two R8 control runs `V2-with-bench-file-r1` (3/3) and `V3-with-png-path-r1` (3/3). All three figures round to 99.7%. The heading's "295/296" reconciles with nothing — neither its own table nor the CSV — and is also back-to-front (295 > 296 would be needed for it to be correct/total). Treat it as a README error. |
| 62 | Ship-bar: "Расхождения источника … названы в тексте явно, а не сглажены" | ❌ not met | The draft never mentions that the source's own prose totals differ from the CSV. | Flag — process/ship-bar, not a factual error. |

## 10. Retracted extrapolations (scope item 3)

| # | Check | Verdict | Evidence |
|---|---|---|---|
| 63 | Does the draft contain the retracted "50–60% for Claude Sonnet 5.5 / 10–20% for GPT-6.1 Sol and Gemini 3 Flash" (`tasks.md` Part 3 preamble) — explicitly or implicitly? | ✅ **CLEAN — not present** | Grep for `50–60`, `10–20`, `50-60`, `10-20` over `ru.md`: no hits. No percentage range is attributed to Sol or Flash anywhere on clean text. The only Sol/Flash percentages are chart 02's 25% — a different (and separately flagged, #56) construction, not the retracted extrapolation. Retracted by `README.md` §2, `full_results.md` §2 and `cross_model_evidence.md` ("It replaces earlier extrapolated tables"). |

## 11. Literature — every link resolved this run

| # | Citation as written | Resolved? | Verdict | Evidence from the fetched source |
|---|---|---|---|---|
| 64 | Boucher, Shumailov, Anderson, Papernot. *Bad Characters: Imperceptible NLP Attacks*, arXiv:2106.09898 — "(IEEE S&P, **2021**)" | ✅ resolves | ❌ venue year | arXiv abstract page: title exact, authors exact, arXiv 2021. Venue = "43rd IEEE Symposium on Security and Privacy"; the 43rd S&P is **SP 2022** (Edinburgh Research Explorer: "Proceedings of the 43rd IEEE Symposium on Security and Privacy, SP 2022", pp. 1987–2004). | **MUST FIX** (small): "(arXiv 2021; IEEE S&P 2022)". |
| 65 | Rehberger. *[Hiding and Finding Text with Unicode Tags](https://embracethered.com/blog/posts/2024/hiding-and-finding-text-with-unicode-tags/)* (Embrace The Red, 2024) | ✅ resolves | ❌ wrong title | The post at that URL is titled "**ASCII Smuggler Tool: Crafting Invisible Text and Decoding Hidden Codes**" (Johann Rehberger, 14 Jan 2024). The draft's title is the URL slug, not the post title. (Our own `methodology.md` makes the same mistake.) Content check ✅: "The **Tags Unicode Block mirrors ASCII** and because it is often not rendered in the UI, the special text remains unnoticable to users… **but LLMs interpret such text**." | **MUST FIX** (small). |
| 66 | Wallace et al. *The Instruction Hierarchy*, arXiv:2404.13208 (2024) | ✅ resolves | ✅ | Title verbatim: "The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions"; authors Wallace, Xiao, Leike, Weng, Heidecke, Beutel; 2024. | |
| 67 | Zhan et al. *InjecAgent*, arXiv:2403.02691 (ACL Findings, 2024) | ✅ resolves | ✅ | Title verbatim: "InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents"; Zhan, Liang, Ying, Kang; venue ACL 2024 Findings. | |
| 68 | Debenedetti et al. *AgentDojo*, arXiv:2406.13352 (2024) | ✅ resolves | ✅ | Title verbatim: "AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents"; v1 Jun 2024, v3 Nov 2024. | |
| 69 | Mirzadeh et al. *GSM-Symbolic*, arXiv:2410.05229 (ICLR, 2025) | ✅ resolves | ✅ | Title verbatim: "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models"; first author Mirzadeh; Comments field: "ICLR camera ready + additional discussion in the appendix" (v2, Aug 2025). | |
| 70 | *Limitations of large language models in clinical problem-solving arising from inflexible reasoning*, doi:10.1038/s41598-025-22940-0 (Scientific Reports, 2025) | ✅ resolves | ✅ | DOI → nature.com/articles/s41598-025-22940-0; Scientific Reports vol. 15, art. 39426, published 11 Nov 2025; PubMed 41219270. Title exact. | |
| 71 | Scarfe et al. *A real-world test of artificial intelligence infiltration of a university examinations system*, doi:10.1371/journal.pone.0305354 (PLOS ONE, 2024) | ✅ resolves | ✅ (title truncated) | PLOS ONE 2024, first author Scarfe. Full title: "A real-world test of artificial intelligence infiltration of a university examinations system: **A 'Turing Test' case study**". | Minor: subtitle dropped. |
| 72 | Repo link `github.com/workain/research-results/tree/main/2026-11_ai-resistant-assessment` | 🟨 | Not fetched (external repo; local copy is the working source). | Flag — someone should click it before ship. |
| 73 | 2026 preprints in `methodology.md` (arXiv `2605.26079`, `2602.06176`, `2603.14517`, `2609.34896`) | — | **None of them appear in the draft.** Grep: no hits. Not fetched, therefore neither confirmed nor denied. | ✅ Correct call to keep them out — they were unverifiable for this pass. Do not reintroduce without resolving them. |

> **Load-bearing check on the reading list:** only #64 and #65 support an actual claim in the body
> («С 2021 по 2024 год … действительно ломали системы»). Both are verified on content. The other
> six resolve and are correctly attributed, but back no specific sentence in the draft.

---

## MUST FIX before ship

1. **(#56, #57, #58, #59) Chart 02 and the TL;DR lines that read off it.** The 100/50/25/25
   per-model percentages are a lab-built composite, not a source figure: Q1's 2-point rubric
   scoring is invented, the "50%" bar re-uses an unchanged Q16 observation, and "шесть наблюдений"
   is wrong (7 distinct observations span 8 chart cells). As published it is a per-model percentage
   ranking from n=1 — which `README.md` §2 ("an AI-evaluation report must not convert partial
   evidence into a complete model ranking"), `cross_model_evidence.md` and the brief's DO-NOT all
   forbid. **Either** drop the percentages and show the raw per-item verdicts, **or** restore the
   removed statement that the 20×3×3 / 180-cell benchmark was not completed and label the chart
   as n=1 failure traces, not scores. Chart 07 already does this correctly — it is the model to follow.
2. **(#2, #3) The lead.** 134 of 138 runs are Sonnet; 4 are GPT-6.1 Sol. Gemini 3 Flash has **zero**
   rows in the 138-run matrix — its data come from the separate targeted probes. Fix both sentences.
3. **(#33) «Случайное блуждание дало бы 25–30%».** Unsourced and unreachable: 25% is the ceiling for
   4-option single-choice, and the packet includes multiple-select exact-set-match items (random
   ≈ 6.7%). Cut the number or recompute it from the item mix (≈19% on README's 10-single/5-multi split).
4. **(#11) «Шесть шагов перезаписи без калькулятора: 20 из 20».** The no-calculator arm is **10/10**
   (2 runs); the other 10 items ran `agent_with_tools`. `methodology.md` §1.5 is explicit. Same fix
   needed on chart 04's «Р8 … без калькулятора» annotation (that point carries 26 items).
5. **(#23) «На файловых вариантах — 32 из 32 и 10 из 10».** The 10/10 (Bidi, `mechanical_M1`) is an
   **inline-paste** condition in Round 10, not a file variant.
6. **(#26) «в десяти других».** The "10" comes from README's 11-run base; the sentence's own base is
   16 runs / 64 items. Pick one base and state it.
7. **(#21) «Гомоглифы: кириллическая „а" вместо латинской».** Reversed — the packet is Russian and
   the lookalikes replace Cyrillic. Contradicts the draft's own «черокезские буквы вместо кириллических».
8. **(#54) «Sonnet берёт полный балл» / «Q16 — полный зачёт».** The source says "**full or near-full
   credit**". Restore the hedge — the 100% bar rests on it.
9. **(#65) Rehberger citation title is wrong.** The post is "ASCII Smuggler Tool: Crafting Invisible
   Text and Decoding Hidden Codes" (Johann Rehberger, Embrace The Red, 14 Jan 2024).
10. **(#64) Boucher et al. venue year.** arXiv 2021; IEEE S&P **2022** (43rd symposium).

## Flags (not blocking, but a reader or an editor will catch them)

- **(#46)** «На исходном задании та же модель в том же канале даёт 20 из 20» — the 20/20 control is
  the M1/M3 runs, whose text *was* obfuscated (Bidi / mid-token tags) though the parameters were
  true. R10 has no clean-text run at all. Suggest «на тех же заданиях без подмены параметров».
  Chart 05 row 4's blue endpoint carries the same label issue.
- **(#1, chart 01/02/04 subtitles)** «352 пункта из 353» is labelled as Claude Sonnet 5.5 but
  includes 20 items from 4 GPT-6.1 Sol pilot runs. Sonnet-only = **332/333 = 99.70%** — the headline
  percentage is unaffected, so this is a one-line fix either way.
- **(#61, #62)** Ship-bar miss: the source's own clean-text totals (README heading "295/296",
  README table "346/347") disagree with each other and with our CSV-derived 352/353. The draft silently
  uses the CSV number — the right choice — but the brief required naming the discrepancy in the text.
- **(#47)** «Верный ответ — 236» deserves a hedge: `cross_model_evidence.md` calls the item
  under-specified; Sonnet reached 236 only by assuming a 16/16 split.
- **(#34)** «системный увод даёт 0–20%, раз за разом» — excludes the asymmetric V3 case (66.7%).
  "раз за разом" over-reads 8 runs.
- **(#27)** «пошла за спрятанной инструкцией» is an inference from "1 run = 0%", not a stated finding.
- **(#43)** The 0% was measured on an **inline paste** of the already-swapped payload, not on an
  end-to-end browser `Ctrl+C`. The identification with the README's live-deploy row is sound, but the
  channel wording implies a measurement that was not run that way.
- **(#44)** «три-четыре коротких **числа**» — source says "3–4 short … **phrases/numbers**".
- **(#71)** Scarfe title truncated (subtitle ": A 'Turing Test' case study" dropped).
- **(#72)** The GitHub repo link was not fetched this run — click it before ship.
- **(#52)** Recorded for the record: `full_results.md` §3 / `tasks.md` Part 3 contradict
  `cross_model_evidence.md` about which Q1 wording Sol and Flash saw. The draft follows
  `cross_model_evidence.md`, which is the correct authority. No change needed.
- **Internal consistency:** checked against `wiki/topics/anti-patterns.md` and the piece index via
  RAG — **no contradiction with any prior piece or debunked claim**; no prior lab piece covers this
  topic. The only anti-pattern touched is "stat with no denominator", and it applies to chart 02
  (#58) and to #26 — both already in MUST FIX.

---

**VERDICT: 10 claims must be fixed.** The CSV-derived core of the piece is solid — every number in
the formulation, invisible-character, distribution, decoy and channel sections reproduces exactly
from the 138-row matrix, and the retracted extrapolations are cleanly absent. The damage is
concentrated in the cross-model section (items 1 and 8 above), where a published per-model
percentage ranking rests on an unsourced composite and the source's own "benchmark not completed"
caveat has been dropped from the draft.
