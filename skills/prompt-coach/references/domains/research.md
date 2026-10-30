# Domain: Research & Decision Support

## Applies when
Route here when the person needs *information gathered and weighed* so they can decide or understand something. Signals:
- Phrases: "which X should I pick", "compare", "what alternatives are there", "market analysis", "competitors", "state of the research", "literature review", "is it worth it", "pros and cons", "best practice for".
- Types: tech/tool comparison (framework, database, hosting, SaaS), market research and sizing, competitor analysis, literature review (academic), vendor/product selection, due diligence, regulation lookup (GDPR, AI Act, tax rules), trend scan.
- Tools the agent may use: web search, deep-research modes, Google Scholar, Semantic Scholar, arXiv, PubMed, company registers (Handelsregister, Crunchbase, North Data), G2/Capterra, GitHub stats, official docs and pricing pages.

Neighbouring domains and how to tell them apart:
- **Data analysis**: if the person has a dataset and wants insight from it, route there. Research gathers external evidence.
- **Writing / content**: if the end product is a polished article or thesis chapter for readers, the research is a phase; ask whether they need the evidence base or the finished text. This playbook covers the evidence and the recommendation.
- **Automation**: "every week, scan for new competitors" is automation with a research step; define the research criteria here, the schedule there.

## What people leave out
1. **The decision the research serves.** "Compare Supabase and Firebase" without saying for what project, team and budget yields a generic blog post.
2. **Criteria and their weights.** Price, speed, lock-in, learning curve. Without weights, every option "has pros and cons" and no recommendation comes out.
3. **Hard constraints (knock-outs).** EU hosting, must support German, budget cap, existing stack. Missing knock-outs waste half the comparison on options that were never possible.
4. **Recency.** Pricing, model capabilities and library versions change monthly; a 2023 source can be flat wrong in 2026.
5. **Allowed sources and quality bar.** Peer-reviewed only? Official docs over blog posts? Vendor marketing counts or not?
6. **Depth and size.** 3 options in 10 minutes or 15 options with a scoring matrix. People mean very different things by "look into it".
7. **How to handle uncertainty.** Whether to mark guesses, show confidence, cite every claim. Without this, hallucinated facts look as solid as verified ones.
8. **Output format.** A one-line recommendation, a comparison table, a memo, an annotated bibliography.

## Discovery map

### Phase 1: The decision and the why
- **Decision or purpose**: the lens for everything that follows. [Q]
  - "What will you decide or do with the result?" Options: (a) pick one option (tool, vendor, approach), (b) go / no-go on an idea, (c) understand a market or field before planning, (d) write something academic (thesis, paper) that needs sources, (e) prepare for a meeting or pitch. Default: ask for (a)-(e) plus the context sentence.
  - Decide for me: "which/should I" → (a); "is it worth it" → (b); "state of the research" → (d).
- **Context**: the same question has different answers for different situations. [Q]
  - Ask for the project, team size, skill level, existing stack, budget. Offer a fill-in line: "for [project], [team], [budget], [existing stack]".
- **Deadline and stakes**: decides depth. [S]
  - Options: (a) quick gut check, reversible decision, (b) matters for months, (c) expensive or hard to reverse (contracts, architecture, thesis direction). Default: (b).
- **Anti-goals**: keeps the output usable. [S]
  - Options: (a) no generic listicle, (b) no options I can't afford/use, (c) no recommendation without sources, (d) no marketing fluff. Default: (a)+(c).

### Phase 2: Options and criteria
- **Option set**: what is in the comparison. [Q]
  - Options: (a) I have a shortlist (name it), (b) find the main candidates, (c) shortlist plus "anything I'm missing", (d) open field scan. Default: (c), capped at 3-5 options.
- **Knock-out constraints**: removes impossible options early. [Q]
  - Offer typical ones: EU/GDPR hosting, budget cap per month, open source / self-hostable, language support (German), must integrate with X, licence (MIT vs AGPL vs commercial), company size or maturity. Default: ask which apply; record none as an assumption.
- **Criteria**: what "better" means here. [S]
  - Draft 4-7 criteria for the domain and let them pick. Examples: tech choice → DX, performance, ecosystem, lock-in, cost at scale, maturity; vendor → price, support, contract terms, integrations; market → size, growth, competition, entry barriers.
- **Weights**: turns a comparison into a recommendation. [S]
  - Options: (a) rank top 3 criteria, (b) assign must/should/nice, (c) numeric weights summing to 100, (d) decide for me. Default: (b). Decide for me: infer from context (solo dev → DX and cost heavy; company → support and compliance heavy).
- **This-or-that calibration**: reveals hidden priorities fast. [D]
  - Pairs like "cheaper but more setup vs pricier but turnkey", "popular and boring vs new and promising", "managed vs self-hosted".

### Phase 3: Sources, recency and depth
- **Allowed sources**: sets the quality bar. [S]
  - Options: (a) official docs, pricing pages and changelogs first, (b) plus reputable tech press, benchmarks and community (GitHub issues, Reddit, HN) for real-world experience, (c) peer-reviewed literature only, (d) market data (Statista, public filings, registers, analyst reports), (e) anything, but mark the source type. Default: (a)+(b) for tech/tools, (c) for academic, (d) for market.
