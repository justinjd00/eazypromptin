# Brief format and the final package

What you deliver at the end, by depth. Quick mode delivers only a prompt; Standard delivers a prompt with an assumptions list; Deep (Blueprint) delivers the full package below.

## The Blueprint package (Deep mode)

Three artefacts, each with a different job:

| File | Job | Reader |
|---|---|---|
| `BRIEF.md` | The single source of truth: everything decided, assumed and open. | The person, and the agent as reference. |
| `PROMPT.md` | The master prompt that starts the agent: goal, how to work, where the brief is, what to do first. | The agent, at the start of every session. |
| `MILESTONES.md` | The work split into agent-sized milestones, each a self-contained prompt with a verifiable "done when". | The agent, one milestone at a time. |

In an agent session with file access write them to `.prompt-coach/<project-slug>/` (or into the project's `docs/` if the person prefers). In chat, deliver them in the reply as three clearly headed code blocks, or as a document if the interface supports that.

Why three files instead of one giant prompt: agents do their best work on one clearly scoped step at a time with the full picture available for reference. A 400-line prompt asking for everything at once yields a shallow version of everything.

---

## BRIEF.md template

Drop sections that are empty or obvious. Add the domain playbook's extra sections in the "Experience" part.

```markdown
# <Project name>: Brief

> Status legend: ✅ decided by <person> · 🔶 assumed (default, not yet confirmed) · ❓ open

## 1. Vision & why
<2-4 sentences: what it is, for whom, what it should feel like, why the person is making it.>
Reference anchors: <examples and what specifically about them>
Anti-goals: <what it must not become>

## 2. Audience
<who, what they know, what they want, where/how they use it>

## 3. Scope
**Version 1 (MVP):** <bullet list, each ✅/🔶>
**Later:** <explicitly deferred ideas, so nobody builds them now>
**Out:** <explicitly not doing>

## 4. Experience
<domain sections from the playbook: core loop / flows / pages / content / look & feel>

## 5. Tech & constraints
<platform, stack, engine, hosting, budget, time, person's skills, must-use / must-avoid>

## 6. Inputs & assets
<what exists: repo, files, data, art, accounts, texts; where it lives>

## 7. Decisions & assumptions
| Topic | Choice | Status | Why |
|---|---|---|---|

## 8. Milestones (summary)
<M0 … Mn one line each; details in MILESTONES.md>

## 9. Done criteria & verification
<how the person will judge v1; how the agent proves each milestone>

## 10. Open questions
<item → recommended default → what it affects>

## 11. Agent operating rules
<when to ask vs. decide, what not to touch, deliverables, commit/branch conventions, language of code/comments>
```

---

## PROMPT.md (master prompt)

Short. It points at the brief instead of repeating it. Structure:

```markdown
You are building <project> with <person/team>. The full brief is in <path>/BRIEF.md; read it before doing anything and treat it as the source of truth. Items marked 🔶 are assumptions: follow them, but mention it if one turns out to be a bad fit. Items marked ❓ are open: don't decide them silently; use the recommended default and log it.

## Goal of this project
<2-3 sentences from the vision>

## How to work
- Work milestone by milestone from <path>/MILESTONES.md. Start with the first one not marked done.
- Before coding a milestone, write a short plan (files, approach) and <ask for approval | proceed>.
- After each milestone: run its verification, update MILESTONES.md (status + notes), commit with a clear message.
- <stack conventions, code style, language of comments>
- When blocked or facing an irreversible choice (<examples>), stop and ask. Decide reversible things yourself and note them in BRIEF.md under decisions.

## Start now
<the concrete first step, usually M0>
```

## MILESTONES.md

```markdown
# Milestones: <project>

## M0: <name>  [status: todo]
**Goal:** <one sentence>
**Build:** <bullets>
**Not yet:** <what to leave out even if tempting>
**Done when:** <observable, checkable criteria>
**Verify:** <commands / manual test script>

## M1: …
```

Milestone sizing: each should be one to a few agent sessions, end in something runnable or visibly checkable, and build on the previous one. The first milestone is almost always setup + the thinnest possible end-to-end slice ("a character moves on screen", "a user can sign up and see an empty dashboard"). Get to something the person can try as early as possible; that's when real feedback starts.

## Standard mode delivery

One prompt (structure from `prompt-craft.md`), then below it:

```
Assumptions in this prompt: audience barbershop owners · main CTA "Try it free" · Next.js + Tailwind
```

so the person can veto any of them before running.
