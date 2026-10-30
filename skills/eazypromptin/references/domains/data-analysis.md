# Domain: Data Analysis

## Applies when
Route here when the person wants to *understand* or *present* data: an answer, a report, a dashboard, a spreadsheet model or an Excel tool. Signals:
- Verbs: "evaluate", "analyse", "why did X drop", "compare", "report", "KPI", "build a dashboard", "Excel tool", "formula", "pivot", "visualise", "forecast".
- Artefacts: CSV/XLSX files, Google Sheets, database tables (Postgres, MySQL, BigQuery, Snowflake), exports from Shopify, Stripe, GA4, HubSpot, Lexoffice, DATEV, survey tools (Typeform, Google Forms).
- Tools: Excel, Google Sheets, Python/pandas/Polars, DuckDB, SQL, Jupyter, Power BI, Looker Studio, Metabase, Tableau, Streamlit, Evidence, Grafana.

Neighbouring domains and how to tell them apart:
- **Automation**: if the work is moving data on a schedule (sync, ETL), route there. If it is answering a question or building a view, stay here. A recurring report needs both: this playbook defines the analysis, automation defines how it refreshes.
- **Software / app**: a dashboard with logins, write-back and many users is an app. A read-only dashboard or an Excel tool with input cells is still data analysis.
- **Research**: research collects external information to support a decision; data analysis works on a dataset the person has (or can export). Market sizing from public stats can be either; ask whether a dataset exists.

## What people leave out
1. **The question behind the request.** "Analyse our sales" has no answer. Without a decision or question, the agent produces 15 charts nobody needs.
2. **Metric definitions.** "Revenue" gross or net, with or without refunds, by order date or payment date. Different definitions give different numbers and destroy trust.
3. **Granularity.** One row per order, per line item or per customer per day. Wrong grain leads to double counting.
4. **Data shape and quality.** Column names, date formats (01.02. vs 02/01), decimal commas, duplicates, test orders, missing months. The agent guesses and computes nonsense confidently.
5. **Time frame and comparison.** "Did it go up?" compared to what: last month, same month last year, a target?
6. **The audience and output.** A CFO needs one page with three numbers; an analyst wants a notebook; a team wants a live dashboard; a client wants an XLSX they can edit.
7. **Refresh cadence.** One-off vs weekly vs live changes the build from "a notebook" to "a pipeline".
8. **How to know it is right.** Without a reference number (the shop's admin total, last quarter's report), errors go unnoticed.

## Discovery map

### Phase 1: The question and the decision
- **Core question**: everything downstream is chosen to answer it. [Q]
  - "What do you want to know, or decide, once this is done?" Options: (a) describe what happened (status, trends), (b) explain why something changed (drill-down), (c) compare groups (products, channels, regions), (d) predict or plan (forecast, budget, scenario), (e) build a reusable tool (calculator, template, tracker). Default: ask for (a)-(e) plus one sentence.
  - Decide for me: infer from verbs; "why" → (b), "tool/template" → (e).
- **Decision it feeds**: separates useful analysis from decoration. [S]
  - "What will you do differently depending on the result?" Offer examples: cut a channel, reorder stock, change pricing, report to investors. If there is no decision, record "exploratory" as an assumption and keep the scope small.
- **Hypotheses**: speeds up drill-downs. [S]
  - "Any suspicion already?" Options: (a) yes (note them), (b) no, explore openly. Default: (b).
- **Anti-goals**: prevents overreach. [D]
  - Options: (a) no fancy statistics, just clear numbers, (b) no new tools, must stay in Excel, (c) no manual steps each month, (d) no raw personal data in the output. Default: (a).

### Phase 2: Data sources and shape
- **Sources**: the agent cannot analyse what it cannot reach. [Q]
  - "Where does the data live?" Options: (a) file(s) you can upload (CSV/XLSX), (b) Google Sheet, (c) database (which one, read access?), (d) SaaS export or API (Shopify, Stripe, GA4, HubSpot), (e) several of these that need joining. Default: (a) export a file for v1.
