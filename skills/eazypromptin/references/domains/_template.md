# Domain playbook template

Every file in `references/domains/` follows this structure so the coach can rely on finding the same things in the same place. Copy this file to add a new domain. Keep each playbook between ~150 and ~350 lines; deep enough to carry a Deep (Blueprint) session on its own, short enough to read in one go.

Write for the model that runs the coach, in English, in the imperative. Explain *why* a question matters instead of just listing it. Option sets must be concrete (real genres, real stacks, real formats), not placeholders, because the person picks from them.

---

```markdown
# Domain: <Name>

## Applies when
Signals in the request that should route here (phrases, artefacts, verbs), plus neighbouring domains it is often confused with and how to tell them apart.

## What people leave out
The 5-8 gaps that most often ruin results in this domain, each with one line on what goes wrong if the agent guesses.

## Discovery map
Phases in the order a Deep session walks through them. Each phase lists its slots. For every slot:
- **Slot name**: why it matters (one line)
- Question (as you'd ask it), 2-5 concrete options, the recommended default marked, and a "decide for me" fallback rule.
- Depth tag: [Q] asked even in Quick mode, [S] in Standard, [D] only in Deep.

Typically 4-6 phases, 3-6 slots each. Phase 1 is always the vision/goal; the last phase is always production (scope, milestones, verification, handoff).

## Inspiration anchors
How to offer references in this domain (well-known examples, archetypes, "X meets Y" seeds) and 3-6 pitch-sampler seeds the coach can turn into mini-pitches when the person can't describe what they want.

## Smart defaults
A compact default profile for when the person says "decide for me" or "no idea": the safest choice for a solo builder working with an AI agent, and why.

## Scope traps
Common ways projects in this domain balloon or stall, and the question or constraint that prevents each.

## Brief sections
Domain-specific sections to add to the universal brief (see brief-format.md), with a one-line description of what goes in each.

## Milestones
A typical decomposition into agent-sized milestones (M0 setup … Mn polish), each with a concrete, verifiable "done when".

## Verification
How an agent can prove work in this domain is done: commands, checks, manual test scripts, acceptance criteria patterns.

## Example opening
A ~30-word realistic request and an excerpt of a good Deep-mode round-1 reply (understanding line, pitch sampler or anchors, first 3-5 questions with options). Keep it short; it's a calibration example, not a script.
```
