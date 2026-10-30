# Domain: Game

## Applies when
The person wants to make a video game, a playable prototype, a game mechanic, a level, a mod, or an experience on a game platform (Roblox, Minecraft, Fortnite UEFN). Signals: "game", "level", "enemies", "player", engine names (Godot, Unity, Unreal, GameMaker, Bevy, Phaser, Roblox Studio, PICO-8), genre words (roguelike, platformer, tower defense, survival, idle, visual novel), "like <game title> but".

Not here:
- A website or app that merely has gamification (points, badges) → `web-app.md` or `mobile-app.md`.
- Game-*adjacent* tools (a Discord bot for a game server, a stats dashboard) → `automation.md` / `web-app.md`.
- Art only (character concept, key art, store capsule) → `design-ui.md`.
- A bug or feature in an existing game repo → start with `code-change.md`, pull slots from here for the gameplay parts.
- A mobile game reads this file plus the store/platform parts of `mobile-app.md`.

## What people leave out
Game ideas arrive as a fantasy ("a dark fantasy game where you hunt monsters") and almost never as a game. The gaps that ruin agent-built games:

1. **The core loop.** What the player does every 30 seconds. Without it the agent builds a menu, a map and nothing fun.
2. **Session and run structure.** 5-minute runs or 40-hour campaign changes saving, content volume and architecture.
3. **Scope reality.** A solo builder with an agent can ship a polished small game; a "small open world RPG" becomes an empty world.
4. **Feel and controls.** Camera, input, responsiveness. Two games with the same mechanics feel completely different; the agent defaults to stiff.
5. **Art pipeline.** Who makes the graphics and in what form. The agent can't draw a consistent sprite set; this must be decided up front (placeholder shapes, asset packs, generated, own art).
6. **Failure and progression.** What happens when you lose, what carries over, what you unlock. This is where motivation comes from.
7. **Target platform and engine.** Changes the whole codebase and what the agent can test.
8. **The first playable.** What the person wants to try *first*, so milestones aim at fun early rather than at systems.

## Discovery map

Show the plan at the start of Deep mode: "Vision → Gameplay → World & look → Tech → Production".

### Phase 1: Vision
Goal: a one-paragraph pitch the person recognises as *their* game.

- **Fantasy** [Q]: what does the player get to *be* or *do* that feels good? Ask open, then mirror it back sharpened. If the person struggles, run the pitch sampler (see Inspiration anchors).
- **Reference anchors** [Q]: "Which 1-3 games come closest, and *what* about them?" Offer examples matched to their words. Always ask what about the reference: "like Hollow Knight" can mean the combat, the map, the art or the difficulty.
- **Mood** [S]: this-or-that in one question: cozy ↔ tense · funny ↔ serious · stylised ↔ realistic · story ↔ sandbox. Answers like "a b a b".
- **Player & why** [S]: who plays it (themselves, friends, kids, Steam audience, portfolio reviewers, a game jam) and why the person is making it (learn, ship, sell, show off, fun with friends). *Why it matters:* a learning project optimises for understanding the code; a commercial one for polish and content; a portfolio piece for one impressive vertical slice.
  a) For me, to learn and have fun (recommended for a first game) · b) To play with friends · c) To publish (itch.io/Steam) · d) Portfolio/job applications · e) Game jam with a deadline
- **Anti-goals** [D]: "What should it definitely not become?" (pay-to-win, grindy, too hard, too childish…).

End of phase: write the pitch in 3-4 sentences + reference anchors and confirm.

### Phase 2: Gameplay
Goal: the core loop and its structure, concrete enough that an agent could build a grey-box prototype.

- **Genre / structure** [Q]: offer the 3-4 closest fits to the pitch, not a list of all genres. Examples: Top-down roguelite (Hades, Enter the Gungeon) · 2D platformer (Celeste, Hollow Knight) · Farming/life sim (Stardew Valley) · Tower defense (Bloons, Kingdom Rush) · Survival crafting (Valheim, Terraria) · Puzzle (Baba Is You, Portal) · Bullet heaven/Survivors-like (Vampire Survivors) · Deckbuilder (Slay the Spire) · Idle/incremental (Cookie Clicker) · Visual novel · Management/tycoon · Racing · Fighting · Rhythm.
- **Core loop** [Q]: propose it as a short chain and let them correct it: "Enter room → fight enemies → pick a reward → next room → boss → run ends → meta upgrade → new run". This is the most important slot; spend a follow-up if it's fuzzy.
- **Scenario walkthrough** [S]: narrate the first two minutes of play in 5-8 short lines (start screen, what you see, first input, first enemy/challenge, first reward) and ask "What's right, what's wrong?". This surfaces controls, camera, onboarding and pacing at once.
- **Player verbs & controls** [S]: what can the player do (move, jump, dash, attack, build, talk, aim) and with what input?
  a) Keyboard + mouse (recommended for PC) · b) Controller · c) Touch · d) Mouse/clicks only
