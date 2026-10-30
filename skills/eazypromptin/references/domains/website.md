# Domain: Website

## Applies when
Route here when the main job is to **present, inform and convert visitors**: people arrive, read, and ideally take one action (call, book, buy, sign up, get in touch).

Signals:
- Nouns: website, homepage, landing page, one-pager, site, web presence, portfolio, blog, company site, event page, link-in-bio page, menu page for a restaurant.
- Verbs: present, show, rank, get found, collect leads, launch, relaunch, "redo".
- Artefacts: sections, copy, photos, logo, contact form, Google ranking, legal notice and privacy policy (for sites in Germany: Impressum, Datenschutzerklärung).
- Phrases: "I need a website for my business", "landing page for my product", "portfolio for job applications".

Tell it apart from neighbours:
- **web-app.md**: visitors log in and manage their own data (bookings, dashboards, accounts). A booking *widget* embedded from a third party (Calendly, Cal.com, Treatwell) keeps it a website; building the booking system yourself makes it a web app. A shop with a handful of products via Stripe Payment Links or Shopify Buy Button stays here; a custom store with carts, accounts and inventory goes to web-app.md.
- **design-ui.md**: the deliverable is a mockup, Figma file, style guide or logo, not a deployed site. If the person wants "just a design for now", route there and offer this playbook for the build afterwards.
- **mobile-app.md**: anything that must be installed from a store.
- **game.md**: interactive experiences whose point is play (a browser mini-game as marketing gimmick is a website section only if it is small; otherwise split it out).
- **code-change.md**: an existing site with a repo the agent will edit ("add a blog to my site"). If the existing site is on Wix/Squarespace/WordPress and the person wants to leave it, it is a relaunch and belongs here, with the old site as an input asset.

## What people leave out
- **The one action a visitor should take.** Without it the agent builds a pretty brochure with five equal buttons and nothing converts.
- **Who the visitor is and what they search for.** Copy and SEO aimed at "everyone" ranks for nothing and speaks to no one.
- **Where the text comes from.** Agents fill gaps with generic marketing filler ("We are your competent partner"), which reads AI-written and kills trust.
- **Real assets.** No logo, photos or testimonials means stock imagery and placeholders that never get replaced.
- **Who edits it afterwards.** A hand-coded site is great until the owner needs to change opening hours and cannot.
- **Legal pages and consent.** For sites in Germany, a missing Impressum (legal notice) or Datenschutzerklärung (privacy policy), or Google Fonts/Maps loaded without consent, invites Abmahnungen (paid cease-and-desist letters).
- **Domain, email and hosting ownership.** The agent cannot deploy or connect a domain it has no access to; launch stalls at the last step.
- **Performance and mobile.** Most local-business traffic is mobile; a heavy hero video and unoptimised photos lose those visitors.

## Discovery map

### Phase 1: Goal & conversion
- **Site type**: sets structure and effort. [Q]
  Options: a) one-page landing page, b) small business site (4-6 pages), c) portfolio/personal site, d) blog or content site, e) product/SaaS marketing site. Default: inferred from the request; b for local businesses, a for a single product or campaign. Decide for me: the smallest type that fits the goal.
- **Primary action**: the page is designed backwards from this. [Q]
  "What should a visitor do before they leave?" Options: a) call or WhatsApp, b) send an enquiry form, c) book an appointment (embedded tool), d) buy / pre-order, e) join a waitlist or newsletter, f) download/view work samples (portfolio). Default: b, with a click-to-call button on mobile for local businesses. Decide for me: pick one primary and at most one secondary action.
- **Success signal**: tells the agent what to measure and optimise. [S]
  Options: a) enquiries per month, b) Google ranking for "[service] [town]", c) signups, d) "looks professional when I send the link". Default: a + b for local business, c for products, d for portfolios.
