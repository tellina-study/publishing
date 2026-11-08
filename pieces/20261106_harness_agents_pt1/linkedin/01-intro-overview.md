---
channel: linkedin
status: draft
title: Here's what I measured so far
image: card_intro_overview.png
series: harness-agents-pt1 (post 1 of 6)
---

**Here's what I've measured so far. Haven't gotten to task G yet — but I've picked up Claude Code, Hermes, and DeepSeek Harness and run a first, light comparison.**

The most surprising finding: running an agent with the harness on vs. off doesn't give the harness a clean win at all. It depends on the task. There's a lot more to try here, but it already looks like these agents are smart enough to find the context they need on their own, without spelling out basic instructions for them.

On the agents themselves: Claude Code is the most token-hungry — and the most stable. Hermes looks a lot cheaper, but also worse at actually getting tasks done (though, to be fair, it was running bare, untuned). DeepSeek Harness, so far, comes out ahead of both — it eats less than Claude Code and solves more than Hermes.

And it's good-looking, open-source, and modular. So I forked it, and I'm building my own cloud "casino" on top of it :)

Details: https://tellian.io/2026/11/08/harness-agents-pt1/

#AIAgents #CodingAgents #OpenSource #DeveloperTools #Benchmarking
