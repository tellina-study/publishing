---
title: AI speeds up every part of software development — and can slow the whole down
slug: ai-delivery-gap
status: draft
categories:
- AI
- Software Engineering
tags:
- AI in SDLC
- Code Review
- Mutation Testing
- DORA
- Quality Gates
wp_post_id: 326
---

> **Fiona Chen and James Stratton of Harvard went through five years of telemetry from 718 firms:
> after the switch to AI agents, 30% more lines of code and the same number of closed tasks. Review
> time in the same sample rose 49%. These are three separate measurements; the data do not assemble
> them into one causal chain.**

The industry answers this gap by taking the human out of the control loop and putting an automatic
gate in their place — a machine check that passes a change onward without a human "yes." And a gate
that has never been fed a defect on purpose should be treated as broken until proven otherwise.

**TL;DR**

- Harvard, telemetry from 718 firms: after the move to AI agents, **+30% lines of code, +20%
  commits, +23% PRs** — and the shipped result did not move by any statistically significant amount.
- In the same measurement, review time rose **49%**, and AI review tools did not take that increase
  away.
- The DORA 2024 survey: for every +25% of reliance on AI, teams rate themselves **+7.5%** on
  documentation quality, **+3.4%** on code quality, **+3.1%** on review speed — while delivery, in
  the same report, goes down: **−1.5%** throughput, **−7.2%** stability.
- The industry answers with automatic gates: in Meta's RADAR the machine approves a change with no
  human in **60.31%** of cases, and those changes are rolled back three times less often than the
  rest.
