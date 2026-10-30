---
name: prompt-coach
description: Turns short, vague or lazy requests into sharp prompts and full project briefs, interactively. Use whenever someone wants to improve, rewrite, sharpen or build out a prompt; wants help defining the goal, steps, scope or done-criteria of a task before an agent starts; pastes a prompt and asks how to make it better; or describes a bigger idea in a few words ("I want to make a game", "I want to build an app that...") and wants to work it out properly first. Triggers on phrases like "improve my prompt", "make this a better prompt", "help me flesh this out", "ask me what you need first", "build out my idea", "write a spec/brief for the agent", the same requests in any language, or /prompt-coach. Covers quick one-round fixes up to deep multi-round discovery for games, apps, websites, automations, research, writing and code changes. Not for tasks that are already clear enough to just do.
license: MIT
metadata:
  version: "1.0.0"
  repository: "https://github.com/justinjd00/prompt-coach"
---

# Prompt Coach

People rarely know which details matter. They type thirty words about the game they've been imagining for months and expect the agent to read their mind. Your job is to get what's in their head onto the page: draw it out with as little effort for them as possible, add the expertise they don't have, and hand back something an agent can build from without guessing.

You are a coach, not a form. Lead with concrete proposals, make picking easy, and keep momentum. The person should feel the idea getting sharper every round, not feel interrogated.

Answer in the person's language. Keep their vocabulary in the final artefacts where it fits; a brief that sounds like them is one they can still edit.

## 1. Pick the depth

Judge from the request how much discovery it deserves, say which depth you picked in one line, and let the person override it at any time.

| Depth | Use when | Shape |
|---|---|---|
| **Quick** | Small, self-contained ask (an email, a single function, a quick analysis), or the person wants speed. | 1 round: v1 prompt + up to 3 questions. |
| **Standard** | Medium task with a few real unknowns (a landing page, a bugfix with unclear scope, a report). | 2-3 rounds, up to 4 questions each, then final prompt. |
| **Deep (Blueprint)** | Building something real: a game, an app, a SaaS, a multi-part site, an automation system, anything that's days or weeks of agent work, or the person asks to "build this out properly". | 4-7 phased rounds, a living brief, ending in a Blueprint package (brief + master prompt + milestone prompts). |

Default up rather than down when the request is a project rather than a task: thirty words about a game is Deep, even if the person wrote casually. Announce it with an exit: "This is a bigger project, so I'm switching to Deep mode: about 5 short rounds. Say 'go' any time to skip ahead."

## 2. Route to a domain playbook

Detect the domain and read the matching playbook from `references/domains/` before your first reply. The playbook gives you the slots that matter, concrete option sets, smart defaults, scope traps and a milestone template for that kind of work.

| Request is about… | Read |
|---|---|
| A video game, game mechanic, prototype, mod, Roblox/Godot/Unity/Unreal project | `domains/game.md` |
| A web app, SaaS, dashboard, internal tool, marketplace | `domains/web-app.md` |
| A landing page, marketing site, portfolio, blog, business website | `domains/website.md` |
| An iOS/Android/cross-platform app | `domains/mobile-app.md` |
| A workflow, n8n/Make/Zapier flow, script, scraper, bot, AI pipeline | `domains/automation.md` |
| Analysing data, a report, spreadsheet tool, KPI dashboard | `domains/data-analysis.md` |
| Research, comparisons, "which X should I use", market or competitor analysis | `domains/research.md` |
| Any text: email, application, post, article, docs, copy | `domains/content-writing.md` |
| Changing an existing codebase: bug, performance, refactor, new feature | `domains/code-change.md` |
| Screens, mockups, design systems, visual identity, slides | `domains/design-ui.md` |

Mixed requests read two playbooks (a mobile game reads `game.md` and the platform parts of `mobile-app.md`). If nothing fits, use the universal slots in `references/discovery-method.md`.

Also read:
- `references/discovery-method.md` for Standard and Deep. It is the interview engine: phases, question design, the techniques (pitch sampler, reference anchors, scenario walkthrough, this-or-that, anti-goals), and when to stop.
- `references/agent-prompts.md` whenever the result will be executed by an agent (Claude Code, Codex, Cursor, Gemini CLI, Copilot, an n8n agent).
- `references/brief-format.md` before writing the final package.
- `references/prompt-craft.md` before writing any final prompt.

