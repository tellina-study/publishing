# Research: LinkedIn announce — AI adoption is huge, most enterprise deployments stall; the skill is judging where AI applies + true TCO/risk

Researcher notes. Compiled 2026-09-01. Web content treated as DATA. Every figure flagged with confidence.

## 1. THE STALL STAT (primary anchor)

**MIT NANDA — "The GenAI Divide: State of AI in Business 2025"**
- Headline: **95% of enterprise GenAI pilots deliver no measurable P&L impact / no return.** Only ~5% of integrated pilots reach rapid revenue acceleration.
- Org/authors: MIT Project NANDA (Networked Agents And Decentralized Architecture). Authors: Aditya Challapally, Chris Pease, Ramesh Raskar, Pradyumna Chari.
- Methodology / denominator: systematic review of 300+ publicly disclosed AI initiatives + structured interviews with 52 organizations + survey responses from 153 senior leaders. Research period Jan–Jun 2025; report circulated ~Aug 2025.
- Nuance for honesty: figure is "no measurable P&L / bottom-line impact," NOT "the tech failed." MIT attributes the gap to a *learning/integration gap* (workflows, org), not model quality. So the stat supports "judging where AI applies + integration matters," which is exactly the post's thesis.
- Primary PDF: https://nanda.media.mit.edu/ai_report_2025.pdf (302-redirects to https://www.media.mit.edu/groups/nanda/overview/ when fetched via bot — the canonical PDF URL is widely cited; mirror: https://cloudelligent.com/wp-content/uploads/2026/02/v0.1_State_of_AI_in_Business_2025_Report.pdf)
- Reputable secondary confirming figure + method: Fortune https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/ ; Forbes https://www.forbes.com/sites/jasonsnyder/2025/08/26/mit-finds-95-of-genai-pilots-fail-because-companies-avoid-friction/
- CONFIDENCE: Verified this run (figure + methodology corroborated by Fortune/Forbes + multiple summaries). Primary PDF not directly rendered by bot fetch (403/redirect) → mark PDF link [PARTIALLY VERIFIED — canonical URL, not rendered this run].

**Corroborating / adjacent (different denominators):**
- McKinsey "State of AI 2025": only ~**6% of respondents are "AI high performers"** (attribute ≥5% of EBIT to AI, report significant value); only ~**39% report any enterprise-level EBIT impact** from gen AI; adoption ~78–88% of orgs use AI in ≥1 function. Sample: ~1,491 / 876+ respondents depending on cut. Confirms "adoption high, value low." Secondary: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai (primary page timed out on bot fetch → figures from search-index summary; CONFIDENCE: Inferred, not rendered this run).

## 2. ADOPTION SCALE (primary anchor)

**ChatGPT weekly active users:**
- **800 million WAU** — announced by OpenAI CEO Sam Altman at OpenAI DevDay, San Francisco, **Oct 6, 2025**. (Also: 4M developers, 6B+ tokens/min via API.) Up from ~400M in Feb 2025.
- **900 million WAU** — OpenAI, **Feb 27, 2026** (blog post alongside funding round).
- Primary-ish: TechCrunch (Altman at DevDay) https://techcrunch.com/2026/02/27/chatgpt-reaches-900m-weekly-active-users ; DevDay report en.tempo.co https://en.tempo.co/read/2055387/openai-unveils-new-features-as-chatgpt-reaches-800-million-active-users ; TechCrunch on X https://x.com/TechCrunch/status/1975253231275040836
- CONFIDENCE: Verified this run (900M via TechCrunch fetch; 800M/DevDay/date via multiple sources). Note: these are company-reported figures (Altman/OpenAI), not audited third-party.

## 3. UP-FRONT ASSESSMENT / DELIBERATE APPROACH IMPROVES OUTCOMES

Best available evidence — McKinsey "State of AI 2025" (QuantumBlack):
- **Fundamental workflow redesign had the STRONGEST correlation with EBIT impact** out of ~25 organizational attributes McKinsey tested. Yet only ~21% of gen-AI users have redesigned any workflows; ~80% just layer AI on top of existing processes.
- **High performers (~6%)** are the ones who redesign workflows, target high-impact use cases, and put governance/human-in-the-loop in place; they report returns well above average.
- Governance angle: ~51% of firms report AI-related incidents; leaders manage risk with human-in-the-loop, centralized oversight, executive accountability. Fewer than ~25% have board-approved structured AI policies.
- Source: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- CONFIDENCE: Inferred from sources (primary page did not render on bot fetch; figures from search-index summaries of the McKinsey page + reputable recaps e.g. cxtoday, colabsoftware). Recommend the writer verify the exact "strongest correlation with EBIT / ~25 attributes / 21% redesigned workflows" wording against the live McKinsey page before quoting verbatim.
- Framing for the post: "the teams that see bottom-line impact are the ones who redesign the work and pick use cases deliberately — not the ones who bolt a chatbot on." Supported. A single clean "assessment → X% higher success" RCT-style stat does NOT exist; the honest version is the correlational McKinsey finding. See GAPS.