- **Shape and size**: decides tool choice. [S]
  - "Roughly how many rows and columns, and what is one row?" Options: (a) <10k rows, (b) 10k-1M, (c) >1M, (d) unknown. Default: ask for a sample of 20 rows or the header row. Rule: always request a sample before building.
- **Granularity (grain)**: avoids double counting. [S]
  - Use **this-or-that**: "one row per order or per line item?", "per day or per transaction?". Default: the finest grain available, aggregated in the analysis.
- **Joins and keys**: multi-source analysis breaks on keys. [D]
  - "How do the sources connect?" Options: (a) shared ID (order ID, customer ID), (b) email/name (fuzzy), (c) date only, (d) not sure. Default: (a); flag (b)/(d) as a risk.
- **Data quality known issues**: the person usually knows the landmines. [S]
  - Options: (a) test/internal orders mixed in, (b) duplicates, (c) currency or VAT mix, (d) missing periods, (e) manual edits in the sheet. Default: assume (a)+(b) exist and check for them.

### Phase 3: Metrics, definitions and cleaning
- **Metric list**: what exactly gets computed. [Q]
  - Draft 3-5 candidate metrics from the question and let them pick, for example revenue, orders, AOV, conversion rate, churn, CAC, margin, retention by cohort.
- **Definitions**: the single biggest source of disagreement. [S]
  - For each metric, offer **this-or-that**: gross vs net, incl. vs excl. refunds/VAT/shipping, order date vs paid date, active = logged in vs paid. Default: net of refunds, excl. VAT, by order date; record as assumptions.
- **Time frame and comparison**: gives numbers meaning. [Q]
  - Options: (a) last 30 days vs previous 30, (b) month over month for the last 12 months, (c) year over year, (d) against a target/budget, (e) custom range. Default: (b).
- **Segments**: the cut that answers "why". [S]
  - Options: channel, product/category, region, customer type (new/returning), cohort (signup month), device. Default: pick the 2 most relevant to the question.
- **Cleaning rules**: must be explicit and reproducible. [D]
  - Options: (a) drop test orders by rule (email domain, flag), (b) dedupe on ID, (c) normalise dates/decimals (German formats), (d) cap or flag outliers, (e) leave raw, report issues only. Default: (a)-(c), log how many rows each rule removed.
- **Statistics level**: avoid both naivety and overkill. [D]
  - Options: (a) descriptive only, (b) plus simple significance check for comparisons/A-B tests, (c) regression/forecast (Prophet, linear trend, ETS), (d) clustering/segmentation. Default: (a); (b) when comparing groups with small numbers.

### Phase 4: Output and audience
- **Audience**: decides density and vocabulary. [Q]
  - Options: (a) just me, (b) my boss/management, (c) a client, (d) a team using it daily, (e) investors/public. Default: (a).
- **Output format**: the deliverable itself. [Q]
  - Options: (a) short written answer with 1-3 charts, (b) XLSX with clean tables, pivots and charts, (c) interactive HTML dashboard (single file), (d) BI dashboard (Looker Studio, Metabase, Power BI), (e) notebook (Jupyter) with code, (f) Excel tool with input cells, formulas and protected sheets. Default: (a) for one-off questions, (b) for anything shared in an office context.
- **Chart and table choices**: prevents chart junk. [S]
  - Offer defaults: line for trends over time, bar for category comparison, table for exact values, cohort heatmap for retention. Ask: "Few key numbers with explanation, or detailed tables?" Default: few key numbers plus one chart per question, details in an appendix tab.
- **Language and formatting**: small details that matter to readers. [D]
  - Options: German number format (1.234,56 EUR), English, both. Default: match the person's language and locale.
- **Excel tool specifics** (if (f)): tools live or die on usability. [S]
  - Ask: who fills it in, which cells are inputs, should formulas be locked, is VBA/macros allowed or formulas only (XLOOKUP, LET, LAMBDA, dynamic arrays), must it work in older Excel or Google Sheets? Default: formulas only, no macros, inputs highlighted, other sheets protected without password.

