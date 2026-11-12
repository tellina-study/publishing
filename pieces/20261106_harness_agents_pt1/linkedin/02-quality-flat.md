---
channel: linkedin
status: draft
title: Same score, harness on or off — that's the surprising part
image: card1_quality_flat.png
series: harness-agents-pt1 (post 2 of 6)
---

**Same task, same agent, harness on vs. off — the quality score didn't move. Not once.**

I ran this on three agents: Claude Code, Hermes, DeepSeek Harness. Each one got the same task twice — once with the full harness (rules, tools, memory wrapped around it), once without.

DeepSeek Harness scored full marks either way. Claude Code scored the same partial result either way. Hermes scored zero either way — it didn't touch a single file in either run. Out of the nine tasks I ran, this was the only one where the three agents actually differed from each other on quality — and that difference had nothing to do with the harness. It's just how good each agent already is on its own.

Here's the part that matters if you're deciding whether to build one of these setups in production: for Hermes, switching the harness on didn't rescue the zero, it just made the attempt roughly four times more expensive. The same rules that cut Claude Code's steps on other tasks here made Hermes re-read the requirements and check against the checklist over and over, without ever getting to an edit. Effort went up; the outcome stayed exactly as zero as before.

So if not quality — what do you think a harness like this is actually buying you?

Full study, open data, open tooling: https://tellian.io/2026/11/08/harness-agents-pt1/

#AIAgents #DeveloperTools #Benchmarking #LLM #SoftwareEngineering