- **Session & run structure** [S] (*decides saving, content volume, difficulty curve*):
  a) Short runs of 5-15 min, restart on death (recommended: little content, lots of replay value) · b) Level-based with progression · c) Continuous campaign with save games · d) Endless/high score
- **Failure & progression** [S]: what happens on failure, what persists?
  a) Permadeath + small meta upgrades · b) Checkpoint, nothing lost · c) Lose resources · d) No failure (cozy/puzzle)
- **Challenge source** [D]: reflexes, tactics/planning, puzzles/logic, resource management, exploration, social.
- **Single- vs. multiplayer** [S] (*expert surfacing: multiplayer multiplies effort 3-5× and needs networking from day one*):
  a) Singleplayer (recommended) · b) Local co-op (one screen) · c) Online co-op/PvP · d) Later, but prepare the architecture
- **Progression systems** [D]: XP/levels, unlock tree, items/loot with rarity, crafting, story chapters, collection. Ask which 1-2 matter; warn against all of them.
- **Economy** [D] (only if there are resources): what's collected, what's spent on, sinks vs. sources.

End of phase: status block (decided / assumed / open) and the core loop in one line.

### Phase 3: World, content & look
Goal: what fills the loop, and how it looks and sounds.

- **Setting** [S]: where/when (fantasy, sci-fi, present day, abstract) and a one-line flavour. Offer 3 options derived from the pitch.
- **Content volume for v1** [S] (*the main scope lever*): how many levels/rooms/biomes, enemy types, items, characters?
  Default proposal for v1: 1 biome, 5-8 room types, 3-5 enemy types + 1 boss, 10-15 upgrades. Make it explicit and small; "later" collects the rest.
- **Story** [S]:
  a) None/barely any (gameplay first, recommended for v1) · b) Light framing story (intro + ending) · c) Story-driven with dialogue · d) Environmental storytelling
- **Visual style** [Q] (*decides the art pipeline; agents can code but not draw consistently*):
  a) Pixel art 16x16/32x32 · b) Low-poly 3D · c) Flat vector/minimal shapes (recommended for a prototype: the agent can generate everything itself) · d) Hand-drawn 2D · e) Realistic 3D (expensive, not recommended solo)
- **Art source** [Q]:
  a) Placeholder shapes now, art later (recommended) · b) Asset packs (Kenney.nl, itch.io, Unity/Godot Asset Library) · c) AI-generated with a fixed style guide · d) I make the art myself · e) Someone else makes it
  If b or c: record the exact pack/style so the agent stays consistent.
- **Camera & perspective** [S]: Side-view · Top-down · Isometric · Third-person 3D · First-person · Fixed screen.
- **Game feel** [D] (*expert surfacing: cheap and makes the biggest difference*): screen shake, hit-stop, particles, knockback, juicy UI, tight input buffering, coyote time for platformers. Ask "Should it feel punchy/arcadey or calm/precise?" and record the answer; the agent adds the matching juice in the polish milestone.
- **Audio** [D]: none in v1 · free SFX packs (Kenney, freesound) · procedural (jsfxr/ChipTone) · own music. Default: SFX pack + one looping track later.
- **UI/HUD** [D]: what's on screen (health, resources, minimap, timer), menus needed in v1 (main, pause, settings, game over).

### Phase 4: Technology & constraints
Goal: a stack the agent can actually build and test, matched to the person's skills and platform.

- **Target platform** [Q]:
  a) PC (Windows/Mac/Linux) (recommended) · b) Browser (itch.io/web) · c) Mobile · d) Console (realistically only later) · e) Roblox/Fortnite UEFN/Minecraft