### Phase 5: Production
- **Refresh cadence**: one-off vs recurring is an architecture decision. [S]
  - Options: (a) one-off, (b) I re-run it manually monthly with a new export, (c) scheduled automatic refresh, (d) live. Default: (a); for (b) make the process "drop new file, run one command"; for (c)/(d) pull in the automation playbook.
- **Validation reference**: proves the numbers. [Q]
  - "Is there a number we can check against?" Options: (a) shop/admin total for a month, (b) last official report, (c) accountant's figures, (d) none. Default: (a); with (d), cross-check totals two different ways.
- **Privacy**: personal data in analysis files spreads easily. [D]
  - Options: (a) fine, internal only, (b) pseudonymise customer data, (c) aggregate only in outputs. Default: (c) for anything shared.
- **Tooling for the agent**: what the agent can run. [S]
  - Options: (a) Python + pandas/Polars + matplotlib/Plotly, (b) DuckDB SQL on files, (c) direct SQL on the DB, (d) Excel/Sheets formulas only. Default: (a) or (b) to compute, export to the chosen output.
- **Scope, milestones, verification**: wrap up per the universal brief.

## Inspiration anchors
Use **reference anchors** the person knows: "like the Shopify Analytics overview, but for our margins", "a Stripe-style MRR chart", "a GA4 funnel", "one-page board report", "a Looker Studio dashboard with date filter", "an Excel calculator like a gross-to-net salary calculator".

Pitch-sampler seeds:
1. **One-pager**: three headline numbers, one trend chart, three bullet explanations of what moved and why.
2. **Drill-down**: start from "revenue down 12%", decompose by channel, product and new vs returning until the driver is found.
3. **Monthly report pack**: XLSX with a summary tab, one tab per area, charts, notes; rebuildable from a fresh export with one command.
4. **Live dashboard**: Looker Studio or Metabase on the DB/Sheet, filters for date and channel, 6-8 tiles maximum.
5. **Excel tool**: input sheet, calculation sheet, output sheet with chart; locked formulas, validation dropdowns, clear instructions tab.
6. **Cohort/retention view**: signup-month cohorts, retention heatmap, a short explanation of what healthy looks like.

## Smart defaults
When the person says "no idea" or "decide for me":
- Question type: descriptive trend plus the top 2 drivers.
- Time frame: last 12 months by month, with the latest month vs previous and vs same month last year.
- Definitions: net revenue excl. VAT and refunds, by order date; test orders and duplicates removed; every rule logged.
- Tool: Python with pandas (or DuckDB for larger files) to compute; output as XLSX plus a short written summary with 2-3 charts.
- Presentation: few key numbers and plain-language explanation of what drives them; details in appendix tables. No dashboards of 20 tiles.
- Locale: the person's language and number format.
- Validation: reconcile one monthly total against the source system.
Why: this answers most "analyse my data" requests, is cheap to redo with a new export, and keeps definitions visible so the numbers can be trusted.

## Scope traps
- **Chart soup**: 20 charts with no conclusion. Constraint: every chart must answer a named question; max 5 in v1.
- **Dashboard before the analysis**: building a live dashboard for metrics nobody has defined yet. Constraint: one-off analysis first, dashboard only for metrics that proved useful.
- **Endless cleaning**: messy data becomes a project of its own. Constraint: timebox cleaning, document known issues, report with caveats.
- **Definition drift**: different tabs compute "revenue" differently. Constraint: one definitions block, referenced everywhere.
- **Excel tool scope creep**: "and it should also send mails and have a login". Constraint: Excel tools stay calculators; anything beyond goes to software or automation.
- **False precision**: forecasts with two decimals on six data points. Constraint: show ranges and state sample size.

