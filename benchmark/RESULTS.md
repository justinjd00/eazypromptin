# Benchmark: Prompt Coach vs. default Claude

Does the coach actually beat a capable model that's simply asked the same thing? This benchmark tests that with simulated people who have a **hidden intent**: what they really want, including things they only mention if something touches them.

## Setup

- **4 scenarios**, each a realistic lazy opening message plus a hidden intent card ([scenarios/](scenarios/)): a game, a small SaaS for a cleaning business, an invoice automation, an email to a landlord.
- **Simulated user** ([user-simulator.md](user-simulator.md)): terse, lowercase, answers only what is asked, reveals card facts only when a question, option or draft touches them, says "idk" to things it doesn't know, and has **at most 3 replies**, the third ending in "go". Personas are deliberately uncooperative because LLM-simulated users are known to be too helpful.
- **Two assistants**, same model (Claude Opus 5.5), same opening message, isolated from each other:
  - **Coach**: follows `skills/prompt-coach` in a plain chat (no subagents, so gate and audit run inline).
  - **Default**: no skill, "respond as you naturally would".
- **Blind judging** ([judge.md](judge.md)): a separate agent per scenario sees the card and both transcripts labelled X/Y in random order and scores the *final deliverable*:
  - intent coverage (each card item correct / wrong / missing)
  - unmarked wrong assumptions
  - HIGH-impact guesses an executor would still have to make
  - items elicited by the assistant vs. volunteered by the person
  - fit of length and form (1-5)
  - overall preference

All transcripts are in [runs/](runs/), all verdicts and the X/Y key in [verdicts/](verdicts/).

## Round 1: v2.0

| Scenario | Coverage (coach / default) | Executor HIGH guesses | Unmarked wrong | Winner |
|---|---|---|---|---|
| SaaS | 10/10 · 10/10 | **1** · 3 | **0** · 1 | **Coach** |
| Automation | **9/9** · 8/9 | **1** · 2 | **0** · 1 | **Coach** |
| Game | 7/9 · **8/9** | 3 · **2** | 0 · 0 | Default |
| Email | 8/8 · 8/8 | 2 · **0** | 1 · **0** | Default |

2:2. The two losses had clear causes:
1. **Email: wrong deliverable.** The person asked for an email; the coach ended with a *prompt that would write* the email. Perfect content, nothing to send.
2. **Game: unsurfaced constraint.** The coach never touched target hardware ("must run on a laptop with integrated graphics"). With the default assistant, the person saw a full plan before "go" and noticed the gap; with the coach the assumption was never visible.

## Fixes (v2.1)

- **Decide the deliverable first** (SKILL.md §2): the finished artefact when they asked for the thing, a prompt/brief only when someone else will execute it. Draft the artefact in round 1, then refine.
- **Visible "Assuming:" line** every round from round 2 on, with the highest-impact assumptions, so the person can veto them before "go".
- **Capacity & environment** (time per week, target hardware, maintenance) as a mandatory slot for builds; target hardware added to the game playbook; the audit now checks for it and for broken internal references.

## Round 2: v2.1 on the two lost scenarios

Fresh coach run and fresh simulated user, judged blind against the *same* default transcripts with the X/Y order swapped.

| Scenario | Coverage (coach / default) | Executor HIGH guesses | Unmarked wrong | Fit | Winner |
|---|---|---|---|---|---|
| Game | **9/9** · 8/9 | **1** · 2 | 0 · 0 | 4 · 4 | **Coach** |
| Email | 8/8 · 8/8 | **0** · 1 | 0 · 0 | **5** · 4 | **Coach** |

In the game rerun the person mentioned the laptop constraint in round 2 because the coach's "Assuming" line showed "normal gaming hardware", and the coach was the only one of the two that captured the 10 h/week budget and sized v1 to it.

## Combined (v2.1 where rerun, v2.0 otherwise)

| | Coach | Default |
|---|---|---|
| Card items captured | **36 / 36** | 34 / 36 |
| HIGH-impact guesses left for the executor | **3** | 8 |
| Unmarked wrong assumptions | **0** | 2 |
| Blind preference | **4 of 4** | 0 of 4 |

## Limits, honestly

- **Small n.** Four scenarios, one run each per condition. Treat this as a strong signal, not a statistically settled result.
- **Simulated people.** Even deliberately terse LLM users are more cooperative than real ones.
- **LLM judge variance.** The same default email got fit 5 from one judge and 4 from another.
- **Mixed versions.** SaaS and automation were run with v2.0; the v2.1 changes (deliverable decision, visible assumptions, capacity slot) shouldn't hurt them but weren't re-measured.
- **Same model on both sides.** The comparison isolates the skill, not the model.
- **Cost.** The coach's packages for big builds are longer (game: ~20k vs ~11k characters). The judges rated fit equal there, but it's a real trade-off.

Rerun it yourself: the scenarios, simulator and judge prompts are plain text; drive them with any agent harness that can run subagents.
