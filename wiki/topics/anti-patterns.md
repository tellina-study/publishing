# Anti-patterns & debunked claims

Things **not to write**: clichés, framings that mislead, and claims we've checked and found
false or unsupported. Check this before drafting — don't resurface a settled point as new.

Add a row whenever a piece debunks a claim or we identify a cliché to avoid (Close-the-Loop trigger).

## Debunked / unsupported claims
| Claim | Why it's wrong / unsupported | Settled by (piece / source) | Date |
|-------|------------------------------|-----------------------------|------|
| "Write prompts in Chinese, you'll save tokens" | The ideograph is dense but the tokenizer fragments it; saving unconfirmed, model-dependent, and quality is on average lower. On popular models Chinese is *not* cheaper. | [language-format-placement](../pieces/INDEX.md) (Mythbuster 2026, arXiv:2604.14210) | 2026-06-21 |
| "Russian is more compact than English for prompts" | Opposite — Russian runs ~×2 the tokens of the same English meaning; Slavic languages sit at the expensive end. | [language-format-placement](../pieces/INDEX.md) (Tokenizer Tax 2026, arXiv:2605.24718) | 2026-06-21 |
| "Emoji / box-drawing glyphs save space" | They cost *more* tokens, not fewer — decorative glyphs fragment badly. | [language-format-placement](../pieces/INDEX.md) | 2026-06-21 |
| "Caveman / brevity prompting cuts ~75% of tokens" | Real savings are modest (~15–20%), sometimes eaten by caching/quality losses — not −75%. | [language-format-placement](../pieces/INDEX.md) (Hakim 2026, arXiv:2604.00025) | 2026-06-21 |
| "A trendy token format (e.g. TOON) is always better than JSON" | It's a data-shape / baseline tradeoff — helps for some shapes, hurts for others; not a universal win. | [language-format-placement](../pieces/INDEX.md) (Matveev 2026, arXiv:2603.03306) | 2026-06-21 |

## Clichés & weak framings to avoid
| Framing | Why it's weak | Use instead |
|---------|---------------|-------------|
| "X is dead / X changes everything" | Over-claim; ages badly; rarely true | State the specific, bounded change |
| Stat with no denominator ("5M users") | Meaningless without the base | Always give the baseline |
| "Now AI can do X" with no date | Freshness-dependent; ages fast, may already be stale | Date the claim; verify, don't recall |

## Process anti-patterns (how we work)
| Don't | Do |
|-------|-----|
| Start a task while it's still fuzzy | Clarity-first: study the KB, then ask sequential questions |
| Dump a big parallel list of questions | Sequential questions, each building on the previous answer |
| Begin work without a task-specific plan | ШАГ 0: write `plan.md` under the task, then work by it |
| Skip recording the owner's reaction | Mirror loop: record every reaction the same turn → `owner-taste.md` |
| Defer with no view of your own | You're a co-author: propose, argue, defend on the merits |
