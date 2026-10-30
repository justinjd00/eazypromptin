# Discovery method

This is the interview engine for Standard and Deep mode. The domain playbook tells you *what* to find out; this file tells you *how* to find it out without wearing the person down.

## Contents
1. The universal slots
2. Phases in Deep mode
3. Designing a good question
4. Techniques
5. Handling answers
6. Pacing and when to stop
7. Showing progress

---

## 1. The universal slots

When no playbook fits, or as the skeleton under any playbook:

| Slot | What it answers | Typical gap |
|---|---|---|
| Vision & why | What should exist afterwards, and what's the person really after (fun, money, learning, a portfolio piece, a client)? | The why changes everything: a learning project and a product want different scope. |
| Audience | Who uses or reads it, and what do they already know/want? | "for everyone" |
| Core experience | The one thing it must do or feel like. | Feature lists without a centre. |
| Scope | What's in the first version, what's explicitly out. | No MVP line, so the agent builds everything shallowly. |
| Inputs & assets | What exists already: code, data, art, texts, accounts, examples. | The agent invents what the person already has. |
| Tech & constraints | Stack, platform, budget, time, skills, must-use/must-avoid. | Stack chosen by the agent's defaults rather than the person's reality. |
| Done & verification | How the person will judge success, how the agent can prove it. | "make it good" |
| Operating rules | When the agent should ask, what it must not touch, what it delivers. | Agent stalls or overreaches. |

## 2. Phases in Deep mode

Walk the phases in order. Each phase is one round (occasionally two). The playbook defines the domain-specific phases; the shape is always:

1. **Vision**: what it is, for whom, why, what it feels like. Establish the centre everything else hangs on. Use the pitch sampler here if the idea is fuzzy.
2. **Core**: the main loop, flow or structure. What the person or user actually does, minute to minute.
3. **Content & experience**: everything that fills the core (levels, pages, screens, features, texts), look and feel.
4. **Tech & constraints**: platform, stack, engine, existing assets, the person's skills, budget, time.
5. **Production**: MVP slice, milestones, what the agent does alone vs. with the person, verification, handoff.

Optional phases the playbook may add (monetisation, multiplayer, content pipeline, compliance) slot in between 3 and 4.

Order matters: tech questions before the vision is clear produce stack debates about a product nobody has defined. If the person opens with tech ("in Godot"), record it and still start with vision.

At the start of Deep mode, show the phase plan in one line ("Vision → Gameplay → World & look → Tech → Production") so the person knows how long this takes.

## 3. Designing a good question

A good question:
- **Changes the result.** If either answer leads to the same build, don't ask; decide.
- **Is answerable in two seconds.** Concrete options the person can recognise, not abstract categories. "Like Stardew Valley, like Hades or like Celeste?" beats "Which genre?".
- **Explains its stakes in half a sentence** when that isn't obvious: "(decides whether we need save games)".
- **Has a recommended default** with a reason, so "go" and lazy answers are safe.
- **Offers a way out**: "decide for me" is always implicitly allowed; mention it once at the start.
- **Asks one thing.** Split compound questions.

Format:

```
2. **How long is a play session?** (decides the save system and amount of content)
   a) 5-10 min, short runs to play in between (recommended for a first project)
   b) 30-60 min sections with save points
   c) Open-ended, you play as long as you like
```

Option count: 2-4 usually, 5 at most. Order: recommended first, or in a natural scale (small → big).

## 4. Techniques

Use these deliberately; each solves a specific kind of stuck.

**Pitch sampler**: when the person can't describe what they want, or the idea is one sentence. Write 2-4 mini-pitches (2-3 sentences each) that are genuinely different interpretations of their words, each with a short name. Ask them to pick, mix ("A with the setting of C") or reject all. This is the single most effective technique for vague ideas, because choosing is easy and describing is hard.

**Reference anchors**: ask for or offer well-known examples: "Which 1-3 games/apps/sites come closest, and what exactly about them?" Always ask *what* about the reference, because "like Minecraft" can mean the building, the survival, the look or the multiplayer.

**Scenario walkthrough**: narrate the first minutes of use and let the person correct it: "You start the game, see …, press …, after 2 minutes …". Corrections to a concrete story surface details no question would. Best in phase 2.

**This-or-that**: contrasting pairs to locate taste quickly: "more cozy or more stressful? more story or more sandbox? more realistic or more stylised?" Three or four pairs in one question, answered "a b a".

**Anti-goals**: "What must it never become?" People often know clearly what they hate. One question, open text, optional.

**Decide for me**: when the person delegates, apply the playbook's smart defaults, tell them in one line what you chose and why, and record it as *assumed*.

**Expert surfacing**: raise decisions the person doesn't know exist, briefly: "One point people rarely think about: should players be able to lose progress? That decides …". Do this for the 2-3 decisions per domain that matter most; the playbook names them.

## 5. Handling answers

- **Lazy codes** ("1b 2a"): apply them; if a code is ambiguous, pick the most plausible reading and say so.
- **Free text that answers more than was asked**: harvest everything, update all affected slots, skip questions it already covers.
- **Contradictions** with earlier answers: point it out in one line and offer the two readings.
- **"No idea"**: offer a pitch sampler for that slot or decide (with reason), mark as assumed, move on. Never re-ask.
- **Scope explosions** ("and multiplayer, and crafting, and an open world"): welcome the vision, then separate "Version 1" from "later" and confirm the line.
- **The person changes direction**: re-run phase 1 with the new framing; keep compatible answers.

## 6. Pacing and when to stop

- Questions per round: Quick ≤3, Standard ≤4, Deep 3-5.
- Rounds: Quick 1, Standard 2-3, Deep 4-7. If you're past 7 in Deep, you're over-polishing; close.
- Stop asking when the remaining open items wouldn't change what the agent builds first. Unresolved items that matter later go into "Open questions" in the brief with a recommended default.
- If answers are getting shorter and lazier, the person is tiring. Compress: merge the remaining phases into one round, or offer "go".

## 7. Showing progress

At the end of each Deep phase, show a compact status (not the whole brief):

```
Status after phase 2:
Decided: top-down roguelite, runs 10-15 min, melee + dash, 1 player character
Assumed: 3 biomes, permadeath with meta upgrades
Open: art style, engine, scope of v1
```

This lets the person catch misunderstandings early and feel the progress. Keep it to a few lines; the full brief lives in the file or appears on "status".
