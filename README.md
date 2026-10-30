# Prompt Coach

**Turns a lazy 30-word prompt into a full agent brief, interactively.**

You type *"I want to make a game, some dungeon thing with monsters, pixel art, for PC"*. Instead of an agent guessing its way into a generic prototype, Prompt Coach walks you through five short rounds, proposes concrete options at every step and ends with a brief, a master prompt and milestone prompts your coding agent can build from without guessing.

It is an [Agent Skill](https://agentskills.io) (`SKILL.md`), so it runs in Claude Code, claude.ai, Codex, Gemini CLI, Cursor, GitHub Copilot and opencode, and there is a plain-text build for ChatGPT, Gemini Gems or any model with a system prompt.

[Install](#install) · [How it works](#how-it-works) · [Domains](#domains) · [Contributing](#contributing)

---

## What it does

| You write | Prompt Coach does |
|---|---|
| "write me a job application" | **Quick**: a sharp v1 prompt right away with its guesses marked, plus up to 3 questions you answer with "1a 2b". |
| "landing page for my tool" | **Standard**: 2-3 rounds, then a final prompt with a list of the assumptions inside it. |
| "I want to build a game / an app / a SaaS" | **Deep (Blueprint)**: 4-7 phased rounds (vision → core → content & look → tech → production) using pitch samplers, reference anchors and scenario walkthroughs, ending in `BRIEF.md`, `PROMPT.md` and `MILESTONES.md`. |
| *pastes a prompt* "the output is so generic" | Explains *why* it's generic, cuts the filler, rebuilds it with real facts. |

Things that make it different from "ask clarifying questions":

- **Draft first, then ask.** You always get something concrete to react to, because recognising what you want is easier than describing it.
- **Every question has options and a recommended default.** Answer with `1b 2a`, say `go` to finish with defaults, or `decide for me`.
- **Pitch sampler.** When the idea is fuzzy it offers 2-4 genuinely different mini-pitches to pick or mix.
- **Domain expertise.** Playbooks surface the decisions you didn't know existed (multiplayer from day one? tenant model? art pipeline?) and push back on scope that won't ship.
- **Decided vs. assumed vs. open.** The final brief marks what you said, what it guessed and what's still open, so the agent doesn't treat guesses as facts.
- **Milestones that reach something usable fast.** M0 is always the thinnest playable/usable slice, with verifiable "done when" criteria.
- **Runs it, too.** Say `run it` and it executes the final prompt in the same session.

Commands work in any language, and the coach answers in whatever language you write in.

**See it in action:** [a full session from 30 words to a game blueprint](examples/game-dungeon-crawler.md) (unedited).

## Install

| Where | How |
|---|---|
| **Claude Code** (plugin) | `/plugin marketplace add justinjd00/prompt-coach` then `/plugin install prompt-coach@prompt-coach` |
| **Any agent** via [skills CLI](https://github.com/vercel-labs/skills) (Claude Code, Codex, Cursor, Gemini CLI, Copilot, opencode, …) | `npx skills add justinjd00/prompt-coach` (add `-g` for global) |
| **GitHub Copilot** | `gh skill install justinjd00/prompt-coach prompt-coach` |
| **Gemini CLI** | `gemini extensions install https://github.com/justinjd00/prompt-coach` |
| **macOS / Linux** script | `curl -fsSL https://raw.githubusercontent.com/justinjd00/prompt-coach/main/install.sh \| bash` |
| **Windows** script | `irm https://raw.githubusercontent.com/justinjd00/prompt-coach/main/install.ps1 \| iex` |
| **claude.ai / Claude desktop** | Download [`dist/prompt-coach.zip`](dist/prompt-coach.zip), then *Settings → Capabilities → Skills → Upload skill*. |
| **ChatGPT Custom GPT, Gemini Gem, Mistral agent, …** | Paste [`dist/chat/instructions.md`](dist/chat/instructions.md) as instructions and upload [`dist/chat/prompt-coach-knowledge.md`](dist/chat/prompt-coach-knowledge.md) as knowledge. |
| **API / Claude Projects / local models** | Use [`dist/prompt-coach-full.md`](dist/prompt-coach-full.md) as the system prompt (everything in one file). |
| **Manual** | Copy `skills/prompt-coach/` to `~/.claude/skills/` (Claude Code) or `~/.agents/skills/` (Codex, Cursor, Gemini CLI, Copilot, opencode). |

The scripts install to `~/.claude/skills` and `~/.agents/skills`. Options: `--claude`, `--agents`, `--all`, `--project`, `--ref <tag>`.

## Usage

Trigger it explicitly with `/prompt-coach` (in Claude Code via the plugin: `/prompt-coach:prompt-coach`), or just ask:

```
help me flesh this out properly before claude code starts: i want to make a game ...
make this prompt better: <prompt>
ask me what you need first, then build it
```

Commands you can use at any point:

| Command | Effect |
|---|---|
| `go` | Stop asking, fill the rest with smart defaults (marked as assumptions), deliver. |
| `decide for me` | Delegate the current question or everything left. |
| `status` | Show the current brief. |
| `deeper X` | More questions on X. |
| `quick` / `deep` | Switch depth. |
| `back` | Revise the last answer. |
| `run it` | Execute the final prompt now. |

In agent sessions with file access the brief lives in `.prompt-coach/<project>/` (`BRIEF.md`, `PROMPT.md`, `MILESTONES.md`) and is updated every round; in chat it's delivered in the reply.

## How it works

```
skills/prompt-coach/
├── SKILL.md                    # depth selection, round format, commands, finishing
└── references/
    ├── discovery-method.md     # interview engine: phases, question design, techniques, pacing
    ├── brief-format.md         # BRIEF.md / PROMPT.md / MILESTONES.md templates
    ├── prompt-craft.md         # rules for writing the final prompt
    ├── agent-prompts.md        # extra slots when an agent executes (scope, verification, guardrails)
    └── domains/                # one playbook per kind of work
```

`SKILL.md` stays short and routes to what's needed: the coach reads the matching domain playbook plus the method files only when the request calls for them (progressive disclosure), so a quick email fix costs little context and a game blueprint gets the full method.

## Domains

| Playbook | For |
|---|---|
| `game.md` | Video games, prototypes, mods, Roblox/Godot/Unity/Unreal/web games |
| `web-app.md` | Web apps, SaaS, dashboards, internal tools, marketplaces |
| `website.md` | Landing pages, marketing sites, portfolios, business sites |
| `mobile-app.md` | iOS/Android/cross-platform apps |
| `automation.md` | n8n/Make/Zapier flows, scripts, scrapers, bots, AI pipelines |
| `data-analysis.md` | Analyses, reports, spreadsheet tools, KPI dashboards |
| `research.md` | Comparisons, market/competitor research, "which X should I use" |
| `content-writing.md` | Emails, applications, posts, articles, docs, copy |
| `code-change.md` | Bugfixes, performance, refactors, features in an existing codebase |
| `design-ui.md` | Screens, mockups, design systems, visual identity, slides |

Each playbook follows [`_template.md`](skills/prompt-coach/references/domains/_template.md): what people leave out, a phased discovery map with option sets and defaults, inspiration anchors and pitch-sampler seeds, smart defaults, scope traps, brief sections, milestones and verification.

## Contributing

- **New domain:** copy `references/domains/_template.md`, fill it in, add a row to the routing table in `SKILL.md` and to the table above.
- **Build:** `python3 scripts/build.py` regenerates everything in `dist/`. CI fails if `dist/` is stale (`python3 scripts/build.py --check`) or the skill doesn't validate (`python3 scripts/validate.py`).
- **Tests:** `evals/` holds test cases in the format `claude plugin eval` reads. Run them with `claude plugin eval . --allow-tools Write,Edit,Bash`.
- Releases: push a `v*` tag; the workflow attaches the `dist/` files to the GitHub release.

## License

MIT. See [LICENSE](LICENSE).
