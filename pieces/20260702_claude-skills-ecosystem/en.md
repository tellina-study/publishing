---
title: 'The Seven Biggest Claude Skills Collections: What''s Inside, Which to Trust,
  and How to Use Them'
slug: claude-skills-collections
status: draft
categories:
- AI Agents
tags:
- claude-code
- skills
- MCP
- security
- llm
wp_post_id: 271
---

> **TL;DR — if you only read this box:**
> - **Start here:** [anthropics/skills](https://github.com/anthropics/skills) for a small, production-grade, vetted set. Add [glebis/claude-skills](https://github.com/glebis/claude-skills)
>   (~90 tidy personal skills) if you want more, or [obra/superpowers](https://github.com/obra/superpowers) if you want a whole workflow, not
>   a grab-bag. Use [travisvn](https://github.com/travisvn/awesome-claude-skills) / [jqueryscript](https://github.com/jqueryscript/awesome-claude-code) as link indexes to discover the rest.
> - **Do skills work?** Yes, with a catch: they're proven in production and show a real but *conditional*
>   lift — a few skills that reliably match your task beat a hundred installed "just in case."
> - **The one thing to avoid:** don't copy [rohitg00](https://github.com/rohitg00/awesome-claude-code-toolkit)'s MCP configs blind — they point your agent at npm
>   packages that don't exist, under an official-looking `@anthropic/` scope that isn't Anthropic's.
> - **The habit that saves you:** give any repo a 15-minute read before you trust it — `npm info` every
>   package it names, `grep` for what runs automatically. A big star count is not a safety check.

If you've gone looking for ready-made "skills" for your Claude agent, you've seen the pattern: a
dozen repositories called some variation of *awesome-claude-skills*, the biggest with more stars than
most programming languages, each promising hundreds of drop-in capabilities. Which one do
you pull from? And once you do, can you trust what you just dropped into a tool that runs
with your permissions?

I went through the seven biggest so you don't have to start from a star count. This is the field
guide I wish I'd had: what a skill is and whether skills even work, what's inside each
collection and who it's for, which ones survive a real security check, and how to use them so they
help instead of just filling up your context window. Every repo name below links straight to its
GitHub page, so any number I quote — starting with those eye-widening star counts — is one click to
check.

First, one line of vocabulary, because the rest leans on it. A **skill** is a small folder — a
Markdown file, sometimes a script or two — that you drop in to change how your agent behaves on a
task ("when the user asks for a spreadsheet, do it *this* way"). An **MCP config** is its sibling: a
little JSON file that tells the agent which external tools to install and run, usually with a line
like `npx -y some-package`. Both install in seconds. That convenience is the whole reason to be a
little careful.

## Do skills actually work?

Yes — with a catch worth understanding before you install twenty of them.

The strongest evidence isn't a benchmark — it's production. Anthropic's own document skills (the ones
that build xlsx, docx, pptx, and pdf files) are, by their own README, the skills that power Claude's
document-creation feature in the actual product. That's not a lab result; it's a capability millions
of people already use, implemented as exactly the kind of skill file you can install yourself.

For an independent number, one study put the format to the test — [*How Well Do Agentic Skills Work
in the Wild*](https://arxiv.org/abs/2604.04323) — and found a genuine lift: on the Terminal-Bench 2.0
benchmark, adding skill retrieval moved pass rate from 57.7% to 65.5%. But the same paper is just as
clear about the ceiling: as the test conditions got more realistic, the gains shrank back toward the
no-skill baseline. Skills help most when the *right* skill reliably fires for the task in front of
the agent.

> 💡 **The catch is triggering, not capability.** A skill only helps if the agent actually loads it
> at the right moment — and "skills that won't trigger" is Anthropic's own top troubleshooting note.
> Each skill also costs context to keep around. So a curated handful you know will fire beats a
> hundred you installed "just in case."

That single idea — *targeted beats maximal* — is the lens for reading the rest of this guide. The
question isn't "which repo has the most skills." It's "which few match what I actually do."

## The map: seven collections, and who each one is for

The star counts *and* the last-updated dates below are live GitHub readings from July 2, 2026, not
numbers from a README. Both matter — a collection is only as good as the last time someone tended it,
and here the freshness split is sharp: three are updated almost daily, one hasn't been meaningfully
touched in months.

| Collection | Stars | Last update | What it really is |
|---|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | 243,958 | Jul 1 · very active | Skills *plus* an enforced end-to-end workflow |
| [anthropics/skills](https://github.com/anthropics/skills) | 157,558 | Jul 1 · near-daily | Anthropic's own first-party skills, auto-synced from internal |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 66,589 | May 22 · stale | Mostly a link index + one company's platform skills |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | 13,870 | Apr 28 · slowing | A clean list of links |
| [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | 2,233 | May 12 · abandoned* | A real toolkit bolted to a dead link dump |
| [jqueryscript/awesome-claude-code](https://github.com/jqueryscript/awesome-claude-code) | 453 | Jun 29 · active | The broadest map of the whole ecosystem |
| [glebis/claude-skills](https://github.com/glebis/claude-skills) | 301 | Jul 2 · active | A tidy personal collection of ~90 skills |

<small>*last commit May 12, but 183 issues sit open and nothing's been merged in ~7 weeks — the pushes stopped, the queue didn't.</small>

Here's the one reason to reach for each — and the maintenance reality that should temper it:

- **[anthropics/skills](https://github.com/anthropics/skills) — pick it for trust.** Anthropic's own skills, mirrored from an internal
  source almost daily. The vetted place to start: the document skills that run in production, plus
  `skill-creator` (a skill that builds and tests skills), `mcp-builder`, `webapp-testing`,
  `frontend-design`. Small on purpose. If you install from nowhere else, install from here.
- **[obra/superpowers](https://github.com/obra/superpowers) — pick it for a whole workflow, not a pantry.** The quarter-million-star one,
  and a different animal: an opinionated process that sequences skills — brainstorm, plan, human
  sign-off, build test-first, review with a fresh agent, finish the branch. Very actively developed,
  though by essentially one maintainer with no CI, so the quality gate is a single person.
- **[glebis/claude-skills](https://github.com/glebis/claude-skills) — pick it for a curated, human-sized set.** Pushed the very day I looked.
  About 90 tidy personal skills — test-driven development, release automation, a small LLM
  command-line tool. If the big two feel like too much, this is the browsable middle.
- **[jqueryscript/awesome-claude-code](https://github.com/jqueryscript/awesome-claude-code) — pick it to see the whole territory.** Recently updated, and
  the broadest census of the ecosystem — apps, tools, and skills, not just a skill list. A map, not a
  toolbox.
- **[travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) — pick it as a clean discovery list.** A well-kept index of
  links, though the updates have slowed since late April. Good for *finding*, not a vetted install.
- **[ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) — pick it only to browse.** A link index padded with one
  company's own platform skills, last touched in May. Its "1000+ production-ready" headline is really
  thirty to forty real skills; the rest is a platform integration count folded in.
- **[rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) — mostly skip, mine for parts.** The competent first-party
  bits are worth a look, but the repo is effectively abandoned (183 open issues, no merges in weeks)
  and its MCP configs are broken in a way that matters — see the caution below. Don't install it
  wholesale.

One habit these last two teach: count the folder, not the banner. [rohitg00](https://github.com/rohitg00/awesome-claude-code-toolkit)'s README claims 35
skills, 135 agents, 176+ plugins; its own `marketplace.json` says 120 plugins; the actual files say
40 skills and 16 MCP configs — three numbers for one repo, none matching.

## How to install one

There are two paths, and neither takes more than a minute — which is why the vetting below matters.

**A single skill, by hand.** A skill is just a folder with a `SKILL.md` inside. Drop it in
`~/.claude/skills/<name>/` and it's available in every project; drop it in `.claude/skills/<name>/`
inside a repo and it ships with that project (and to your teammates via git). Claude Code picks it up
live — no restart. So to grab one skill from any of these collections, you can literally clone the
repo and copy the folder you want:

```bash
git clone https://github.com/glebis/claude-skills
cp -r claude-skills/skills/tdd ~/.claude/skills/tdd    # now available as a skill
```

**A whole collection, via the plugin marketplace.** The bigger repos ship as installable plugins.
Add the repo as a marketplace, then install what you want from it — all inside Claude Code:

```
/plugin marketplace add anthropics/skills   # register the collection
/plugin                                      # browse and install from it
```

[obra/superpowers](https://github.com/obra/superpowers) is on Anthropic's own official marketplace, so it installs the same way — open
`/plugin`, find it, install. Use `/plugin` any time to see what's installed or turn things off.

**An MCP config** (the tool bundles) is separate: you either run `claude mcp add --transport http
<name> <url>` or drop a `.mcp.json` at your project root. This is the one to slow down on — it's the
[rohitg00](https://github.com/rohitg00/awesome-claude-code-toolkit) case from earlier, where the config named packages that don't exist. Run `npm info` on
every package a config lists *before* you let it install anything.

## Which ones to trust: what a real check turns up

Stars measure how far a project spread, not whether anyone vetted what it ships. So for the three
collections that contain runnable code — [anthropics/skills](https://github.com/anthropics/skills), [superpowers](https://github.com/obra/superpowers), and the [rohitg00](https://github.com/rohitg00/awesome-claude-code-toolkit)
toolkit — I ran an actual security pass, not a glance. (The rest are link lists; nothing to run,
nothing to check.) Two of the three came back clean, and even the alarming-looking one is mostly a
false alarm.

Take [superpowers](https://github.com/obra/superpowers), the assertive one. It installs a hook that fires before you type anything,
injecting a block marked `<EXTREMELY_IMPORTANT>` that reads, verbatim, *"IF A SKILL APPLIES TO YOUR
TASK, YOU DO NOT HAVE A CHOICE."* That looks like a red flag. It isn't: it's disclosed, versioned,
MIT-licensed text the project applies to its own agent in the open, and you can read every line
before it runs. Underneath is a genuinely careful design — human approval before code gets written, a
fresh sub-agent per task, an independent reviewer told not to trust the first agent's word.
[anthropics/skills](https://github.com/anthropics/skills) was clean too, down to its one `shell=True` call sitting in a browser-testing
script the agent already had the keys to run.

The one caution in the whole set is worth stating plainly, because it's the kind of thing a star
count will never warn you about.

> 📌 **Don't copy [rohitg00](https://github.com/rohitg00/awesome-claude-code-toolkit)'s MCP configs blind.** They tell your agent to install npm packages
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
- **Skim the git log.** Two commits on day one and nothing since (the [rohitg00](https://github.com/rohitg00/awesome-claude-code-toolkit) story) tells you no one's minding it.

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
- **Prefer disclosed and maintained.** [superpowers](https://github.com/obra/superpowers) is loud but transparent; a silent, unmaintained
  repo with a big number is the worse bet.

## The one-line takeaway

The star count told me almost nothing. The cleanest collection in the set had 244,000 stars; the one
with the namespace hole had 2,233; the tidy, careful personal set had 301. Popularity tracked reach,
not whether anyone had looked inside.

So if you're shopping for skills: start with [anthropics/skills](https://github.com/anthropics/skills) for things known to work, add
[glebis](https://github.com/glebis/claude-skills) or [superpowers](https://github.com/obra/superpowers) if you want more or want a whole workflow, use the link indexes to discover
the rest — and give anything a fifteen-minute read before you trust it. That's less time than you'll
spend picking which skills to install, and it's the difference between a tool you understand and a
number you hoped was fine.
