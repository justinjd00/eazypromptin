# Intent engine

The belief state you maintain throughout a session. LLMs update beliefs about a user poorly when the state stays implicit in the chat; they do much better when it is written down and rewritten after every answer. So write it down.

## Contents
1. Hypotheses
2. Slot table
3. Formedness
4. Correlated dimensions
5. Update rules
6. Cue mining
7. Where the state lives

---

## 1. Hypotheses

Keep 2-4 competing interpretations of what the person ultimately wants. A hypothesis is not a feature list; it's a coherent picture of the finished thing and why they want it.

```
H1 (leading): couch co-op roguelite, short runs, played with friends tonight-style. Evidence: "with friends", "keep getting stronger", "a bit of godot".
H2: loot crawler with a persistent character, weeks of play. Evidence: "keep getting stronger" read as long-term progression.
H3: survivors-like horde game. Evidence: "monsters", "stronger", fits "a bit of godot". Weak.
```

How to generate them:
- Write them one after another, each one deliberately different from the ones before (vary the core activity, the audience, the scale, the purpose). Sequential generation yields more diverse interpretations than asking for "a few interpretations" at once.
- Include at least one that differs in **purpose** (learn vs. ship vs. impress vs. solve a problem at work), because purpose changes scope more than any feature does.
- Drop any hypothesis that contradicts something the person already said. Re-check this every round; hypotheses that drift away from the history are the most common failure.

Show only the leading hypothesis and the strongest alternative in "My read". Keep the rest internal.

## 2. Slot table

The universal slots, each with a state and an impact rating. Domain playbooks add their own.

| Slot | What it answers |
|---|---|
| Goal & why | What should exist afterwards, and the real reason (fun, money, learning, portfolio, a client, a deadline). |
| Audience | Who uses or reads it, what they know, what they want. |
| Core | The one thing it must do or feel like. |
| Scope | What's in v1, what's later, what's out. |
| Conditional rules & edge cases | "If X then Y", error handling, limits, what happens when things go wrong. |
| Constraints | Stack, platform, budget, skills, must-use / must-avoid, non-functionals (security, performance, privacy). |
| Capacity & environment | Time available (hours per week, deadline), target devices and hardware (low-end laptop? phone? old browsers?), who maintains it. Forgotten by people and coaches alike, and it changes scope and tech more than most features; always surface it for builds, at least as a visible assumption. |
| Inputs & assets | What exists already and where. |
| Done & verification | How the person will judge success; how the agent proves it. |
| Operating rules | When the agent asks vs. decides, what it must not touch, what it delivers. |

States:
- **known**: the person said it (quote it).
- **inferred**: you derived it from cues or context (name the cue). Shown in My read, confirmable with one word.
- **assumed**: you chose a default because the slot is low-impact; visible in the brief as an assumption.
- **open**: unknown and still matters.
- **conflict**: two things the person said don't fit together. Always the first thing you raise next round.

Impact: **high** if different values produce a different build or a costly rework, **low** if the agent can adjust it in minutes. Only high-impact open or conflict slots are question candidates.

Spend effort on conditional rules, edge cases, constraints and non-functionals. Models guess format and obvious conventions well on their own and guess conditional requirements badly; people omit exactly those.

## 3. Formedness

How much of the intent exists in the person's head right now. Decide it every round from their language:

| Formedness | Signals | Your move |
|---|---|---|
| **Unformed** | One-line idea, "something like", "cool", "idk", vague feedback ("not quite", "make it better"), answers that contradict each other. | Probes: 2-3 contrasting options on named axes (`probes.md`). Don't ask abstract questions; they can't be answered yet. |
| **Forming** | Picked a direction, has preferences when shown options, answers multiple choice quickly. | Targeted multiple-choice questions that split hypotheses (`question-selection.md`). Probes only on the one dimension still vague. |
| **Formed** | Precise answers, names specifics, corrects details. | Converge: draft, confirm conditional rules, close. |

Formedness differs per dimension: someone can be fully formed on "co-op with my friends" and unformed on art style. Probe the unformed dimension, ask about the forming ones.

## 4. Correlated dimensions

One answer often settles several slots at once. Use these priors to update multiple slots from a single answer, and prefer questions whose answer moves many slots:

- **Purpose: learning** → readable code, comments, smaller scope, person wants to touch the code, slower milestones with explanations.
- **Purpose: ship/sell** → polish, content volume, store/legal requirements, analytics, performance matter.
- **Purpose: portfolio/application** → one impressive vertical slice, clean repo and README, demo-ability over breadth.
- **Audience: investors/boss/client** → formal tone, numbers first, brevity, a decision or ask at the end.
- **Audience: friends/self** → fun and speed over robustness, fewer edge cases, no compliance work.
- **"Quick", "just", "simple"** → minimal scope, defaults everywhere, Quick mode; but check once whether "simple" means simple to build or simple to use.
- **"With friends" (games)** → co-op decision is high impact; local is far cheaper than online.
- **Deadline mentioned** → scope becomes the main lever; milestones must reach a usable state early.
- **Non-expert signals** (no jargon, "idk how") → ask about behaviour and examples only, never about implementation; stronger defaults.
- **Expert signals** (names libraries, versions, patterns) → fewer explanations, respect their choices, ask about trade-offs they care about.

Treat these as priors, not facts: they set the leading hypothesis and get confirmed through My read.

## 5. Update rules

After every answer:
1. Apply the answer to every slot it touches (including correlated ones).
2. Strike hypotheses it rules out; if only one survives, it becomes the working spec.
3. If the answer contradicts an earlier one, mark **conflict** and raise it first next round, offering both readings.
4. If the answer was "decide for me" or "no idea", apply the playbook's smart default, mark **assumed**, never re-ask.
5. If the person picked "other, because…", the *because* is the most valuable signal in the session; mine it for new cues and possibly a new hypothesis.
6. Re-check every remaining hypothesis against the full history (not just the last answer).
7. Rewrite the compact state.

## 6. Cue mining

Implicit preferences hide in phrasing. Turn each into an inferred slot with its evidence:

| They say | Likely means |
|---|---|
| "for my boss / the client / investors" | Polished, formal, decision-oriented, low risk tolerance |
| "quick", "just", "real quick" | Minimal scope; speed over completeness |
| "I'm swamped", "no time" | Strong defaults, few questions, Quick mode unless stakes are high |
| "properly", "flesh this out", "before the agent starts" | Deep mode is welcome |
| "like X" | A reference anchor; ask *what* about X |
| "maybe", "or something" | That dimension is unformed; probe it |
| "I know a bit of Y" | Use Y; keep code readable; avoid exotic stacks |
| A tool or stack named casually | Constraint unless contradicted |
| Emotional words ("hate", "love", "annoying") | Strong preference or anti-goal; record it |

## 7. Where the state lives

- **Agent session with files**: `.prompt-coach/<slug>/STATE.md` (hypotheses, slot table with states and evidence, conflicts), rewritten every round, next to `BRIEF.md`. It survives context limits and the person can edit it.
- **Chat**: in your reasoning, rewritten every round; shown on "status" and compressed at the end of each Deep phase:

```
Status after phase 2
Decided: couch co-op roguelite, 15-20 min runs, Hades-like combat, controller-first
Inferred (say if wrong): you'll play it with 1 friend, not 3; dark tone
Assumed: Godot 4 + GDScript, placeholder art until combat feels good
Open: setting, content volume
```

Store every belief with its source (said / inferred from / assumed because). A bare claim without its source is how a coach starts confidently building on its own guesses.
