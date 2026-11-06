# Mirror review: harness-agents-pt1

> Supersedes the prior pass (verdict REVISE, 3 must-fix items). All three are confirmed
> resolved in this draft — see "Where it nails his taste" below for what to check if you
> want to verify rather than trust my read. This pass covers only what changed or could have
> drifted during the ~1.9x expansion (4809 words now vs. the earlier draft), not a re-litigation
> of ground already cleared.

## Where this misses Max's bar (must fix)

None found. The expansion did not reintroduce any banned tic, and the three must-fix items
from the prior mirror pass are gone from the text (verified by direct grep, not just re-reading):
the quality/price causal merge ("одной природы") is gone, "не приговор продукту" is gone, and
the agent-pillar now has its summary table (lines 123–127: Агент × разброс повтора × цена на
дешёвой модели × балл).

## Would nudge

- **"честно" recidivism watch** — two instances survived the expansion: "Это честно помечено
  как «не измерено»" (строка про оставшиеся шесть задач) and "Мерить всё это честно трудоёмко"
  (ловушки). Neither is the banned `(честно)`/`честный итог` parenthetical-apology pattern he
  blew up at before — both are adverbs modifying a verb/adjective, not a standalone label — but
  given the explicit recidivism history ("ты откуда такой стиль взял?!"), I'd rather flag both
  for a second look than let the word quietly creep back in under a technically-different
  grammatical disguise. Cheap fix: "честно помечено" → "прямо помечено"; "честно трудоёмко" →
  cut "честно" entirely, "трудоёмко" carries it alone.
- **"придумано постфактум задним числом"** — doubles two near-synonyms for the same idea
  (постфактум = after the fact, задним числом = after the fact). Minor Nora Gal prополка item,
  pick one.
- **The 874s/1124s aside in the infra-noise paragraph** doesn't clearly pay for itself — fact-check
  already flagged this as "mentioned but not clearly load-bearing," and on a craft read I agree:
  the comparison to "a pricier model in another round" doesn't prove the 874s run was clean (the
  free-resource re-run already established that), so it reads as an extra number for its own sake
  in a piece that otherwise never puts a number in without a job for it to do. Cut it or give it
  an explicit point.
- **Line ~200 (infra-noise paragraph) is the single longest paragraph in the piece** (~1100
  characters) and bundles two separate ideas — the throttling anecdote and the "why we don't use
  the stopwatch as primary evidence" methodological principle. Both are good; a paragraph break
  between them would give the second idea (which is actually a standalone, quotable methods
  point) room to land instead of riding in on the anecdote's momentum.
- **"звучит почти как шутка над самим собой"** (измеримость-задача) — a self-aware aside about
  the test design itself, not about the writing process, so it's a different animal from the
  DeepSeek Harness joke he had cut. I read it as fine — it's commentary on what the data is, not
  a wink about how the piece was made — but flagging it explicitly since it's the one place in
  4800 words that risks reading as "coy" if he's still calibrated tight on that after the last cut.

## Where it nails his taste

- **All three prior must-fix items are resolved, confirmed by direct text check, not just
  re-read**: no sentence anywhere ties Hermes's price win to its quality loss as "one nature"
  (grep clean); "не приговор продукту" is gone entirely (grep clean); the agent-pillar now carries
  its own summary table.
- **The genre directive ("упрощённая, но научная статья") is the headline win of this pass.**
  Methodology + limits now run ~1750 words — the single biggest block in the piece — and almost
  none of it is procedural recitation. The model-pinning war (a CLI flag silently defaulting to
  the expensive model; a shared config file fixed with a pre/post checksum check), the proxy that
  records real provider responses independently of agent self-report, the recalibration against
  fifty known-price cases, the three traps (price confound, 50x self-report error, 10x cache-token
  conflation), and the independent-recheck-of-every-claim paragraph (with a named retracted claim —
  "самом стабильном" didn't survive re-derivation) — every one of these is a concrete war story
  with stakes, not a dry "here is our method." This is exactly "просто в языке, сложнее в смыслах"
  applied to methodology, not just to findings.
- **The agent-comparison pillar is now genuinely co-equal, by the numbers, not just by claim.**
  Pure agent-pillar content (~765 words) plus the two agent-dependent synthesis sections (~774
  words) together outweigh the pure harness-only content (~701 words). This is the explicit
  2026-11-06 correction landing for real, not just in the brief's intent.
- **Two separate, concrete practical blocks** ("Про харнес" / "Про выбор агента"), and every
  bullet in both ties back to a specific number established earlier in the piece — no abstract
  "проверяйте на своём агенте" floating free of the data that earned it.
- **Zero decorative emoji, bold used only as functional list-item lead-ins** (agent names, task
  categories, trap names) — never as mid-sentence emphasis-tic. The one callout he gets is a plain
  blockquote, no 💡/📌 — the deliberate "this genre doesn't need the scanability cards" call from
  the last pass holds up under the longer draft too.
- **No mentor tone, no process leakage, no hype language** — grepped for "разберёмся/рассмотрим/
  давайте", "(ROAST)/alm#/agent-lab-manager", "game changer/меняет всё" — all clean, despite
  nearly doubling the word count. Expansion didn't dilute the voice discipline.
- **The DeepSeek Harness fix holds**: the three-agent list is now plain, with one functional
  clarifying line ("несмотря на название — это имя продукта, не наш термин «харнес»") instead of
  a joke. Exactly the requested swap.
- **Headers are concrete findings, not category labels** — "Один рычаг, а знак разный", "Тот же
  тумблер, но в руках разных агентов", "Когда харнес просто дороже" all read as sentences with a
  claim in them, not filing labels. None of the mutable-pathos-section-name problem from the
  transformers piece recurred here.
- **The thesis sits in paragraph 1's last clause** ("быстрой, однозначной победы харнеса не
  нашёл") — the earlier would-nudge about the two-answer framing arriving late in the intro is
  moot now: the single-sentence verdict is already there before the two-pillar roadmap even
  starts.

## Calibration gaps (instinct vs. profile)

- I'm reading the "измеримость" self-irony aside as acceptable because it comments on the
  experiment's content, not on the act of writing the piece — different in kind from the banned
  DeepSeek Harness wink. That's my read of *why* the ban applied, not something the profile states
  explicitly as a rule with that exact boundary. Worth a one-line confirmation if he's still
  sensitive about this after the last cut.
- The two "честно" instances read to me as grammatically distinct from the banned pattern (adverb
  modifying a verb, not a standalone apologetic label). Given the recidivism history on this exact
  word, I'd rather he make the call than have me silently decide it's fine.

## Verdict: SHIP

Satisfies: genre directive (methodology/tables/honest-limits as the biggest single block, not a
garnish on top of findings-prose); agent-pillar now equal or slightly ahead of the harness-pillar
by word count, not just by claim; DO-NOT list clean (no quality/price conflation, no Hermes/dsh
evaluative language, no private-repo leakage, no hype); voice discipline (no mentor tone, no
emoji/bold tics, no process leakage) held through a near-doubling of length; all three prior
must-fix items confirmed resolved in the text itself, not just claimed resolved.

one-line: ship as-is, but run the two "честно" instances and the postfactum/задним-числом
redundancy past him explicitly given the recidivism history on that exact word — everything else
is a stylist-ru-level nudge, not a reason to hold.
