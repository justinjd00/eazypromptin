# Domain: Design & UI

## Applies when
The deliverable is primarily visual: app or web screens, mockups and clickable prototypes, landing-page designs, dashboards (the look, not the data pipeline), design systems and component libraries, brand looks without logo design (palette, type, imagery style), posters, flyers, social graphics, slide decks.

Signals: "design", "mockup", "screen", "UI", "looks ugly", "make it modern", "Figma", "style guide", "color palette", "presentation", "slides", "poster", "Look", "redesign", screenshots attached with "make it look like this".

Neighbours and how to tell them apart:
- **Code change**: "make my existing settings page look better" needs both. Use this playbook for the visual decisions and code-change for implementation constraints (framework, components, no new deps).
- **New app build**: if the person wants a working product, design is one phase of that domain. Stay here when the output is the design itself (Figma file, static HTML mockup, images).
- **Content writing**: slide decks and posters need words; collect the content inventory here, but if the text itself is the hard part, borrow the reader and fact slots from content-writing.
- **Logo design**: out of scope for this playbook. Offer a wordmark in an existing typeface or note that a logo is a separate input.

## What people leave out
- **Purpose of the design**: a pitch mockup, a production-ready spec and a mood exploration need different fidelity. Guessing wastes effort on the wrong polish.
- **Content inventory**: what actually goes on the screen or slide. Without it, the agent fills layouts with lorem ipsum and the real content later breaks them.
- **Concrete references**: "modern and clean" describes every design since 2015. Two named references beat ten adjectives.
- **Brand constraints**: existing colors, fonts, logo files, tone. Ignoring them makes the result unusable.
- **Platform and sizes**: iPhone vs desktop dashboard vs 1080x1350 Instagram vs 16:9 slides. Layout logic changes completely.
- **Accessibility**: contrast, font sizes, touch targets. Often skipped until it fails a review or real users.
- **Deliverable format**: Figma file, HTML/CSS, Tailwind components, PNG/PDF, PPTX. The agent's tools and process differ per format.
- **States and edge cases**: empty, loading, error, long names, many items. Happy-path mockups fall apart in implementation.

## Discovery map

### Phase 1: Purpose and success
- **What it's for** [Q]: sets fidelity and effort.
  "What will this design be used for?" Options: (a) explore a direction / mood, (b) pitch or investor/client presentation, (c) hand-off to development, (d) final asset to publish/print, (e) usability test prototype. Default: (c) for apps, (d) for posters/graphics, (b) for decks. Decide-for-me: infer from the artefact type.
- **Artefact** [Q]: what exactly is designed.
  Options: single screen, user flow (3-8 screens), full app set, landing page, design system/tokens, poster/flyer, social post set, slide deck. Default: as named.
- **Success test** [S]: how the person will judge it.
  Options: "looks as good as <reference>", a dev can build it without asking, users finish the flow, client says yes, the deck fits the time slot. Default: dev-ready or publish-ready depending on purpose.

### Phase 2: Audience and context
- **Audience** [Q]: who looks at it and in what situation.
  Options: (a) consumers on a phone, on the go, (b) professionals at a desktop, task-focused, (c) decision makers in a meeting, (d) passers-by (poster) with 3 seconds, (e) internal team. Default: (a) for apps, (c) for decks.
- **Key task or message** [Q]: the one thing the design must make obvious.
  "If someone sees this for 5 seconds, what must they get?" Offer 2-3 guesses from the request. Decide-for-me: the primary action or headline implied by the request.
- **Usage scenario** [S]: use a scenario walkthrough.
  "Describe one moment: who opens it, where, why, what do they do next?" This reveals lighting (dark mode), one-handed use, projector vs laptop, viewing distance.
- **Locale and language** [S]: German text runs ~30% longer than English; right-to-left needs mirrored layouts.

### Phase 3: Mood and references
- **Reference anchors** [Q]: the fastest way to align taste.
  "Name 1-3 apps, sites or designs whose look you like, or pick a direction." Offer direction anchors (see Inspiration anchors). Default: one calm, neutral direction. Decide-for-me: pick the direction matching audience and purpose, write it as an assumption.
- **This-or-that** [S]: three contrasting pairs in one line.
  Light vs dark, dense vs airy, rounded vs sharp, photographic vs illustrated vs typographic, playful vs serious, colorful vs monochrome with one accent. Lazy answer: "1a 2b 3a".
- **Anti-goals** [S]: what it must not look like.
  "Anything that would make you say no immediately?" Starter list: generic SaaS gradient, stock-photo people, everything in rounded cards, glassmorphism everywhere, emoji as icons, purple-blue AI look. Default: avoid templated defaults.
- **Imagery** [D]: photos, illustrations, icons, 3D, none.
  Options: own photos, licensed stock (Unsplash), generated images, icon set (Lucide, Phosphor, Material Symbols), purely typographic. Default: icon set plus typography, real images only if supplied.

