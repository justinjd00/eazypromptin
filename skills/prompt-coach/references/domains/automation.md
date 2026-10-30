# Domain: Automation

## Applies when
Route here when the request is about making something happen *without a person doing it by hand*, repeatedly or on an event. Signals:
- Tools: n8n, Make (Integromat), Zapier, Pipedream, Power Automate, Activepieces, GitHub Actions, cron, systemd timers, Airflow, Temporal, Trigger.dev, Inngest, Windmill.
- Verbs: "automatically", "every morning", "if X then Y", "sync", "scrape", "forward", "monitor", "notify", "pipeline", "bot", "agent that checks...".
- Artefacts: webhooks, API keys, Google Sheets as a database, inbox rules, CRM records (HubSpot, Pipedrive, Salesforce), Slack/Teams/Telegram messages, RSS feeds, CSV exports.
- AI pipelines: "LLM classifies incoming mails", "agent researches leads and writes drafts", RAG ingestion jobs, MCP-tool chains.

Neighbouring domains and how to tell them apart:
- **Software / app** (a product with users and a UI): if the person wants a dashboard, accounts or a frontend that others use, it is an app with automation inside. If the output is a side effect (a mail sent, a row written), stay here.
- **Data analysis**: if the goal is an insight or report, route to data-analysis; if the goal is *moving or transforming* data on a schedule (ETL, sync), stay here. A scheduled report touches both: the analysis defines *what*, this playbook defines *how it runs*.
- **Research**: a one-off "find me 50 competitors" is research. "Every Monday, find new competitors and post them to Slack" is automation with a research step.

## What people leave out
1. **The trigger.** "Automate my invoices" without saying whether it starts on a new mail, a schedule, a form or a button click. Guessing wrong means the flow never fires or fires on everything.
2. **What happens on failure.** Without an error path, the first API hiccup silently drops records and nobody notices for weeks.
3. **Duplicates and re-runs (idempotency).** Retries and overlapping runs create double invoices, double mails, double CRM contacts.
4. **Credentials and access.** Which account, which scopes, who owns the API key. The agent cannot log into your Gmail; it needs an OAuth app, an app password or a service account, and you have to provide it.
5. **Volume and rate limits.** 20 items a day and 20,000 items a day are different architectures. Free tiers of Zapier/Make count tasks/operations and run out fast.
6. **Where it runs and who pays.** n8n Cloud vs self-hosted on a VPS vs a laptop cron job that stops when the lid closes.
7. **Human approval points.** Sending mails to customers or changing CRM deals without review is risky; people assume "of course I check first" but never say it.
8. **The real edge cases.** Attachments missing, mails in English instead of German, a scraped site changing its HTML. Without examples, the agent builds for the happy path only.

## Discovery map

### Phase 1: Goal and the manual baseline
- **Job to be done**: anchors everything; an automation replaces a concrete manual routine. [Q]
  - "What do you do by hand today that this should take over?" Options: (a) copy data between two tools, (b) react to incoming mails/forms, (c) produce something on a schedule (report, digest, backup), (d) watch something and alert me (prices, websites, errors), (e) multi-step AI work (research, classify, draft). Default: ask for (a)-(e) plus one sentence.
  - Decide for me: infer from the request's verbs and record as an assumption.
- **Current effort and pain**: tells you how robust it must be and whether it is worth building. [S]
  - "How often and how long?" Options: (a) a few times a week, minutes each, (b) daily, ~30 min, (c) many times a day, hours total, (d) it does not happen today because it is too much work. Default: (b).
- **Success picture**: defines done. [Q]
  - Use a **scenario walkthrough**: "Monday 8:00, a new lead fills the form. 30 seconds later... what should exist where?" Offer a filled-in draft for them to correct.
- **Anti-goals**: prevents dangerous overreach. [S]
  - "What must it never do?" Options: (a) never send anything externally without my OK, (b) never delete data, (c) never touch existing records, only add, (d) never cost more than X per month. Default: (a)+(b).

### Phase 2: Trigger and inputs
- **Trigger type**: decides architecture and hosting. [Q]
  - Options: (a) schedule (cron: hourly, daily 07:00, weekly), (b) event via webhook (form submit, Stripe event, GitHub push), (c) polling a source (new mail, new row, RSS), (d) manual button / chat command, (e) another automation. Default: (b) if the source offers webhooks, else (a) daily.
  - Decide for me: prefer webhooks over polling; polling every 15 min is the fallback.
