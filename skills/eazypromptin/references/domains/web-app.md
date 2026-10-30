# Domain: Web App & SaaS

## Applies when
Route here when the person wants software that people **log into and work with** in a browser: data is created, changed and stored per user or per organisation.

Signals:
- Nouns: app, tool, platform, portal, dashboard, admin panel, backend, SaaS, CRM, booking system, marketplace, internal tool, "like Notion/Trello/Calendly but for ...".
- Verbs: manage, track, book, assign, approve, invite, pay, subscribe, sync, import.
- Artefacts: user accounts, roles, records, lists and detail views, reports, subscriptions, an API.
- Phrases: "I want to build an app where customers ...", "a tool for my team", "a platform where providers and customers ...".

Tell it apart from neighbours:
- **website.md**: the main job is to *inform or convert* visitors (landing page, company site, blog, portfolio). A contact form or newsletter signup does not make it a web app. If there is a login with per-user data, it is a web app; a marketing site in front of a SaaS is two projects, so run this playbook and treat the landing page as one milestone or a separate brief.
- **mobile-app.md**: the person expects an icon on the phone, App Store / Play Store presence, push notifications or device features (camera, GPS, offline) as core. "App" alone is ambiguous (many people use it for any software); ask "Browser or App Store?" as the first this-or-that. A responsive web app or PWA is the default when the store is not a requirement.
- **game.md**: the core loop is play, score, levels or simulation rather than managing records. A browser game lives there even if it has accounts.
- **design-ui.md**: the deliverable is screens, a design system or a clickable prototype, not working software with persistence.
- **code-change.md**: a codebase already exists and the request is a feature, fix or refactor inside it. If the person says "in my existing Laravel app", route there and borrow only the relevant slots (auth, payments, data model) from this file.

## What people leave out
- **Who the roles are and what each may do.** The agent invents a single "user" and permissions have to be retrofitted across every query.
- **The core objects and how they relate.** Without "a Salon has many Staff, a Booking belongs to one Staff and one Customer" the agent guesses a schema that breaks at milestone three.
- **Whether data is per person or per organisation (tenancy).** Switching from single-user to multi-tenant later touches every table, route and test.
- **How money flows.** "With payments" can mean one-off checkout, subscriptions, usage billing or marketplace payouts; each is a different Stripe product and data model.
- **What is out of scope for the MVP.** Agents happily build settings pages, notifications and analytics nobody asked for while the core flow stays broken.
- **Where it runs and who pays for it.** The stack choice depends on hosting budget and whether the person wants managed services or a VPS.
- **Legal and data constraints.** EU users mean GDPR, a data processing agreement with every vendor, EU hosting regions and a deletion path; adding these late is painful.
- **What "done" looks like.** Without a walkthrough script and seed data, the agent declares victory on a page that renders but cannot complete the core flow.

## Discovery map

### Phase 1: Vision & job to be done
- **One-sentence job**: anchors every later trade-off. [Q]
  "In one sentence: who uses it to get what done?" Offer a fill-in: "*[Role]* uses it to *[verb]* *[object]* instead of *[current workaround]*." Default: derive it from the request and ask for confirmation. Decide for me: write the sentence yourself and mark it as an assumption.
- **Current workaround**: tells you the real competitor and the minimum bar. [S]
  "What do they use today?" Options: a) Excel / Google Sheets, b) WhatsApp + paper, c) an existing tool that is too expensive or too generic (name it), d) nothing, it is a new behaviour. Default: a. Decide for me: assume spreadsheets, so import from CSV becomes a nice-to-have.
- **Product shape**: decides architecture more than any other answer. [Q]
  This-or-that: a) internal tool for one team, b) single-tenant app for one customer/business, c) multi-tenant SaaS that many organisations sign up for, d) two-sided marketplace (providers and buyers), e) personal productivity app (each user alone). Default: b for a first build, c if the person says "sell it" or "subscription". Decide for me: b, with tenant_id prepared only if the person mentions selling it.
