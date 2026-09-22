# Mirror review: linkedin.md (v4) — 20260921_lec3-agent-scaling

## Where this misses Max's bar (must fix)

1. **"Same headcount, far fewer compounding errors — that's the 4x vs 17x above."**
   (tip #2, 🧭) — this restates a number the reader just read two paragraphs up and points
   backward with "above." Violates "показывать, не называть" / "не разжёвывать читателю" —
   he doesn't need the callback spelled out, the number already landed. It also reads as a
   footnote breaking into the flow (mild проговор: pointing at the post's own structure).
   Fix: cut the clause entirely, or fold the payoff into the tip itself without naming the
   earlier figures again ("coordinator, not swarm — the topology alone is most of the
   difference").

2. **First visible chunk before the LinkedIn fold is weaker than the actual hook.**
   Canon (2026-09-01, restated in log 2026-09-21): "первая строка = то, что видно в ленте до
   сгиба... это и есть хук." The twist — "gets worse at its job, not better" — sits in the
   *second* sentence. On mobile (~125 char fold) the pre-fold text is likely just "AI agents
   get things done. Chain a few of them together without a plan, and the system quietly gets"
   — cut mid-clause, no payoff yet. "AI agents get things done" alone is not a hook, it's a
   warm-up. Fix: compress into one sentence that front-loads the contrarian claim, e.g. "AI
   agents get things done — chain a few together without a plan and the system gets worse at
   its job, not better." (single sentence, twist inside the fold).

## Would nudge

- **Inline academic citation style** — "(Kim et al., 2026)", "(Anthropic)", "(τ-bench)" —
  three bracketed source-tags stacked across two paragraphs read like a lit-review, not
  "рассказ другу." Contrast with the plain, punchy tips section right after — this is the
  clearest register seam in the piece (stats paragraphs feel denser/more formal than the
  advice paragraphs). Sourcing is non-negotiable per ship-bar, but attribution can be
  prose-native ("Anthropic's own numbers put a multi-agent setup at ~15x") instead of a bare
  parenthetical. Not a rule violation, just not his cleanest voice.
- 🎯 for "hard stop / cost ceiling" is a semantic mismatch (🎯 reads as "goal," not
  "boundary/circuit-breaker"). 🧭 and 🔍 both land correctly. Minor swap candidate (🛑/⏱️).
- #Agents + #AIAgents in the hashtag line are near-duplicate tags — "не облако" is nominally
  respected (5 tags, in range) but two of five carry no distinct signal.
- Four separate numeric claims now live in one post (90%, 17x/4x, 4x/15x, 61%/25%) — this
  directly contradicts the brief's original "don't stack more than 2 numbers," but that
  ship-bar item is now stale: round 3 was Max's own explicit ask for "more numbers." Flagging
  only so the stale ship-bar line in brief.md gets corrected, not as a v4 defect.

## Where it nails his taste

- **Hook is the insight, not the anecdote.** Round-1 correction fully absorbed — the PocketOS
  case from the brief's narrative spine is gone entirely, no residual scene-setting language
  anywhere in the piece. This was the thing he was angriest about; it's clean now.
- **Absolutes softened correctly**: "tends to backfire," "usually cheaper," "It might" — matches
  "менее категорично" calibration (2026-06-21) exactly, no "X wins/always/never."
- **Casual-reader carve-out done right**: "If you just chat with an assistant day to day, none
  of this changes anything for you. If you're the one deciding..." — this is the expected
  structural element (Каркас поста-анонса #4), correctly placed before the closing question,
  not confused with the banned "if you've shipped..." CTA-gatekeeping pattern.
- **Closing question is bespoke, not a stock filler** — "what would make you trust a longer
  agent chain with something you can't undo?" ties directly back to the piece's own stakes
  (irreversible errors), not a generic "thoughts?"
- **Simplicity mostly holds**: "burns roughly 4x the tokens," "run away from you," "Free and
  open" — plain words over correct-sounding ones, in line with the "risks and all" precedent.
  Would still benefit from one more simplicity pass per the 2026-09-01 pattern (he simplified
  that post three times even after it already read clean) — expect him to touch wording again
  regardless of the two must-fix items above.
- **Emoji count (3 tips + 1 CTA pointer) matches published precedent** (🌐📍🧱 pattern from the
  June post) — not overuse, this is calibrated correctly, don't flag it as decorative.

## Calibration gaps (instinct vs. profile)

- brief.md's ship-bar still says "Hook is a concrete, dated case — not an abstract stat" —
  this is the OLD instruction, superseded by Max's live 2026-09-21 correction on this same
  draft (documented in blueprint/channels/linkedin.md log). v4 correctly follows the newer
  correction, not the stale brief line. The brief itself should be patched so it doesn't
  mislead the next pass — process note, not a v4 voice issue.
- No clear signal in the profile on whether academic-style inline citations "(Author, year)"
  are acceptable in his LinkedIn voice at all — I'm inferring from the general Нора Галь /
  plain-word principles that he'd want them softened, but there's no direct prior correction
  on this exact pattern. Flagging for confirmation rather than asserting it as settled taste.

## Verdict: REVISE
one-line: cut the backward-pointing "that's the 4x vs 17x above" line and rewrite the opening as one sentence so the contrarian twist sits inside the LinkedIn fold — everything else is a light pass, not a structural problem.