- **Relaunch or new**: an old site is both an asset and a constraint. [S]
  Options: a) brand-new, b) replacing an existing site (URL?), c) replacing a social-media-only presence. Default: a. For b, collect the old URL, keep ranking pages and plan 301 redirects.
- **Anti-goals**: [S] "What should it definitely not feel like?" Examples: no stock-photo corporate look, no pop-ups, no cookie-banner wall, not "too playful". Default: no pop-ups, no autoplay video.

### Phase 2: Audience & message
- **Visitor profile**: decides tone, language and what proof they need. [Q]
  "Who lands on it, and from where?" Options: a) local customers via Google/Maps, b) B2B decision-makers via LinkedIn or referrals, c) recruiters/clients checking your work, d) social-media followers, e) people from paid ads. Default: a for local businesses. Decide for me: infer from site type, record it.
- **Main objection**: the copy must answer it above the fold. [S]
  "Why would someone hesitate to contact you?" Options: too expensive, not sure you do X, trust (are you legit?), too far away, no time. Default: trust; answer with real photos, reviews and clear prices or price ranges.
- **Proof**: converts more than any headline. [S]
  Options: a) Google reviews, b) customer logos or testimonials, c) before/after photos, d) certificates, master craftsman certificate (Meisterbrief in Germany), memberships, e) project case studies, f) none yet. Default: whatever exists; never invent testimonials.
- **Language(s) & tone**: [S] Options: one language only, two languages (e.g. German + English), informal or formal form of address (in German: "du" vs. "Sie"). Default: the local language, formal for trades and B2B, informal for lifestyle, gastro and creative work.
- **Keywords**: a local site lives on 3-5 phrases. [D]
  "What would a customer type into Google?" Default: propose "[service] [town]" variants (e.g. "roofer Koblenz", "physiotherapy Mainz home visits") and let the person correct.

### Phase 3: Structure & content
- **Sections / pages**: the skeleton the agent builds. [Q]
  Offer a proposed outline the person edits. Landing page default: Hero (promise + primary action) / Problem or benefits / Services or features / Proof / How it works (3 steps) / Prices or packages / FAQ / Final call to action / Footer with legal links. Small business default pages: Home, Services, About us, References, Contact, plus for sites in Germany Impressum (legal notice) and Datenschutz (privacy policy).
- **Copy source**: the biggest quality lever. [Q]
  Options: a) I provide all text, b) I give bullet points, the agent writes the copy, c) agent drafts from my old site / Google profile / Instagram, d) agent writes everything from a short interview. Default: b, with the rule that every factual claim (years in business, prices, certifications) comes from the person. Decide for me: d, and mark all facts as placeholders to confirm, visibly highlighted in the build.
- **Assets on hand**: decides whether the look can be real. [S]
  Checklist: logo (SVG?), brand colours, photos of team/place/work, product shots, videos, testimonials, opening hours, address, prices. Default: use what exists; for missing photos, prefer clean typographic layouts over stock imagery and list "real photos" as an open item.
- **Forms**: where leads arrive. [S]
  Options: a) simple contact form to email (Formspree, Web3Forms, or a serverless function + Resend), b) form into a CRM or Google Sheet, c) multi-step quote request, d) no form, just phone/WhatsApp/email links. Default: a with spam protection (honeypot + Cloudflare Turnstile) and a privacy consent line.
- **Embeds**: each one has privacy and performance costs. [D]
  Options: Google Maps, booking widget (Cal.com, Calendly, Treatwell, Doctolib), Instagram feed, YouTube video, reviews widget. Default: static map image linking to Google Maps, video behind a click-to-load facade, no Instagram feed.

### Phase 4: Look, CMS & tech
- **Visual direction**: gives the agent a target instead of the generic template look. [Q]
  Use reference anchors and this-or-that: a) clean and minimal (lots of white, one accent colour), b) warm and local (photos, earthy tones, rounded type), c) bold and modern (big type, strong contrast), d) premium and calm (dark, serif headlines), e) playful. Ask for 1-3 sites they like and one they dislike. Default: a, using existing brand colours. Hand off to design-ui.md if they want a full brand identity first.