- **Why now / success signal**: keeps scope honest. [D]
  "How will you know in 8 weeks it worked?" Options: a) I use it daily myself, b) first 3 paying customers, c) the team stopped using the spreadsheet, d) a demo for investors/class. Default: a or c. Decide for me: c.
- **Anti-goals**: the cheapest scope control there is. [S]
  "What must it NOT become?" Offer examples: not a full ERP, no mobile app yet, no AI features in v1, no public signup. Default: no native mobile app, no public API in v1.

### Phase 2: Users, roles & core flows
- **Roles**: drives auth, permissions and navigation. [Q]
  "Who logs in?" Options: a) just me/admin, b) admin + staff, c) admin + staff + end customers, d) org owner + members + guests (SaaS), e) buyers + sellers + platform admin (marketplace). Default: b. Decide for me: pick the smallest set that completes the one-sentence job.
- **Permission rules**: prevents data leaks between users. [S]
  "Can staff see each other's records? Can customers see anything besides their own?" Options: a) everyone in the org sees everything, b) owners see all, members see their own, c) fine-grained per-record sharing. Default: b. Decide for me: b, enforced server-side in every query.
- **Core objects**: becomes the data model. [Q]
  "Name the 3-6 things the app manages." Use a reference anchor to help: "Trello: Board, List, Card, Member. Calendly: EventType, Availability, Booking." Default: propose a list from the request and let them edit. Decide for me: propose and record as assumption.
- **Primary flow**: the one path that must work end to end. [Q]
  Run a scenario walkthrough: "A new [role] opens the app for the first time. What do they do in the first two minutes?" Narrate it yourself if the person stalls, then ask "is that right?". Default: the coach's narration. Decide for me: keep the narration and mark it as assumption.
- **Secondary flows**: what comes after the MVP. [D]
  "Which of these matter later?" Options: a) notifications (email), b) reports/exports (CSV, PDF), c) search and filters, d) comments/activity log, e) calendar sync. Default: a + c in MVP, rest later.
- **Empty and edge states**: where agent-built apps feel broken. [D]
  "What happens when there is no data yet / a booking is cancelled / a payment fails?" Default: empty states with a clear call to action; cancellation as a status, never a hard delete.

### Phase 3: Data, auth & money
- **Tenancy model**: costly to change later. [S]
  Options: a) single database, no tenants, b) shared database with `organization_id` on every row + row-level security, c) database per tenant. Default: a for internal tools, b for SaaS. Decide for me: b if more than one business will ever use it; never c for a solo builder.
- **Auth method**: affects onboarding friction and the vendor. [Q]
  Options: a) email + password, b) magic link, c) Google/Microsoft sign-in, d) passkeys, e) SSO/SAML for enterprise customers. Default: magic link + Google. Decide for me: use the auth that ships with the chosen stack (Supabase Auth, Laravel Breeze/Fortify, Better Auth or Auth.js for Next.js, Clerk if speed matters more than cost).
- **Payments**: separate product, separate data model. [S]
  Options: a) none in v1, b) one-off payments (Stripe Checkout), c) subscriptions with plans (Stripe Billing + Customer Portal), d) usage-based billing, e) marketplace payouts (Stripe Connect). Default: a, or c via Stripe Checkout + Customer Portal + webhooks if the person wants to charge. Decide for me: no payments in MVP; add a "Payments" milestone. Mention Lemon Squeezy or Paddle as merchant of record if the person wants VAT handled for them.
- **Data sensitivity & compliance**: decides hosting region and vendors. [S]
  "Whose data is stored?" Options: a) only business data, b) personal data of EU customers (names, emails, phone), c) health, financial or children's data. Default: b, treat as GDPR: EU region, DPA with each vendor, export and delete account, minimal logging of personal data. For c, flag that legal review is needed and record it as an open question.
