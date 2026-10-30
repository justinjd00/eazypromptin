# Domain: Content Writing

## Applies when
The deliverable is text a human will read: emails, cold outreach, follow-ups, job applications and cover letters, LinkedIn or X posts, newsletters, blog articles, documentation and READMEs, speeches and toasts, video or podcast scripts, landing-page and ad copy, product descriptions.

Signals: "write me", "word this", "draft", "post", "mail to", "cover letter", "text for", "copy", "script", "rewrite this", "make it sound better", a pasted draft with "improve this".

Neighbours and how to tell them apart:
- **Design / UI**: if the person cares about how the page or slide *looks*, route to design-ui; if they care about what it *says*, stay here. A slide deck often needs both: words here, layout there.
- **Code change**: README or docstring edits inside a repo stay here unless they come bundled with code changes.
- **Research / analysis**: if the person needs facts gathered first ("write an article about X market"), note that the research is a precondition and capture it as an input, not something the writer invents.

## What people leave out
The core lesson of this domain: **generic output comes from missing facts, not missing adjectives.** "Make it punchy and professional" changes nothing; "we cut onboarding from 3 weeks to 4 days for a 40-person agency" changes everything. Spend questions on facts, not on style words.

- **The desired reaction**: without it the model writes something "nice" that asks for nothing. Every text should make one specific thing happen (reply, book a call, approve, share, feel reassured).
- **Who exactly reads it**: "recruiters" and "a CTO who has 90 seconds between meetings" produce different texts. Guessing gives a reader-for-everyone, which is a reader-for-no-one.
- **Concrete facts the model cannot know**: numbers, names, dates, results, the one detail that proves the sender has done their homework. If missing, the model invents plausible filler or hollow claims.
- **The sender's real voice**: without samples, the model defaults to polished LinkedIn-speak that the person then has to rewrite line by line.
- **Channel and length limits**: a 400-word cold email on mobile dies unread; a 3-sentence article is useless.
- **Phrases to avoid**: everyone has a list ("I hope this email finds you well", "leverage", "in today's fast-paced world"). If not collected, the first draft will contain them.
- **Relationship context**: first contact, warm intro, reply to an existing thread, or re-engagement after silence. Tone and length depend on it.
- **Constraints that are non-negotiable**: legal claims, brand terms, required links, a fixed call to action, gendered language rules, formal vs informal address (e.g. the formal and informal "you" in German or French).

## Discovery map

### Phase 1: Purpose and reaction
- **Desired reaction** [Q]: the single most predictive slot for quality.
  "What should the reader *do or feel* right after reading?" Options: (a) reply / book a call, (b) say yes to a specific request, (c) understand something and act correctly, (d) share or comment, (e) feel reassured / appreciated. Default: (a) for outreach, (c) for docs. Decide-for-me: infer from text type and write it into Assumptions.
- **Text type and occasion** [Q]: anchors format conventions.
  "What exactly are we writing?" Options: cold email, follow-up after no reply, cover letter, LinkedIn post, blog article, README / docs page, speech, short video script. Default: whatever the request names. Decide-for-me: the closest named type.
- **Why now** [S]: a trigger gives the opening line its reason to exist.
  "Is there a hook in time?" Options: (a) event or news about the reader, (b) a launch or result on your side, (c) a deadline, (d) none, evergreen. Default: (d). Decide-for-me: open with the strongest fact instead of a time hook.
- **Success test** [D]: makes "done" checkable.
  "How will you know it worked?" Options: reply rate, a specific yes, fewer support questions, comments/shares, applause at the right moment. Default: a reply or the requested action.

### Phase 2: Reader
- **Reader profile** [Q]: who, role, what they already know, how much time they have.
  "Who reads this, and what's on their desk?" Options: (a) a decision maker who skims, (b) a specialist who checks details, (c) a broad audience scrolling a feed, (d) people who already know you. Default: (a). Decide-for-me: write for a busy, skeptical skimmer.
- **Reader's problem or interest** [S]: the bridge between their world and your message.
  "What do they care about that this text touches?" Offer 2-3 guesses based on the role and let them pick. Decide-for-me: name the most likely pain for that role and mark it as an assumption.
- **Relationship** [S]: decides formality and how much context is needed.
  Options: cold, warm intro via someone, existing thread, colleague/internal, fan/follower. Default: cold.
- **Objections** [D]: what makes the reader say no.
  "What would make them ignore or refuse this?" Options: no time, wrong person, sounds like spam, too expensive, not convinced you can deliver. Address the top one in the text.

### Phase 3: Facts and substance
This is the phase that fixes generic output. Ask it even in Quick mode if facts are thin.
- **Key facts** [Q]: concrete, checkable, specific to this sender and reader.
  "Give me 3-5 facts I can't invent." Prompt with categories: a number or result, a name or project, a specific detail about the reader, a credential, a date or deadline. Lazy answers are fine as bullet fragments. Decide-for-me: none; the coach must not invent facts. Leave clearly marked placeholders like `[RESULT: e.g. 30% fewer tickets]` and list them under Open questions.