- **Engine** [Q] (*recommend based on platform, 2D/3D and the person's languages*):
  - **Godot 4 (GDScript or C#)**: free, light, great for 2D and small 3D, text-based scene files that agents can read and edit well. Default for 2D and small 3D.
  - **Unity (C#)**: huge ecosystem and tutorials, heavier editor, scene files less agent-friendly.
  - **Unreal (Blueprints/C++)**: high-end 3D; slow iteration for agents, overkill for most first projects.
  - **Phaser / Excalibur / Kaplay (TypeScript)**: browser 2D, agent can run and test everything in a headless browser. Default for web games and for people who know JS/TS.
  - **Bevy (Rust)**, **LÖVE (Lua)**, **Pygame**, **MonoGame**: for people who want code-first and know the language.
  - **Roblox Studio (Luau)**: when the audience is on Roblox; note that the agent can edit scripts but not drive Studio itself unless tooling (e.g. Rojo) is set up.
  If the person has a preference, take it and only flag real risks.
- **Language & skills** [S]: what the person codes in and how much they want to understand/touch the code. *Why:* decides whether the agent writes idiomatic beginner-readable code with comments, or optimises freely.
- **Agent tooling** [D]: which agent builds it (Claude Code, Codex, Cursor…), and whether it can run the game (headless runs, screenshots, MCP for the engine like a Godot MCP server, browser automation for web). *Why:* verification is only as good as what the agent can observe; plan tests the agent can run itself.
- **Existing assets** [S]: repo, prototype, design doc, art, sounds. Read them if available before asking more.
- **Time & budget** [S]: hours per week, deadline (jam?), money for assets/tools/store fees (Steam Direct fee, Apple developer account).
- **Save system** [D]: none, local JSON, cloud. Derived from run structure; usually decide, don't ask.
- **Multiplayer tech** [D] (only if online): authoritative server vs. P2P, engine-native networking (Godot High-level Multiplayer, Unity Netcode/Mirror/FishNet), Steam networking, hosting. Recommend a vertical slice that proves networking first.

### Phase 5: Production
Goal: an MVP line, milestones that reach fun fast, and rules for the agent.

- **First playable** [Q]: "What do you want to be able to play first of all?" Propose: "One character that feels good, one room, one enemy, and you can win and lose." Everything else waits until this is fun.
- **v1 cut** [S]: show v1 vs. later lists built from all previous answers and confirm the line.
- **Collaboration mode** [S]:
  a) Agent builds, I test after every milestone (recommended) · b) Agent explains and I build along · c) Agent builds everything, I just want results
- **Definition of fun-check** [D]: what the person will look for when testing each milestone ("combat feels punchy", "after dying I want to go again right away").
- **Deliverable & repo** [D]: repo structure, git, builds (export presets, itch.io butler), where builds go.

## Inspiration anchors

Offer anchors that match the person's words, 2-4 at a time, each with *what* about it:
- Combat feel: Hades (dash + combos), Dead Cells, Enter the Gungeon, Hollow Knight
- Cozy: Stardew Valley, A Short Hike, Unpacking, Animal Crossing
- Building/survival: Terraria, Valheim, Factorio, Minecraft
- Minimal but addictive: Vampire Survivors, Brotato, Balatro, Mini Metro
- Puzzle/clever: Baba Is You, Portal, Return of the Obra Dinn
- Narrative: Undertale, Night in the Woods, Disco Elysium
- Small multiplayer fun: Among Us, Lethal Company, Overcooked, Fall Guys

**Pitch sampler seeds.** Turn the person's fantasy into 3 genuinely different mini-pitches by varying genre and structure. For "a game where you're a wizard":
- **A: Spell Rogue**: Top-down roguelite, you combine two elements into new spells, 10-minute runs, a new rune after every room. (Hades × Magicka)
- **B: Tower School**: Cozy management, you run a wizard school, teach students, expand the tower, yearly cycle. (Two Point Campus × Stardew)
- **C: Duel**: 1v1 online wizard duels, spells are drawn with gestures, short matches. (Rocket League-length × gesture controls)
Then: "Which one is closest? You can also mix, e.g. 'A with the setting of B'."

Other seed axes: same fantasy as roguelite / cozy / puzzle / multiplayer party; same genre in three settings; same game at three scopes (jam, 3 months, 1 year).

## Smart defaults
When the person says "decide for me" or "no idea", for a solo builder with an agent:

- **Scope:** small, replayable, systemic (roguelite, survivors-like, puzzle, arcade) over content-heavy (RPG, story, open world). One biome, one character, one boss in v1.
- **Structure:** short runs, permadeath with light meta-progression. Replayability from systems instead of hand-made content.
- **Engine:** Godot 4 + GDScript for desktop 2D; Phaser 3 + TypeScript for browser; respect any engine the person knows.
- **Art:** geometric placeholders with a fixed palette for the prototype, swap to one consistent asset pack (Kenney) or the person's art later. Never mix styles.
- **Input:** keyboard + mouse, controller support later.
- **Singleplayer.**
- **Audio:** SFX pack in the polish milestone, music later.
- **Saving:** settings + meta-progression as local JSON.
- **Collaboration:** agent builds, person play-tests after every milestone.
Record every default as 🔶 assumed in the brief.

## Scope traps
- **"Open world / MMO / RPG with everything"** → ask what the *first 10 minutes* are; build those as v1. Name the trap honestly, with a version that can ship.
- **Multiplayer as an afterthought** → decide in phase 2; retrofitting networking means a rewrite.
- **Content before fun** → milestones must reach a playable core loop before menus, story, settings, save systems.
- **Systems soup** (crafting + skill tree + loot + housing + pets) → pick 1-2 progression systems for v1.
- **Art paralysis** → placeholders until the loop is fun.
- **Procedural everything** → procedural generation is a project of its own; v1 uses hand-placed rooms or simple templates.
- **No end** → define what "a finished run/level/game" is, or testing has no target.