- **Files & media**: storage choice and limits. [D]
  Options: a) none, b) user uploads (images, PDFs) via S3-compatible storage (Supabase Storage, Cloudflare R2), c) generated files (invoices, exports). Default: a or b with a 10 MB limit.
- **Audit & history**: often required in B2B. [D]
  Options: a) none, b) created_by/updated_at on every row, c) full activity log. Default: b.

### Phase 4: Integrations, stack & hosting
- **Integrations**: each one is a milestone with its own failure modes. [S]
  "Does it need to talk to anything?" Options: a) email sending (Resend, Postmark), b) calendar (Google Calendar, Outlook), c) accounting (lexoffice, sevDesk, DATEV export), d) messaging (WhatsApp Business, Slack), e) AI features (OpenAI / Anthropic API), f) none. Default: a only. Decide for me: transactional email only; everything else goes to "later".
- **Stack**: the agent works best in a stack it knows deeply and can test. [Q]
  Offer three committed paths, recommend one:
  a) **Next.js (App Router) + TypeScript + Postgres via Supabase** (auth, storage, RLS included) + Tailwind + shadcn/ui, deploy on Vercel. Recommended default for most SaaS and dashboards.
  b) **Laravel 12 + Inertia + Vue or React** (or Livewire) + Postgres/MySQL, deploy on Laravel Cloud, Forge or a VPS. Great when the person knows PHP, wants batteries included (queues, mail, auth, billing via Cashier).
  c) **NestJS API + React/Vue SPA + Postgres with Prisma or Drizzle**. Choose when a separate API is required (mobile client later, third-party consumers).
  d) **Low-code backend**: Supabase alone, PocketBase or Convex with a thin frontend, for internal tools and prototypes.
  Decide for me: a, unless the person's existing skills point clearly elsewhere (then their stack wins, because they must maintain it).
- **Existing skills**: the person will debug what the agent writes. [S]
  "Which languages/frameworks do you read comfortably?" Options: TypeScript/React, PHP/Laravel, Python/Django, none. Default: let this override the stack default.
- **Hosting & budget**: constrains vendors and region. [S]
  Options: a) free tiers first (Vercel Hobby + Supabase Free), b) ~20-50 EUR/month managed (Vercel Pro, Supabase Pro, Laravel Cloud), c) own VPS (Hetzner + Coolify or Docker Compose), d) company cloud (AWS, GCP, Azure). Default: a during build, b at launch; Hetzner/Coolify when EU hosting and low cost matter most. Decide for me: managed, EU region.
- **UI approach**: speeds up the agent and keeps it consistent. [D]
  Options: a) component library (shadcn/ui, Mantine, Vuetify, Filament for Laravel admin), b) custom design from Figma, c) admin template. Default: a. Hand off to design-ui.md if the person wants a bespoke visual identity first.

### Phase 5: Production: scope, milestones, verification, handoff
- **MVP cut**: the single most valuable decision in the session. [Q]
  Present the feature list as three columns (MVP / soon / later) with your proposed cut; ask "does this cut work for you?". Default: MVP = auth + core objects CRUD + primary flow + one notification email.
- **Seed data & demo account**: makes verification possible. [S]
  Default: a seed script with one demo org, two users per role, realistic sample records.
- **Testing depth**: what the agent must prove. [S]
  Options: a) typecheck + lint + smoke test, b) + unit tests for business rules, c) + end-to-end tests (Playwright) for the primary flow. Default: c for the primary flow only.
- **Deploy target & environments**: ends "works on my machine". [D]
  Default: preview deploys per branch, one production environment, secrets in the host's env settings, migrations run in CI.
- **Agent operating rules**: [S] Default: work milestone by milestone, run tests before claiming done, never commit secrets, ask before adding a paid service or a new dependency category, keep a CHANGELOG or progress notes.

## Inspiration anchors
Use reference anchors as shorthand for structure, not looks: "Linear-style issue list", "Calendly booking flow", "Stripe-dashboard tables", "Notion-like sidebar with nested pages", "Airbnb two-sided listing + booking", "Shopify admin". Ask "Which existing tool is closest, and what annoys you about it?" The annoyance is usually the product.