- **Proof** [S]: why should the reader believe it.
  Options: metric, client or employer name, link to work, short story, quote. Default: one metric plus one link.
- **The ask** [Q]: one concrete next step.
  "What exactly do you ask for?" Options: 15-minute call with two time slots, reply with yes/no, look at a link, attend an event, nothing (informational). Default: one low-friction ask. Decide-for-me: a single small ask, never two.
- **Must-include items** [S]: links, legal lines, signature, names, references, job ID.
- **Inputs to read** [S]: job ad, reader's website, previous thread, CV, product page, existing draft. Collect pasted text or URLs; the agent quotes from them instead of guessing.

### Phase 4: Voice, tone, structure
- **Writing samples** [S]: the fastest route to the sender's voice.
  "Paste 1-3 texts you wrote yourself and liked (emails, posts, messages)." Options: (a) paste samples, (b) describe your voice in 3 words, (c) use a reference anchor, (d) neutral default. Default: (a). Decide-for-me: (d), plain, direct, short sentences.
- **Tone anchors** [S]: use this-or-that pairs, not adjectives.
  Formal vs casual, warm vs crisp, confident vs humble, playful vs serious, formal vs informal address. Ask as 3 pairs in one line: "1a/1b 2a/2b 3a/3b".
- **Phrases to avoid** [S]: anti-goals for language.
  "Anything you never want to read in your own text?" Offer a starter list: "I hope this finds you well", "I'm reaching out because", "passionate", "leverage", "synergy", "game changer", "in today's fast-paced world", em dashes, emoji, exclamation marks. Default: avoid the whole starter list.
- **Structure** [S]: pick a proven skeleton.
  Options: (a) hook, relevance, proof, ask (outreach), (b) problem, insight, example, takeaway (post/article), (c) context, steps, troubleshooting (docs), (d) story, point, call (speech), (e) AIDA (ad copy). Default: by text type. Decide-for-me: the matching skeleton.
- **Length and channel** [Q]: hard limits shape every sentence.
  Options: under 80 words (cold email, DM), 120-200 words (follow-up, cover letter paragraph), 150-300 words (LinkedIn post), 800-1500 words (article), 2-5 minutes spoken (~130 words per minute). Default: shortest option that fits the type. Note channel quirks: mobile preview truncates after ~90 characters of the subject plus first line; LinkedIn cuts after ~210 characters before "see more".
- **Language and locale** [Q]: German vs English, de-DE vs de-CH (Swiss German writes "ss" instead of the sharp s), US vs UK spelling.

### Phase 5: Production
- **Variants** [S]: comparison makes picking easy.
  "How many versions?" Options: 1 polished, 2 contrasting (e.g. short vs story), 3 subject lines + 1 body, A/B pair for testing. Default: 2 contrasting.
- **Series or one-off** [D]: a sequence needs consistent facts and escalating asks.
  Options: single text, 3-step outreach sequence (day 0, 3, 8), weekly post series, docs set. Default: single.
- **Review loop** [D]: how the person will give feedback.
  Options: line comments, "more like version B", rewrite a paragraph themselves and let the agent match. Default: pick a version, then one revision round.
- **Deliverable format** [S]: plain text ready to paste, Markdown, HTML email, Google Doc, subject line plus body separated. Default: plain text with subject line on top.

## Inspiration anchors
Offer anchors as voice or format references, not as texts to copy:
- Outreach: "Patrick McKenzie-style plain helpfulness", "a 3-line Basecamp-style email", "the friend-of-a-friend intro".
- Posts: "a Paul Graham essay compressed to 200 words", "a build-in-public update with one real number", "a teardown post".
- Docs: "Stripe docs (task first, then reference)", "the Diataxis split: tutorial, how-to, reference, explanation".
- Speeches: "a wedding toast with one story and one line to raise glasses to", "a 5-minute TED-style talk with one idea".
- Copy: "Apple product page brevity", "Mailchimp's friendly-but-clear voice guide".

Pitch-sampler seeds (turn 2-4 into one-line mini-pitches that differ in strategy, not wording):
1. **The specific compliment**: open with one precise observation about the reader's work, then one sentence on how you fit.
2. **The result first**: open with your strongest number, then the ask.
3. **The tiny ask**: almost no pitch, one question that is easy to answer.
4. **The story**: one 3-sentence anecdote that shows the skill instead of claiming it.
5. **The contrarian take** (posts): state a belief most peers disagree with, then back it with one experience.
6. **The useful gift**: give a small insight or audit up front, ask nothing big.