### Phase 4: Brand, content, layout
- **Brand constraints** [Q]: hard limits first.
  "Is there an existing brand?" Options: (a) yes, I'll share colors/fonts/logo, (b) partial (just a color or logo), (c) none, propose one, (d) must match an existing product/site (link). Default: (c). Decide-for-me: propose a small token set (1 neutral scale, 1 accent, 1 typeface pair) and mark it as an assumption.
- **Typography** [S]: biggest single lever on look.
  Options with current, free choices: Inter / Geist (neutral UI), IBM Plex Sans (technical), Fraunces or Instrument Serif headlines with a sans body (editorial), Space Grotesk (techy, distinctive), system font stack (fast, native). Default: one sans family for UI, optional display face for headlines.
- **Content inventory** [Q]: real content per screen/slide.
  "List what must appear: headings, data fields, buttons, images, number of items." Ask for real copy or a realistic sample; for decks, the slide-by-slide outline. Decide-for-me: agent drafts realistic content from the request and marks it for review. Never lorem ipsum in the final.
- **Layout and navigation** [S]: structure before style.
  Options for apps: bottom tab bar, sidebar, top nav, single-page flow. For decks: title, section, content, image-led, quote, comparison layouts mixed. For posters: headline-dominant, image-dominant, grid. Default: platform convention (tab bar on mobile, sidebar for desktop tools).
- **States** [D]: empty, loading, error, success, long text, zero/one/many items, logged out.

### Phase 5: Platform, accessibility, production
- **Platforms and sizes** [Q]: drives the grid.
  Options: mobile 390x844 (iPhone 15/16 class), Android 412x915, desktop 1440 wide, responsive (mobile plus desktop breakpoints), A4/A3 print with 3 mm bleed, Instagram 1080x1350 and stories 1080x1920, slides 16:9 at 1920x1080. Default: mobile-first responsive for web, 16:9 for decks.
- **Accessibility** [S]: build it in, don't retrofit.
  Options: WCAG 2.2 AA (contrast 4.5:1 body, 3:1 large text and UI, 24x24 px minimum targets, 44x44 recommended on touch), AAA for public sector, basic only. Default: AA. Also: dark-mode support, reduced motion, not relying on color alone.
- **Deliverable format** [Q]: decides the agent's toolchain.
  Options: (a) Figma file with components and variables, (b) static HTML/CSS or Tailwind mockup in the browser, (c) React/Vue components ready for the codebase, (d) PNG/SVG/PDF exports, (e) PPTX or Google Slides. Default: (b) for quick iteration with an AI agent, (a) if a designer or Figma workflow exists, (e) or PDF for decks.
- **Iteration plan** [S]: how rounds work.
  Options: (a) 2-3 low-fi directions, pick one, then refine (recommended), (b) one high-fi design, then feedback rounds, (c) component library first, screens after. Default: (a) with max 3 refinement rounds.
- **Hand-off details** [D]: tokens as CSS variables or JSON, spacing scale, component names matching code, export sizes, annotations.

## Inspiration anchors
Offer anchors as named directions, each with 2-3 well-known examples:
- **Calm productivity**: Linear, Things 3, Notion. Neutral greys, one accent, tight type.
- **Editorial**: Stripe Press, The Pudding, Arc browser marketing pages. Serif headlines, generous whitespace, strong grid.
- **Playful consumer**: Duolingo, Headspace, Airbnb illustrations. Color, illustration, friendly shapes.
- **Swiss / brutalist typographic**: classic Swiss posters, Vercel, Teenage Engineering. Grid, big type, few colors.
- **Data-dense tool**: Bloomberg Terminal light, Grafana, Figma's own UI. Compact, high information per pixel.
- **Native platform**: Apple Human Interface Guidelines, Material 3 Expressive. Feels like it belongs on the device.
- Decks: "Apple keynote (one idea per slide, big image)", "McKinsey-style (action titles, one chart)", "Swiss editorial deck with original images and varied layouts".

"X meets Y" seeds: "Linear meets Duolingo" (calm structure, playful rewards), "Stripe docs meets a magazine", "Teenage Engineering for a recipe app".

Pitch-sampler seeds (turn 2-4 into one-line visual directions):
1. **Quiet tool**: monochrome, one accent color, dense but calm, Inter, no illustrations.
2. **Warm editorial**: serif headlines, off-white background, photography led, lots of air.
3. **Bold typographic**: huge type, strict grid, two colors, no imagery.
4. **Friendly illustrated**: soft palette, custom spot illustrations, rounded but not card-heavy.
5. **Dark pro**: dark background, high-contrast data, subtle motion, techy grotesk.
6. **Native and invisible**: system fonts and platform components, polish through spacing only.

