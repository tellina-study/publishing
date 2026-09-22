# Roast: lec3-agent-scaling (linkedin.md, v4)

Independent editorial critique (run by the `editor` agent — **not** the writer). Function: find
what's weak so we fix it before readers do. Checked against `brief.md` (delivered the promise?
drifted into DO-NOT?) and `blueprint/channels/linkedin.md` (channel canon, incl. the 2026-09-21
owner correction on hook style).

## Critical (must fix before ship)

1. **"17x" / "4x" topology stat has no stated baseline.** — para 2, lines 13–16 ("an independent
   swarm of agents amplifies errors close to 17x, while one coordinator managing the same agents
   holds it closer to 4x"). 17x/4x *relative to what*? A single agent doing the whole task alone?
   Zero agents? The comparison basis is never named, unlike the two other stat blocks in the same
   post (τ-bench: "same task, same model, just repeated"; tokens: "vs a single chat call"). For a
   reader with zero agent-framework background this is the single most confusing number in the
   post — it sounds precise (17x!) while actually being unanchored. **Fix:** add the missing
   clause, e.g. "...amplifies errors close to 17x compared to a single agent doing the task alone."

2. **"4x" is reused for two unrelated quantities in adjacent paragraphs.** — line 15 ("one
   coordinator... holds it closer to 4x") vs. line 18 ("One agent burns roughly 4x the tokens of a
   single chat call"). Same number, same paragraph-distance, completely different referents (error
   amplification factor vs. token-cost multiplier). A 5-second skim reader is exactly the reader
   most likely to conflate these — "wait, didn't we just say coordinator = 4x?" **Fix:** change one
   of the two numbers' framing/wording so they're visually distinguishable, or explicitly
   contrast them ("a *different* 4x — this one's about tokens, not errors").

3. **The topology figure is stated as an established fact, not a single (unverified) study's
   result — unlike the other two stats in the same post.** — para 2 vs. para 3. The τ-bench line is
   explicitly scoped ("on a benchmark of realistic agent tasks... one model solved..."); the
   token-cost line has "roughly" and "closer to." The topology line has "close to" too, but no
   framing that this is *one paper's* number, not a settled multiplier — and per the brief's own
   `[VFY-day-of]` flag in the source chapter, even the course itself isn't confident in this figure
   yet. Per the channel canon's "less categorical" rule, this is the stat most in need of a hedge
   ("in one recent study...") and currently has the least. Treating it as flat as the other two
   overclaims relative to its own sourcing status.

4. **The post stacks four distinct ideas, not one.** — reliability-compounds-multiplicatively
   (para 2a), topology/coordinator-vs-swarm (para 2b), cost multiplier (para 3a), benchmark
   pass@1-vs-pass@8 (para 3b), three mitigations (bullets), workflow-vs-agent (para 5). Channel
   canon calls for "один разворот мысли" (one turn of thought) for a post like this. Six numbers
   and effectively four separable claims is a lot to track in a feed skim, even with good
   transitions — this reads as "stitched together" more than the channel's own bar wants, and is
   the most likely reason a first-time reader bounces mid-post rather than reaching the CTA.
   **Fix:** the cost-multiplier stat (para 3a) is the weakest link to the actual thesis (topology +
   workflow-vs-agent) — consider cutting it and letting the τ-bench number stand alone as the
   "here's what the gap costs" proof point.

## Should fix

- **Self-reported word count is wrong.** The file's own footer claims "~350" words; actual count
  (measured, hashtags included) is **421** — 20% higher, and much closer to the 500-word channel
  ceiling than the draft's own note suggests. This matters because whoever gates this on "350,
  that's mid-range, fine" is gating on a false number; the real density is closer to the top of the
  range, which reinforces finding #4 above.
- **The 17x/4x stat doesn't get its own "so what" line.** Owner-taste (`blueprint/channels/
  linkedin.md`, 2026-09-01 entry): "После цифры — вывод до сути/цели, не филлер." The τ-bench block
  closes with "That gap is what 'reliability' actually costs" immediately after the numbers; the
  topology stat (lines 13–16) just ends on "(Kim et al., 2026)" — its payoff doesn't land until
  bullet 2, three sentences later ("that's the 4x vs 17x above"). Inconsistent with the pattern the
  post otherwise follows correctly.
- **The PocketOS case (brief's own narrative-spine step 1) was dropped entirely, not just moved.**
  The channel log's 2026-09-21 correction says drop story-*as-hook*, but explicitly leaves room for
  "конкретный кейс, если он вообще нужен, идёт ПОСЛЕ хука как иллюстрация" (after the hook, as
  illustration). v4 has zero concrete case anywhere — it's 100% abstract numbers. Given owner-taste
  is show-don't-tell and the case (agent deletes prod DB + backups in 9 seconds) is vivid and
  recent, this reads like an over-correction: swap "story-first" for "no story," rather than
  "story second." Worth one sentence reintroducing it as illustration, e.g. after the mitigations,
  or cut it deliberately and say so rather than by omission.
- **Citation format is inconsistent and one is untraceable.** "(Kim et al., 2026)" vs. "(Anthropic)"
  — the latter names no paper/post, just a company, so a reader who wants to check it has nothing
  to search for. Minor credibility/traceability gap, easy fix (name the source or drop the
  parenthetical).
- **Closing question is only loosely tied to the actual argument.** "Where do you draw the line —
  what would make you trust a longer agent chain with something you can't undo?" is about
  irreversibility/trust threshold; the body's actual claims are about topology (coordinator vs.
  swarm) and workflow-vs-agent detection. A question that grows more directly out of either of
  those (e.g., "when do you reach for a coordinator instead of letting agents run as peers?") would
  close the loop tighter.

## Minor / polish

- "Reliability compounds down, not sideways" is a clever line but the "down vs. sideways" spatial
  metaphor may not parse instantly for a no-ML-background skim reader; consider testing it against
  someone outside the field.
- Hashtags: `#AI #SoftwareEngineering #Agents #AIAgents #MachineLearning` — 3 of 5 tags
  (AI/Agents/AIAgents) cover nearly the same ground; trim to 3–4 for a curated rather than cloud
  feel (channel canon: "не облако").
- Opening line "AI agents get things done." is a soft, generic warm-up clause ahead of the actual
  contrarian claim in sentence two. Measured, the full two-sentence hook is ~130 characters, likely
  safe under LinkedIn's fold — but worth confirming render on mobile before shipping given the
  channel canon's emphasis on the literal first line carrying the hook.
- The file's own "Open before shipping" list (arXiv re-verification, lessons.tellian.io live-status
  confirmation, roast/mirror-editor routing) is still unresolved — not this pass's job to close, but
  flagging it stays a hard ship blocker regardless of this roast's verdict.

## What works (briefly)

- Hook correctly follows the 2026-09-21 owner correction: direct counterintuitive insight
  ("agents get things done... but chaining them without a plan makes things worse"), not a
  narrative/anecdote intro.
- τ-bench and token-cost stats are both properly scoped with explicit baselines and appropriate
  hedge words ("roughly," "closer to," "on a single try").
- Three mitigations are concrete and actionable, and correctly avoid naming the full five-pattern
  workflow taxonomy (DO-NOT compliance, brief item 2).
- Casual-reader carve-out and open closing question both hit the channel's required structural
  beats; CTA has no "if you've..." framing; single in-body link; emoji used as point-markers only.
- Avoids the "AI agents bad" reduction the brief explicitly forbids — acknowledges agents "get
  things done," offers concrete mitigations rather than a blanket dismissal.

## Verdict: REVISE
- substance_fraction: 0.7
- one-line: Give the 17x/4x topology stat an explicit baseline and stop reusing "4x" for two
  different things in back-to-back paragraphs — that's the pair most likely to confuse a
  5-second-skim reader and undercut the post's own credibility.
