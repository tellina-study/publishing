---
title: "Language, format, placement: how to write prompts an LLM understands better"
slug: language-format-placement
status: draft
categories: [Prompt Engineering]
tags: [LLM, Prompts, Tokenization, Context Engineering]
# wp_post_id:   — auto-filled after first publish; do not set by hand
---

**I spend my days wrangling big prompts to language models — and the same question keeps coming up: what actually works better?** Is it true that if you write tersely, telegraph-style, with no filler, the model both understands more precisely and costs you less? People say Chinese prompts come out cheaper — does that hold up? And more broadly: does the language you write in matter, do you really need headings and lists, and where do you put the main question so it doesn't get lost?

These questions come up on their own; now and then you stumble onto something worth passing along. I dug through the research, checked it against my own experience — here's what came out. Sharing it.

**TL;DR.** The short version — here's what works:

- 🌐 **Language.** It pays to write your instructions in English: in another language the prompt doesn't shrink, it bloats — a non-English language costs the model roughly twice as much (for Russian, about ×2). And "write in Chinese, you'll save tokens" is, for the popular models, just a myth.
- 📍 **Placement.** A model notices the beginning and the end best, and loses the middle easily. So put the most important things — and the question itself — at the edges; don't bury them in the middle.
- 🧱 **Form.** Simple markup with headings and lists is the clearest of all; save heavy technical formats for data, not for the request itself.
- ✂️ **Brevity.** Cutting filler words really does help — but it saves a real ~15–20%, not the promised "minus 75."
- 🔣 **Glyphs.** Emoji and box-drawing characters used to "save space" only get in the way.
- 🪜 **Order.** First sort out what goes where and how it's formatted, then language, and squeezing the length is the very last thing to do.

If you're just chatting with a bot, the first two — language and placement — are what truly help you; the rest matters more for people tuning a model to their task or wiring it into a product. From here, each point in turn, with examples and numbers.

---

## Before you start: two budgets

Whatever you're writing to the model, it all comes down to two limited resources — and almost every technique below is about spending them wisely.

### 💰 The token budget — that's money and space

The model doesn't see letters: text is cut into tokens (chunks of words), you pay per token, and tokens are also what fills up the context window. You don't do the cutting — the tokenizer does, and unevenly: the same meaning takes a different number of tokens across languages and formats. An English phrase packs noticeably tighter than a Russian one; clean Markdown packs tighter than the same meaning in JSON. By exactly how much — we'll count in the techniques; the gap between languages isn't a matter of percent, it's a multiple.

### 🎯 The attention budget — that's quality

Even when everything fits in the window, the model reads it unevenly: attention is a finite resource, and it goes mostly to the edges, while the middle sags. The longer the prompt, the stronger the effect. So where you put the important stuff directly decides whether the model notices it.

Next we'll go through five key techniques for working with prompts and optimizing these budgets. But the same technique costs differently in a live chat and in a prompt "baked into" a product: in one place a miss is pennies, in another it multiplies across millions of calls. So keep four task types in mind — each with its own cost of error and its own budget headroom:

### Four task types

- **Chat** — you write to the model directly, in plain words, one-off. A mistake is cheap: didn't like it, you ask again.
- **Production prompt** (system prompt) — a single prompt baked into a product and called at scale; the answer is often parsed by code. Every extra token and every ambiguity multiplies across the call volume.
- **Agent harness** — the permanent "scaffolding" of an autonomous or coding agent: instructions, a skill set, tool descriptions, memory between steps. The context is huge and long-lived, so the cost — both in tokens and in inattention — is highest here.
- **Data** — whatever you pour inside any of the three: documents, tables, tool outputs, chunks pulled in by search. Broken out separately, because data has its own packing rules.

---

## Technique 1 · 🌐 Language and tokenization

Choice of language is a lever on cost and quality, not on size: you won't shrink a prompt by switching languages, but you can easily overpay and lose precision. On Western models an English instruction core is usually both cheaper and more accurate — but you can address the model in whatever language is convenient, and that works fine.