Pitch-sampler seeds (turn 2-4 into mini-pitches of 2 lines each):
- **Vertical booking SaaS**: "Calendly for [salons/physios/driving schools]": public booking page per business, staff calendars, reminders, no-show tracking.
- **Spreadsheet replacement**: "the team's Excel, but with roles, history and a form for each entry": CRUD + filters + CSV export.
- **Client portal**: "where my customers log in to see status, upload documents and approve offers": single-tenant, invite-only.
- **Niche marketplace**: "providers list offers, buyers request and pay, platform takes a fee": Stripe Connect, reviews, admin moderation.
- **Ops dashboard**: "one screen with the numbers and alerts from three tools we already use": read-only integrations, scheduled sync, charts.
- **Loyalty / membership tool**: "customers collect points via QR code, businesses see who comes back": multi-tenant, mobile-first web.

## Smart defaults
When the person says "decide for me" or "no idea", apply this profile and record every item under Decisions & Assumptions:
- Shape: single business first, `organization_id` on tenant-owned tables if selling is mentioned.
- Stack: Next.js (App Router, TypeScript, server actions) + Supabase (Postgres, Auth, Storage, RLS) + Tailwind + shadcn/ui; Drizzle or Supabase client for queries; Zod for validation. Swap to Laravel + Inertia if the person knows PHP.
- Auth: magic link + Google; roles stored in a `memberships` table (user, org, role).
- Payments: none in MVP; Stripe Checkout + Customer Portal + webhook handler as a later milestone.
- Email: Resend with React Email templates.
- Hosting: Vercel + Supabase, EU region (Frankfurt); move to Hetzner + Coolify only for cost or data-residency reasons.
- Compliance: GDPR baseline (EU region, account export + delete, no personal data in logs, cookie-less analytics such as Plausible).
- Quality: TypeScript strict, ESLint, Vitest for business rules, Playwright for the primary flow, GitHub Actions running all of them.
Why: this is the combination current coding agents produce most reliably, every piece has a free tier, and it can be verified headlessly.

## Scope traps
- **"Like X, but for Y" copies all of X.** Ask: "Which three features of X would your users miss on day one?" Build only those.
- **Admin everything.** Settings pages, role editors and theme switches eat milestones. Constraint: roles are fixed in code for v1.
- **Marketplace chicken-and-egg.** Two-sided products need both sides to work. Ask which side the person can bring personally and build that side's flow first; the other side may be the admin manually at first.
- **Payments before value.** Subscriptions, plans and dunning before the core flow works. Constraint: payments milestone only after the primary flow passes its E2E test.
- **Premature multi-tenancy or microservices.** Ask "How many organisations in the next 6 months?" Under ~50 needs nothing beyond `organization_id` + RLS in one monolith.
- **Integration sprawl.** Every API brings auth, rate limits and failure states. Constraint: at most one third-party integration in the MVP besides email.
- **AI sprinkled on top.** "With AI" without a defined input/output. Ask for one concrete AI task with an example input and expected output, or defer it.
- **Endless polish.** Constraint: done criteria are the walkthrough script, not "looks finished".

## Brief sections
Add these to the universal brief:
- **Roles & permissions matrix**: roles as rows, core objects as columns, cells = none / read own / read all / write own / write all.
- **Domain model**: core objects with key fields and relations (a short list or Mermaid ER diagram), plus status fields and their transitions.
- **Primary flows**: numbered step lists for the 1-3 flows that must work end to end, written from the user's point of view.
- **Tenancy & data ownership**: how data is scoped, how isolation is enforced, what happens on account deletion.
- **Auth & onboarding**: sign-in methods, invite flow, first-run experience.
- **Payments**: model, provider, plans/prices, webhook events handled, what happens on failed payment (or "none in v1").
- **Integrations**: each external service, what it is used for, credentials needed, failure behaviour.
- **Compliance & privacy**: data categories, hosting region, vendors needing a DPA, retention and deletion.
- **Environments & deployment**: hosts, environments, env vars list (names only), migration strategy.