- The price is misses: the classifier Anthropic put in place of manual approvals misses **17%** of
  dangerous actions (computed on 52 cases, and by the system's own builder).
- A control that has gone quiet is indistinguishable from a working one: a green CI looks the same
  whether everything is fine or the detector is dead. That is why you test a control by feeding it a
  defect on purpose.

## Every part is faster. The whole is not

A part here is one step of the work and the artifact it leaves: code, documentation, a review. The
whole is what reached the user: a task closed, a release shipped.

Two independent 2026 measurements showed the two quantities coming apart: Chen and Stratton on
telemetry from 718 firms (Harvard), and Demirer, Musolff and Yang on half a million GitHub accounts
(NBER). Two more measurements from the same year count not the gap but the price the speed-up leaves
behind in the code: RAMP across 441 repositories, and "Debt Behind the AI Boom" across 302.6
thousand AI-written commits.

### More code, the same amount delivered

Chen and Stratton took data from the Jellyfish platform: **300 million work events** — GitHub
activity, Jira tickets, calendar meetings — from **725,938 workers at 718 firms**, January 2021 to
March 2026 ([Harvard, August 2026](https://fion.ac/jellyfish.pdf)). This is telemetry, not a survey.
The method is staggered difference-in-differences: firms that switched AI on later serve for a while
as a control group for those that switched it on earlier. That separates the effect from the
market's overall trend.

The result: firms that moved to agents wrote markedly more code — **+30% lines, +20% commits, +23%
PRs**. The shipped result — closed tasks and epics — moved by a "small positive, but statistically
insignificant" amount: the upper bound the data allow is plus **12%**.

What separates the two groups of numbers is whether the result has a customer outside the team. A
closed task has one; a line, a commit and a PR do not. You cannot divide one by the other: no theory
says that +30% lines owes you +30% tasks.

→ **Takeaway:** lines, commits and PRs report on what was produced, not on what reached the user;
this data does not let you swap one for the other.

### One part of the work got slower — review

Same paper, same sample: review time rose **49%**, the share of PRs that come back with change
requests nearly doubled, and comments per PR rose **35%**. Whether AI review tools take that increase
away, the authors checked separately. They do not: the bottleneck holds even after those tools land.

→ **Takeaway:** buying an AI reviewer in the hope that it restores your old speed is premature. The
data contain no causal link from "more code" to "review is the bottleneck": these are separate
measurements.

### A different sample: releases did rise, but the count is not the same count

Demirer, Musolff and Yang ([NBER WP 35275](https://www.nber.org/papers/w35275), September 2026
revision) matched 500,000+ GitHub developers in a matched event study: **commits +240%, projects
+80%, releases +30%** — cumulative across three generations of tools, not from one switch being
flipped. Here the whole did move. But these numbers and Harvard's are not comparable: +20% commits
against +240% is a twelvefold difference. It comes from who gets counted — a firm's employed
developers, or a person's entire public account, everything they do outside work included.

→ **Takeaway:** across such studies the shape of the curve is comparable, the height is not: "+240%"
was computed on a different population, and the number does not carry over to your team.

### The price of speed: what stays behind in the code

You pay for the speed-up with what stays in the repository. That price has been measured twice.

[RAMP](https://arxiv.org/abs/2608.25241), 441 repositories: agents speed everyone up by roughly the
same amount, **+28–38% commits**; what diverges is the consequences. Among repositories where the
agent writes a noticeable share of the code and where the contrast can be identified, the authors
compared two cases: a committed instruction file for the agent sits next to the code, or it does not.
Without one, cognitive complexity (a readability metric: how hard the function is to hold in your
head) grows twice as fast, **+53% against +27%**, and static-analysis warnings accumulate **1.7
times** faster. And **73.8%** of the instruction files themselves are written once and never updated.
Rising complexity is not a defect, but it predicts what the next edit will cost. The authors state
the caveat themselves: they observed repository maturity rather than assigning it, and they present
the findings as hypothesis-generating.

The second measurement is "[Debt Behind the AI Boom](https://arxiv.org/abs/2603.28592)": **302.6
thousand** verified AI commits from **6,299** repositories, with a static analyzer run before and
after each commit. More than **15%** of commits introduce at least one finding, and **22.7%** of all
tracked findings survive into the latest version. A finding here is one analyzer hit, and **89.3%**
of them are code smells: a sign of badly arranged code — a long method, duplication, a tangled
conditional.

→ **Takeaway:** these percentages count the future cost of edits, not a flow of incidents reaching
users; budget for them when you estimate the next tasks against the same code.

### The DORA puzzle: every local metric up, delivery down

The fifth source is not a measurement but a survey, and it is the most awkward of the lot. The annual
[DORA](https://dora.dev/research/2024/dora-report/) report asks engineers how heavily they lean on AI
and how their work is going. In the 2024 edition, page 37: the more a team leans on AI, the higher it
rates its own work — every **+25% of reliance** comes with **+7.5% documentation quality, +3.4% code
quality, +3.1% review speed**. Three local metrics, three pluses.

Seven pages later, in the same report and off the same increase in reliance, stands the heading "AI
is hurting delivery performance" and a pair of numbers with the opposite sign: **−1.5% throughput and
−7.2% delivery stability**. There is the puzzle: one survey, the same teams — documentation, code and
review better by their own rating, delivery worse. And this minus is what the word "slow" in the
title rests on: the gap in the earlier measurements says only that the whole did not move.

Before we unpick it, three things about that number, and you need all three.

**What "+25% of reliance" means.** Not "a quarter more AI-written code in the repository." DORA did
not look into repositories at all: it asked seven questions about AI use and collapsed the answers
into one scale. Plus 25% on that scale is a shift in how a team describes its own work, not a reading
off a meter.

**The scale was later changed.** In 2025 DORA replaced those seven questions with three, one of them
about trust in AI. So "2024 had a minus, 2025 has a plus" compares formally different variables: what
changed is not only the finding but the instrument.

**What actually reversed in 2025.** In the [2025 report](https://dora.dev/dora-report-2025/) the sign
flipped for throughput, while AI's link to delivery instability held — "AI is associated with an
increase in software delivery instability." But without percentages now, in standardized effects and
on a different scale. The direction of the finding stood; the −7.2% figure itself has been
re-measured by nobody using a comparable method.

Now the answer, which is also an answer to what these metrics measure. Nobody measures documentation
quality, code quality or review speed directly: behind each one stands a control — a linter, a test,
a review, a CI gate. And every control has a state that from outside is indistinguishable from
working: silence. A green CI, an empty list of policy violations, a quiet alerting stack look the
same whether everything is fine or the detector is dead. The signal is pleasant: all green, the team
moves on. The feedback arrives with the incident — by which time the detector should already have
fired.

This is an argument, not a measurement: almost nobody has measured directly how often a control dies
quietly. But it explains how "every local metric improved" and "nothing reached the user" live
together in the same data — the metric is read off a control that may have gone quiet. And it
explains why the gap is invisible from inside the team: the metrics that go up are exactly the ones
people look at every week.

→ **Overall takeaway:** the three caveats above have to travel with the −7.2% wherever it is quoted:
the 2026 data support neither "AI made delivery worse" nor its denial. And you cannot read a
control's silence as good news until you know when it last caught anything. There is one way to find
out: feed it a defect on purpose and see whether it catches it.

> 📌 **Section in short**
>
> Local metrics rise — more code, documentation and code better by the teams' own rating — and at the
> output there is no gain. Something eats it on the way, and no local control will show you that:
> every one of them is in the black.

## The industry's answer: take the human out of the loop

The control loop is the chain a change passes through before it reaches a user: review, CI gates,
approval to roll out. Take the human out of it, and "let this through or not" is decided by an
automatic gate instead. The trade has been measured on both sides, but with very different precision
— and that asymmetry is itself a finding here.

### What removing the human buys

**The looser the risk threshold, the more changes the machine takes on itself — and the less often
they are rolled back.**

[RADAR](https://arxiv.org/abs/2605.30208) is an automatic review-approval system built and described
by Meta: 535 thousand diffs (a diff is one code change submitted for review), 331 thousand of which
made it to the main branch. An auto-approved diff goes into the branch without a human "yes," and the
rollback rate of such diffs is the most direct measure of how many mistakes slipped past. The risk
threshold was loosened, and the system started taking on not a quarter of the safest changes but
half: the auto-approved share rose to **60.31%**, those diffs are rolled back three times less often
than diffs that skip auto-approval, and they carry fifty times fewer production incidents. But the
system itself selects diffs by risk; this is not randomization. "Fifty times fewer" means, among
other things, that low-risk changes really are low-risk — and the paper gives no absolute incident
rate.

→ **Takeaway:** nothing here lets you carry "fifty times fewer incidents" over to your own changes.
What carries over is the dial — the risk threshold that governs how much the machine takes. Set it
narrow and widen it against your own rollback measurements, not against someone else's percentage.

**External change approval does not deliver what it is introduced for.**

[DORA 2019](https://dora.dev/research/2019/dora-report/2019-dora-accelerate-state-of-devops-report.pdf)
(and a [separate page on the practice](https://dora.dev/capabilities/streamlining-change-approval/)):
teams whose significant changes are approved by an outside body — a change advisory board or a senior
manager — are **2.6 times more likely** to be low performers, and, in the same report, verbatim: "no
evidence to support" the hypothesis that such approval reduces the share of failed changes (about
1,000 respondents).

→ **Takeaway:** if your change advisory board has no measurement of the defects it has caught, you
have nothing to cite for its usefulness. The cure is cheap — start that measurement: a list of the
changes the board turned back, with a reason for each.

**A human who is asked too often stops being a control.**

[Anthropic, March 2026](https://www.anthropic.com/engineering/claude-code-auto-mode): Claude Code
users approve **93%** of permission prompts — the "the agent wants to run a command, allow?" dialogs.
The vendor calls this approval fatigue and replaces the dialogs with a classifier that reads the
session transcript and decides on its own: 0.4% false positives across ten thousand cases of real
traffic.

→ **Takeaway:** how often you ask is a design parameter, not an interface detail: ask only about what
you are willing to read.

### What it costs

This side was measured mostly by the people who removed the control: vendors and platform teams, with
no control group and no interest in publishing a failure. Only three measurements aim at the removal
of the control itself rather than at the quality of AI code with a human still in the loop.

**The classifier that replaced the prompts misses 17% of dangerous actions.**

The number comes from the same Anthropic write-up as the 93%; it is computed on 52 hand-labeled
cases, and it is self-reported by the builder of the system. No other published numbers on the cost
of that swap exist, and the silence does not argue for the swap.

→ **Takeaway:** automatic permission is paid for with a known miss rate. Before you swap prompts for
a classifier, get that rate on your own traffic: pick a hundred sessions where the agent did
something dangerous and run the classifier over them.

**The one controlled experiment on weakening human control came out negative.**

Requirements inspection: [34 participants, a crossover design, Bayesian
analysis](https://arxiv.org/abs/2608.21298) — each worked both with model support and without, so the
comparison is not between different people but between one person in two modes. Model support
**worsened** defect detection and did not cut the time; the participants, the authors note, were
novice inspectors. The human is formally in the loop here, but their ability to spot a defect falls —
and that ability is exactly what "the model will back you up" is supposed to protect.

→ **Takeaway:** "the model will back the inspector up" is a hypothesis whose only direct test came
back with the opposite sign. Until someone re-tests it, put the model in front of the human, not
beside them.

**Agent PRs get reviewed more often than human ones, but a quarter of the comments under them are
orders to the worker.**

The [measurement](https://arxiv.org/abs/2605.02273) speaks for the agents at first: in the
intersection of repositories, **28.92%** of agent PRs go without review against **34.52%** of human
ones. But the composition of that review differs: **25.92%** of human comments under agent PRs are
instructions to the agent rather than a judgment on the change (under human PRs such comments run
1.63%). And across the full sample of the same study, **61.38%** of agent PRs get no review at all.

→ **Takeaway:** you can no longer count "it was reviewed" from the mere presence of a comment under a
PR. What to measure is the share of comments that judge the change — label your last hundred comments
into two classes.

The argument "remove the human or not" cannot be settled in general: the upside is better measured
than the downside, and that is a finding, not an argument. A different question can be settled —
**what exactly we are trading the human for**. A human reviewer, for all those 93% approved without
looking, can say "no" for a reason nobody anticipated. An automatic control says "no" exactly where
it was taught to. So everything comes down to one thing: whether it still can.

> 📌 **Section in short**
>
> The trade is measured asymmetrically: the gain, on hundreds of thousands of diffs and by the most
> direct measure there is, rollbacks; the cost, on 52 cases, 34 novice inspectors and one sample of
> PRs. It does not follow that there is no cost; it follows that nobody has counted it properly — and
> that you will have to get your own number.

## How to tell a control that has gone quiet from one that works

There is one way, and it is older than half the tools discussed here: feed the control a defect on
purpose and see whether it catches it.

### Where the technique comes from, and why it lives inside code

It has been known since 1972: Harlan Mills ("On the Statistical Validation of Computer Programs," IBM
FSD) proposed planting known defects in a program and using the share that gets found to estimate
**how many defects remain unfound**. The literature calls this bebugging; below it is mostly seeding
a known defect. The modern reading turns the same arithmetic onto a different object: if the control
found three of ten planted defects, you have learned its sensitivity. Mills was measuring the
artifact — this version is ours, and Mills never put it that way.

After that the technique narrowed down to code for a technical reason: a code mutant is generated
from the grammar of the language — automatically, by the thousand. A mutant is a copy of the program
with one small break in it; if even one test fails on it, the mutant is killed; if all stay green, it
survived. A surviving mutant is a hole in your test suite, demonstrated.

### Three measurements: what an untested control costs

**Coverage tells you how many lines ran, and nothing about whether the tests would catch a defect.**

Google measured how well it works ([ICSE 2021](https://arxiv.org/abs/2103.07189)): about 400 thousand
mutants, more than 33 million test-target runs. Of 1,502 high-priority bugs, a mutant would have
surfaced the defect right on the change that introduced it — **1,043 cases, 70%**; this is a
reconstruction after the fact, on bugs already known. But the authors' verbatim conclusion is blunt:
each such bug-introducing change "was covered by the existing tests," and "code coverage had
exhausted its usefulness."

→ **Takeaway:** green coverage is not evidence that your tests catch anything. The only thing that
gives you evidence is feeding in a defect on purpose.

**You can make a control measure its own uselessness.**

[Tricorder](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43322.pdf)
(ICSE 2015) counts the share of "not useful" reactions among all explicit developer reactions. The
thresholds are set in advance and in numbers: **≥10% puts the analyzer on probation, >25% can get it
switched off**. The argument "do we still need this analyzer?" starts from data, not from opinion.
Once it played out exactly that way: in 2014 the DocComments analyzer broke in week 24, a spike in
"not useful" showed it, and it was fixed by week 33. **Nine weeks of quiet garbage** — and this is
the single documented case: one analyzer, one year, one company.

→ **Takeaway:** give your analyzers a reaction counter and a switch-off threshold in advance: then a
broken analyzer surfaces on its own, without an incident review.

**The detecting layer breaks too, and how often has been counted.**

[Microsoft Teams, SoCC 2022](https://dl.acm.org/doi/10.1145/3542929.3563482) — 152 incidents of
severity ≤2 over a year, and in **27.7%** of them the monitor was broken or missing. A caveat: 27.7%
is the sum of three categories from the authors' own breakdown (a bug in the monitor, no monitor, a
gap in telemetry), computed by us.

→ **Takeaway:** in an incident review keep the second question next to the first — why it broke, and
why the monitor did not say so.

### The same rule was written down outside software long ago

[NFPA 72](https://www.pottersignal.com/resources/conference/presentations/nfpa-72.pdf) requires that a
smoke detector be tested with smoke, and the companion standard for carbon-monoxide detectors says
the decisive part out loud: the gas is introduced into the sensing chamber, and "an electronic check
(magnets, analog values, etc.) is not sufficient to comply with this requirement." Only a test in
which the substance the detector must smell physically reached it counts as a test.
[EICAR](https://www.eicar.org/download-anti-malware-testfile/) explains its test file by the same
logic; auditing and metrology arrived at the same place by their own routes — we come back to them at
the end.

> 📌 **Section in short**
>
> The three measurements above say the same thing from three directions: tests can be green on the
> very change that introduces a bug; an analyzer can emit garbage for nine weeks until somebody
> counts the reactions; in 27.7% of serious incidents the monitor was broken or absent.
>
> What they share is that none of these failures is visible without a separate action. You need a
> second loop: not "did the control fire," but "have we checked that it still can," and when we last
> did.

## A pass through the stages: what AI breaks, what it fixes, and how to test it

Six stages, ordered by distance from what can be broken mechanically. For each: what control stands
there, what has been measured, what AI does here — and a concrete seeding recipe, where one exists.

### 1. Requirements and acceptance criteria

**What stands there, and what has been measured.** Specification inspection and acceptance criteria;
the planted defect is a contradiction or an omission. There is one measurement, thirty years old and
with no seeding in it: [Porter, Votta and Basili, TSE
1995](https://drum.lib.umd.edu/bitstreams/332d6328-bdce-4726-9102-e00bac748f9a/download) — 48
participants, 16 teams of three, two documents holding 42 and 26 defects. On average a team finds
**24 to 57%** of the known defects, depending on the reading method and the document; individual
teams fall anywhere from 19 to 74%. And the team meeting adds **zero net gain** over reading alone;
[Fagan](https://eden.dei.uc.pt/~mvieira/Fagan02.pdf) himself names the price — **20–30% of the
effort** of the first half of development. And 24–57% is a share of the defects the documents were
**already known** to hold: they were found in advance, not planted. About the unknown ones the
experiment says nothing.

**What AI breaks.** Requirements have become cheap to produce, while inspection still costs the same
20–30% of effort, and that cost does not divide by volume. The first prop people reach for did not
work: the only direct experiment in which a model supported the inspector (34 participants, the
section above) made defect detection worse.

**What it fixes.** The model as a separate screening pass, ahead of the human, has been measured on
its own: the best of ten models found a median of **47%** of the issues experts had labeled, at
**11%** false flags ([a benchmark on INCOSE criteria, with no defects
seeded](https://arxiv.org/abs/2609.03230)). Half the issues for a cheap pass is a lot for a screener
and little for a control.

**Seeding recipe — there is no ready one.** The only tool that mutates a specification itself is
[MuAlloy](https://github.com/kaiyuanw/MuAlloy): nine operators, mutations at the syntax-tree level, a
SAT check that the mutant is not equivalent to the original. But it works only on a specification
written in Alloy — it does not apply to a prose spec or to Gherkin. *Our proposal, not industry
practice:* put a dozen defects into a copy of the specification, drawn from the catalog of
"requirements smells" in [ISO/IEC/IEEE 29148](https://arxiv.org/pdf/1611.08847) — an unmeasurable
"fast" in place of a number, an "it" with no clear antecedent, a condition with one branch dropped, a
requirement that contradicts its neighbor — and do not tell the inspectors the count. The share they
find is the sensitivity of your inspection; ready-made sets of such defects, and a number to compare
your share against, do not exist.

→ **Takeaway:** put the model in front of the inspection, not inside it — let it mark up a draft the
human then reads himself. And you will have to measure the inspection's sensitivity yourself: no tool
for a prose specification exists.

### 2. Architecture and ADRs

**What stands there, and what has been measured.** Decision review and fitness functions —
architectural requirements turned into checks and tied to the working cycle ([*Building Evolutionary
Architectures*](https://openlibrary.org/works/OL19541931W), 2017). Some run at build time: a test
sitting next to the code, along the lines of "the payments module does not import the reporting
module," which [ArchUnit](https://www.archunit.org/) can do. Others watch the running system:
"95th-percentile response time no higher than 300 ms." Under its own name the practice has never been
measured once — [Technology
Radar](https://www.thoughtworks.com/radar/techniques/architectural-fitness-function) put it in the
Trial ring in 2017 and has not returned to it since May 2018 — while the mechanism has been measured
twice, on tiny samples: [three teams out of
six](https://fb-swt.gi.de/fileadmin/FB/SWT/Softwaretechnik-Trends/Verzeichnis/Band_29_Heft_2/06-knodel.pdf)
(2008) with such a check had 60% fewer structural violations at comparable effort; [four student
projects out of eight](https://urn.kb.se/resolve?urn=urn:nbn:se:lnu:diva-60472) (2016) had
significantly fewer violations, with no effect size given. And whether an ADR — a written
architectural decision with its context and consequences — is still alive, nobody measures: a corpus
of [4,316 ADRs from 547 projects](https://arxiv.org/html/2609.07375) **does not measure** staleness
and does not propose how to detect it (and it only runs up to 2020). A neighboring drift has been
measured: [3.9% of references to code elements in documentation are
stale](https://arxiv.org/abs/2212.01479) — 7,910 out of 201,852, affecting **28.9%** of projects,
with an average staleness age of **4.7 years**.

**What AI breaks.** Not authorship: an agent writes a decent ADR. What breaks is the order — the
decision gets written after the fact, to fit code that already exists, and then the ADR records not a
decision but an outcome. And speed: a rule that lives only in prose gets broken by an agent exactly
like any other rule not lifted into a check.

**What it fixes.** A rule compiled into a test is, to an agent, a signal of the same class as a
compiler error: the failure comes back into its loop, and it fixes the code itself. Unlike an entry
in a document, a decision in that form cannot be quietly ignored. Nobody has measured this particular
effect on agents — it is an argument about mechanics, not a measurement.

**Seeding recipe for architectural rules — ready, and the best of the six.** There is a whole
repository built on the technique: in
[ArchUnit-Examples](https://github.com/TNG/ArchUnit-Examples), `src/test` holds the rules and
`src/main` holds production code that deliberately breaks them. Verbatim from the README: "These
tests are all designed to fail". You run `./gradlew test` and the tests are supposed to fail; in
Python the same thing assembles out of
[pytest-archon](https://github.com/jwbargsten/pytest-archon) or
[import-linter](https://import-linter.readthedocs.io/). **The trap:** ArchUnit has a freeze mode,
`FreezingArchRule` — "on consecutive runs only new violations will be reported". A frozen rule by
construction **does not fail** on violations that already exist, so seeding an old one into it proves
nothing: the test stays green. The seed has to be new.

**No check for whether an ADR is current exists.** The official [ADR tooling
catalog](https://adr.github.io/adr-tooling/) lists tools for capturing decisions; not one of them
checks "is this decision still in force?" *Our proposal:* treat as unverifiable any ADR that has not
a single consequence lifted into an executable check, and once a quarter run a fresh violation
through those checks.

→ **Takeaway:** turn an architectural rule you care about into a fitness function or an executable
example ([doctest](https://docs.python.org/3/library/doctest.html) and its relatives run an example
from the documentation as a test), and start your testing with a fresh violation — on an old one a
frozen rule stays silent.

### 3. Code

**What stands there, and what has been measured.** Tests and coverage; the check on the control
itself is mutation testing. [Google, TSE 2021](https://arxiv.org/abs/2102.11378): 16.9 million
mutants, more than 24 thousand developers. At first developers called **85%** of the mutants shown to
them useless; after six years of hand-written suppression rules, authored separately for each
language, **82%** of the mutants that reach a developer are judged useful (different populations:
before the filter and after). Google rejected the mutation score as a metric: it is "neither concrete
nor actionable".

**What AI breaks.** The agent writes the code, and the same agent writes the tests for it — the
checker and the checked are one. A test written against code that already exists is green by
construction: it repeats the behavior instead of checking it — and coverage goes up all the same.

**What it fixes.** A mutant judges the tests, not the code — so a surviving mutant exposes a hole no
matter who wrote the two sides, or in what order. Here too there are no comparative measurements of
"with an agent versus without": this is an argument from how the check is built, not a measured
effect.

**Seeding recipe — ready on four stacks.** [PIT](https://pitest.org/quickstart/maven/) for Java,
[mutmut](https://mutmut.readthedocs.io/en/latest/) and [Cosmic
Ray](https://cosmic-ray.readthedocs.io/en/latest/tutorials/intro/index.html) for Python,
[Stryker](https://stryker-mutator.io/docs/stryker-js/getting-started/) for JS/TS and .NET: install,
run one command, look at the survivors. The price has been measured — the Cosmic Ray tutorial names
it outright: if the tests take 10 seconds and the tool found a thousand mutations, a full pass will
take **about 2.7 hours**; hence the incremental modes in all four. A separate `baseline` step runs
the tests without mutations and has to come back green: the tool itself insists you confirm the
control is not red for some other reason.

→ **Takeaway:** run mutation testing on a critical module as a one-off diagnosis, and budget an
evening for it rather than minutes; as a blanket gate, and on non-critical code, mutants turn into
noise — which is what Google demonstrated on itself.

### 4. Agent instruction files

**What stands there, and what has been measured.** A text file of rules the agent reads before it
works; the planted defect is a task that can only be finished by breaking a written rule. This is the
best-studied of the six stages, not a blank spot: an ablation across 1,650 sessions, a dedicated
benchmark on obeying prohibitions, and several other papers. The next section is given over to it
entirely.

**What AI breaks.** An agent does not go and read the rules of its own accord.
[RepoComplianceBench](https://arxiv.org/abs/2607.26819): 106 tasks from 49 repositories whose rules
explicitly restrict AI-made contributions; four frontier models — the agents "almost never
proactively retrieve the contribution rules" and "never refuse to contribute in AI-banned
repositories under any condition". An outright prohibition, written down in text, stopped no agent
even once.

**What it fixes.** This stage also holds the one measured case where AI works as the generator of the
planted defect used to test a control: [probe-and-refine](https://arxiv.org/abs/2606.20512) produces
synthetic bug-fix probes, uses them to diagnose the instruction file, and edits the file on the
results — a solved-task rate of **33.0%** against **28.3%** for a static file and **25.5%** for no
file at all.

**Seeding recipe — no engineering one, despite plenty of measurement.** The closest ready thing is
promptfoo's [Test Agent Skills](https://www.promptfoo.dev/docs/guides/test-agent-skills/) guide: a
runner and a set of assertions, including a negative one — "this rule should not have fired here."
But it compares **two versions** of the file, not "with the file and without," and it does not build
the provocation task. *Our proposal, a harness on top of promptfoo:* two copies of the repository,
one with the instruction file and one without; one task for which breaking the rule is the shortest
path to the result; twenty runs per copy; the threshold — if the violation rate with the file is no
lower than without it, the rule does not work.

→ **Takeaway:** run that check on one of your own rules today — it costs one run. And move a critical
prohibition out of text and into an enforcing control: a deterministic interceptor in the harness
stopped the agent [120 times out of 120](https://arxiv.org/abs/2606.06460), while the same
instruction delivered as text worked in 23% of cases.

### 5. CI and rollout

**What stands there, and what has been measured.** Policy as code —
[OPA](https://www.openpolicyagent.org/docs/policy-testing),
[Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/docs/),
[Kyverno](https://kyverno.io/docs/kyverno-cli/reference/kyverno_test/),
[`terraform test`](https://developer.hashicorp.com/terraform/language/tests) — and the build
accelerator, the machinery that runs only the affected tests instead of all of them. There are two
kinds of planted defect here: a manifest the gate is obliged to reject, and a mutant aimed not at the
tests but at the accelerator. On builds: [MSR
2024](https://rebels.cs.uwaterloo.ca/papers/msr2024_zeng.pdf), 10 projects, 2,237 "gap mutants" —
**between 0.11% and 23.50%** of mutants come out differently in an accelerated build than in an
ordinary one, and **69%** of the discrepancies have reproducible causes: a green accelerated build
and a green build are different things. On policies the measurement is old but head-on: [Martin and
Xie, WWW 2007](https://archives.iw3c2.org/www2007/papers/paper447.pdf), 11 policies, 906 mutants —
**98.6% structural coverage yields 59% of mutants killed**, and condition coverage in the same study
is 21.21%.

**What AI breaks.** The agent writes both the manifest and the policy that checks it — again the
checker and the checked coincide. And volume: configs and manifests pile up faster than anyone can
read them by eye, while the build accelerator decides which tests to run from the list of affected
files — a list an agent inflates wider than a human does.

**What it fixes.** Producing a bad artifact is work a model is objectively good at: a bad manifest or
bad HCL takes seconds, and you need a lot of them. No measured work on this exists, so it is a use,
not a recommendation.

**Seeding recipe — ready and built in.** In the official [Gatekeeper policy
library](https://github.com/open-policy-agent/gatekeeper-library/blob/master/library/general/containerlimits/suite.yaml)
every policy ships two examples — `example_allowed.yaml` and `example_disallowed.yaml` — and the test
suite carries an assertion `violations: yes`: on the second example violations are obliged to turn
up, which the `gator verify` command checks. The neighbors have the same thing as standard: Kyverno
writes `result: fail` in the test manifest; [`conftest verify`](https://www.conftest.dev/) puts the
known-bad HCL directly in the body of the test; and `terraform test` accepts an `expect_failures`
block — with a limitation from its own documentation: "Expected failures only apply to user-defined
custom conditions", which means you can seed a violation of your own validation, not an arbitrary
break. **For a broken migration there is no format at all:** in Flyway, Liquibase and Alembic alike,
we did not find a construct for "this migration must be rejected by the gate." *Our proposal:* keep a
catalog of known-bad migrations next to your real ones — dropping a column with no compatibility
window, altering the schema of a large table with no lock timeout — and run the gate over that
catalog every time the gate itself changes.

→ **Takeaway:** every policy should have a manifest it is obliged to reject — in two of the four
tools this is a ready format you can copy whole. And remember who writes that manifest: a class of
input the policy's author never imagined, the gate will miss twice.

### 6. Monitoring and release acceptance

**What stands there, and what has been measured.** Alerting rules and the canary release, where a new
version first goes to a small share of traffic; next to them the [dead man's
switch](https://runbooks.prometheus-operator.dev/runbooks/general/watchdog/), an alert that burns
forever and whose silence means the delivery path is broken. We did not find a figure anywhere for
the share of rules covered by tests — but the canon itself admits the problem: the [SRE
Workbook](https://sre.google/workbook/alerting-on-slos/) works through arithmetic in which, at a 90%
target and a threshold of "2% of the error budget in an hour," a 100% outage consumes 1.4%, and
concludes: **"this alert could never fire."** The canary has the same failure shape, presented as a
quality metric: [Gandalf](https://www.usenix.org/system/files/nsdi20spring_li_prepub.pdf) (Microsoft
Azure) reports **100%** recall at one of the rollout stages — but recall there is defined as "no
severe incident was caused by a bad rollout," that is, counted over incidents that happened; how much
bad went through unnoticed, the system cannot report.

**What AI breaks.** The failure of an AI feature often has no metric: the process is alive, the
response codes are 200s, latency is normal, and the answer is wrong — while the canary compares time
series this kind of failure does not produce. This is an argument, not a measurement: we did not find
any studies.

**What it fixes.** A model writes the synthetic series for a rule test in a minute — exactly the kind
of work where you need volume from it, not precision. Here too no measured study exists: a use, not a
recommendation.

**Seeding recipe — ready, for alerts and for the canary alike.** [`promtool test
rules`](https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/) runs your
rules against a synthetic series and compares the alerts that fired with the ones expected: the
series is the planted defect — you drop the `up` metric to zero and demand that the alert go off. A
large ready-made set of such tests sits in
[kubernetes-mixin](https://github.com/kubernetes-monitoring/kubernetes-mixin/blob/master/tests/tests.yaml)
and can be copied whole; the negative half is standard there — the steps at which an alert must not
burn are written with no expected alerts.
[Flagger](https://docs.flagger.app/tutorials/istio-progressive-delivery) has the procedure for
feeding in a deliberately bad version right in its official tutorial: you swap the image for one that
returns 500s, and the events show "Halt … success rate 69.17% < 99%", followed by "Rolling back …
failed checks threshold reached 10".

**What is missing is a check on the canary analysis itself.** *Our proposal:* Kayenta has a
[retrospective mode](https://spinnaker.io/docs/guides/user/canary/best-practices/) that runs the
analysis over a historical window of metrics without waiting for new points; run it over the window
of a past bad release and require a verdict of "bad." Spinnaker's documentation describes the mode as
a way to iterate faster on canary configuration and proposes no such check — the framing is ours.

→ **Takeaway:** set up the rule test, the dead man's switch and a canary run from the Flagger
tutorial right away — it is minutes, and all of it is ready-made. Compute your alert threshold by
hand against your own error budget: an alert that cannot fire in principle passes the rule test as a
working one.

### What the six stages show together

A ready seeding recipe exists at four stages: architectural rules, code, CI policies, alerts and the
canary. It is missing wherever the artifact is written in prose, or wherever what needs testing is
not the artifact but the analysis itself: prose requirements, whether an ADR is current, an
engineering test of the instruction file, database migrations, canary analysis. Five holes — and all
five had to be filled with proposals of our own. The pattern is simple: a recipe exists where the
defect can be generated from a grammar — of a programming language, of a manifest, of a metric
series. I picked the six stages myself, out of how the work runs, not by the strength of the
conclusion: this is an observation, not a law of nature.

> 📌 **The stage-by-stage tally**
>
> At five points there is no recipe at all, and at each of them we propose our own — tested by nobody
> but us. The price is known at one stage only: about 2.7 hours per thousand mutations with
> ten-second tests; for the rest nobody has published it.
>
> Which means the answer to "does your control work" costs different amounts at different stages —
> and most of all where the control is guarding prose.

## Your own instruction file: how to test it where you are

The previous section named the instruction file —
[CLAUDE.md](https://docs.claude.com/en/docs/claude-code/memory), [AGENTS.md](https://agents.md/),
[cursor rules](https://docs.cursor.com/context/rules) — as the stage where the test costs one run.
Here is how to set it up, and first, what to expect from it.

That such a file improves the result is not confirmed: a direct ablation on real tasks — two agents,
three repositories, 17 tasks, [288 runs](https://arxiv.org/abs/2607.27250) scored against reference
tests — returned "no measurable improvement in correctness on either agent". That the file changes
behavior is measured, and strongly. The whole distance between "changes behavior" and "improves the
result" is the story of this section: the practice works, but without a guarantee, and you have to
test it one rule at a time. None of the corpus studies below found tests on the rules themselves in
public repositories.

**A rule that is not written down is never followed. A rule that is written down is lost a third of
the time.**

[The ablation experiment](https://arxiv.org/abs/2605.10039): **1,650 sessions, 16,050 function-level
observations**, two TypeScript codebases, three models. An ablation is when you remove one element
from a system and watch what changes; here what was removed was the instruction file itself, and the
rule was deliberately trivial. Without the file it was followed **0 times out of 524** (upper
confidence bound 0.73%); with the file, 67.7% across 529 observations. This is not "the model
sometimes forgets": the file has an effect, a large one, but an effect and a guarantee are different
things.

Neither file size (from 25 to 500 lines), nor the rule's position inside it, nor splitting across
several files produces any distinguishable effect. Within a session, though, the **odds** of
compliance fall by roughly 5.6% with each further generated function, and the fall is concentrated in
the first three or four: the median first violation is the fourth function. The source is a
single-author preprint, not peer-reviewed.

→ **Takeaway:** writing rules down is worth it — without the file they are followed zero times. It
does not amount to a guarantee, and a long session is worth cutting short or backing with an
enforcing control.

**An enforcing control stands behind only 4.4% of the security rules people write.**

The second measurement is a corpus study. [481 public CLAUDE.md
files](https://arxiv.org/abs/2608.23550): **4.4%** (confidence interval 2.6–6.7%) — and that is under
the strictest matching criterion; under a loose one the share reaches 16%. Enforcing means a
mechanism that physically will not let the rule be broken: a gate, a hook, a check in CI. The
authors' diagnosis, verbatim: "a developer writes a security rule but gets no feedback on whether a
control will enforce it". Neither of the two other corpus studies of instruction files — [2,303 files
from 1,925 repositories](https://arxiv.org/abs/2511.12884) and [401 repositories with cursor
rules](https://arxiv.org/abs/2512.18925) — raises the question of tests on the rules at all.

→ **Takeaway:** count your own security rules one by one: behind each there is either a gate, a hook
or a check in CI, or nothing but text, which the model loses a third of the time.

**How to make the test real.**

Give the agent a task it cannot finish without breaking a written rule, and see whether it breaks it:
for a "do not touch production" rule, ask for something that requires touching production. Three
details, without which the test means nothing. Breaking the rule has to be the shortest path to the
result: an agent with a detour available tells you nothing about the rule. Do not remind it of the
rule inside the task — a reminder tests your memory, not the file. And run at least five or six
functions in a row: on one, the test will almost always pass.

From there the test scales itself. A rule that got broken is either rewritten until it is
unambiguous or moved into an enforcing control. A rule that held stays as text — but now by a
decision you made knowing the price.

> 📌 **Section in short**
>
> The instruction file is the cheapest control in this piece and the weakest guarantee: without it a
> trivial rule was followed 0 times out of 524, with it in two thirds of cases, and the ablation
> found no gain in correctness at all.
>
> So what to test is not "does the file work" but "does this particular rule work": one at a time, on
> a provocation where breaking it is the shortest path.

## Generating planted defects got cheaper — so far only inside code

You cannot generate a "deliberately wrong requirement" from a grammar: a requirement is written in
prose, and only something that grasps the meaning can break it into a plausible defect. For half a
century that meant manual work — which in practice meant almost never. Models change this.

### What has been measured

**The defects a model generates are closer to real bugs than what classical operators give.**

LLM mutants detect defects in **76.5% of cases against 44.2%** for classical operators; coupling with
real bugs is **51.5% against 24.4%**; the number of syntax-node types they touch is 49 against two.
The counts were made on [851 real bugs](https://arxiv.org/abs/2406.09843), with a control for
training-data leakage. Coupled means a test that kills the mutant also catches the bug: it is the
question "does the planted defect resemble a real one" turned into a number.

→ **Takeaway:** the argument "there is no decent mutant generator for our language" is out of date:
not to try seeding now is to refuse the test over a price that no longer exists.

**There is one industrial case: half the tests that uniquely kill a mutant add not one line of
coverage.**

[Meta ACH](https://arxiv.org/abs/2501.12862): 10,795 Kotlin classes, 31,677 generated defects, of
which 9,095 (29%) build, and 571 tests at the output; what reached production was what passed human
review — of 191 tests engineers looked at, 140 were accepted. **277 of 571 (49%)** tests that
uniquely kill a mutant **add not one line of coverage**.

→ **Takeaway:** a team that gates on coverage would have thrown those 277 tests away and the number
would not have twitched. And the funnel 31,677 → 571 → 140 says the second thing: this comes cheap to
nobody.

### What AI still cannot do

**ACH specifies a failure class not in plain text but in text plus an example of a past real diff.**

The wording in the paper is "a typical bug that introduces a privacy violation similar to {diff}":
that is closer to a catalog of your own past failures than to generation from a description, and the
authors themselves concede — "we have no way to consistently and reliably measure problem similarity
or relevance".

→ **Takeaway:** to carry this over you will need your own analyzed archive of failures; the option
"we'll describe in words what counts as a defect" is not tested by this work.

**17% of real bugs are coupled to no mutant at all, and AI has not closed that hole.**

[Just and co-authors, FSE
2014](https://homes.cs.washington.edu/~rjust/publ/mutants_real_faults_fse_2014.pdf) — 357 real
defects, 321 thousand lines — found these **17%** and described them as "mostly involving algorithmic
changes or code deletion". The counter-number is direct: on code deletion, the share of deleting
mutations from an LLM is **0.1–5.5% against 15.3%** for a classical tool. **The hole Just found, AI
has not closed.**

→ **Takeaway:** read the mutation score as a lower bound on your tests' sensitivity: algorithmic
errors and code deletion do not stand behind it.

**Outside code we found exactly one study** — probe-and-refine from the previous section, where the
model generates probes to test the instruction file. Nothing else: not on requirements, not on
acceptance criteria, not on ADRs, not on infrastructure as code, not on pipeline configs, not on
migrations. The one mutation of a non-code artifact we found is an executable model — that is, a
grammar again.

→ **Takeaway:** seeding outside code is done at your own risk and by hand — there is nothing here to
report as an established practice.

> 📌 **The edge of what's measured**
>
> Inside code, the model as a defect generator already beats classical operators on both of the
> measures used for this, and has been taken to production once.
>
> Past that the unmeasured begins: outside code we found a single study, and the two classes of
> defect that have been out of reach of mutants since 2014 the model has not closed — and it got
> worse where the code has to be deleted.

## Three ways to test a detector

Seeding a known defect is one of three ways, and the other two are worth knowing, because where there
is nothing to seed they are all that is left: **independently redo the work**, planting nothing (this
is how auditors' inspections work —
[PCAOB](https://pcaobus.org/documents/staff-update-2024-inspection-activities-spotlight.pdf) found
deficiencies in 39% of the audits it inspected in 2024), and **continuously measure a reference**
(this is how the check standard works in metrology: [NIST IR
6969](https://doi.org/10.6028/NIST.IR.6969-2019) declares the phrase "calibration as needed"
**unacceptable**). A principle from functional safety ties them together: undetectable failures
accumulate unnoticed, and the expected probability of a miss is proportional to half the interval
between tests of the detector ([IEC
61508/61511](https://61508.org/wp-content/uploads/2024/11/10B-SIL-Calculations-and-use-of-IEC-61508-6.pdf)).
Hence the rule: **the interval at which you test a control is a design parameter of risk; it is set
either deliberately or by accident.** A caveat: the arithmetic was derived for random hardware
failures, and the standard treats software errors separately. We carry over the frame, not the
arithmetic.

And a counterweight, from the discipline that reveres verification most. Blinding in clinical trials:
a [meta-study](https://doi.org/10.1136/bmj.l6802) across **142 meta-analyses and 1,153 RCTs** found
no average difference in effect estimates between blinded and unblinded trials. The authors leave two
explanations open and recommend keeping blinding anyway. Seeding is in the same position: it has a
price, and its benefit is measured less well than one would like — which argues for caution, not
against the technique.

What stands is what was said at the start: a control that has never been fed a defect on purpose
should be treated as broken until proven otherwise. The six stages above did not soften that — at
four of them the recipe is ready and costs an evening's work; at the rest nobody has one, and you
build the seeding yourself. Either way, the cheaper place to start is not a tool but what has already
happened: your past incidents are a ready set of known defects, expensively obtained and invented by
nobody. Run them through your current gates and see which one stays silent. In that very experiment,
Porter, Votta and Basili deliberately refused to seed defects — "No faults were intentionally
seeded… All faults are naturally occurring" — and it still holds: your own defects are more
trustworthy than invented ones.

When did your gate last say "no" — and do you know whether it still can?

## Further reading

Not a bibliography but what is worth opening yourself: the fourteen works this piece leans on
hardest. For each, what exactly it measures.

**What has been measured about speed and delivery**

- **Chen and Stratton, Harvard, 2026** — ["Artificial Intelligence in the Firm: Bottlenecks in
  Software Production"](https://fion.ac/jellyfish.pdf). 718 firms, 300 million telemetry events: +30%
  lines of code against a statistically insignificant shift in the shipped result, and +49% review
  time. The only work in which the parts of the job and its final result are measured on one sample
  by one method.
- **Demirer, Musolff and Yang, NBER, 2026** — ["Writing Code vs. Shipping
  Code"](https://www.nber.org/papers/w35275). 500,000+ GitHub developers: +240% commits against +30%
  releases. The same gap on a different population — and a lesson in how far the population moves the
  magnitude.
- **DORA, State of DevOps 2024** — [full report
  (PDF)](https://services.google.com/fh/files/misc/2024_final_dora_report.pdf). Both halves of the
  paradox in one document: +7.5% / +3.4% / +3.1% on documentation quality, code quality and review
  speed on p. 37, and −1.5% / −7.2% on delivery on pp. 39–40. Read it with p. 30 on the self-report
  scale, or the numbers are easy to mistake for meter readings.
- **RAMP, 2026** — ["A Few Pages of Markdown"](https://arxiv.org/abs/2608.25241). 441 repositories:
  agents speed everyone up equally, but cognitive complexity grows twice as fast where no committed
  agent instruction file sits next to the code. The price of the speed-up, measured in the code.

**Checking the checks themselves**

- **Porter, Votta and Basili, TSE 1995** — ["Comparing Detection Methods for Software Requirements
  Inspections"](https://drum.lib.umd.edu/bitstreams/332d6328-bdce-4726-9102-e00bac748f9a/download).
  48 participants, 16 teams: they find 24–57% of a document's known defects, and the team meeting
  adds nothing on top. Thirty years on, there is still no replacement for this measurement.
- **Petrović, Ivanković, Fraser and Just, Google, ICSE 2021** — ["Does mutation testing improve
  testing practices?"](https://arxiv.org/abs/2103.07189). 1,502 real bugs: a mutant would have
  surfaced the defect in 70% of cases, and every bug-introducing change was covered by tests at the
  time. The most direct argument against reading green coverage as evidence.
- **Just and co-authors, FSE 2014** — ["Are Mutants a Valid Substitute for Real
  Faults?"](https://homes.cs.washington.edu/~rjust/publ/mutants_real_faults_fse_2014.pdf). 357 real
  defects: 17% are coupled to no mutant — "mostly involving algorithmic changes or code deletion".
  The method's boundary, named by its own supporters.
- **Foster and co-authors, Meta, 2025** — ["Mutation-Guided LLM-based Test Generation at
  Meta"](https://arxiv.org/abs/2501.12862). 10,795 classes, 31,677 generated defects, 571 tests at
  the output: 49% of the tests that uniquely kill a mutant add not one line of coverage. There is no
  other industrial case of a model seeding defects.

**Controls and the human**

- **DORA, State of DevOps 2019, p.
  50** — [report](https://dora.dev/research/2019/dora-report/2019-dora-accelerate-state-of-devops-report.pdf).
  External change approval by a board or a senior manager: such teams are 2.6 times more likely to be
  low performers, and "no evidence to support" the hypothesis that approval reduces the share of
  failed changes. The oldest and most awkward result on the list.
- **RADAR, Meta, 2026** — ["Automating Low-Risk Code Review at
  Meta"](https://arxiv.org/abs/2605.30208). 535 thousand code changes: the risk threshold as the dial
  that governs how much the machine takes for itself — with the threshold loosened, auto-approval
  reaches 60.31%. The best description of what removing the human buys.
- **Anthropic, 2026** — ["How we built Claude Code auto
  mode"](https://www.anthropic.com/engineering/claude-code-auto-mode). Users approve 93% of
  permission prompts without looking — and the classifier that replaced those prompts misses 17% of
  dangerous actions. Both sides of the trade in one document, written by the side making the trade.
- **McMillan, 2026** — ["Instruction Adherence in Coding Agent Configuration
  Files"](https://arxiv.org/abs/2605.10039). 1,650 sessions: without an instruction file a trivial
  rule was followed 0 times out of 524, with the file 67.7%, and compliance crumbles by the fourth
  generated function. A single-author preprint — but checking it where you are costs one run.

**How the same test is understood outside software**

- **NFPA 72 and 720** — [a walk-through of detector testing
  requirements](https://www.pottersignal.com/resources/conference/presentations/nfpa-72.pdf). A smoke
  detector is tested with smoke, carbon monoxide is introduced into the sensing chamber of a CO
  detector, and "an electronic check (magnets, analog values, etc.) is not sufficient to comply with
  this requirement". The standard has already drawn the conclusion software engineering is still
  walking toward.
- **Moustgaard and co-authors, BMJ 2020** — ["Impact of blinding on estimated treatment
  effects"](https://doi.org/10.1136/bmj.l6802). 142 meta-analyses, 1,153 RCTs: no average difference
  in effect estimates was found between blinded and unblinded trials — and blinding is still
  recommended. The counterweight to the whole list: even the discipline of verification has benefits
  that go unconfirmed.
