# Mirror review: claude-skills-ecosystem (en-draft)

Judging as Max would, against `notes/owner-taste.md`. Factual spine verified against
`materials/` — star counts are live `gh api` captures, the npm-404 finding, the
marketplace.json↔filesystem discrepancies, and `defi-mcp` all match the review notes.
This is a *taste* verdict, not a fact-check.

## Where this misses Max's bar (must fix)

1. **Понты — repeated lab-credential flexing.** The persona doesn't stop at one aside; it
   recurs: "I run a lab that's about to build its own version of this exact thing" (¶4),
   "I run a version of that same loop… as a hard rule for how I manage my own lab" (P3),
   "how I manage my own lab," "one of my own team's reports," "the bar I held everyone else
   to." Max's rule is explicit: никаких понтов и саморекламы; **максимум одна фраза вскользь,
   не хвастливый абзац** — and repeated "я крутой, я уже так делаю" is a named AI-generation
   tell. → Keep the origin frame once (I reviewed one repo, that felt like a shortcut, so I
   looked at the rest). Cut the rest of the lab-cred to a single glancing mention.

2. **Pattern 3 is a victory lap, not a finding.** "The biggest repo didn't teach me anything
   new. It confirmed something I'd already built." → "wasn't a 'great minds think alike'
   moment. It was a sanity check that the shape isn't a personal preference." This is the
   smuggest passage in the piece and it's about *the author*, not the reader. It also braids
   a second thesis (review-loop convergence) onto what should be one spine (verify your
   numbers and your packages). → Deflate hard or cut. If kept, reframe from "confirmed what I
   built" to "three unrelated teams landed on the same discipline" — reader-facing, not
   self-facing.

3. **Tell-don't-show / reader-scolding register.** "Here's a number that should bother you
   more than it probably does." "Read that again slowly, because the mechanism matters more…"
   "What would you find if you actually read the thing you starred?" This is the ментор/
   gotcha register Max bans — telling the reader how to feel and implying they're lazy. His
   register is warm, on равных, "нашёл интересное, делюсь, смотрите как это работает" — not
   "I did the work you were too lazy to do." → Re-register: let the 404s land on their own;
   drop the "should bother you," "read that again slowly," and the scolding kicker.

4. **Meta-проговор — leaking the kitchen into the text.** "Here's the finding I'd lead with
   if I were writing this for someone about to install that toolkit." Announces the writing
   move instead of just making it — exactly the анти-проговор рецидив flagged repeatedly in
   the taste file. → Just lead with the finding.

5. **A number without its base, in a piece about numbers without their base.** "Most of them
   never read past the README" (¶2) has no denominator — the precise sin the whole article
   prosecutes. Self-refuting if a sharp reader catches it. → Cut or downgrade to an honest
   "few of us read past the README" claim you can carry.

## Would nudge

- **Title oversells the verb.** "Tried to Break Them" promises a red-team break attempt; the
  actual work was reading code, grepping for eval/exec, and `npm info` checks. The
  supply-chain hole is real, so the second half of the title is earned — but "tried to break
  them" dramatizes. Max hates a title that oversells the body.
- **Two theses.** The load-bearing, genuinely novel spine is the `@anthropic/`-scoped
  namespace-squatting hole + the base-checking discipline (Patterns 1–2). Pattern 3 is a
  different essay. One thesis, shown — consider making the supply-chain finding the whole
  spine and letting P3 be a short coda at most.
- **"tried to make each one do something it shouldn't"** — slightly inflates a grep pass.
  Fine if the title stops promising a break.

## Where it nails his taste

- **Numbers carry their base — the piece *is* this rule.** Corrects "1000+ production ready"
  to 30–40; sets README vs. marketplace.json vs. filesystem against each other; every count
  is filesystem- or API-derived, not README-quoted. This is Max's rule #2 made flesh. Keep.
- **Usefulness over hype.** The reader leaves able to *do* one concrete thing: `npm info`
  every package before an agent runs an MCP config. Named, cheap, reusable. Exactly "reader
  leaves able to do something differently."
- **Calibration honesty in the right spots.** "self-reported 94% rejection rate,"
  "That's not proof of malice either," "as far as I can tell" — earned hedges, not blanket
  certainty. Good.
- **Concrete detail over category.** The 82-file YAML-frontmatter bugfix as a tell that bulk
  generation wasn't reviewed; 183 open PRs; two day-one commits — божественная деталь, not
  родовая категория. This is the good stuff.

## Calibration gaps (instinct vs. profile)

- **First-person is fine; the *flex* is not.** The taste profile welcomes warm first-person
  "рассказ другу," so the "I" itself passes — my objection is strictly the понты/gotcha
  register, not the person. Flag only if Max reads the persona as more of a problem than I do.
- **Big star counts (244k / 158k) are sourced but eyebrow-raising.** They come from a dated
  `gh api` capture, so within this piece they're honestly sourced — not a taste violation.
  But a piece whose thesis is "don't repeat a headline number unchecked" dies if a reader
  finds those counts implausible. This is a fact-check flag to confirm before ship, parked
  here because it directly threatens the article's own credibility.
- **The scolding kicker as a question.** Max's LinkedIn taste likes closing on a question —
  so the *form* of the closer is on-brand, but its *tone* ("if you actually read") is the
  accusatory version. I read it as off; confirm whether he wants the question kept but warmed.

## Verdict: REVISE

The substance clears the bar — a real, reproducible supply-chain finding wrapped in exactly
the base-checking discipline Max preaches. What fails is voice: it wears a smug, gotcha,
"look how my lab already does it right" register that trips his понты and анти-проговор rules
in the way he's flagged over and over. Fixable without touching the facts.

**One-line:** Strip the self-congratulation and the reader-scolding — re-register from
"I did the work you were too lazy to do" to "found something worth sharing," and let the
`@anthropic/`-scope hole be the single spine.