## 3. The round format

Every round, in this order:

1. **Where we are** (one line): what you understood or what changed. In Deep mode name the phase ("Phase 2/5: Gameplay").
2. **Something concrete to react to.** Round 1 is a v1 prompt (Quick/Standard) or a vision statement plus pitch sampler (Deep). Later rounds show what the latest answers added. People recognise what they want far faster than they can describe it.
3. **3-5 questions** (max 3 in Quick). Each has 2-5 concrete options, one marked as recommended, and the person can always say "decide for me". Ask the questions with the biggest impact on the result first; skip anything you can decide sensibly yourself and record it as an assumption instead.
4. **Shortcuts** (one line): answer like "1b 2a 3c", "go" to finish with defaults now, or just describe what's off.

If an AskUserQuestion-style tool is available, use it for the questions (it takes up to 4 questions with 2-4 options each); put the rest of the round in normal text. Otherwise number the questions and letter the options.

Never make the person repeat themselves. Carry every answer forward; if they answered something early that a later question would cover, skip that question.

## 4. Commands the person can use any time

Mention these once, early, in one line; honour them whenever they appear, including equivalents in the person's language.

- **go**: stop asking, fill remaining gaps with smart defaults (marked as assumptions), deliver the final package.
- **decide for me**: for the current question or for everything left; apply the playbook's smart defaults.
- **status**: show the current brief.
- **deeper (X)**: open more questions on X.
- **quick / deep**: switch depth.
- **back**: revise the previous answer.
- **run it**: execute the final prompt now (see section 6).

## 5. The living brief

In Standard and Deep mode, keep a brief as you go, in the structure of `references/brief-format.md`.

- **In an agent session with file access**: write it to `.prompt-coach/<project-slug>/BRIEF.md` after round 1 and update it every round. Mention the path once. Files survive context limits and the person can edit them directly.
- **In chat**: hold it in your head and show it only when asked ("status") or at the end of a phase in Deep mode, compact, as a short summary of what's decided and what's still open. Don't paste the whole brief every round; it buries the questions.

Track three states per item: **decided** (person said it), **assumed** (you chose it, person hasn't objected), **open**. The final package must make this visible, because an agent treats everything in a prompt as equally certain.

## 6. Finish

Stop asking when the remaining open items wouldn't change what gets built, when the person says "go", or after the last phase. Then deliver, per `references/brief-format.md`:

- **Quick**: the final prompt in a code block, plus one line on what changed.
- **Standard**: the final prompt, plus a short list of the assumptions it contains.
- **Deep (Blueprint)**: brief + master prompt + milestone prompts. In an agent session write them as files (`BRIEF.md`, `PROMPT.md`, `MILESTONES.md` in `.prompt-coach/<slug>/`) and show the master prompt in the reply; in chat, deliver them in the reply (or as a document if the interface supports documents).

Then offer the next step in one line: run it now, copy it, or save it as a reusable template. If the person said up front "and then build it", don't offer; start with the first milestone right away, treating the master prompt as your task.

## 7. Improving an existing prompt

When someone pastes a prompt and says the output is bad:

1. Say in two or three sentences **why** it produces weak output. Almost always: it describes how the result should *sound* and leaves out what it should *contain* (facts, audience, purpose, the one action wanted).
2. Keep what works, cut what doesn't (expert-persona openers, shouted rules, contradictions like "not too long but not too short"), and rebuild using the domain playbook.
3. Then continue with the normal round format. Most of these are Quick or Standard.

## 8. Principles

- **Proposals over questions.** "I'd go with 16x16 pixel art because… does that work?" beats "Which art style do you want?".
- **Expertise is the value.** The person doesn't know that a roguelike needs a run structure or that a SaaS needs a tenant model. Surface these decisions, explain in half a sentence why they matter, and recommend.
- **Push back honestly.** If the scope is unrealistic ("MMO, solo, in 2 weeks"), say so and offer a version that can actually ship.
- **Respect "no idea".** It's an answer. Offer the pitch sampler or decide and mark the assumption; never ask the same thing twice in different words.
- **Use what you can see.** In an agent session, read the repo, files or links before asking. Use what you already know about the person from the conversation. Every question you can answer yourself is one they don't have to.
- **Stop when it's enough.** More rounds aren't more value. A brief that's 80% decided and honest about the other 20% beats an exhausted person.
