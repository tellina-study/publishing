# The coding-agent harness effect: what rules+tools+memory actually buy you

Our evergreen take on what happens when you wrap a coding agent in a **harness** — a rules file,
a set of tools, and memory carried between steps — on top of its stock setup. Settled (so far) by
[harness-agents-pt1](../pieces/INDEX.md) (live 2026-11-08,
[blog](https://tellian.io/2026/11/08/harness-agents-pt1/)). **This is Part 1 of a series — the
take below is deliberately partial, not a final verdict.** Part 2 (not yet written) takes the
harness apart into its components (memory / tools / connected helpers / external access / rules
text) to find which piece is actually doing the work. Don't re-derive the base measurement —
extend it as Part 2 and later pieces land.

## The method, in one line

Three agents (Claude Code, Hermes, DeepSeek Harness/dsh), the same nine tasks, each run twice —
harness on vs. harness off, model held fixed — 54 runs total, n=1 per cell. Full dataset and
methodology are open: [`workain/research-results`](https://github.com/workain/research-results/tree/main/2026-11_harness-agents).

## Durable takeaways (as of Part 1 — expect refinement in Part 2)

- **The harness is not an unconditional win.** Quality never moved, on any task where it could be
  measured at all (3 of 9 tasks carried a rubric). Whatever the harness buys, in this sample it
  isn't a better answer.
- **The harness's effect on spend is not one effect — it's three, and they don't generalize from
  each other:**
  1. A **genre-dependent effect, shared by all three agents** — "investigate" tasks get cheaper
     under the harness (≈0.84× the steps), "build" tasks get pricier (≈1.16× the steps); the
     per-step price barely differs by genre, so the two multiply into very different outcomes.
  2. An **agent-task-specific effect that can flip sign entirely** — the same harness switch, same
     task (J), raised Claude Code's tokens ≈4.33× and *dropped* Hermes's to ≈0.26× (dsh landed in
     between, ≈1.57×) — a 16.5× gap between two agents on the identical switch.
  3. A **pure-cost-no-outcome-change effect** — on task G, turning the harness on made Hermes's
     already-zero attempt (0 files changed either way) cost roughly 4× more, with no change to the
     outcome at all. Effort and outcome are different quantities; the harness only reliably moves
     the first.
- **Agents differ from each other, harness aside, by at least as much as the harness changes
  anything — sometimes far more.** Hermes's own repeat-run spread (up to 9.3×, same task, same
  settings, run twice) exceeds the single loudest harness effect measured anywhere in the study
  (Claude Code, 4.33× on task J). Comparing two agents off one run each risks ranking noise, not
  agents.
- **No agent wins on both cost and quality at once** at the aggregate level across all nine tasks.
- **Self-report honesty about an agent's own cost/token count is agent-specific, not a general
  rule** — Claude Code's own counters disagreed by up to ≈25× on tasks with sub-agent delegation
  and had a separate ≈50× bug from a missing price-table row; Hermes conflated fresh/cached tokens
  for up to ≈10× price discrepancy; dsh's self-report matched independent provider billing closely
  across all 18 of its runs. Don't trust an agent's printed cost number without checking which
  counter it is.
- **A cheaper model from the same lineup pays off very differently by agent** (≈9× for Claude
  Code, ≈56× for Hermes) — driven by each agent's own call count and cache-read share, not the
  rate card — and **capability at that price is also agent-specific**: on the same cheap model,
  same task, dsh scored full marks, Claude Code half marks, Hermes zero. A harness won't rescue a
  task the agent can't do at the price you picked.

## What this piece deliberately does NOT claim

- **No "you need a harness" / "you don't" verdict.** The piece is explicit that this question
  needs to be asked per task-type and per agent, not resolved in general — and that this is Part 1
  of a series precisely because the whole-harness question is the wrong grain of question.
- Not a claim that any one agent is simply "better" — see
  [anti-patterns](anti-patterns.md) for what *is* settled (and what remains open).

## Open, for Part 2

If the whole-harness effect is this uneven — helps here, hurts there, depends on who got it — is
the benefit (or the harm) concentrated in one or two of the harness's components (memory, tools,
connected helpers, external access, rules text), with the rest riding along as paid-for ballast?
That decomposition is Part 2's job, not Part 1's — update this page's take once it ships rather
than inferring an answer here.

## Related

- [Prompt packaging](prompt-packaging.md) already named the agent harness as "the costliest class
  of prompt" (huge, long-lived) before this piece measured it directly — this piece is the
  follow-through on that claim with real runs.
- [Anti-patterns / debunked claims](anti-patterns.md) — the specific claims this piece settled.

## Sources

Two external benchmarking papers cited in the piece, plus our own open dataset — curated in
[`sources/INDEX.md`](../../sources/INDEX.md): `coding-agents-converged`,
`same-model-different-harness`, `agent-runtime-instruments`,
`workain-research-results-harness-agents`.