- **Input shape**: the agent needs real examples to parse correctly. [S]
  - "Paste or describe 2-3 real inputs, including one ugly one." Options: (a) structured (JSON, form fields, CSV), (b) semi-structured (mails with a pattern, PDFs from one vendor), (c) unstructured (free text, varied PDFs, web pages). Default: ask for samples; if none, mark "sample inputs" as an open question.
- **Volume**: drives rate limits, cost and tool choice. [S]
  - Options: (a) <50 items/day, (b) 50-1,000/day, (c) 1,000-50,000/day, (d) bursts (e.g. 5,000 at month end). Default: (a).
- **Latency**: real-time vs batch changes everything. [D]
  - Options: (a) seconds, (b) within 15 min, (c) once a day is fine. Default: (b).

### Phase 3: Steps, systems and credentials
- **Step list**: the skeleton of the flow. [Q]
  - Draft it yourself from what you heard (trigger, fetch, transform, decide, write, notify) and ask them to correct. Use **this-or-that** for unclear steps: "update existing contact or always create new?"
- **Systems involved**: each one needs auth and has quirks. [S]
  - "Which tools does it read from and write to?" Offer typical combos: Gmail/Outlook, Google Sheets/Airtable/Notion, HubSpot/Pipedrive, Slack/Teams/Telegram, Stripe/Lexoffice/sevDesk, Shopify/WooCommerce, OpenAI/Anthropic API, Postgres/Supabase.
- **Credentials and ownership**: blocks the agent if missing. [S]
  - Options: (a) I have API keys / can create them, (b) needs OAuth app setup (Google, Microsoft), (c) company account, IT must approve, (d) no API at all, needs browser automation. Default: (a); flag (b)-(d) as risks in the brief.
  - Rule for the agent: secrets go in env vars or the tool's credential store, never in code or the brief.
- **Platform choice**: the biggest fork. [Q]
  - Options: (a) **n8n** (self-host or cloud; visual, code nodes, good AI nodes, cheap at volume), (b) **Make** (visual, strong for SaaS glue, ops-based pricing), (c) **Zapier** (easiest, most integrations, expensive at volume), (d) **code**: Python or TypeScript script with cron/GitHub Actions/a small worker (full control, versioned, testable), (e) durable workflow engine (Temporal, Inngest, Trigger.dev) for long-running or AI-agent jobs. Default: (a) n8n for SaaS glue with an agent helping; (d) code when logic is heavy or the person is a developer.
  - Decide for me: developer + >3 branching rules → code; non-developer + standard SaaS → n8n Cloud or Make.
- **AI steps** (if any): model behaviour needs a spec, not a vibe. [S]
  - "What does the AI decide or write?" Options: (a) classify/route (fixed labels), (b) extract fields to JSON, (c) draft text for review, (d) autonomous agent with tools. Default: (a)/(b) with a JSON schema; avoid (d) unless they insist, and then add a human checkpoint.

### Phase 4: Reliability
- **Error handling**: the difference between a demo and something you can trust. [S]
  - Options: (a) retry 3x with backoff, then alert me, (b) push failures to a dead-letter sheet/queue for manual review, (c) stop the whole run, (d) skip and log. Default: (a)+(b).
- **Idempotency and duplicates**: retries must not double-act. [S]
  - "How do we recognise an item we already processed?" Options: (a) source ID (message-id, order ID), (b) hash of key fields, (c) a "processed" label/flag in the source, (d) a state table. Default: (a) stored in a small state table or sheet.
- **Rate limits and quotas**: APIs throttle; scrapers get blocked. [D]
  - Ask what plan they are on; default to batching, backoff on 429, and concurrency 1-3. For scraping: respect robots.txt and ToS, prefer official APIs, cache pages, add delays.
- **Human-in-the-loop**: where a person approves. [S]
  - Options: (a) none, fully automatic, (b) approve via Slack/Telegram button before external actions, (c) drafts land in a folder/inbox for review, (d) daily summary to spot-check. Default: (c) for anything customer-facing, (a) for internal syncs.
- **Logging and monitoring**: you need to know it ran. [D]
  - Options: (a) the platform's execution log is enough, (b) a run log sheet/table (time, items, errors), (c) alert on failure to Slack/mail, (d) heartbeat check (healthchecks.io, Uptime Kuma) that alerts when it did *not* run. Default: (a)+(c), add (d) for cron jobs.

