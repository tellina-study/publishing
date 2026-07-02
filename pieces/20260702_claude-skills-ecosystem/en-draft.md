# I Cloned the Seven Biggest "Claude Skills" Repos and Tried to Break Them. One Has a Live Supply-Chain Hole.

*Draft for tellian.io — category: AI Agents. Not yet published; see result.md.*

Here's a number that should bother you more than it probably does: **243,958**. That's the star
count on a GitHub repo called `superpowers` that installs itself into your coding agent and tells it
what to do on every single session. Not "here's a helpful tool you might use" — a mandatory hook
that runs before you type a word, injecting a block of text marked `<EXTREMELY_IMPORTANT>` that
says, verbatim, "IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE."

A quarter of a million people starred that. Most of them never read past the README.

I did read past the README — for that one and six others. I cloned each repo, read the actual code
and the actual agent instructions, and spent real effort trying to make each one do something it
shouldn't. Not because I assumed malice. Because "I trust it, it has a lot of stars" is exactly the
kind of reasoning that gets people hurt, and I run a lab that's about to build its own version of
this exact thing.

## The field, by the numbers that are actually true

I didn't take star counts, skill counts, or plugin counts from any README. Every number below is
either a live GitHub API call or something I counted myself off the filesystem.

| Repo | Stars | What it actually is |
|---|---|---|
| `obra/superpowers` | 243,958 | Skills + an *enforced* methodology |
| `anthropics/skills` | 157,558 | Anthropic's own first-party skills — some of these literally power Claude's document-creation feature |
| `ComposioHQ/awesome-claude-skills` | 66,589 | Mostly a link index, plus Composio's own platform skills |
| `travisvn/awesome-claude-skills` | 13,870 | Pure curated link list |
| `rohitg00/awesome-claude-code-toolkit` | 2,233 | A real toolkit stapled to an abandoned link dump |
| `jqueryscript/awesome-claude-code` | 453 | The broadest map of the whole ecosystem |
| `glebis/claude-skills` | 301 | A personal, well-built 90-skill collection |

That last one — 301 stars — is the one that started this. I reviewed it first, on its own, expecting
a quick "looks fine" and moving on. It *was* fine. But reviewing one small personal repo and calling
that "the landscape" felt like exactly the kind of shortcut this whole investigation is about not
taking. So I went and looked at the other six.

## Pattern 1: the bigger the number, the more likely it's wrong

`ComposioHQ/awesome-claude-skills` claims "1000+ production ready" skills. I counted what's actually
in the repo: 30 to 40. The other 960-odd comes from Composio's own platform integration count — a
completely different kind of number, quietly merged into the headline.

`rohitg00/awesome-claude-code-toolkit` is the more instructive case, because it contradicts *itself*.
Its README says 35 skills, 135 agents, 176+ plugins. Its own `marketplace.json` — a file the
maintainer wrote — says 120 plugins and 6 MCP configs. The filesystem says 40 skills, 136 agents, 16
MCP configs. Three sources, inside one repo, agreeing on nothing.

I went looking for why, and the git history explains it cleanly. The entire first-party toolkit was
generated in two commits on day one, back in February. `commands/` hasn't been touched since.
`plugins/` got exactly one commit after that — a bugfix for missing YAML frontmatter across 82
files, which is itself a tell that the initial bulk generation wasn't reviewed carefully. Almost
every one of the repo's 700 commits since then is a merged pull request adding *someone else's*
project to a link table. Then, seven weeks before I looked, the maintainer stopped merging even
those. 183 pull requests are sitting open, untouched.

None of this makes the first-party toolkit worthless — the agents, commands, and hooks that are
actually there are competently structured. It means the number on the tin was never the number in
the box, and nobody had checked in months.

## Pattern 2: a live supply-chain hole, hiding in plain sight

Here's the finding I'd lead with if I were writing this for someone about to install that toolkit.

Its `mcp-configs/` directory ships pre-built MCP server configurations — one per task category:
security, design, DevOps, and so on. The security config and two of the design configs reference
three npm packages under the `@anthropic/` scope: `mcp-ghidra`, `mcp-figma`, `mcp-server-figma`.