## Brief sections
Add to the universal brief:
- **Question & decision**: the core question, the decision it informs, hypotheses.
- **Data inventory**: each source, location, access method, row grain, size, sample attached or pending.
- **Metric dictionary**: each metric with formula, inclusions/exclusions, date basis.
- **Cleaning log rules**: filters, dedupe keys, format normalisation, outlier policy.
- **Segments & time frame**: dimensions to cut by, periods, comparison baseline.
- **Output spec**: format, sections/tabs, chart list (chart type + question it answers), locale.
- **Refresh & reproducibility**: one-off or recurring, how to rerun, where code lives.
- **Validation references**: known totals to reconcile against.

## Milestones
- **M0 Access & sample**: data loaded, schema printed. Done when: row count, columns, types and date range are reported and match the person's expectation.
- **M1 Profiling & cleaning**: quality report and cleaning rules applied. Done when: a cleaning log lists rows removed per rule and remaining issues.
- **M2 Metrics**: metric dictionary implemented. Done when: one monthly total reconciles with the reference within an agreed tolerance (e.g. 0.5%).
- **M3 Core analysis**: answers to the core question with segments. Done when: each question in the brief has a number, a chart or table and a one-sentence takeaway.
- **M4 Output build**: XLSX/dashboard/tool in its final shape. Done when: it opens without errors, formats follow locale, charts are labelled with units and periods.
- **M5 Review & polish**: summary written for the audience, caveats listed. Done when: the person can read the summary in 2 minutes and the open questions list is empty or accepted.
- **M6 Rerun path** (if recurring): Done when: dropping a new export and running one command (or pressing refresh) reproduces the output for the new period.

## Verification
- **Reconciliation**: compare at least one aggregate against the source system or an existing report; state the difference.
- **Two-way totals**: compute totals from detail rows and from grouped results; they must match.
- **Row accounting**: input rows = kept rows + removed rows per cleaning rule.
- **Grain check**: assert uniqueness of the key at the intended grain (e.g. order ID unique in the orders table).
- **Spot check**: pick 3 random records and trace them by hand through the calculation.
- **Sanity bounds**: no negative counts, rates within 0-100%, dates within range, no sudden zero months without explanation.
- **Excel tools**: test inputs with known expected outputs (including edge values: 0, empty, very large); formulas show no #REF!/#N/A; protected cells cannot be edited; works in the target Excel version.
- **Dashboards**: filters change all tiles consistently; numbers match the analysis for the same period.
- Acceptance criteria pattern: "For [period], [metric] equals [reference] within [tolerance], and the summary answers [question] in plain language."

## Example opening
Request (~30 words):
> "got a csv export from our shopify store covering last year. can you analyse it and show me what's working and what isn't, maybe as an excel file or a dashboard?"

Deep-mode round-1 reply excerpt:
> Got it: you have a Shopify CSV export covering one year and want to see what's working and what isn't, delivered as an Excel file or a dashboard.
>
> Three possible directions, pick one or mix:
> - **A One-pager:** three key numbers (revenue, orders, average order value), a 12-month trend, plus a short explanation of what moved.
> - **B Product check:** which products and categories carry the revenue, which ones are shelf warmers, where it is declining.
> - **C Customer view:** new vs returning customers, repeat purchase rate, how long customers stick around.
>
> 1. **Which decision should this support?** (a) trim the product range, (b) allocate the marketing budget, (c) just an overview for the team **(recommended, if still open)**, (d) numbers for a bank or investor
> 2. **How do we count revenue?** (a) net excl. VAT, refunds deducted, by order date **(recommended)**, (b) gross, as in the Shopify dashboard, (c) both side by side
> 3. **What is one row in the export?** (a) one order, (b) one line item per order, (c) not sure, then just send me the first 20 rows **(recommended)**
> 4. **Output:** (a) Excel with an overview tab and details **(recommended)**, (b) interactive HTML dashboard, (c) Looker Studio, (d) short written answer with 2 or 3 charts
> 5. **Do we have a reference number?** For example the annual revenue from the Shopify admin. Then I can check that my numbers are right.
>
> A short answer is enough, e.g. "A+B, 1a 2a 3c 4a". Or "decide for me", and I'll take the recommendations and note them as assumptions.