- **Who edits afterwards**: decides CMS or not. [Q]
  Options: a) nobody, changes go through me/the agent (static site in Git), b) owner edits text and images occasionally (Git-based or headless CMS), c) owner posts regularly (blog, news, menu), d) non-technical team edits daily. Default: a for portfolios and landing pages, b for small business. Decide for me: a, with content in Markdown/JSON files the agent can update.
- **Stack**: [S] Offer a committed recommendation:
  a) **Astro** + Tailwind, content in Markdown/MDX collections. Recommended default: fast, static, SEO-friendly, easy for an agent.
  b) **Astro + headless CMS** (Keystatic, Decap, Sanity, Storyblok) when the owner edits.
  c) **Next.js** when the site sits next to a Next.js web app or needs heavy interactivity.
  d) **WordPress** (block theme) or **Webflow/Framer** when the owner insists on a visual editor or an agency hands it over; note that an agent can do less here and verification is harder.
  Decide for me: a, or a + Keystatic if anyone but the builder will edit.
- **Hosting & domain**: launch blocker if unclear. [S]
  Options: a) Netlify, Vercel or Cloudflare Pages (free for static sites), b) German hoster (IONOS, Strato, all-inkl, Hetzner Webhosting) because the domain and email already live there, c) existing WordPress hosting. Default: Cloudflare Pages or Netlify with the domain's DNS pointed there; keep email where it is. Ask who owns the domain login.
- **Analytics & consent**: decides whether a cookie banner is needed. [S]
  Options: a) none, b) cookie-less analytics (Plausible, Umami, Cloudflare Web Analytics), c) Google Analytics 4 + consent banner, d) Meta/Google Ads pixels + consent management. Default: b, which avoids a consent banner in most setups; self-host fonts.

### Phase 5: Production: legal, SEO, scope, verification, handoff
- **Legal pages (DE/EU)**: required, not optional. [Q] for sites in Germany
  Impressum, the mandatory legal notice (§ 5 DDG, the German Digital Services Act: name, address, contact, register entry, VAT ID (USt-IdNr.) if any, person responsible for content), and Datenschutzerklärung, the GDPR (DSGVO) privacy policy, listing every processor (hoster, form service, analytics, embeds). Default: generate structure and placeholders from a German legal-text generator the person fills in (eRecht24, Dr. Schwenke/Datenschutz-Generator.de, IT-Recht Kanzlei); the agent never invents legal facts. Record "legal text reviewed by owner" as a done criterion.
- **SEO baseline**: [S] Default: unique title + meta description per page, one H1, semantic headings, alt text, sitemap.xml, robots.txt, Open Graph image, LocalBusiness/Organization schema (JSON-LD), canonical URLs, Google Search Console + Google Business Profile linked. Redirect map for relaunches.
- **Performance & accessibility targets**: [S] Default: Lighthouse ≥ 90 in all four categories on mobile, images as AVIF/WebP with explicit sizes, no layout shift, WCAG 2.2 AA contrast and keyboard navigation.
- **Launch checklist & ownership**: [D] Default: domain connected with HTTPS, form tested end to end, 404 page, favicon, legal pages linked in footer, access handed to owner, short edit guide.
- **Agent operating rules**: [S] Default: no invented facts, testimonials or prices; placeholders marked `[[TODO: ...]]` and listed; no third-party scripts without listing them for the privacy policy (Datenschutzerklärung); run build + Lighthouse before claiming done.

## Inspiration anchors
Ask for sites they like, in their own industry and outside it. Useful archetypes to name: "Apple-style product page with big sections", "Stripe/Linear-style SaaS landing", "local bakery with a warm photo-led page", "architect portfolio with full-bleed images", "personal site with a short bio and project list (like a developer's GitHub-linked one-pager)", "event page with schedule and ticket button". Seed with "X meets Y": "a trades business, but it feels like a modern design studio".

