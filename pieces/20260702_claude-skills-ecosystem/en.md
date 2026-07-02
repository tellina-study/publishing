# The Seven Biggest Claude Skills Collections: What's Inside, Which to Trust, and How to Use Them

> **TL;DR — if you only read this box:**
> - **Start here:** `anthropics/skills` for a small, production-grade, vetted set. Add `glebis/claude-skills`
>   (~90 tidy personal skills) if you want more, or `obra/superpowers` if you want a whole workflow, not
>   a grab-bag. Use `travisvn` / `jqueryscript` as link indexes to discover the rest.
> - **Do skills work?** Yes, with a catch: they're proven in production and show a real but *conditional*
>   lift — a few skills that reliably match your task beat a hundred installed "just in case."
> - **The one thing to avoid:** don't copy `rohitg00`'s MCP configs blind — they point your agent at npm
>   packages that don't exist, under an official-looking `@anthropic/` scope that isn't Anthropic's.
> - **The habit that saves you:** give any repo a 15-minute read before you trust it — `npm info` every
>   package it names, `grep` for what runs automatically. A big star count is not a safety check.

If you've gone looking for ready-made "skills" for your Claude agent, you've seen the pattern: a
dozen repositories called some variation of *awesome-claude-skills*, the biggest with more stars than
most programming languages, each promising hundreds of ready-to-install capabilities. Which one do
you actually pull from? And once you do, can you trust what you just dropped into a tool that runs
with your permissions?

I went through the seven biggest so you don't have to start from a star count. This is the field
guide I wish I'd had: what a skill is and whether skills even work, what's actually inside each
collection and who it's for, which ones survive a real security check, and how to use them so they
help instead of just filling up your context window.

First, one line of vocabulary, because the rest leans on it. A **skill** is a small folder — a
Markdown file, sometimes a script or two — that you drop in to change how your agent behaves on a
task ("when the user asks for a spreadsheet, do it *this* way"). An **MCP config** is its sibling: a
little JSON file that tells the agent which external tools to install and run, usually with a line
like `npx -y some-package`. Both install in seconds. That convenience is the whole reason to be a
little careful, and we'll get to it.

## Do skills actually work?

Short answer: yes, with a catch worth understanding before you install twenty of them.

The strongest evidence isn't a benchmark — it's production. Anthropic's own document skills (the ones
that build xlsx, docx, pptx, and pdf files) are, by their own README, the skills that power Claude's
document-creation feature in the actual product. That's not a lab result; it's a capability millions
of people already use, implemented as exactly the kind of skill file you can install yourself.