**Why the same meaning costs different amounts.** Two things get conflated here. First, information density: how much meaning fits in a character (it's high for ideographic scripts). Second, how the tokenizer cuts the text: under the hood is BPE (byte-pair encoding — slicing into frequent chunks), trained mostly on English, so it encodes English economically and fragments the rest. These two forces pull in opposite directions — and the slicing outweighs the density.

Rough guides for Western tokenizers:

- **English** — about 4 characters per token, the most economical language.
- **Non-English languages** — multiples more tokens for the same meaning. Russian, for example, is roughly twice as many: [Tokenizer Tax across 25 European languages (2026)](https://arxiv.org/abs/2605.24718), the first controlled comparison on parallel texts, puts Slavic languages at the most expensive end, while [Petrov et al. (2023)](https://arxiv.org/abs/2305.15425) gives a gap of more than 4× for some language pairs — and English carries the smallest markup.
- **Cyrillic** pays extra at the byte level: a [study on Ukrainian (Frontiers, 2025)](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1538165/full) reminds us that a Cyrillic character is encoded as 2 bytes even when it isn't in the vocabulary.

[STRR (2025)](https://arxiv.org/abs/2510.09947), on six tokenizers and seven languages, confirms the same picture: English keeps tokens-per-word consistently low, and outside the Latin script it's high.

> 💡 **What this means in practice.** The same prompt in a non-English language is multiples more tokens; for Russian it's about ×2: twice as expensive, and you hit the window twice as fast. Not by percentages — by multiples.

This is also where the advice "write in Chinese, you'll save tokens" falls apart. The ideograph is dense, but the tokenizer fragments it into several tokens, and the gain gets eaten. A direct test came from [Mythbuster (2026)](https://arxiv.org/abs/2604.14210) (preprint): the saving isn't confirmed, it depends on the model, and quality in Chinese is on average lower. For the popular models, Chinese isn't cheaper — and not rarely it's more expensive and worse. So language by itself doesn't shrink the prompt: all of English's advantage is in the price of tokens and in quality, not in size.

### A common case: English instructions — answer in the user's language

English lives better in instructions — but it's often more convenient and more effective for the user to write in their own language, and that works. The typical setup: system prompt and instructions in English, while the user writes in their own language and wants the answer in it too. The setup works; let's look at its strengths and the places where it stumbles.

**Why an English core pays off.** The English-centricity of models is a measured fact. [Cross-lingual studies (2025)](https://arxiv.org/abs/2504.10906) consistently give English instructions first place on quality — *with an important caveat*: for small post-trained models (7–9B) the picture flips in places, and the native language works no worse. That is, "English is better" is about large frontier models, not a law of nature. Plus an English core is cheaper in tokens.

**How to keep a non-English output from "drifting."** There are proven techniques:

- **Give the output-language command on a separate line and at a pole** (at the start or the end), don't weave it into the middle. [Language Confusion (EMNLP 2024)](https://arxiv.org/abs/2406.20052) shows it directly: an isolated language instruction confuses the model noticeably less than an integrated one, and **a single example** lifts the share of correct-language output to about 80% even where the model was floundering.
- **Align the language of input, reasoning, and output.** [When Language Shapes Thought (2025)](https://arxiv.org/abs/2505.24409): a forced mismatch ("think in one, answer in another") worsens knowledge retrieval. If you need nuance in the user's language — let it reason in that language too; if factual accuracy matters more — English reasoning plus a translation into the user's language at the end.

**Where it stumbles:**

- **Matching languages doesn't save you on its own.** [Tears or Cheers? (2026)](https://arxiv.org/abs/2601.13024): English prompts are on average better, while matching the prompt's language to the data's language does *not* improve quality. "At least it's all in one language" is not an argument.
- **Translation loses shades.** The "English core → user-language render" chain is accurate on facts but poorer on nuance and tone than reasoning in the user's language. For legal or cultural nuance, that's a price.
- **Safety.** [XSafety (2023)](https://arxiv.org/abs/2310.00905): on non-English prompts models more often produce unsafe answers — for production systems with user input that's a separate risk, which an English instruction core partly removes.

> 📌 **Short recipe.** English instructions + an explicit, isolated output-language command + one example. Reasoning in the user's language — where nuance matters; an English core with a translation at the end — where accuracy and cost matter more. And don't expect "everything in one language" to improve anything on its own.

### On tone: politeness and language

An unexpected but tested nuance. [Mind Your Tone (2025)](https://arxiv.org/abs/2510.04950), on a small sample, found that a slightly rude prompt gave higher accuracy than a polite one. It's tempting to conclude "be rude to the model" — **but don't rush**: [a cross-lingual study (2024)](https://arxiv.org/abs/2402.14531) shows that the politeness optimum *depends on the language*, and the balance point is different for each. For most non-English languages there's no separate measurement, so the takeaway is modest: excess politeness ("please, would you be so kind, if it's not too much trouble") is just tokens, you can cut it; deliberately being rude isn't worth it.

| ✅ Pattern | ⛔ Antipattern |
| --- | --- |
| Instructions in English; language command explicit, at a pole, + one example | Shrinking a prompt by "rewriting it in Chinese" |
| Aligned language of input / reasoning / output | Forcing the model to think in one language and answer in another with no need |
| Cut excess politeness (it's just tokens) | Thinking "at least it's all in one language" will improve the answer |

---

## Technique 2 · ✂️ Caveman / brevity (telegraphic style)

"Caveman," telegraphic style is when you throw out the "glue" (function words, courtesies) and keep only the substance: rules, tool names, values. Example:

> **Before:** "Please, would you mind, if it's not too hard, looking through the list below and removing the duplicate entries from it."
> **After:** "Scan the list, remove duplicates."

Same meaning, a third of the tokens. This style fully pays off in agents, in a lightened form — in system prompts, and in ordinary chat it isn't needed: there's no point squeezing a one-off short request. On instructions it saves **about 15–20%**, not the viral "−75%."

Where the numbers come from. "−75%" is a best case and only for *output* tokens ("up to 75%" on a chatty answer), not a saving on the prompt itself. By actual measurements it's more modest, but still nice:

- On instructions — **~15–20%** (14–21% across different measurements) while preserving meaning. In one reproducible micro-test by the author, [an 85-token distillate beat a 552-token prompt while keeping 100% of the facts](https://github.com/kuba-guzik/caveman-micro) — it's not a big benchmark, but it's telling.
- In multi-turn sessions with caching it adds up to [~39%](https://betterstack.com/community/guides/ai/caveman-llm/).
- Agentic patterns cut more radically: [CaveAgent (2026)](https://arxiv.org/abs/2601.01569) — −28% total tokens with a rising success rate by collapsing steps.
- The bonus isn't only about money: [Hakim, "Brevity Constraints" (2026)](https://arxiv.org/abs/2604.00025), on 31 models and 1485 tasks — a brevity constraint raised large-model accuracy by +26 pp where verbosity was confusing things (the model talks itself into the wrong answer). This is one study so far, but the effect is striking.

A counterweight from practitioners cools expectations: the saving across a whole session more often comes out at ~4–10%, and [part of what's claimed doesn't survive to the token bill](https://medium.com/hecatus-research/less-is-more-for-llms-a-critique-of-prompt-based-compression-910978d8bad4).

**An important caveat about reasoning.** Apply telegraph to *instructions and output*, but **not to the internal chain of reasoning**: with DeepSeek-R1 or Claude in extended thinking, clamping the reasoning is harmful. And don't over-engineer the compressor itself — a short directive ("be concise, cut the water, keep all rules and values") beats an elaborate rulebook.

| ✅ Pattern | ⛔ Antipattern |
| --- | --- |
| Cut the glue in reusable and agentic prompts | Turning on telegraph for a one-off chat request |
| Preserve rules, names, values verbatim | Cutting so hard that meaning is lost |
| Brevity on the final output | Clamping the internal reasoning of a reasoning model |

---

## Technique 3 · 🧱 Formats: Markdown, XML, YAML, JSON

Models understand Markdown best: training text is saturated with it, and the tokenizer encodes it economically, whereas JSON with its brackets and quotes gets fragmented. And keep in mind that **the markup itself is also tokens**: every tag, bracket, and quote is paid for, so heavy markup (XML, JSON) on the same content comes out more expensive than light markup (Markdown).

And a model best understands the formats it has seen a lot of in training, *regardless* of their theoretical elegance. The fate of the TOON format is telling: it saves tokens but loses on comprehension, because there are few examples of it. All of this applies first of all to the body of the instruction (the system prompt) and to the form in which you feed in data.

> 🛠️ **From my practice: structure pays off twice.** While you're breaking the instruction into sections and bullets, you're clarifying it for yourself — half of a prompt's bugs get fixed simply because you write *structurally* rather than as a wall of text. And only then the second payoff: the model reads such an instruction more precisely. So structure works for you even before it reaches the model.

> 🛠️ **From practice: write it readably while a human is working with the prompt.** When you yourself read and debug the instructions and answers, a human-readable format (Markdown, YAML) is half the battle: your eyes can see where the prompt broke and what the model misread. But if both the prompt and the answer are generated and consumed only by code, readability is no longer the priority — optimize for the machine.

**How to apply it:**

- **Instruction body — Markdown** (headings, bullets). Mark up the prompt like a short article: `## Role`, `## Context`, `## Task`, `## Output format`, with lists inside. That format affects quality is confirmed by [He et al. (2024)](https://arxiv.org/abs/2411.10541): for GPT-3.5 the spread across templates reached 40% (large models are steadier). There's no single optimum, but Markdown is a solid default.
- **Section boundaries — XML tags** (`<instructions>`, `<context>`, `<examples>`, `<output_format>`). Wrap large blocks in tags so the instruction doesn't "leak" into the data, or an example into the context. XML is verbose, so it's a container for boundaries, not the language of the body itself.
- **Nested data — YAML, not JSON.** The same data in YAML is shorter and readable by eye — indentation instead of a ladder of brackets and quotes. In [improvingagents (2025)](https://improvingagents.com/blog/best-nested-data-format/) measurements YAML beats XML, which inflates tokens by +80% over Markdown (on most models). For tables, [Markdown-KV is good (~60.7%, benchmarked on GPT-4.1-nano)](https://improvingagents.com/blog/best-input-data-format-for-llms/).
- **JSON — only at the output boundary**, where the result is parsed by code (for example, the answer goes to an API or a script). Rigid structured output chokes reasoning: [Tam et al., "Let Me Speak Freely?" (2024)](https://arxiv.org/abs/2408.02442) records a noticeable drop. Let the model solve a reasoning task in prose, and package the finished answer into JSON in a separate step.

**About trendy "economical" formats — go carefully.** Serializations keep surfacing with the promise of "the same data, but a fraction of the tokens." The big one right now is **TOON** ([Token-Oriented Object Notation](https://github.com/toon-format/toon)): a compact repacking of JSON — indentation instead of brackets, tabular rows for homogeneous arrays. The interest is real (a 1.0 release, thousands of stars, SDKs for dozens of languages), and imitators are already multiplying. Before you move a prompt to a trendy format — a couple of sobering facts:

- **Cheaper ≠ clearer, and the saving is measured against bloated JSON.** The claimed "minus 40–55%" is against "indented" JSON: against compact JSON the gain drops to about 25%, against YAML to 38%, and for flat tables plain **CSV is shorter than TOON itself**. And in a comparison of 11 formats ([improvingagents, 2025](https://improvingagents.com/blog/best-input-data-format-for-llms/)) the most economical, CSV, gave the worst accuracy (~44%), while the most accurate, Markdown-KV (~61%), cost almost three times more tokens.
- **But it's not "always worse" either.** On homogeneous tabular data, TOON in its own benchmark beats JSON on both axes at once. So it's not "economy always kills comprehension," but **a trade-off whose direction depends on the shape of the data and on what you're comparing against** — an independent measurement ([Matveev, 2026](https://arxiv.org/abs/2603.03306)) on short contexts actually handed accuracy to plain JSON.

And don't confuse format with **prompt compression** (like LLMLingua, which uses a separate model to throw out low-value tokens) — that's a different tool.

The takeaway: chasing an economical format for the sake of tokens almost never pays off in the instruction body. For data it's sometimes justified — but only if you measured it on your own task and data shape, rather than believing the headline.

| ✅ Pattern | ⛔ Antipattern |
| --- | --- |
| Markdown body + XML section boundaries | Writing the whole instruction body in JSON |
| YAML / Markdown-KV for data | Deeply nested JSON as a reasoning format |
| JSON only on a parsed output | Rigid JSON output on a reasoning task |

---

## Technique 4 · 📍 Placement and attention

> 💡 The important things and the question itself go at the poles of the window, not in the middle: attention barely reaches there. Don't count on the whole window: the reliable length is less than in the spec, and the longer the prompt, the more a placement miss costs.

Behind this are several converging results. [Lost in the Middle (2023)](https://arxiv.org/abs/2307.03172): accuracy is U-shaped — higher when the needed thing sits at the edges, and it sags in the middle (on multi-document QA — a gap of around 20 points). [Found in the Middle (2024)](https://arxiv.org/abs/2406.16008) exposes the mechanism: attention itself is distributed toward the poles, *regardless* of where the answer lies. [Chroma "context rot" (2025)](https://research.trychroma.com/context-rot): similar but irrelevant content actively throws it off — even one extra chunk drops quality, four make it worse. And the working length of the window is shorter than advertised: ["Context Is What You Need" (2025)](https://arxiv.org/abs/2509.21361) records effective context many times below the stated figure, and the benchmarks [NoLiMa (2025)](https://arxiv.org/abs/2502.05167) and [RULER (2024)](https://arxiv.org/abs/2404.06654) show that already at 32K half the models fall apart. **The space the model actually trusts is smaller than the spec says, and its middle is the weakest.** Now — where to put what, by task type:

- **Chat:** if a long document is pasted above, put the question itself at the very end.
- **Production prompt:** the format spec and the variable part — at the tail.
- **Harness:** critical rules — at the poles: the context is huge (200k+), and the middle sags the most. The stakes here are many times higher than in chat.
- **Data:** relevant chunks — at the poles, ranked by relevance; don't dump everything "just in case": the extra only throws it off.

This also applies to **examples (few-shot)**: [a study on the positional bias of few-shot (2025)](https://arxiv.org/abs/2507.22887) shows that the *same* block of examples, shifted by position, moves accuracy by up to 50 pp. Examples are not only "which" but "where."

And while we're on examples — it's better to set the form of the model's answer by a sample than by a prohibition:

> 📌 **An example beats a prohibition.** "Don't do X" without showing "do it like this" works poorly — the model latches onto the form of the example, not onto the abstract prohibition. For a structured answer this rule is ironclad: give at least one sample.
>
> ```
> ⛔ Prohibition without a sample:
>    "Don't write at length. Don't use markdown. Answer in JSON only."
>
> ✅ Structure + one sample:
>    <output_format>
>    Return JSON strictly per the sample:
>    {"verdict": "pass", "score": 0.87, "reason": "one short phrase"}
>    </output_format>
> ```

You can also **direct attention explicitly**, but with a caveat: [Attention Instruction (2024)](https://arxiv.org/abs/2406.17095) shows that a *by-index* pointer ("block #2," "section X") works reliably, while a vague "pay attention to the middle" is weaker. Inference-time methods like [SEAL (2025)](https://arxiv.org/abs/2501.15225) also help pull the needed thing out of a long context (it's a trainable attention-strengthening method, not just a prompt trick). On models — a separate section below.

| ✅ Pattern | ⛔ Antipattern |
| --- | --- |
| Key content, the question, and examples — at the poles | Hiding the main instruction or examples in the middle |
| One answer sample for structured output | A bare "don't do it like this" prohibition with no "do it like this" |
| Relevant data — toward the edges, ranked | Dumping everything into the window "just to have it" |
| A by-index pointer "look at block #X" | Hoping the model finds the needed thing in the middle on its own |

---

## Technique 5 · 🔣 Special characters, emoji, separators

The intuition that "compact glyphs save space" breaks against the tokenizer. A simple emoji weighs about a token, while composite ones — flags, modifiers — unfold into several byte tokens, sometimes up to a dozen, whereas the word "the" costs one. Box-drawing and ASCII tables are also expensive: a heap of tokens goes on the borders. Program symbols (`===`, operators), on the other hand, are cheap.

**Separators, though, are an underrated lever.** A separator is what you use to set off one chunk of the prompt from another: `###` in a heading, a `---` line, `<context>…</context>` tags, triple quotes around text, a vertical bar in a table. Seems like a trifle — but ["A Single Character can Make or Break Your LLM Evals" (2025)](https://arxiv.org/abs/2510.05152) shows that the choice of separator alone shifts the result by tens of percent, and — most unpleasant — **the fragility grows with model scale**: by picking a separator you can even tweak which model "wins" in a comparison.

> 📌 The takeaway isn't "find the magic symbol," but "pick sensible separators (Markdown headings, XML tags) and stick with them across the whole prompt."

A simple failure: in one section you set off blocks with hashes `###`, in another with asterisks, in a third with just a blank line; it's harder for the model to tell where the instruction ends and the data begins, and your own measurements turn to noise.

So for saving space, glyphs are useless — emoji and box-drawing are only a minus. But for reliability, the choice of separator matters more than it seems. Build structure with headings and tags, not with glyphs.

*(And yes — this post has emoji, but they're for you, the humans, to grab the key points on the run. Inside a prompt for the model there's no point putting them.)*

| ✅ Pattern | ⛔ Antipattern |
| --- | --- |
| Simple, consistent separators (Markdown/XML) | Changing separators from section to section |
| Minimum of decorative characters | Wrapping the prompt in emoji "for focus" |
| Structure through headings/tags | ASCII tables and borders for the sake of "looks" |

---

## How different models work

The techniques are general, but frontier models place their accents in their own way.

Everyone agrees on one thing: structure the prompt with XML tags or Markdown with explicit separators. And, as the [Gemini documentation](https://ai.google.dev/gemini-api/docs/prompting-strategies) puts it directly, the choice of format itself is secondary — what matters more is to pick one and stick with it. And in reasoning modes the advice is common to all: don't overload the prompt, don't force examples, give a high-level goal.

- **ChatGPT (OpenAI).** Instructions up front, separators sharp; responsive to a conversational, role-based style. GPT-5 has an anchored system layer.
- **Claude (Anthropic).** XML-native: tags for sections, the request at the end of a long context (Anthropic's docs record a gain of "up to 30%"). The guide ["Effective context engineering"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) calls for "the smallest set of high-signal tokens" and the "right altitude" for instructions; ["Building Effective Agents"](https://www.anthropic.com/engineering/building-effective-agents) adds, separately, that tool descriptions deserve as much attention as the prompt itself.
- **Gemini (Google).** Likes compact prompts; XML or Markdown — your choice, but consistently; terse by default. Grounding via search is a *toggleable tool*, not a phrase in the prompt.
- **DeepSeek.** V3/V4 [like structure](https://passhulk.com/blog/deepseek-prompt-engineering-guide-master-r1-v3-models-2025/): Markdown headings, bullets, and XML improve adherence. The cache works top to bottom: static content up top, the dynamic request at the end, don't mix them. R1 (reasoning) — no few-shot, high-level goals; JSON is weaker on R1 than on V3. (There's an idea that [XML markers help MoE routing](https://promptsera.com/how-to-prompt-deepseek-v4-xml/) — the model picks which of its many expert sub-networks to switch on — but that's the guess of a single blog, not a documented mechanism; don't bank on it.)

---

## Finale: assembling per task

### General decisions — for any task type

First, the cross-cutting questions: the answer to them doesn't depend on whether you've got a chat, a production prompt, or an agent.

- **Need to save?** First put placement and format in order, then think about language, and leave compression (caveman) for last: it gives the least and breaks meaning the most easily.
- **Is the task a reasoning one?** Let the model think in prose — don't clamp the reasoning with rigid JSON and don't turn on telegraph for the reasoning chain; you'll impose structure on the finished answer in a separate step.
- **Is the prompt long?** The important things and the question itself — at the poles, not the middle, and don't count on the whole window.
- **Does a program read the answer?** JSON only at the very output boundary and as a separate step — not in the same place where the model reasons.
- **Writing in a non-English language?** An English instruction core + an explicit output-language command at a pole + one example.

### Stack per type

**Chat — don't overcomplicate:**
- prose, a convenient language; the output-language command — explicit and at a pole;
- the question at the end, if there's a long text above;
- don't optimize tokens, don't turn on caveman. The cost of a mistake is pennies.

**Production prompt:**
- body — Markdown, section boundaries — XML;
- caveman-lite: cut the "glue," but preserve rules and names;
- a couple of canonical examples (few-shot);
- the format spec and the variable part — at the tail;
- JSON — only on the output that a program parses.

**Agent harness:**
- caveman full-bore; work tool descriptions like a separate prompt;
- critical rules — at the poles; memory between windows (a progress file);
- don't clamp the reasoning; remember that the effective window is smaller than stated.

**Data:**
- YAML or Markdown-KV instead of JSON/CSV; don't overcomplicate the format;
- cut into chunks and pull out what's needed, rather than dumping everything;
- the relevant stuff — at the poles.

And a quick run-through before sending a big prompt: key content and the question at the poles? body — Markdown, section boundaries — XML? JSON/YAML — only for data, not for the instruction body? "glue" cut (if the prompt is reusable or agentic)? reasoning not clamped? language command — with an example? separators chosen and uniform across the whole prompt?

And one last thing — so this mountain of numbers doesn't throw you off. Trust the large, repeatedly reproduced effects (important things at the poles, an English core is cheaper, rigid JSON chokes reasoning) and take the one-off sensational percentages more calmly: some of them live only in the way they were measured ([Flaw or Artifact?, 2025](https://arxiv.org/abs/2509.01790)). Have your own task — measure on it, not on someone else's benchmark.

---

## Sources

**Tokenization and languages.** [Petrov et al., 2023](https://arxiv.org/abs/2305.15425); [Mythbuster: Chinese is not more efficient, 2026](https://arxiv.org/abs/2604.14210) (preprint); [STRR / Beyond Fertility, 2025](https://arxiv.org/abs/2510.09947); [Tokenizer Tax, 25 European languages, 2026](https://arxiv.org/abs/2605.24718); [Ukrainian tokenization, Frontiers, 2025](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1538165/full).

**Caveman / brevity.** [Hakim, Brevity Constraints, 2026](https://arxiv.org/abs/2604.00025); [CaveAgent, 2026](https://arxiv.org/abs/2601.01569); [caveman-micro (Guzik)](https://github.com/kuba-guzik/caveman-micro); [Better Stack (≈39% with caching)](https://betterstack.com/community/guides/ai/caveman-llm/); [critique of compression, Hecatus, 2026](https://medium.com/hecatus-research/less-is-more-for-llms-a-critique-of-prompt-based-compression-910978d8bad4).

**Placement and attention.** [Lost in the Middle, 2023](https://arxiv.org/abs/2307.03172); [Found in the Middle, 2024](https://arxiv.org/abs/2406.16008); [Attention Instruction, 2024](https://arxiv.org/abs/2406.17095); [Chroma context rot, 2025](https://research.trychroma.com/context-rot); [Context Is What You Need (MECW), 2025](https://arxiv.org/abs/2509.21361); [NoLiMa, 2025](https://arxiv.org/abs/2502.05167); [RULER, 2024](https://arxiv.org/abs/2404.06654); [SEAL, 2025](https://arxiv.org/abs/2501.15225); [few-shot position, 2025](https://arxiv.org/abs/2507.22887).

**Formats.** [He et al., effect of format, 2024](https://arxiv.org/abs/2411.10541); [Tam et al., "Let Me Speak Freely?", 2024](https://arxiv.org/abs/2408.02442); [improvingagents: nested data](https://improvingagents.com/blog/best-nested-data-format/) and [tables](https://improvingagents.com/blog/best-input-data-format-for-llms/); [TOON (format + benchmark)](https://github.com/toon-format/toon); [Matveev, independent TOON measurement, 2026](https://arxiv.org/abs/2603.03306); [Flaw or Artifact?, 2025](https://arxiv.org/abs/2509.01790).

**Language, tone, safety.** [When Language Shapes Thought, 2025](https://arxiv.org/abs/2505.24409); [Language Confusion, 2024](https://arxiv.org/abs/2406.20052); [Tears or Cheers?, 2026](https://arxiv.org/abs/2601.13024); [cross-lingual retrieval, 2025](https://arxiv.org/abs/2504.10906); [Mind Your Tone, 2025](https://arxiv.org/abs/2510.04950); [politeness cross-lingually, 2024](https://arxiv.org/abs/2402.14531); [XSafety, 2023](https://arxiv.org/abs/2310.00905); [the separator decides, 2025](https://arxiv.org/abs/2510.05152).

**Context engineering and models.** [Anthropic, context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents); [Anthropic, building effective agents](https://www.anthropic.com/engineering/building-effective-agents); [Gemini prompting docs](https://ai.google.dev/gemini-api/docs/prompting-strategies); [DeepSeek guide](https://passhulk.com/blog/deepseek-prompt-engineering-guide-master-r1-v3-models-2025/).