## Smart defaults
When the person says "you do it" or "no idea":
- Purpose: dev-ready mockup (apps/web), publish-ready export (graphics), presentable deck (slides).
- Direction: quiet tool / calm neutral, one accent color derived from the brand or the product's subject.
- Type: one sans family (Inter or Geist) with a 1.25 modular scale, body 16 px web / 17 pt iOS.
- Layout: platform conventions, 8 px spacing grid, mobile-first responsive.
- Accessibility: WCAG 2.2 AA, light and dark mode tokens.
- Content: realistic German or English sample content written by the agent, marked for review.
- Format: static HTML/Tailwind mockup for screens (fast to iterate and close to code), PDF plus source for decks and posters.
- Iteration: 2 low-fi directions, pick one, 2 refinement rounds.
- Avoid: lorem ipsum, stock photos of people, generic gradient hero, uniform rounded cards everywhere.
Why: conventions plus one clear accent rarely look bad, are easy to implement, and leave room to add personality once real content exists.

## Scope traps
- **Infinite taste loop**: rounds of "make it pop". Prevent with anchors and anti-goals up front and a fixed number of refinement rounds; each round must name what to change.
- **Design system before product**: building 60 components for 4 screens. Default to tokens plus only the components the agreed screens need.
- **Every screen at once**: 30 screens in one go. Agree on 1-3 key screens first; the rest follow the established pattern.
- **Lorem ipsum layouts**: break on real content. Require the content inventory before high fidelity.
- **Pixel-perfect on the wrong platform**: polished desktop when users are on phones. Ask platform in Quick mode.
- **Deck as document**: 40 dense slides. Ask speaking time; roughly one slide per minute, one message per slide.
- **Brand invention creep**: a poster request turns into a full brand identity. Confirm whether a brand look is in scope or just the single asset.

## Brief sections
- **Design Purpose & Fidelity**: what it's for, artefact list, fidelity level, success test.
- **Audience & Scenario**: who, where, device, key task or message, usage walkthrough.
- **Visual Direction**: chosen anchors, this-or-that choices, anti-goals, imagery and icon set.
- **Brand & Tokens**: colors (hex), typefaces, spacing scale, radius, logo files, existing guidelines link.
- **Content Inventory**: per screen/slide/asset: headings, copy, data fields, images, item counts, states.
- **Platforms & Accessibility**: sizes, breakpoints, print specs, WCAG level, dark mode, motion.
- **Deliverables & Iteration**: format, file structure, export sizes, number of directions and rounds, hand-off requirements.

## Milestones
- **M0 Inputs**: collect references, brand assets, content inventory. Done when every screen/slide has listed content and the direction is chosen or two candidates are named.
- **M1 Directions**: 2-3 low-fi variants of the key screen/slide/poster. Done when the person picks one (or mixes parts).
- **M2 Tokens and key screen**: color, type, spacing tokens applied to the chosen key screen at full fidelity. Done when it passes contrast checks and matches the brief's direction.
- **M3 Full set**: remaining screens/slides/formats using the same tokens and components, including states. Done when every item in the content inventory is placed.
- **M4 Refinement**: agreed feedback rounds. Done when the person approves or the round budget is used.
- **M5 Hand-off / export**: final files in the agreed format, tokens exported, exports at required sizes, short usage notes. Done when files open correctly and are listed with paths.

## Verification
- Screenshot every screen at each target size (e.g. Playwright at 390x844 and 1440x900) and check for overflow, clipped text and horizontal scroll.
- Contrast check all text/background pairs and UI elements against WCAG 2.2 AA; list any exceptions.
- Touch targets at least 24x24 px (44x44 recommended on mobile).
- Real content present: search for "lorem", "placeholder", "TODO".
- Long-content test: longest realistic German strings, 0/1/many items, error and empty states rendered.
- Consistency: all colors and font sizes come from the token set (grep for stray hex values in HTML/CSS).
- Anti-goal check against the brief's list, item by item.
- Print: correct size, 3 mm bleed, 300 dpi images, CMYK or printer's profile if required.
- Decks: slide count matches speaking time, one message per slide, layouts varied, readable from the back of the room (body text at least 24 pt).

## Example opening
Request (~30 words):
> "I need a design for my barber booking app. Customers should book an appointment via QR code. It should look modern, not like every other app. Ideally straight away as HTML."

Excerpt of a good Deep-mode round-1 reply:
> Understood: the booking flow of a barber app, entry via QR code in the shop, the goal is a design that stands out and is delivered as an HTML mockup.
>
> Three directions, pick one or mix:
> **A Quiet tool:** almost black and white, one accent color, very fast to use, in the style of Linear.
> **B Warm editorial:** large serif type, cream background, real photos from the shop.
> **C Bold typographic:** huge type, strict grid, two colors, no images.
>
> 1. Who books, and where? a) customer in the shop, phone in one hand (recommended) b) customer at home, taking their time c) both
> 2. Which screens first? a) choose service, choose time, confirm (recommended) b) plus customer account c) plus a view for the barber
> 3. Are there already colors, fonts or a logo? a) yes, I'll send them b) just one color c) no, suggest something
> 4. What must it never be? Suggestion: no stock photos, no purple gradient, not everything in rounded cards. OK?
> 5. Process: a) two rough directions, you pick, then refine (recommended) b) straight to one finished design
>
> Short is fine: "A, 1a 2a 3c 4 ok 5a". Or "decide for me".