- **Recency window**: stale facts are the most common error. [Q]
  - Options: (a) last 6 months, (b) last 12 months, (c) last 3 years, (d) timeless/foundational allowed. Default: (b) for tools, pricing, AI models; (c) for academic with classics allowed.
  - Rule: prices, limits and versions must come from a source dated within the window, with the date shown.
- **Depth**: matches effort to stakes. [Q]
  - Options: (a) quick: 3 options, short table, 1 recommendation, (b) standard: 3-5 options, weighted matrix, memo, (c) deep: systematic search, 5-10 options or 20+ papers, evidence table, risk analysis, (d) proof: hands-on test or prototype of the top 2. Default: (b).
- **Geography and language**: markets and regulation differ. [D]
  - Options: (a) Germany/DACH, (b) EU, (c) US, (d) global. Sources in German, English, both. Default: the person's market, sources in both languages.
- **Academic specifics** (if (d) in Phase 1): needed for citations to hold up. [S]
  - Ask: citation style (APA 7, IEEE, Harvard, DIN ISO 690), databases, inclusion/exclusion criteria, years, whether a PRISMA-style search log is needed. Default: APA 7, Google Scholar + Semantic Scholar, last 10 years, search log included.

### Phase 4: Uncertainty and output
- **Citation rule**: makes the output checkable. [S]
  - Options: (a) every factual claim linked inline, (b) sources list per section, (c) only for numbers and key claims. Default: (a) for decisions with stakes, (c) for quick checks.
- **Uncertainty handling**: separates facts from estimates. [S]
  - Options: (a) mark each claim as verified / reported / estimate, (b) confidence level per conclusion (high/medium/low), (c) list "unknowns" separately, (d) all of these. Default: (b)+(c). Rule: never fill a gap with a plausible guess; write "not found" and suggest how to find out.
- **Conflicting sources**: common in benchmarks and pricing. [D]
  - Options: (a) show both with dates and context, (b) prefer the primary source, (c) flag and ask me. Default: (a)+(b).
- **Output format**: the artefact the person actually uses. [Q]
  - Options: (a) short answer: recommendation plus 3 reasons and the main trade-off, (b) comparison table plus 1-page memo, (c) decision memo (context, options, criteria, scoring, recommendation, risks, next steps), (d) annotated bibliography / literature matrix, (e) slide-ready summary. Default: (a) for quick, (c) for stakes.
- **Recommendation strength**: some people want a verdict, some just the facts. [S]
  - Options: (a) commit to one pick with reasoning, (b) pick per scenario ("if X then A, if Y then B"), (c) no recommendation, neutral comparison. Default: (a), with a runner-up and the condition that would flip it.

### Phase 5: Production
- **Validation step**: research can be wrong in confident ways. [S]
  - Options: (a) re-check every price and limit against the vendor page, (b) second pass looking for counter-evidence, (c) hands-on test of the top pick, (d) expert/peer review by the person. Default: (a)+(b).
- **Follow-up and shelf life**: decisions get revisited. [D]
  - Options: (a) one-off, (b) note when to re-check (e.g. pricing in 6 months), (c) recurring scan (hand to automation). Default: (a) plus a "valid as of" date.
- **Agent capabilities**: what the agent can actually access. [S]
  - Confirm web access, paywalled sources (none unless the person provides PDFs), and whether the agent may run code to test libraries. Record limits as assumptions.
- **Scope, milestones, verification**: wrap up per the universal brief.

## Inspiration anchors
Offer **reference anchors** as formats the person recognises: "a Wirecutter-style 'our pick, runner-up, budget pick'", "a ThoughtWorks Tech Radar entry (adopt/trial/assess/hold)", "an Amazon-style 6-page decision memo", "a G2 grid but with your criteria", "a systematic review's evidence table", "a YC-style market map".

Pitch-sampler seeds:
1. **Verdict card**: one pick, one runner-up, one budget option, each with "choose this if...", sources linked, valid-as-of date.
2. **Weighted matrix**: 4-5 options x 6 criteria, weights agreed upfront, scores with a source per cell, sensitivity note ("if cost matters more, B wins").
3. **Decision memo**: context, knock-outs, shortlist, scoring, risks, reversibility, next step (often: build a 1-day spike with the top pick).
4. **Market snapshot**: market size estimate with method, 8-12 competitors mapped by price and segment, gaps worth attacking.
5. **Literature map**: 15-30 papers clustered by theme, a matrix (question, method, finding, limitation), research gap paragraph.
6. **Spike plan**: desk research narrows to two; then a hands-on prototype test with defined pass/fail checks decides.

## Smart defaults
When the person says "decide for me":
- Purpose: pick one option for their stated context.
- Options: their shortlist plus up to 2 serious alternatives they missed, max 5 total.
- Criteria: 5, weighted must/should/nice, inferred from context (solo builder → cost, DX, lock-in, maturity, docs quality).
- Sources: official docs/pricing/changelogs first, then community experience; vendor marketing only for features, never for comparisons.
- Recency: last 12 months for anything that changes (prices, limits, versions, AI models); every price shows its date.
- Uncertainty: confidence per conclusion, separate "unknowns" list, no guessed facts.
- Output: committed recommendation with runner-up and the condition that would flip it, a compact comparison table, sources inline.
- Validation: re-check every number against its primary source before handing over.
Why: this gives a decision rather than a listicle, stays checkable, and fails visibly instead of confidently.

