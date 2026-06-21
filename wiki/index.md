# Publishing Wiki — Master Index

> **Navigation-only index.** Pointers, not metric tables — tables here rot within a week.
> Currency is maintained by the `librarian` under the Close-the-Loop Protocol (`CLAUDE.md`).

## Catalogs
- [Shipped pieces](pieces/INDEX.md) — every published/in-flight piece, by status.

## Topics
Evergreen takes, one page per subject. Create a page when a topic recurs across pieces.

| Topic | Currency | Updated when |
|-------|----------|--------------|
| [Anti-patterns / debunked claims](topics/anti-patterns.md) | ✅ current | Close-the-Loop (a claim is debunked / a cliché named) |
| [Publishing to tellian.io](topics/publishing-to-tellian.md) | ✅ current | The publish pipeline / site setup changes |
| [Prompt packaging: language, format, placement](topics/prompt-packaging.md) | ✅ current | A new piece touches prompt language / format / placement |
| _(add topic pages here as they emerge)_ | | |

## How to query the knowledge base

| Query shape | Tool |
|-------------|------|
| "What do we know / have we written about X?" | `python3 scripts/rag_search.py "X"` |
| "Which pieces cover topic Y?" | [pieces/INDEX.md](pieces/INDEX.md) or `ontology/store.md` |
| "What's our take / have we debunked Z?" | [topics/](topics/) + [anti-patterns](topics/anti-patterns.md) |
| Read a file at a known path | Read tool |
| Find an exact string / filename | Grep / Glob |

## Related
- Curated sources: [`sources/INDEX.md`](../sources/INDEX.md)
- How we work: [`blueprint/conventions.md`](../blueprint/conventions.md), [`lessons-learned.md`](../blueprint/lessons-learned.md)
- Decisions & reflections: [`notes/decisions.md`](../notes/decisions.md), [`notes/reflections/`](../notes/reflections/)
