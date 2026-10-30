# Probes: show, don't ask

When intent isn't formed yet, questions fail: the person can't answer what they haven't decided, and abstract questions ("what tone?", "what art style?") get shrugs or random answers. People can recognise what they want long before they can describe it. A probe is a small concrete artefact they can react to; their pick (and especially their "none of these, because…") tells you more than three questions.

## When to probe

- The request is one sentence or uses words like "something", "cool", "modern", "fun".
- The person answered "no idea" or "decide for me" on a dimension that has high impact on the result.
- Feedback is vague: "not quite", "make it better", "more professional".
- Two answers contradict each other (show both readings side by side).

Don't probe dimensions the person has already formed or that have low impact; that's busywork.

## How to build a good probe set

1. **Name the axes first.** Pick the 1-2 dimensions that are still unformed and matter (e.g. *structure*: short runs vs. persistent campaign; *tone*: cozy vs. tense). Every variant must differ on a named axis, so the pick resolves a specific unknown. Variants that differ randomly teach you nothing.
2. **Three variants, genuinely different.** Two is a coin flip, more than three overwhelms. Give each a short name and say in one line what choosing it implies for the build.
3. **Add a wildcard** when the space is wide: one deliberately off-axis option ("or something completely different: …"). It counters anchoring on your first idea.
4. **Label them as probes, not proposals**: "These are to find your direction; pick, mix, or tell me why none fits."
5. **Invite mixing and rejection**: "A with the setting of C" and "none, because…" are both great answers.
6. **Diverge, then converge.** Once they pick or name a property, switch to refining one draft. Go back to divergence only for a dimension that is still vague. Avoid long runs of either.

## Probe types

| Type | Good for | Form |
|---|---|---|
| **Pitch sampler** | Whole-project direction | 3 mini-pitches (2-3 sentences each), each with a reference anchor. |
| **Sample output** | Writing, reports, emails, copy | 2-3 short excerpts (an opening paragraph, a subject line + first sentence) in different tones or structures. |
| **Brief variants** | Any prompt or spec | 2-3 versions of the key paragraph of the brief, differing on one axis. |
| **Scenario walkthrough** | Games, apps, flows | Narrate the first 2 minutes of use in 5-7 lines; ask what's wrong. |
| **Edge-case probe** | Conditional rules | "When X happens, should it A, B or C?" with a concrete situation. |
| **Visual mockup** | UI, sites, layouts, look & feel | A small inline HTML/SVG wireframe or 2-3 layout sketches, if the interface can render them; otherwise a structured text wireframe. |
| **Greybox prototype** | Game feel, interactions, "does this feel right?" | In an agent session: a tiny playable throwaway (a single HTML file with canvas, or a minimal engine scene) of the core loop with placeholder shapes, built in minutes. Ask "does the dash feel right? faster/slower?" Only when feel is the open question and the person can run it; it's a probe, not M0. |
| **Data probe** | Analyses, dashboards | A mock of the final table or chart with fake numbers: "is this the shape of answer you need?" |

Pick the cheapest probe that resolves the uncertainty. A three-line scenario often beats a mockup.

## Example (unformed game idea)

```
My read: a dungeon game you play with friends where you keep getting stronger. "Stronger" and "dungeon" fit three quite different games:

A: Roguelite runs: short 15-min runs, pick 1 of 3 upgrades per room, die and restart a little stronger. (Hades, Soul Knight)
B: Loot crawler: one character you level for weeks, gear with rarities, saves. (Diablo-lite)
C: Horde survivor: you only move, attacks are automatic, hundreds of monsters. (Vampire Survivors)
Wildcard: co-op dungeon *builder*: you build the dungeon and your friends try to survive it.

These are probes to find your direction: pick one, mix ("A with the loot of B"), or tell me why none fits.
```

## Anti-anchoring

Showing examples makes people fixate on them. Counter it:
- Keep variants on clearly different points of each axis, not three shades of your favourite.
- Include the wildcard for wide-open requests.
- When they pick, ask once: "What made you pick it?" The answer tells you which property mattered, which generalises better than the pick itself.
- Flag capability limits early: if a probe implies something the target agent or tool can't deliver (hand-drawn animation sets, realistic 3D, a store release in a week), say so before it becomes an expectation.
