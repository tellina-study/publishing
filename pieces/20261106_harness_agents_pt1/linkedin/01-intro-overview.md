---
channel: linkedin
status: draft
title: Honest measurements say the harness matters less than you'd think
image: card_intro_overview.png
series: harness-agents-pt1 (post 1 of 6)
---

**Honest measurements say the harness matters a lot less than you'd think.**

Here's what I've measured so far: I picked up Claude Code, Hermes, and DeepSeek Harness and ran a first, light comparison across nine tasks. The most surprising finding: running the same agent with the harness on vs. off doesn't give the harness a clean win at all. It depends on the task.

And that's not a vibe, it's measured. Across all three agents, on "investigate" tasks (gather facts, don't touch the code) the harness reliably cuts steps — down to about 0.84× of what the agent needed without it. On "build" tasks, it's the opposite: about 1.16× more steps. Same harness, same rules, opposite direction, just depending on what kind of task it's pointed at. There's a lot more to try here, but it already looks like these agents are smart enough to find the context they need on their own, without spelling out basic instructions for them.

On the agents themselves: Claude Code is the most token-hungry — and the most stable. Hermes looks a lot cheaper, but also worse at actually getting tasks done (though, to be fair, it was running bare, untuned). DeepSeek Harness, so far, comes out ahead of both — it eats less than Claude Code and solves more than Hermes.

One more thing that surprised me: you can't just trust what an agent says about its own cost. Claude Code turned out to have three token counters under the same label, up to 25× apart from each other on tasks involving sub-agents — plus a separate bug where a missing row in its price table made it report one run's cost at roughly 50× the real one. Hermes conflates fresh and cached tokens after the fact, for up to a 10× price gap. I ended up recalculating every cost from the providers' own billing instead of trusting any agent's self-report — DeepSeek Harness was the only one whose own numbers actually matched the real bill.

And it's good-looking, open-source, and modular. So I forked it, and I'm building my own cloud "casino" on top of it :)

Details: https://tellian.io/2026/11/08/harness-agents-pt1/

#AIAgents #CodingAgents #OpenSource #DeveloperTools #Benchmarking