Pitch-sampler seeds:
- **Trust-first local business**: real team photo hero, three core services with prices "ab", Google reviews, big call/WhatsApp button, map and hours.
- **Single-product launch page**: one promise, a 30-second demo video, three benefits, pricing, FAQ, waitlist form.
- **Work-speaks portfolio**: name and one line, 4-6 case studies with images and outcome, contact and CV download.
- **Restaurant/café page**: atmospheric photo, menu as a fast HTML page (not a PDF), reservations via embedded tool, opening hours prominent.
- **Recruiting page**: "Working at [Company]": day-in-the-life photos, benefits, open positions, 60-second application form.
- **Expert blog**: articles that answer the questions customers ask, each ending in a soft call to action.

## Smart defaults
When the person delegates, apply and record:
- Type: the smallest that serves the goal (one-pager unless there are clearly separate services/audiences).
- Primary action: enquiry form + click-to-call on mobile.
- Stack: Astro + Tailwind, content collections in Markdown, no client-side framework unless needed; Keystatic if the owner edits.
- Forms: serverless endpoint (Astro action or Netlify/Cloudflare function) sending via Resend, or Web3Forms; honeypot + Turnstile.
- Hosting: Cloudflare Pages or Netlify, domain DNS pointed there, email stays with current provider.
- Privacy: self-hosted fonts, no Google Maps iframe (static image link), Plausible or Umami, so no cookie banner; Impressum + Datenschutz pages (for sites in Germany) from a generator with placeholders.
- Copy: agent drafts from the interview, in the site's language (German for German businesses), tone matched to industry, every fact flagged for confirmation.
- Quality: Lighthouse ≥ 90 mobile, WCAG AA, valid HTML, sitemap and schema markup.
Why: a static Astro site is cheap, fast, hard to break, ranks well, and every claim can be verified by a build and an automated audit.

## Scope traps
- **Feature creep into a web app.** Customer logins, custom booking logic, member areas. Ask: "Can an embedded tool do this?" If yes, embed; if no, split into a web-app brief.
- **Waiting for perfect content.** Projects stall on missing photos and text. Constraint: launch with marked placeholders for non-critical items; copy and photos are their own milestone.
- **Too many pages.** Ten thin pages rank worse than four good ones. Ask what each page answers that the others do not.
- **Blog nobody writes.** Ask "Who writes the second post, and when?" If no answer, no blog in v1.
- **Animation obsession.** Parallax, scroll-jacking and 3D heroes tank performance. Constraint: Lighthouse budget is a done criterion.
- **Multilingual by default.** Doubles content work. Only if a real audience needs it; otherwise later.
- **Design by committee.** Ask who has the final say on the look before showing anything.

## Brief sections
Add these to the universal brief:
- **Conversion goal**: primary and secondary action, where they appear, what counts as a lead.
- **Audience & message**: visitor profile, main objection, value proposition in one sentence, tone and form of address.
- **Sitemap & sections**: pages and, per page, ordered sections with their purpose.
- **Copy plan**: source per section (provided / agent-drafted / placeholder), facts to confirm, keywords per page.
- **Brand & visual direction**: colours, fonts, logo files, reference sites liked/disliked, image style.
- **Assets inventory**: what exists, format, where it is; what is missing and the fallback.
- **Forms & embeds**: each form's fields, recipient and spam protection; each embed with its privacy handling.
- **SEO & analytics**: keywords, schema type, Search Console/Business Profile, analytics tool, redirects.
- **Legal & privacy**: legal notice data (Impressum), list of processors for the privacy policy (Datenschutzerklärung), consent approach.
- **Editing & ownership**: CMS choice, who edits, domain/DNS/hosting account owners.