### Phase 5: Production
- **Hosting**: where it lives decides uptime and cost. [S]
  - Options: (a) SaaS platform (Zapier/Make/n8n Cloud), (b) VPS with Docker (Hetzner, Netcup, ~5-10 EUR/month) running n8n or scripts, (c) serverless/cron (GitHub Actions schedule, Cloudflare Workers Cron, Vercel Cron, Supabase Edge Functions), (d) local machine. Default: (a) for non-devs, (b) or (c) for devs. Warn against (d) for anything important.
- **Budget**: tasks and LLM tokens add up. [S]
  - Options: (a) free tiers only, (b) up to 20 EUR/month, (c) up to 100 EUR/month, (d) cost is secondary. Default: (b). Do a quick estimate: items/day x steps x price.
- **Data and compliance**: personal data in automations triggers GDPR duties. [D]
  - Ask whether personal data flows through US SaaS or LLM APIs; options: (a) fine, (b) EU hosting required, (c) no personal data may leave our systems. Default: (a) for personal projects, (b) for client work in the EU.
- **Ownership and handover**: who maintains it when it breaks. [D]
  - Options: (a) me, (b) a client, needs docs, (c) a team. Default: (a); with (b) add a runbook milestone.
- **Scope, milestones, verification**: wrap up per the universal brief.

## Inspiration anchors
Offer **reference anchors** as recognisable patterns, not brands: "the Zapier classic: form to CRM to Slack", "Gmail + LLM triage like Superhuman's auto labels", "Changedetection.io-style site watcher", "n8n AI agent template: lead research to drafted mail", "GitHub Actions nightly job".

Pitch-sampler seeds (turn into 2-4 one-line mini-pitches):
1. **Inbox triage**: new mail, LLM classifies (lead / invoice / support / spam), labels it, invoices go to accounting folder, leads to CRM, daily digest in Telegram.
2. **Lead pipeline**: form or LinkedIn export, enrich (website, size), score, create CRM contact, AI drafts first mail into drafts folder for approval.
3. **Watcher**: check 20 URLs every hour for price or content changes, diff, alert only on real changes.
4. **Weekly report bot**: Monday 07:00 pull numbers from Stripe/Analytics/Sheets, build summary, post to Slack and archive as PDF.
5. **Document intake**: PDFs dropped in a folder, extract fields to JSON, validate, write to sheet/ERP, flag low-confidence ones for review.
6. **Sync job**: keep two systems consistent (Shopify orders to Lexoffice invoices) with a nightly reconciliation report.

## Smart defaults
When the person says "decide for me":
- Platform: n8n (Cloud for non-devs, Docker on a small VPS for devs); plain Python/TypeScript + GitHub Actions cron if it is a pure script with no SaaS glue.
- Trigger: webhook if available, else schedule every 15 min (polling) or daily 07:00 for reports.
- Every item keyed by its source ID; processed IDs stored; re-runs are safe.
- Errors: 3 retries with exponential backoff, then a failure row in a "dead letters" sheet and a Telegram/Slack/mail alert.
- External actions (sending mails, changing customer data): drafts plus approval in v1.
- AI steps: classify/extract with a fixed JSON schema, low temperature, confidence field; below threshold goes to review.
- Logging: run log with timestamp, items in, items out, errors.
- Secrets in the platform credential store or `.env` (gitignored).
- Budget target under 20 EUR/month.
Why: these choices keep a solo builder safe from the three classic failures (silent drops, duplicates, embarrassing auto-sent messages) without much extra work.

## Scope traps
- **"And then it should also..."**: flows grow branches until nobody understands them. Constraint: v1 handles one trigger and one main path; every extra branch is a later milestone.
- **Automating a process that does not exist yet**: if the manual process is unclear, the automation encodes chaos. Ask: "Walk me through the last time you did this by hand."
- **Full autonomy too early**: an agent that sends mails or edits CRM deals unsupervised. Constraint: human approval until 2 weeks of clean runs.
- **Scraping fragility**: sites change, block or forbid scraping. Ask for an official API or export first; budget a maintenance milestone otherwise.
- **Platform lock-in surprises**: Zapier/Make bills explode with volume. Run the cost estimate during Phase 5, not after launch.
- **Testing in production**: first run on real customers. Constraint: a test mode with sandbox accounts or a dry-run flag that logs instead of acting.

