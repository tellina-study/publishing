---
channel: linkedin
status: draft
title: The harness can cost you more without buying you anything
image: card1_quality_flat.png
series: harness-agents-pt1 (post 2 of 6)
---

**Honest measurements say the harness can cost you more without buying you anything.**

I gave an agent a full harness — rules, tools and memory wrapped around it — ran one task with it on, then ran the exact same task with it off. Did that for three agents: Claude Code, Hermes, DeepSeek Harness. The quality score didn't move once.

DeepSeek Harness scored full marks either way. Claude Code scored the same partial result either way. Hermes scored zero either way — it didn't touch a single file in either run. Out of the nine tasks I ran, this was the only one where the agents actually differed from each other on quality — and that difference had nothing to do with the harness being on or off.

Here's the part that matters if you're deciding whether to build one of these setups in production: for Hermes, switching the harness on didn't rescue the zero, it just made the attempt roughly four times more expensive. The same rules that cut Claude Code's steps on other tasks here made Hermes re-read the requirements and check against the checklist over and over, without ever getting to an edit. Effort went up; the outcome stayed exactly as zero as before.

So if not quality — what do you think a harness like this is actually buying you?

Full study, open data, open tooling: https://tellian.io/2026/11/08/harness-agents-pt1/

#AIAgents #DeveloperTools #Benchmarking #LLM #SoftwareEngineering