## Scope traps
- **Boiling the ocean**: "compare all CRMs". Constraint: knock-outs first, then cap at 5 options.
- **Analysis paralysis**: more research instead of deciding. Constraint: agree upfront what result would end the research, and default to a cheap hands-on test for reversible decisions.
- **Criteria shopping**: changing weights after seeing scores to justify a favourite. Constraint: lock weights before scoring; show a sensitivity note instead.
- **Stale facts**: training-data knowledge presented as current. Constraint: everything time-sensitive needs a dated source from the window.
- **Citation theatre**: links that do not support the claim, or invented papers. Constraint: each cited source must be opened and the supporting passage quoted or summarised; DOIs checked for academic work.
- **Context-free answers**: "it depends" without saying on what. Constraint: always end with a scenario rule or a committed pick.

## Brief sections
Add to the universal brief:
- **Decision statement**: the decision, context, stakes and deadline in two sentences.
- **Options & knock-outs**: candidate list, hard constraints, options excluded and why.
- **Criteria & weights**: each criterion with definition, weight and how it is measured.
- **Source policy**: allowed source types, priority order, recency window, languages, paywall limits.
- **Uncertainty & citation rules**: citation style, confidence labels, how conflicts and gaps are reported.
- **Output spec**: format, length, sections, recommendation strength.
- **Validation plan**: what gets re-checked and how (price re-check, counter-evidence pass, spike test).

## Milestones
- **M0 Framing**: decision statement, knock-outs, criteria and weights locked. Done when: the person confirms them in one line.
- **M1 Landscape scan**: long list gathered and knock-outs applied. Done when: a list exists with each excluded option and its reason.
- **M2 Evidence collection**: facts per option per criterion with dated sources. Done when: every cell in the matrix has a value or "not found" plus a source.
- **M3 Scoring & synthesis**: weighted scores, trade-offs, sensitivity note. Done when: the recommendation follows from the scores and the flip condition is stated.
- **M4 Validation**: re-check numbers, counter-evidence pass, optional spike. Done when: a validation log lists each checked claim and any corrections.
- **M5 Deliverable**: memo/table/bibliography in the agreed format. Done when: it fits the agreed length, every claim with stakes is cited, and the "valid as of" date is set.

## Verification
- **Source audit**: sample 5 claims at random; each link opens and supports the claim; dates are inside the recency window.
- **Number re-check**: every price, limit or benchmark matches its primary source on the day of delivery.
- **Knock-out check**: no recommended option violates a hard constraint.
- **Consistency**: recommendation matches the weighted scores; if not, the memo explains why.
- **Counter-evidence**: at least one search for "problems with / migrating away from [top pick]" was run and summarised.
- **Academic**: DOIs resolve, citation style is consistent, inclusion/exclusion criteria applied as stated, search log reproducible.
- **Spike test** (if agreed): defined pass/fail checks run on the top 1-2 options with results recorded.
- Acceptance criteria pattern: "Given [context and knock-outs], the deliverable recommends [one option] with [runner-up], every key claim has a dated source, and unknowns are listed."

## Example opening
Request (~30 words):
> "need to pick a backend for my new app, supabase, firebase or just build something myself with nestjs and postgres. can you research it and tell me what actually makes sense?"

Deep-mode round-1 reply excerpt:
> Got it: you want a well-founded decision between Supabase, Firebase and your own backend with NestJS and Postgres for your new app, ending in a clear recommendation.
>
> Here's what the result could look like, pick one:
> - **A Verdict:** one clear recommendation, a runner-up, three reasons each, sources linked.
> - **B Matrix:** the three options against 5 or 6 weighted criteria, with a note on when the result flips.
> - **C Memo plus test:** research narrows it down to two, then a small prototype with login and one table makes the call.
>
> 1. **What kind of app?** (a) web app, (b) mobile with React Native or Flutter, (c) both, (d) describe it briefly and I'll infer the rest **(recommended)**
> 2. **What are the knock-out criteria?** (a) EU hosting because of GDPR **(recommended to check)**, (b) budget under 25 EUR per month at the start, (c) no vendor lock-in, (d) none
> 3. **What matters most?** (a) going live fast, (b) cost as you grow, (c) full control and flexibility, (d) decide for me based on your context
> 4. **Sources and freshness:** (a) official docs and pricing pages from the last 12 months, plus experience reports from the community **(recommended)**, (b) official sources only
> 5. **How committed should the recommendation be?** (a) a clear pick with the condition under which the other would be better **(recommended)**, (b) a recommendation per scenario, (c) a neutral comparison without a verdict
>
> A short answer is enough, e.g. "B, 1b 2a 3a 4a 5a". Or "decide for me", and I'll take the recommendations and note them as assumptions.
