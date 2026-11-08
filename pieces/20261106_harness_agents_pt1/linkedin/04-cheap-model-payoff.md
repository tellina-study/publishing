---
channel: linkedin
status: draft
title: Bigger isn't always better
image: card4_cheap_model.png
series: harness-agents-pt1 (post 4 of 5)
---

**Two AI coding agents got the exact same advice — switch to the cheaper version of the same model. The savings weren't close to equal. And "cheaper" didn't automatically mean "worse," either.**

Across the full test — 54 runs, three agents, token cost plus a quality check — no single agent came out ahead on both price and quality at once. The cheapest agent by tokens also scored the lowest on quality, where quality could be measured at all. The agent with the best quality score wasn't the cheapest one.

Then we looked at one specific move: shifting an agent from the pricier version of a model to the cheaper one in the same lineup, same tasks. Claude Code's bill fell roughly 9×. Hermes's fell roughly 56× — more than six times the gap, from the identical move. The difference comes down to how each agent is built: how often it calls the model, and how much it rereads from cache instead of resending context fresh — not the price list itself.

On the one task where we could compare a single agent's own result before and after that switch, Claude Code's score fell by half on the cheaper model. DeepSeek Harness, tested only on the cheaper model, still turned in a perfect score.

A pricier model isn't automatically the better choice. A cheaper one isn't automatically the worse one. Worth checking on your own tasks before assuming either way.

Has a cheaper model ever cost you more than it saved — or surprised you by holding up just fine?

Full study, open data, open tooling: https://tellian.io/2026/11/08/harness-agents-pt1/

#AIAgents #CostOptimization #DeveloperTools #LLM #Benchmarking
