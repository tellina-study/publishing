---
channel: linkedin
status: draft
title: 'Just use a cheaper model'
image: card4_cheap_model_payoff.png
series: harness-agents-pt1 (post 4 of 5)
---

**"Just switch to a cheaper model" is the same advice for every agent. The payoff isn't.**

We moved two coding agents from the expensive version of a model to the cheap one in the same lineup, same tasks. Claude Code's bill dropped 9×. Hermes's dropped 56×. More than a sixfold gap between them, from the identical switch.

The rate card is the same for both. What differs is how each agent is built — how often it calls the model, and how much it rereads from cache instead of resending fresh. Cache is priced differently from a fresh token, so an agent that leans on cache gets a double discount when the model gets cheaper. One that doesn't, gets a single one.

If you're optimizing spend by model tier alone, the agent's own architecture might matter more than the price list.

Anyone measured this on their own stack — did the "obvious" savings actually show up?

Full study, open data, open tooling: [link to tellian.io]

#AIAgents #CostOptimization #DeveloperTools #LLM #Benchmarking