## Smart defaults
When the person says "decide for me" or "no idea":
- Purpose: one clear action the reader can take in under a minute.
- Reader: busy, skeptical, reading on a phone.
- Length: the shortest band for the text type (outreach under 120 words).
- Structure: hook, relevance, proof, ask.
- Voice: plain, direct, short sentences, active verbs, no buzzwords, no em dashes, no emoji.
- Language: the language of the request; formal address for first contact in German business contexts, informal address for startups and creative industries if the reader's own site uses it.
- Variants: two contrasting versions plus three subject lines.
- Facts: never invented; missing facts become visible `[PLACEHOLDER]` markers listed under Open questions.
Why: short, specific and honest text fails gracefully; long, polished and vague text fails silently.

## Scope traps
- **Endless polishing**: tone tweaks without new facts. Prevent by asking "what fact is missing?" before any "make it better" round.
- **Kitchen-sink content**: every achievement squeezed into one email. Prevent with the rule: one message, one ask, max three proof points.
- **Template-for-everyone**: the person wants "a mail I can send to 50 companies". Agree on a skeleton plus 2-3 personalization slots per reader, and show it filled for one real reader.
- **Voice drift in series**: posts 1 and 5 sound like different people. Capture a voice card (samples, tone pairs, banned phrases) in the brief and reference it in every milestone prompt.
- **Facts invented by the model**: especially in applications and case studies. Agent rule: never add numbers, names or claims not in the inputs.
- **Article without research**: the person expects expertise the inputs don't contain. Make research a separate milestone with sources, or narrow the topic to the person's own experience.

## Brief sections
- **Purpose & Reaction**: text type, the one action or feeling wanted, success test.
- **Reader Card**: role, context, prior knowledge, time available, objections, relationship.
- **Fact Sheet**: bullet list of verified facts, proof points, links, names; placeholders marked.
- **The Ask**: exact call to action, wording constraints, time slots if any.
- **Voice Card**: writing samples (or excerpts), tone pairs chosen, address form, phrases and characters to avoid.
- **Structure & Length**: chosen skeleton, word or time limit, channel quirks, language/locale.
- **Variants & Series**: number of versions and how they differ; sequence timing if relevant.

## Milestones
- **M0 Inputs**: collect samples, facts, reader material. Done when the fact sheet has no unmarked gaps and the voice card is filled.
- **M1 Skeleton**: outline per variant with one line per section and the chosen hook. Done when the person picks a skeleton (or says "go").
- **M2 First drafts**: full variants within length limit. Done when each passes the checklist in Verification.
- **M3 Revision**: apply feedback, merge preferred parts. Done when the person approves one version.
- **M4 Packaging**: subject lines, preview text, alt versions for other channels, follow-up drafts if a sequence. Done when everything is paste-ready in the agreed format.

For Quick mode, M0-M2 collapse into a single prompt.

## Verification
The agent checks each draft against the brief before returning it:
- Word count within limit (state the count).
- The ask appears exactly once and is concrete.
- Every number, name and claim traces to the fact sheet; placeholders are listed, nothing invented.
- No phrase from the avoid list; search explicitly for banned characters (em dash, en dash) and emoji if banned.
- First sentence is about the reader or the strongest fact, not about the sender's intent to write.
- Address form and locale are consistent throughout.
- Read-aloud test for speeches and scripts: estimate spoken time at ~130 words per minute.
- Swap test: if the reader's name could be replaced with any other company and the text still works, it is too generic. Add a reader-specific fact.

## Example opening
Request (~30 words):
> "write me an email to an agency in frankfurt, i want to apply as a working student in web dev. shouldn't sound too stiff but still professional. got experience with vue and php."

Excerpt of a good Deep-mode round-1 reply:
> Got it: an unsolicited application by email to a Frankfurt agency, the goal is an intro call about a working-student position. So the mail doesn't sound like a hundred others, I mainly need facts, not style words.
>
> Three directions, pick one or mix:
> **A Project first:** You open with a concrete Vue/PHP project and a number.
> **B Agency first:** You mention one of the agency's projects that caught your eye and why you fit in there.
> **C Mini question:** Three sentences, one simple question asking whether they're looking for working students.
>
> 1. What should the agency do? a) Reply with a time for a call (recommended) b) Ask for your CV c) Forward you to the right person
> 2. Three facts I can't invent: a project with a result, your availability (hours per week, from when), and one detail about the agency. Keywords are enough.
> 3. Greeting: a) "Dear Ms/Mr [last name]" (recommended for first contact) b) "Hi [first name]", if the agency's own site is on a first-name basis
> 4. Length: a) under 120 words (recommended) b) about 200 words with a short project story
> 5. Do you have a mail or message you wrote yourself and liked? Paste it and I'll match your tone.
>
> Short answers work: "B, 1a 3a 4a" plus your facts. Or "decide for me", and I'll put placeholders in for the missing facts.
