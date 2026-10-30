# EazyPromptin

**Reads the intent behind a lazy 30-word prompt and turns it into exactly what you meant: a finished result or a full agent brief.**

You type *"i wanna make a game, some dungeon thing with monsters, pixel art, maybe with friends"*. A normal assistant either guesses or fires off a questionnaire. EazyPromptin does what a good senior colleague does: it says what it thinks you mean, shows you concrete options when you haven't decided yet, asks only the one or two questions that actually change the result, and before handing off, simulates the agent that has to build it to find what that agent would still have to guess.

It's an [Agent Skill](https://agentskills.io) (`SKILL.md`), so it runs in Claude Code, claude.ai, Codex, Gemini CLI, Cursor, GitHub Copilot and opencode, with a plain-text build for ChatGPT, Gemini Gems or any model with a system prompt.

[Results](#does-it-actually-work) · [How it works](#how-it-works) · [Install](#install) · [Research](docs/RESEARCH.md) · [Domains](#domains) · [Contributing](#contributing)

---

## Does it actually work?

Blind benchmark against the same model without the skill: simulated people with a **hidden intent** they only reveal when asked the right thing, three terse replies, then "go". A separate judge scores the final result against the hidden intent without knowing which assistant is which.

| | EazyPromptin | Default Claude |
|---|---|---|
| Hidden-intent items captured | **36 / 36** | 34 / 36 |
| High-impact guesses left for the executor | **3** | 8 |
| Unmarked wrong assumptions | **0** | 2 |
| Blind preference | **4 of 4 scenarios** | 0 of 4 |

The first version lost two of the four. Both losses had clear causes (it delivered a prompt when the person wanted the email itself, and it never surfaced a hardware constraint); both were fixed and re-measured. Full method, transcripts, verdicts and honest limits (n=4, simulated users) are in [benchmark/RESULTS.md](benchmark/RESULTS.md).

## How it works

Every round runs an **intent engine** with a visible belief state, built on 2025-2026 research on clarification and intent discovery ([docs/RESEARCH.md](docs/RESEARCH.md) maps every rule to its evidence):

1. **Mine before asking.** Your wording ("for my boss", "with friends", "quick"), earlier messages, files, the repo. Anything it can infer, it doesn't ask.
2. **"My read".** It states its leading hypothesis about what you want, the evidence, the strongest alternative and what's still open. A wrong read costs you one word to correct.
3. **Gate: ask, assume or defer.** A separate step decides whether a gap is worth your time. Separated monitors beat "ask if unclear" in agent studies.
4. **The most informative move.** If your intent isn't formed yet, it **shows** 2-3 contrasting options on named axes instead of asking abstract questions. If it is forming, it asks the 1-3 multiple-choice questions that best **split its competing hypotheses**, goal first, each with a recommended default.
5. **"Assuming:" line.** The highest-impact assumptions it would build on, visible every round, so you can veto them before "go".
6. **Executor audit.** Before delivering, 2-3 simulated readers (a context-free coding agent, a domain expert, a skeptical QA) list what they'd still have to guess. Divergent, high-impact guesses become one last question or a marked assumption.
7. **Short, selective output.** The finished artefact when you asked for the thing; a prompt or a Blueprint (`BRIEF.md`, `PROMPT.md`, `MILESTONES.md`) when an agent will build it. Conditional rules and edge cases explicit, contracts instead of adjectives, every guess marked.

| You write | You get |
|---|---|
| "write an email to my landlord about the heating" | **Quick**: a draft right away, 1-2 questions, then the finished email. |
| "landing page for my tool" | **Standard**: 2-3 rounds, then the page prompt (or the page) with its assumptions listed. |
| "I want to build a game / an app / a SaaS" | **Deep (Blueprint)**: 3-6 phased rounds, audit, then brief + master prompt + milestones (M0 = the thinnest playable or usable slice). |
| *pastes a prompt* "the output is so generic" | Why it's generic, then a rebuilt prompt with real facts instead of adjectives. |

Answer lazily: `1b 2a`, `go` (finish with defaults), `decide for me`, `status`, `deeper X`, `back`, `run it`. Commands work in any language; the coach answers in yours.

**See it in action:** [a full session from 30 words to a game blueprint](examples/game-dungeon-crawler.md), and every benchmark transcript in [benchmark/runs/](benchmark/runs/).

## Install

| Where | How |
|---|---|
| **Claude Code** (plugin) | `/plugin marketplace add justinjd00/eazypromptin` then `/plugin install eazypromptin@eazypromptin` |
| **Any agent** via [skills CLI](https://github.com/vercel-labs/skills) (Claude Code, Codex, Cursor, Gemini CLI, Copilot, opencode, …) | `npx skills add justinjd00/eazypromptin` (add `-g` for global) |
| **GitHub Copilot** | `gh skill install justinjd00/eazypromptin eazypromptin` |
| **Gemini CLI** | `gemini extensions install https://github.com/justinjd00/eazypromptin` |
| **macOS / Linux** script | `curl -fsSL https://raw.githubusercontent.com/justinjd00/eazypromptin/main/install.sh \| bash` |
| **Windows** script | `irm https://raw.githubusercontent.com/justinjd00/eazypromptin/main/install.ps1 \| iex` |
| **claude.ai / Claude desktop** | Download [`dist/eazypromptin.zip`](dist/eazypromptin.zip), then *Settings → Capabilities → Skills → Upload skill*. |
| **ChatGPT Custom GPT, Gemini Gem, Mistral agent, …** | Paste [`dist/chat/instructions.md`](dist/chat/instructions.md) as instructions and upload [`dist/chat/eazypromptin-knowledge.md`](dist/chat/eazypromptin-knowledge.md) as knowledge. |
| **API / Claude Projects / local models** | Use [`dist/eazypromptin-full.md`](dist/eazypromptin-full.md) as the system prompt (everything in one file). |
| **Manual** | Copy `skills/eazypromptin/` to `~/.claude/skills/` (Claude Code) or `~/.agents/skills/` (Codex, Cursor, Gemini CLI, Copilot, opencode). |

The scripts install to `~/.claude/skills` and `~/.agents/skills`. Options: `--claude`, `--agents`, `--all`, `--project`, `--ref <tag>`.

## Usage

Trigger it explicitly with `/eazypromptin` (in Claude Code via the plugin: `/eazypromptin:eazypromptin`), or just ask:

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

In agent sessions with file access the belief state and brief live in `.eazypromptin/<project>/` (`STATE.md`, `BRIEF.md`, `PROMPT.md`, `MILESTONES.md`) and are updated every round; in chat it's delivered in the reply.

## Structure

```
skills/eazypromptin/
├── SKILL.md                    # the loop: deliverable, read, gate, move, update, audit, compile
└── references/
    ├── intent-engine.md        # belief state: hypotheses, slots, formedness, correlated dimensions, cue mining
    ├── question-selection.md   # splitting hypotheses, answerability filters, budgets, interviewer mistakes
    ├── probes.md               # show-don't-ask: variants on named axes, sample outputs, mockups, greyboxes
    ├── executor-audit.md       # simulated readers list what they'd have to guess
    ├── brief-format.md         # selective specs, contracts, spec vs. plan, milestones with drift checks
    ├── prompt-craft.md         # rules for the final prompt
    ├── agent-prompts.md        # extra slots when an agent executes
    ├── discovery-method.md     # phase order and interview techniques for Deep mode
    └── domains/                # one playbook per kind of work
agents/
├── gap-monitor.md              # Claude Code subagent: ask / assume / defer per round
└── executor-auditor.md         # Claude Code subagent: context-free reader of the draft brief
benchmark/                      # scenarios, simulator, judge, transcripts, results
docs/RESEARCH.md                # every rule mapped to its 2025-2026 evidence
```

`SKILL.md` stays short and routes to what's needed (progressive disclosure): a quick email costs little context, a game blueprint gets the full engine. In Claude Code the gate and the audit run as separate subagents; elsewhere the coach switches roles explicitly.

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

Each playbook follows [`_template.md`](skills/eazypromptin/references/domains/_template.md): what people leave out, a phased discovery map with option sets and defaults, inspiration anchors and pitch-sampler seeds, smart defaults, scope traps, brief sections, milestones and verification.

## Contributing

- **New domain:** copy `references/domains/_template.md`, fill it in, add a row to the routing table in `SKILL.md` and to the table above.
- **Build:** `python3 scripts/build.py` regenerates everything in `dist/`. CI fails if `dist/` is stale (`python3 scripts/build.py --check`) or the skill doesn't validate (`python3 scripts/validate.py`).
- **Tests:** `evals/` holds test cases in the format `claude plugin eval` reads. Run them with `claude plugin eval . --allow-tools Write,Edit,Bash`.
- Releases: push a `v*` tag; the workflow attaches the `dist/` files to the GitHub release.

## License

MIT. See [LICENSE](LICENSE).