## Milestones
- **M0 Setup**: repo, Astro (or chosen stack) scaffold, Tailwind, design tokens (colours, fonts self-hosted), deploy preview. Done when: preview URL loads and the build passes in CI.
- **M1 Skeleton**: all pages and sections with real headings and placeholder copy, navigation, footer with legal links, responsive layout. Done when: every page in the sitemap exists and works at 375 px and 1440 px.
- **M2 Copy & assets**: final or agent-drafted copy, optimised images, testimonials, all `[[TODO]]` items listed in one file. Done when: no lorem ipsum remains and the TODO list is reviewed by the person.
- **M3 Forms & embeds**: contact form end to end with spam protection, click-to-call, booking embed or map facade. Done when: a test submission arrives in the target inbox and failing validation shows clear errors.
- **M4 SEO, legal & privacy**: meta tags, sitemap, robots, JSON-LD, OG images, legal notice and privacy policy (Impressum and Datenschutz) filled, analytics, redirects for relaunches. Done when: the SEO check script passes and no third-party request fires before consent (or none at all).
- **M5 Polish & performance**: animations (subtle), accessibility pass, Lighthouse tuning, 404 page, favicon. Done when: Lighthouse mobile ≥ 90 in all categories on every page template.
- **M6 Launch & handoff**: domain and HTTPS, Search Console + Business Profile, editor guide for the owner. Done when: the production domain serves the site, the form works there and the owner has made one test edit.

## Verification
- Build: `npm run build` with zero errors and warnings; `astro check` or `tsc --noEmit` if TypeScript.
- Audits: Lighthouse CI (`lhci autorun`) against the preview URL with budgets per category; `pa11y-ci` or axe for accessibility; an HTML validator; a link checker (`lychee` or `linkinator`) for broken links.
- Privacy check: load each page in a headless browser (Playwright) and assert no requests to fonts.googleapis.com, google-analytics, facebook or other third parties unless consented.
- SEO check: script asserting every page has a unique `<title>`, meta description, exactly one `<h1>`, alt on all images, canonical URL; sitemap lists all pages; JSON-LD validates.
- Form test: Playwright submits the form and checks the success state; the person confirms the email arrived.
- Responsive screenshots at 375, 768 and 1440 px for each template, reviewed by the person.
- Acceptance pattern: "On mobile, a visitor from Google can reach [primary action] within one tap from the first screen."
- Content check: grep for `[[TODO`, "lorem", and placeholder phone numbers must return nothing before launch.

## Example opening
Request:
> "need a website for my roofing business in koblenz, should look modern and show up on google so more enquiries come in. only got a logo and a few phone pics"

Excerpt of a good Deep-mode round-1 reply:
> Got it: a site for your roofing business, the goal is more enquiries from Koblenz and the surrounding area via Google. You've got a logo and a few photos, we'll build the rest together.
>
> Three directions, pick one or mix:
> **A) "Trust first"**: a big photo of you and the team, three services with "from" prices, Google reviews, a big call and WhatsApp button.
> **B) "Let the work speak"**: a before/after gallery of your roofs front and centre, short texts, enquiry form at the end.
> **C) "Emergency focus"**: storm damage and repairs right at the top, phone number always visible, everything else below.
>
> 1. **What should a visitor do?** a) Call (recommended, plus a form as the second option) b) Enquiry form with photos of the roof c) WhatsApp
> 2. **How many pages?** a) One long page (recommended to start) b) Home, Services, References, About us, Contact
> 3. **Who writes the copy?** a) You give me bullet points, I write it (recommended) b) I write everything from a short interview c) You provide finished texts
> 4. **Will you need to change things yourself later?** a) No, changes go through me (recommended) b) Yes, texts and images now and then
> 5. **Where is your domain?** a) With IONOS/Strato or similar b) No domain yet c) Don't know
>
> A short answer is enough, e.g. "A, 1a 2a 3a 4b 5a" or "decide for me".