## Milestones
- **M0 Setup**: repo, framework scaffold, linting, typecheck, test runner, CI, deploy of a hello page. Done when: CI is green and the preview URL loads.
- **M1 Data model & seed**: schema/migrations for core objects, seed script, RLS or policies. Done when: migrations apply from scratch, seed runs, a test proves user A cannot read org B's rows.
- **M2 Auth & roles**: sign-in, memberships, role checks, protected routes. Done when: each seeded role can log in and sees only allowed navigation and data.
- **M3 Core CRUD**: list, detail, create, edit, archive for each core object with validation and empty states. Done when: every object can be managed through the UI with seeded users.
- **M4 Primary flow**: the end-to-end path from Phase 2 incl. status transitions and the notification email. Done when: a Playwright test walks the full flow on a fresh seed.
- **M5 Payments or key integration** (if in scope): Stripe Checkout/Billing with webhook handling in test mode, or the one integration. Done when: test-mode purchase updates the plan in the DB and the Customer Portal opens.
- **M6 Compliance & hardening**: account export/delete, rate limiting on auth, error pages, logging without personal data, legal pages linked. Done when: delete removes or anonymises all personal rows, verified by test.
- **M7 Polish & launch**: responsive check, accessibility pass, production env, domain, backups. Done when: the walkthrough script passes on production with a fresh account.

## Verification
- Commands: `pnpm typecheck && pnpm lint && pnpm test && pnpm exec playwright test` (or `php artisan test` + `vendor/bin/pint --test` + Pest/Dusk for Laravel). CI must run the same.
- Fresh-start check: drop DB, run migrations + seed, start app; nothing manual in between.
- Isolation test: an automated test that logs in as a user of org A and requests org B's records by ID through every API route; all must return 403/404.
- Role walkthrough: for each role, a scripted list "log in, see X, cannot see Y, can do Z".
- Payments: Stripe CLI `stripe listen` + `stripe trigger checkout.session.completed` / `invoice.payment_failed`; DB state checked after each.
- Acceptance criteria pattern: "Given [role] in [state], when [action], then [visible result] and [DB result]." Write one per primary-flow step.
- Manual smoke script for the person: 10 numbered steps, under 5 minutes, ending in the core value moment.

## Example opening
Request:
> "wanna build an app for hair salons where customers can book appointments online and the salon can manage its staff and appointments. should be sellable to other salons later too"

Excerpt of a good Deep-mode round-1 reply:
> Got it: a booking platform for hair salons, customers book online, the salon plans staff and appointments, and later other salons should be able to use it too. That makes it a multi-tenant SaaS, so I'll plan for that from the start.
>
> So we're picturing the same thing, here are three directions (pick one or mix):
> **A) "Calendly for salons"**: a public booking page per salon, the customer picks a service, a stylist and a time, and gets an email reminder.
> **B) "Salon cockpit"**: focus on the salon, a calendar for all staff, walk-ins can be entered, the booking page is just an add-on.
> **C) "Regulars tool"**: booking plus a customer file with history, colour notes and a no-show counter.
>
> 1. **Who logs in?** a) Salon owner + staff, customers book without an account (recommended) b) Customers need an account too c) Only the owner
> 2. **Browser or App Store?** a) Web app that works on the phone (recommended) b) A real iOS/Android app on top
> 3. **Payments in the MVP?** a) None, customers pay at the salon (recommended) b) Deposit at booking via Stripe c) Salons pay you a subscription
> 4. **What do you know your way around?** a) TypeScript/React b) PHP/Laravel c) Don't care, use the most reliable option (then Next.js + Supabase)
>
> A short answer is enough, e.g. "A, 1a 2a 3a 4b", or "decide for me".
