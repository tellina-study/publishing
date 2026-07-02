# I Read Past the README on the Seven Biggest "Claude Skills" Repos. One Points Your Agent at npm Packages That Don't Exist.

A "skill" is a little folder you drop into a coding agent — a Markdown file plus maybe a script or
two — that quietly changes how the agent behaves on every task. An "MCP config" is the sibling of
that: a small JSON file that tells the agent which external tools to install and run, usually with a
line like `npx -y some-package`. Both install in seconds. Both run with your permissions. And both
are being collected, right now, into giant "awesome-Claude-skills" repositories that thousands of
people install on the strength of a star count and a nice README.

I wanted to know what was actually inside them. So I cloned the seven biggest, read the code and the
agent instructions, and — where there was anything runnable — tried to make each one do something it
shouldn't. Not because I assumed malice. Because "it has a lot of stars, it's probably fine" is the
exact reasoning that gets people hurt, and I'm about to build a collection like this myself.

One of the seven has a real problem. It's not the one I expected.

## The field, and where the numbers come from

Every count below is a live GitHub API call I made on July 2, 2026 — not a number copied from
anyone's README. That distinction turns out to matter more than I thought.

| Repo | Stars (live) | What it actually is |
|---|---|---|
| `obra/superpowers` | 243,958 | Skills plus an *enforced* workflow |
| `anthropics/skills` | 157,558 | Anthropic's own first-party skills |
| `ComposioHQ/awesome-claude-skills` | 66,589 | Mostly a link index + one company's own skills |
| `travisvn/awesome-claude-skills` | 13,870 | A curated list of links |
| `rohitg00/awesome-claude-code-toolkit` | 2,233 | A real toolkit stapled to an abandoned link dump |
| `jqueryscript/awesome-claude-code` | 453 | The broadest map of the ecosystem |
| `glebis/claude-skills` | 301 | A tidy personal 90-skill collection |

Yes, the top line really is a quarter of a million stars — I re-ran the call twice because I didn't
believe it either. A repo that installs itself into your agent and tells it what to do has more stars
than most programming languages. Hold that thought; it comes back.

## The headline number is almost never the real number

`ComposioHQ/awesome-claude-skills` advertises "1000+ production-ready" skills. I counted what's in
the repo: thirty, maybe forty. The other ~960 is the company's platform-integration count, a
different kind of number entirely, folded quietly into the headline.

`rohitg00/awesome-claude-code-toolkit` is the sharper example, because it disagrees with *itself*.
The README says 35 skills, 135 agents, 176+ plugins. Its own `marketplace.json` — a file the
maintainer wrote — says 120 plugins and 6 MCP configs. The filesystem says 40 skills, 136 agents, 16
MCP configs. Three sources inside one repo, none of them matching.

The git history explains why. The whole first-party toolkit was generated in two commits on day one,
back in February. `commands/` hasn't been touched since. `plugins/` got exactly one commit
afterward — a bulk fix for missing YAML frontmatter across 82 files, which tells you the first pass
wasn't reviewed closely. Almost every commit since is a merged pull request bolting *someone else's*
project onto a link table. Then, seven weeks before I looked, the maintainer stopped merging even
those. 183 open issues sit untouched.

The first-party toolkit isn't worthless — the agents and hooks that are actually there are put
together competently. It's that the number on the box was never the number in the box, and nobody
had looked in months.

## The one that made me stop: a config full of packages that don't exist

Here's the finding I'd lead with if you were about to install that toolkit.

Its `mcp-configs/` folder ships ready-made tool configurations, one per task type — security, design,
DevOps, and so on. Each one tells your agent to go fetch and run some npm packages. Three of those
packages are named under the `@anthropic/` scope: `mcp-ghidra`, `mcp-figma`, `mcp-server-figma`.

I checked all three against the npm registry. **None of them exist — 404, every one.** So do two
more the configs name: `kubectl-mcp-app` and `mcp-terraform`. That's five package references, in a
2,233-star toolkit, pointing at nothing.

The nonexistence isn't even the scary part. Look at the scope. `@anthropic/` *reads* like Anthropic's
own namespace — which is exactly why it's worth checking that it isn't. Anthropic actually publishes
under `@anthropic-ai` (`@anthropic-ai/sdk`, `@anthropic-ai/claude-code` — both live). `@anthropic`,
the one in these configs, belongs to no one I could find. And that's the whole problem: an unclaimed
scope that looks official is a slot waiting to be filled. If anyone registers `@anthropic` and
publishes something under `mcp-ghidra`, the first people to run it are the ones who copied this
config and trust the name — following the toolkit's own instructions, believing they're installing
official Anthropic tooling. (A sixth reference, `defi-mcp`, *does* exist: one version, one
maintainer, published once in January, wired into a crypto-wallet config. Not proof of anything —
just the exact shape a real supply-chain attack likes to wear.)

I don't think anyone did this on purpose. These read like names a language model invented when asked
to write a config, that nobody ran `npm info` against — not the author, not the 2,233 people who
starred it, not anyone in those 183 open issues. Which is the actual lesson, and it costs one command
to apply:

> 📌 **Before you let an agent install anything, check that every package it names is real.**
> One `npm info <package>` per line. A name that doesn't resolve is a blank the next person can fill.

None of the other six repos had anything like this. The problem isn't "this repo has a bug." It's a
check none of us were running, and now I am.

## The biggest repo was the most reassuring, not the least

Remember the quarter-million-star repo. `superpowers` installs a hook that runs before you type a
word, injecting a block marked `<EXTREMELY_IMPORTANT>` that says, verbatim, "IF A SKILL APPLIES TO
YOUR TASK, YOU DO NOT HAVE A CHOICE." On first read that's alarming — it's not language you expect
from open-source tooling, and I spent real time looking for the manipulation under it.

There isn't any. It's disclosed, versioned, MIT-licensed text the project applies to its own agent,
in the open, and you can read every line before it runs. What's underneath is a genuinely careful
workflow: a hard stop for human approval before any code is written, a fresh sub-agent per task, and
an independent reviewer whose instructions explicitly forbid trusting the first agent's self-report.
Anthropic's own `skill-creator` does a quieter version of the same thing — it runs an actual
evaluation harness and has its grader critique its own conclusions before trusting them.

That's the part worth sitting with. Two teams that have never coordinated — plus, for what it's
worth, the way I'd already been building my own setup — landed on the same rule: never trust what a
process says about itself; verify with fresh eyes. When unrelated people keep re-deriving the same
discipline, that's a stronger signal than any of them inventing it alone. Neither repo is spotless
underneath — `superpowers` runs on a single maintainer with no CI, and Anthropic's repo takes almost
no outside contributions — but the star count, for once, was pointing at something real.

## What the star count actually told me

Nothing, is the honest answer. The cleanest repo in the set had 244,000 stars; the one with the
namespace hole had 2,233; a tidy, careful personal collection had 301. Popularity tracked how far a
project had spread, not whether anyone had checked what it shipped.

So here's what I'd do before installing any of these, and it's short: read the actual files, not the
README; run `npm info` on every package a config names; and treat a big number as a reason to look
closer, not a reason to skip looking. All of that took me an afternoon. The specific commit I pulled
apart is `ebdf1d5` in `rohitg00/awesome-claude-code-toolkit`, if you want to check the five packages
yourself — they're still 404 as I write this.

The thing you starred is not the thing you read. It's worth a few minutes to find out how far apart
they are.
