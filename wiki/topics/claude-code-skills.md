# Claude Code skills ecosystem — do they work, and how to vet a repo

Evergreen take from [`claude-skills-collections`](../pieces/INDEX.md) (published 2026-07-02,
[blog](https://tellian.io/2026/07/02/claude-skills-collections/)). Update when a new piece touches
Claude Code skills, agent tooling, or supply-chain hygiene for agent configs.

## Do skills work?
Yes — but the lift is **real and conditional**, not automatic.
- Proven in production and in one controlled benchmark: skill retrieval moved Terminal-Bench 2.0
  pass rate **57.7% → 65.5%** ([Skills in the Wild, arXiv:2604.04323](../../sources/INDEX.md#skills-in-the-wild)).
- Same paper is honest about the ceiling: gains **shrink on realistic tasks**, and the hard part is
  **triggering** — the model has to reach for the right skill at the right moment.
- Practical rule: **a couple of skills that fit your task beat a hundred installed "just in case."**
  Loading unused skills is context cost with no payoff.

## How to vet a skills repo (15-minute pass, before you trust it)
1. **Ignore the star count.** Stars measure hype, not safety or upkeep (see below).
2. **Check freshness, not fame** — last commit, open-issue backlog, whether PRs actually merge. A repo
   can be "244k stars" and abandoned (pushes stopped, queue didn't).
3. **`grep` for anything that runs itself** — `shell=True`, shell-outs, `curl | sh`, post-install hooks.
4. **`npm info` every package** an MCP/tool config tells your agent to install. Confirm the package and
   the **scope** exist and are the ones you think they are.
5. **Read the actual skill files** you'll use — a small vetted set > a big unaudited grab-bag.

## The map (7 collections, 2026-07)
- **Trust-first default:** [`anthropics/skills`](../../sources/INDEX.md#anthropics-skills) — first-party,
  auto-synced from internal, small and vetted.
- **Want a whole workflow, not a grab-bag:** [`obra/superpowers`](../../sources/INDEX.md#obra-superpowers)
  (skills + enforced end-to-end workflow).
- **Want more, tidy and personal:** [`glebis/claude-skills`](../../sources/INDEX.md#glebis-claude-skills)
  (~90 clean skills; 301 stars — small yet clean).
- **Discovery / link indexes:** `travisvn/awesome-claude-skills`, `jqueryscript/awesome-claude-code`.
- **Handle with care:** [`rohitg00/awesome-claude-code-toolkit`](../../sources/INDEX.md#rohitg00-toolkit)
  — real toolkit, but abandoned and carries the namespace-squatting defect below.
- Install/usage mechanics: [Claude Code docs](../../sources/INDEX.md#claude-code-docs)
  (`~/.claude/skills/<name>/`, `/plugin marketplace add …`, MCP config).

## Two durable anti-patterns this settled
Both logged in [anti-patterns.md](anti-patterns.md):
- **Stars ≠ safety/quality.** Cleanest audited repo = 244k stars; the one with the defect = 2.2k; a
  clean personal set = 301. Marketing counts inflate too ("1000+" ≈ 30–40 real).
- **Look-alike scope ≠ official.** `rohitg00`'s MCP configs point your agent at `@anthropic/mcp-ghidra`,
  `@anthropic/mcp-figma`, etc. — **all 404**. Anthropic's real scope is **`@anthropic-ai`**. A
  plausible-but-unclaimed official-looking scope full of hallucinated package names is a latent
  **namespace-squatting** risk class (an attacker could register those names). Never copy MCP configs
  blind; `npm info` first.
