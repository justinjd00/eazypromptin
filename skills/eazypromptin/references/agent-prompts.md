# Agent prompts: what to add beyond a chat prompt

An agent works for a long time without the person watching, touches real files and tools, and decides on its own when it's finished. Vague agent prompts fail in predictable ways: the agent fixes the wrong thing, touches files it shouldn't, declares victory without checking, or stalls on a question nobody is there to answer. These slots prevent that.

In Deep mode these slots feed the brief (see `brief-format.md`): they land in the scope, done criteria and agent operating rules sections, and in each milestone's "Done when" and "Verify".

## Extra slots for agent mode

| Slot | What to pin down | Typical question if missing |
|---|---|---|
| Scope | Which repo, folder, feature, files. What is explicitly out of scope. | "Only the checkout, or the cart too?" |
| Starting state | How to reproduce the problem, current behaviour vs. expected. | "How do you notice the bug, what happens and what should happen?" |
| Done criteria | Observable conditions: tests pass, page loads under X, endpoint returns Y. | "How will you know it's fixed?" |
| Verification | How the agent proves it: run tests, start the dev server and click through, compare output. | Usually don't ask; propose a default. |
| Guardrails | Things not to touch (prod DB, migrations, public API, other branches), no new dependencies, no force push. | "May it add dependencies / change the schema?" |
| Autonomy | When to stop and ask vs. decide and note the decision. | Default: decide on reversible things, ask before irreversible ones. |
| Deliverable | Commit, PR, branch, a summary, a file. What the final message should contain. | "At the end, a PR or just a local commit?" |

## Look before you ask

In an agent session you can usually answer half these questions yourself: read the README, `package.json`/`composer.json`, the test setup, the file the person mentioned, recent git log. Do that first, then fold what you found into the draft as context ("Stack: Laravel 11 + Vue 3, tests with Pest") instead of asking.

## Skeleton for a finished agent prompt

```
## Goal
<what should be true afterwards, and why>

## Context
<stack, relevant files/folders, what you found, prior attempts>

## Task
<the concrete ask; steps only if the order matters>

## Boundaries
<out of scope, don't touch, no new deps, etc.>

## Done when
- <observable criterion 1>
- <observable criterion 2>

## Verify
<how to verify: commands to run, flows to click through>

## If you get stuck
<ask vs. decide-and-note; what counts as irreversible>

## At the end
<deliverable + what the summary should contain>
```

Drop sections that would be empty or obvious. A small bugfix might only need Goal, Context, Done when, Verify.

## Splitting big tasks

If the request is really several tasks ("build auth, payments and an admin dashboard"), say so and propose an order, with one prompt per step or a plan-first prompt ("First write a plan in PLAN.md, wait for approval, then implement step 1"). One giant prompt for a week of work tends to produce a shallow version of everything.