## Brief sections
Add under "Experience" in the brief:
- **Pitch**: 3-4 sentences + reference anchors with what about each.
- **Core loop**: one-line chain + 30-second / 5-minute / session view.
- **First two minutes**: the confirmed scenario walkthrough.
- **Player verbs & controls**: table of action → input.
- **Run / progression structure**: failure, persistence, unlocks.
- **Content list v1**: enemies, rooms/levels, items, with counts; "later" list.
- **Look & feel**: style, palette, camera, art source with exact pack/style guide, game-feel notes, audio plan.
- **UI/HUD & menus**: what's on screen, which menus exist in v1.
- **Tech**: engine + version, language, platform, project structure, how the agent runs/tests the game.

## Milestones
Typical decomposition; adapt to genre. Each milestone ends in something the person can play.

- **M0 Setup & feel**: project, repo, engine settings, placeholder player that moves/jumps/dashes with good feel (acceleration, input buffering), camera. *Done when:* moving around feels good to the person; build runs from a clean checkout.
- **M1 Core loop slice**: one room/level, one enemy or challenge, win and lose conditions, restart. *Done when:* a full loop (start → challenge → win/lose → restart) works and the person wants a second try.
- **M2 Progression**: rewards/upgrades, run structure or level sequence, simple meta-progression and save. *Done when:* choices change how the next part plays.
- **M3 Content pass**: the v1 content list (enemy types, rooms, items, boss), difficulty curve. *Done when:* a full run/level set is playable start to end.
- **M4 Look & sound**: swap placeholders for the chosen art, add game feel (shake, hit-stop, particles), SFX, music. *Done when:* screenshots look consistent; hits feel impactful.
- **M5 UI & flow**: main menu, pause, settings (volume, keybinds), game over/victory screens, tutorialising the first minute. *Done when:* a new player can start, understand and finish without explanation.
- **M6 Ship**: export builds for the target platform, performance check, upload (itch.io butler, Steam build) if wanted. *Done when:* the build runs on a clean machine.

## Verification
Games are hard for agents to verify by looking; plan checks they can run:
- **Build check:** headless export/build succeeds (`godot --headless --export-release`, `npm run build`).
- **Smoke run:** run the game headless for N seconds/frames without errors (`godot --headless --quit-after 600`, Playwright for web games).
- **Logic tests:** unit tests for pure logic (damage formulas, loot tables, save/load roundtrip, procedural generation constraints) with GUT/gdUnit4 (Godot), Unity Test Framework, Vitest/Jest (web).
- **Scripted input:** simulate inputs to check a level is completable or a menu flow works.
- **Screenshots:** capture frames at key moments so the agent (and person) can check layout and art consistency.
- **Debug overlay:** FPS, entity count, state, toggled by a key.
- **Person's fun-check:** each milestone lists 2-3 things the person should try and how it should feel. Fun is the person's call; the agent should ask, not claim.

## Example opening

**Request (~30 words):** "wanna make a game, like a dungeon thing with monsters where you keep getting stronger, pixel art, maybe play it with friends, for pc. got a bit of experience with godot."

**Round 1 reply (excerpt):**

> This is a bigger project, so I'm switching to deep mode: Vision → Gameplay → World & look → Tech → Production, about 5 short rounds. Say "go" to cut it short at any time, or "decide for me" to hand off individual questions.
>
> **Phase 1/5: Vision.** What I'm reading: dungeon, monsters, getting stronger, pixel art, PC, Godot, maybe co-op. But "dungeon + getting stronger" can be three pretty different games:
>
> **A: Roguelite runs**: Short runs through random rooms, pick an upgrade after every room, on death you lose everything except small meta upgrades. (Hades, Enter the Gungeon)
> **B: Dungeon crawler with loot**: Fixed dungeon with floors, items with rarity, your character levels up permanently, save games. (Diablo light, Soul Knight)
> **C: Survivors-like**: You only move, attacks fire automatically, hordes of monsters, a level-up every 30 seconds. (Vampire Survivors, Brotato)
>
> 1. **Which direction?** a) A b) B c) C d) Mix, e.g. "A with the loot from B"
> 2. **Co-op: how important?** (Online co-op multiplies the effort and has to be planned from the start)
>    a) Solo first, co-op later (recommended) b) Local co-op on the same PC c) Online co-op is the core
> 3. **What are you making it for?** a) Learning and fun (recommended for now) b) Playing with friends c) Publishing on itch.io/Steam d) Portfolio
> 4. **Mood, one letter each:** cozy (a) or tense (b) · funny (a) or dark (b) · more story (a) or pure gameplay (b)
>
> Answer e.g. "1a 2a 3b 4 b b b".