## Brief sections
Add to the universal brief:
- **Trigger & schedule**: event or cron expression, timezone, expected frequency and volume.
- **Flow diagram**: numbered steps (trigger, fetch, transform, decide, act, notify), optionally as a Mermaid flowchart.
- **Systems & credentials**: each system, direction (read/write), auth method, scopes, who provides the key; never the secret itself.
- **Data contract**: sample input, mapped output fields, JSON schema for AI steps.
- **Reliability rules**: retries, idempotency key, duplicate handling, rate limits, dead-letter location.
- **Human checkpoints**: where approval happens and through which channel.
- **Observability**: run log, alerts, heartbeat.
- **Hosting & cost estimate**: where it runs, monthly cost calculation.
- **Runbook**: how to pause, re-run a failed item, rotate a key.

## Milestones
- **M0 Setup**: platform/repo ready, credentials connected, test accounts or sandbox data available. Done when: a "hello" step can read from the source and write a test value to the target.
- **M1 Happy path**: trigger plus main steps on one real sample input. Done when: the sample produces the expected output in the target system, shown by a screenshot or log entry.
- **M2 Edge cases**: handle the ugly samples (missing fields, other language, attachments). Done when: all provided samples pass, each with a recorded result.
- **M3 Reliability**: retries, idempotency, dead letters, alerts. Done when: running the same input twice creates one result, and a forced failure (wrong key, timeout) produces an alert and a dead-letter entry.
- **M4 Human-in-the-loop & AI tuning** (if applicable): approval step, confidence thresholds. Done when: low-confidence items land in review and an approved draft is sent correctly.
- **M5 Deploy & monitor**: production hosting, schedule active, heartbeat. Done when: 3 consecutive scheduled runs succeed and appear in the run log.
- **M6 Handover**: runbook and README. Done when: someone else can pause, re-run and rotate a credential by following the doc.

## Verification
- **Dry run**: a flag or test mode that logs intended actions without executing them; run it on the sample set and compare against expected outputs.
- **Golden samples**: keep 5-10 real inputs with expected outputs in a fixtures folder (or a test sheet); every change re-runs them.
- **Idempotency check**: trigger the same event twice; assert exactly one record/mail/contact exists.
- **Failure injection**: revoke a key, point to a bad URL, send malformed input; assert retries, alert and dead-letter entry.
- **Rate-limit check**: run with the expected peak volume in sandbox; no 429 cascades, total runtime acceptable.
- **Schedule check**: confirm the cron expression and timezone (`crontab.guru`, n8n schedule preview); watch the first live runs.
- **For code**: unit tests on transform/parse functions, `--dry-run` CLI flag, linting; for n8n/Make: exported workflow JSON committed to the repo.
- Acceptance criteria pattern: "Given [input], when [trigger], then [target state] within [latency], and running it again changes nothing."

## Example opening
Request (~30 words):
> "i want the invoices in my gmail inbox to get picked up automatically, the data dropped into a google sheet and a quick heads-up on telegram for me. ideally with n8n."

Deep-mode round-1 reply excerpt:
> Got it: invoice mails in Gmail should be detected automatically, parsed and written as a row into a Google Sheet, plus a Telegram message. Platform: n8n.
>
> Here's how it could look, pick one or mix:
> - **A Lean:** n8n checks for new mails with a PDF attachment every 15 minutes, an LLM reads amount, date and sender, a row goes into the sheet, short Telegram ping.
> - **B With control:** like A, but uncertain cases land in a "Review" tab and you confirm with a Telegram button.
> - **C Bookkeeping-ready:** like B, plus the PDF gets filed in Google Drive by month and you get a total at month end.
>
> 1. **How do we recognise an invoice?** (a) PDF attachment plus words like "invoice/receipt" **(recommended)**, (b) fixed sender list, (c) a Gmail label you set yourself, (d) the LLM decides on every mail
> 2. **Which fields do you need?** (a) date, sender, gross amount **(recommended)**, (b) also net, VAT, invoice number, (c) everything including line items
> 3. **Where does n8n run?** (a) n8n Cloud **(recommended, no server hassle)**, (b) Docker on your VPS, (c) locally on your machine
> 4. **What happens on errors or duplicate mails?** (a) process each mail only once via its Message-ID, report errors on Telegram **(recommended)**, (b) just skip them, (c) decide for me
> 5. **Do you have 2 or 3 sample invoices**, including an "ugly" one? Then I build against real cases instead of assumptions.
>
> A short answer is enough, e.g. "B, 1a 2b 3a 4a". Or "decide for me", and I'll take the recommendations and note them as assumptions.