For an independent number, one study put the format to the test — [*How Well Do Agentic Skills Work
in the Wild*](https://arxiv.org/abs/2604.04323) — and found a genuine lift: on the Terminal-Bench 2.0
benchmark, adding skill retrieval moved pass rate from 57.7% to 65.5%. But the same paper is honest
about the ceiling: as the test conditions got more realistic, the gains shrank back toward the
no-skill baseline. Skills help most when the *right* skill reliably fires for the task in front of
the agent.

> 💡 **The catch is triggering, not capability.** A skill only helps if the agent actually loads it
> at the right moment — and "skills that won't trigger" is Anthropic's own top troubleshooting note.
> Each skill also costs context to keep around. So a curated handful you know will fire beats a
> hundred you installed "just in case."

That single idea — *targeted beats maximal* — is the lens for reading the rest of this guide. The
question isn't "which repo has the most skills." It's "which few match what I actually do."

## The map: seven collections, and who each one is for

Every star count below is a live GitHub reading from July 2, 2026, not a number from a README — a
distinction that turns out to matter, as the next section shows.

| Collection | Stars | What it really is | Reach for it if… |
|---|---|---|---|
| `anthropics/skills` | 157,558 | Anthropic's own first-party skills, auto-synced from internal | You want a small, production-grade, vetted set |
| `obra/superpowers` | 243,958 | Skills *plus* an enforced end-to-end workflow | You want a whole disciplined process, not a grab-bag |
| `glebis/claude-skills` | 301 | A tidy personal collection of ~90 skills | You want a curated, human-sized set to browse |
| `ComposioHQ/awesome-claude-skills` | 66,589 | Mostly a link index + one company's platform skills | You're surveying what's out there |
| `travisvn/awesome-claude-skills` | 13,870 | A clean, maintained list of links | Same — a discovery hub |
| `jqueryscript/awesome-claude-code` | 453 | The broadest map of the whole ecosystem | You want the widest census, not just skills |
| `rohitg00/awesome-claude-code-toolkit` | 2,233 | A real toolkit bolted to an abandoned link dump | With care — see the caution below |

A few of these deserve more than a table row.

**`anthropics/skills` — the vetted starting point.** Seventeen skills, all first-party, and the best
place to begin if you want things that are known to work. Beyond the document skills, it ships
`skill-creator` (a skill for *building* skills, with its own testing harness), `mcp-builder`,
`frontend-design`, `webapp-testing`, `canvas-design`. Small on purpose. If you install nothing else,
install from here.

**`obra/superpowers` — a process, not a pantry.** This is the quarter-million-star one, and it's a
different kind of thing: less a bag of skills, more an opinionated workflow that sequences them —
brainstorm, write a plan, get human sign-off, build test-first, review with a fresh agent, finish
the branch. Reach for it if you want to adopt a whole way of working. Just know going in that it's
assertive about it (more on that in a second).

**`glebis/claude-skills` — the human-sized set.** Only 301 stars, but a tidy, well-built personal
collection of about 90 skills spanning test-driven development, release automation, and a small
LLM-command-line tool. If the big two feel like too much, this is the browsable middle.

**The link indexes — `ComposioHQ`, `travisvn`, `jqueryscript`.** These aren't collections you install
so much as maps you read. `jqueryscript` is the broadest census of the whole ecosystem; `travisvn` is
a clean, actively maintained list; `ComposioHQ` mixes a link index with its own platform's skills.
Useful for *finding* things — just don't mistake a link table for a vetted recommendation.

One caution about headline numbers before you trust any of them: `ComposioHQ` advertises "1000+
production-ready" skills, but the repo itself holds thirty to forty — the rest is a platform
integration count folded into the headline. `rohitg00`'s README claims 35 skills, 135 agents, 176+
plugins; its own `marketplace.json` says 120 plugins; the actual files say 40 skills and 16 MCP
configs. Three numbers for one repo, none matching. Count the folder, not the banner.

## Which ones to trust: what a real check turns up

Stars measure how far a project spread, not whether anyone vetted what it ships. So for the three
collections that contain runnable code — `anthropics/skills`, `superpowers`, and the `rohitg00`
toolkit — I ran an actual security pass, not a glance. (The rest are link lists; nothing to run,
nothing to check.) The good news first: two of the three came back clean, and even the alarming-
looking one is mostly a false alarm.

Take `superpowers`, the assertive one. It installs a hook that fires before you type anything,
injecting a block marked `<EXTREMELY_IMPORTANT>` that reads, verbatim, *"IF A SKILL APPLIES TO YOUR
TASK, YOU DO NOT HAVE A CHOICE."* That looks like a red flag. It isn't: it's disclosed, versioned,
MIT-licensed text the project applies to its own agent in the open, and you can read every line
before it runs. Underneath is a genuinely careful design — human approval before code gets written, a
fresh sub-agent per task, an independent reviewer told not to trust the first agent's word.
`anthropics/skills` was clean too, down to its one `shell=True` call sitting in a browser-testing
script the agent already had the keys to run.

The one caution in the whole set is worth stating plainly, because it's the kind of thing a star
count will never warn you about.

> 📌 **Don't copy `rohitg00`'s MCP configs blind.** They tell your agent to install npm packages
> under the `@anthropic/` scope — `mcp-ghidra`, `mcp-figma`, `mcp-server-figma` — that **do not
> exist** (all 404), along with `kubectl-mcp-app` and `mcp-terraform`. Anthropic's real scope is
> `@anthropic-ai`, not `@anthropic`. An official-looking, *unclaimed* namespace pointing at missing
> packages is a slot waiting to be filled: if someone registers it and publishes malware, the people
> who run it first are the ones who copied this config trusting the name.

Nobody there did this on purpose — these read like package names a model invented and no one ran
`npm info` against. Which is exactly the habit worth borrowing, and it costs one command.

## How to actually use skills well

Two halves: check what you install, then use less of it than you think.

**Before you install anything — a fifteen-minute vet.** None of this is hard, and it's the same list
regardless of the repo:

- **Read the actual files, not the README.** The gap between the two is the whole point of this piece.
- **`npm info` every package a config names.** A name that doesn't resolve is a blank someone else can fill.
- **`grep` for ungated `eval`, `exec`, `child_process`, `subprocess`, `shell=True`.** A hit isn't automatically bad — it's a thing to understand before you run it.
- **`grep` for `curl … | bash` and `wget … | sh`.** Piping the internet straight into a shell is the classic install-script trap; it usually shows up for *linked third-party* projects, not the repo's own code.
- **`grep` the hooks for network calls.** Hooks run automatically every session — that's where a phone-home would hide.
- **Skim the git log.** Two commits on day one and nothing since (the `rohitg00` story) tells you no one's minding it.

**Then use fewer skills than you want to.** Because triggering is the bottleneck, not capability, the
winning move is a small set matched to your real work:

- **The description is the skill's on-switch.** Skills undertrigger; a vague description means it never
  loads and never helps. Prefer skills whose descriptions clearly name when they apply — and sharpen
  your own.
- **Keep each skill small.** The best ones use "progressive disclosure" — a one-line summary always
  loaded, the full instructions pulled in only when triggered, heavy references fetched on demand.
  Bloated skills cost context for nothing.
- **Don't install everything.** A hundred dormant skills is a hundred descriptions competing for the
  agent's attention and your token budget. Curate to the handful you'll actually hit.
- **Prefer disclosed and maintained.** `superpowers` is loud but transparent; a silent, unmaintained
  repo with a big number is the worse bet.

## The one-line takeaway

The star count told me almost nothing. The cleanest collection in the set had 244,000 stars; the one
with the namespace hole had 2,233; the tidy, careful personal set had 301. Popularity tracked reach,
not whether anyone had looked inside.

So if you're shopping for skills: start with `anthropics/skills` for things known to work, add
`glebis` or `superpowers` if you want more or want a whole workflow, use the link indexes to discover
the rest — and give anything a fifteen-minute read before you trust it. That's less time than you'll
spend picking which skills to install, and it's the difference between a tool you understand and a
number you hoped was fine.