I checked all three against the npm registry. **None of them exist.** 404, all three.

Read that again slowly, because the mechanism matters more than the specific packages. These look
like hallucinated names — the kind of plausible-sounding string a model produces when asked to write
a config and nobody runs `npm info` to check. The scope is the actual danger, not the package: a
name under `@anthropic/` *reads as official*, and trust transfers from the name whether or not the
package behind it is real. If anyone ever claims that scope and publishes something malicious as
`mcp-ghidra`, the first people to type `npx -y @anthropic/mcp-ghidra` — trusting a brand they
recognize — will be the users of this exact toolkit, following its own documented instructions. Two
more references (`kubectl-mcp-app`, `mcp-terraform`) are equally nonexistent. A fourth,
`defi-mcp`, does exist — as a single version published once in January by a single maintainer, wired
into a crypto-wallet-adjacent config. That's not proof of malice either. It's just the exact risk
profile a real supply-chain attack would target, sitting there, recommended by default, in a project
with 2,233 stars.

None of the other repos I reviewed had anything like this. So the finding isn't really "this one
repo has a bug." It's a check I wasn't running before, and now I am: **before you let an agent run
any MCP config or dependency list, verify every package it names actually exists.** That takes one
`npm info` call per package. Nobody in this toolkit's chain — not the author, not 2,233 people who
starred it, not (as far as I can tell) anyone in 183 open pull requests — ran it.

## Pattern 3: the biggest repo didn't teach me anything new. It confirmed something I'd already built.

`superpowers`'s aggressive bootstrap sounds like a red flag on first read — "you do not have a
choice" is not language you expect from open-source tooling. I spent real time trying to find the
manipulation underneath it. I didn't find any. What I found instead was a genuinely disclosed,
transparent, MIT-licensed control loop: brainstorm, with a hard human-approval gate before any code
gets written; dispatch to a fresh subagent per task; independent review from a *second* subagent
whose instructions explicitly forbid trusting the first one's self-report ("a stated rationale never
downgrades a finding's severity"); verify with fresh evidence before anyone is allowed to say "done."

I run a version of that same loop — scope, dispatch, independent adversarial review, verdict — as a
hard rule for how I manage my own lab. Finding it re-derived, almost word for word, inside the single
most popular project in this entire space, wasn't a "great minds think alike" moment. It was a
sanity check that the shape isn't a personal preference — it's what the discipline converges to when
enough people get burned by trusting a self-report. Anthropic's own `skill-creator` skill runs a
smaller version of the same idea: an actual paired A/B evaluation harness, with a grader that's
instructed to critique its own assertions before it trusts them.

Neither project is clean on *process*, to be fair. `superpowers` has zero CI and a self-reported 94%
pull-request rejection rate — a single maintainer is the whole quality gate. Anthropic's repo takes
effectively no outside contributions at all. But the review discipline itself — independently
arrived at by three unrelated teams — is a stronger signal than any one of us inventing it alone
would be.

## What I actually changed because of this

- Subagent handoffs now go through files — a path, not a wall of pasted context — because
  `superpowers` measured its own dispatch prompts hitting 42,000 characters, 99% of it re-pasted
  history, and fixed it that way.
- My review-agent instructions now explicitly ban pre-judging a finding in the dispatch prompt
  ("treat this as Minor at most") — `superpowers` bans the same thing, for the same reason: it
  quietly neuters the review before it starts.
- I adopted Anthropic's "progressive disclosure" vocabulary for context budgets outright — metadata
  always resident, the instruction body loaded only when triggered, everything else on demand. It's
  cleaner than anything I'd have written myself.
- Every MCP config gets `npm info`'d, every package, before it ships. No exceptions, no "it's
  probably fine."

And one thing I'm *not* doing differently: repeating a headline number — anyone's, including my
own — without checking it against the thing it's supposedly describing first.

Every claim in this piece is tied to a specific commit, a specific file, a specific line. That's not
a style choice. It's the same bar I'd have to clear if one of my own team's reports made a claim I
couldn't reproduce — so it's the bar I held everyone else to, including a quarter-million-star repo
that never asked to be fact-checked.

What would you find if you actually read the thing you starred?
