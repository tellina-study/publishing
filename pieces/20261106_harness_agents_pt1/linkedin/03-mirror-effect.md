---
channel: linkedin
status: draft
title: Same switch, opposite effect
image: card3_mirror_effect.png
series: harness-agents-pt1 (post 3 of 5)
---

**Flip the exact same switch — turning a "harness" (rules, tools, memory) on — for two different AI coding agents, on the same task. One agent's cost went up 333%. The other's dropped 74%. Both still got it wrong.**

The task was a PR review with an answer key written independently in advance, so right and wrong were decided before we ran anything. Claude Code's cost quadrupled when the harness switched on. Hermes's cost dropped to a quarter. Neither agent found the actual defects in the pull request — with the harness, or without it.

Tokens moved in opposite directions. Correctness didn't move at all.

The same switch doesn't do the same thing twice. Tune a setup for one agent, and it's tuned to that agent's own habits — not something that automatically carries over to the next one.

Has switching tools or agents ever flipped a setup that "just worked" for you?

Full study, open data, open tooling: https://tellian.io/2026/11/08/harness-agents-pt1/

#AIAgents #PromptEngineering #DeveloperTools #LLM #Benchmarking