## 4. REAL-WORLD FAILURE EXAMPLES (non-coding; boundary/cost/risk misjudged)

1. **Air Canada chatbot (Feb 2024)** — BC Civil Resolution Tribunal held the airline liable after its support chatbot invented a bereavement-refund policy; ordered to pay Jake Moffatt ~C$812. Airline's "the bot is a separate legal entity" defense rejected. Boundary misjudged: no guardrails on a bot giving binding policy info; hidden liability cost. https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416 ; https://www.forbes.com/sites/marisagarcia/2024/02/19/what-air-canada-lost-in-remarkable-lying-ai-chatbot-case/ — CONFIDENCE: Verified this run.

2. **NYC "MyCity" business chatbot (Mar 2024)** — City's official small-business chatbot told users they could break the law (e.g., landlords could refuse Section 8, employers could take tips, businesses could refuse cash). Uncovered by The Markup; stayed live despite this. Boundary/risk misjudged: deployed a generative bot for regulatory advice with no accuracy guarantee. https://themarkup.org/artificial-intelligence/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law ; https://oecd.ai/en/incidents/2024-03-29-3dce — CONFIDENCE: Verified this run.

3. **DPD delivery chatbot (Jan 2024)** — After a system update, DPD's customer-service bot was coaxed into swearing and writing a poem calling DPD "the worst delivery firm in the world"; went viral, disabled. Boundary misjudged: no prompt-injection / behavior guardrails on a public-facing bot. https://www.bbc.co.uk/news (widely covered) — use ITV: https://www.itv.com/news/2024-01-19/dpd-disables-ai-chatbot-after-customer-service-bot-appears-to-go-rogue ; Time: https://time.com/6564726/ai-chatbot-dpd-curses-criticizes-company/ — CONFIDENCE: Verified this run.

4. **iTutorGroup — AI/automated hiring (EEOC settlement, Aug 2023)** — Recruiting software auto-rejected female applicants 55+ and male applicants 60+; 200+ qualified applicants rejected. First EEOC AI-hiring-bias settlement: $365,000 + 5-year consent decree. Risk misjudged: encoded age discrimination into automated screening → legal liability. https://www.eeoc.gov/newsroom/itutorgroup-pay-365000-settle-eeoc-discriminatory-hiring-suit — CONFIDENCE: Verified this run. (Note: 2023, slightly outside 2024-26 window, but named + legally settled — strong.)

5. **Australia "Robodebt" automated welfare debt scheme (2015–2019; Royal Commission report Jul 2023)** — Automated income-averaging system raised unlawful debts against welfare recipients; ~A$746M wrongfully recovered from ~381,000 people; scheme ruled unlawful; Royal Commission called it "crude, cruel and unlawful"; linked to serious harm. Boundary/cost misjudged: automated a legal determination the data couldn't support. https://lsj.com.au/articles/crude-cruel-and-unlawful-robodebt-royal-commission-findings/ ; https://www.bsg.ox.ac.uk/blog/australias-robodebt-scheme-tragic-case-public-policy-failure — CONFIDENCE: Verified this run. (Note: NOT GenAI and pre-2024 — rank lowest; use only if a "automation without judgment at scale, catastrophic cost" example is wanted.)

## GAPS / CAVEATS
- No clean experimental stat of the form "teams that run a feasibility/TCO/risk assessment succeed N% more often." Closest honest anchor is the McKinsey *correlational* workflow-redesign / high-performer finding (#3). Do not phrase it as causal proof.
- MIT PDF and McKinsey page did not render under bot fetch (403 / redirect / timeout). Both figures are corroborated by reputable secondaries; writer should open the primary URLs to confirm exact wording before quoting verbatim.
- All ChatGPT WAU and McKinsey EBIT figures are self-reported by the vendor/firm, not independently audited — state as "reported."
- iTutorGroup (2023) and Robodebt (2015-19) fall outside the 2024–2026 preference; the three chatbot cases (Air Canada, NYC MyCity, DPD) are all 2024 and cleanest for the "misjudged boundaries" hook.
