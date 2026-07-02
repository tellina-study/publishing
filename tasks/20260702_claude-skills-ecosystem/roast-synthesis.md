# Roast synthesis — 3 independent lenses converged on REVISE

Editor (adversarial), mirror-editor (owner's taste), reader-fan (cold reader) all returned REVISE /
"meh-leaning-yes". Their findings overlap tightly. Consolidated ship-blockers:

## Ship-blockers (all lenses agree)

1. **Factual correction — the linchpin (editor, critical; mirror flagged credibility).**
   Real Anthropic npm scope = `@anthropic-ai` (verified: `@anthropic-ai/sdk`, `@anthropic-ai/claude-code`
   → 200), NOT `@anthropic` (404). Two consequences: (a) "reads as official" is imprecise — `@anthropic/`
   is a plausible look-alike, not the real namespace; (b) severity hinges on whether the `@anthropic`
   scope is *claimable* — the piece never establishes this. Reframe: latent namespace-squatting risk,
   not a "live supply-chain hole".

2. **Title/hook bait-and-switch (editor).** Title + first 3 paragraphs load all menace on
   `superpowers` (244k, "the biggest") — but Pattern 3 *exonerates* it, and the actual hole is in
   rohitg00 (2.2k, 5th of 7). Hook and payload point at different repos. "Live" over-claims what the
   body itself hedges ("*if* anyone ever claims that scope").

3. **Понты / victory lap (mirror + reader + editor — independent hits).** Repeated lab-credential
   flexing ("I run a lab about to build this", "how I manage my own lab", "the bar I held everyone
   else to"). Pattern 3 is self-facing ("didn't teach me anything new — confirmed what I'd built"),
   braids a second thesis. Scolding register ("Read that again slowly", kicker "what would you find
   if you actually read the thing you starred?"). Re-register to warm / on равных / "делюсь интересным".

4. **243,958 ages + no "live API" reassurance (all three).** Reader nearly bounced on disbelief at
   the quarter-million count; one clause ("pulled live from the GitHub API on <date>") defuses it.
   Precise numbers frozen in an evergreen post is also ironic given the thesis.

## Should-fix (editor + mirror nits)
- "two more" 404s → **three** (draft drops `chartlibrary_mcp`).
- "183 pull requests" vs source's "issues" — reconcile (source: 183 open **issues**; separately a PR backlog).
- "Most of them never read past the README" — invented denominator, self-refuting in a piece about denominators. Cut or soften.
- Traceability boast ("tied to a specific commit, file, line") but zero links in body — surface a couple or drop the claim.
- "tried to break them" oversells a read-and-grep audit.
- Reader wants a one-line definition of "skill" / MCP config up front (assumes knowledge).

## What all three praised (keep)
- The supply-chain finding itself — concrete, reproducible, novel, memorable.
- Pattern 1 number-inflation teardown (three sources in one repo agreeing on nothing).
- One explicit do-this-today takeaway (`npm info` every package before an agent runs a config).
- Voice broadly matches the channel; honest hedges ("not proof of malice", "self-reported 94%").

**Net:** the fixes are honest framing + de-flexing + one factual correction, not a rewrite. The spine
(the `@anthropic`-scope finding) is real and strong.
