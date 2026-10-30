# Example: from 30 words to a game blueprint

An unedited Deep-mode session with eazypromptin. The person types a vague 30-word idea and answers lazily; four rounds later there is a brief, a master prompt and milestones Claude Code can build from.

---

## Round 1

**User:**

> i wanna make a game, some dungeon thing with monsters where you keep getting stronger, pixel art, maybe with friends, for pc. i know a bit of godot. help me flesh this out properly before claude code starts

**EazyPromptin:**

This is a bigger project, so I'm switching to **Deep mode**: Vision → Gameplay → World & look → Tech → Production, about 5 short rounds. At the end you get a brief, a master prompt for Claude Code and one prompt per milestone.

Commands you can use any time: **go** (stop asking, I fill the rest with sensible defaults), **decide for me** (for one question or everything), **status** (show what's decided so far), **back** (change your last answer).

**Phase 1/5: Vision.** What I've got so far: dungeon, monsters, you keep getting stronger, pixel art, PC, Godot (you know a bit), maybe with friends. That's a solid starting point, but "dungeon + getting stronger" can be three quite different games:

**A: Roguelite runs.** Short runs (10-20 min) through randomly ordered rooms. After each room you pick one of three upgrades, so every run builds differently. You die, you lose the run, but keep a few small permanent unlocks. *(Hades, Enter the Gungeon, Soul Knight)*

**B: Dungeon crawler with loot.** A dungeon with floors you push deeper into. Monsters drop items with rarities, your character levels up permanently, you save and continue. Getting stronger comes from gear and levels. *(Diablo-light, Wizard of Legend's loot side)*

**C: Survivors-like.** You only move; attacks fire automatically. Hordes of monsters, a level-up every 30 seconds or so, and after a few minutes the screen is chaos. Very fast to get fun, very little content needed. *(Vampire Survivors, Brotato)*

1. **Which direction is closest?**
   a) A, roguelite runs (recommended: the "keep getting stronger" feeling every few minutes, with little hand-made content needed)
   b) B, crawler with loot
   c) C, survivors-like
   d) Mix, e.g. "A with the loot of B"

2. **How important is playing with friends?** (Online co-op roughly triples the work and has to be built in from day one; adding it later usually means a rewrite)
   a) Solo first, but structure the code so co-op is possible later (recommended)
   b) Local co-op on one PC, couch style (much cheaper than online)
   c) Online co-op is the core of the game, it's pointless solo
   d) Not needed

3. **What are you making it for?** (Decides whether we optimise for code you understand, or for polish and content)
   a) To learn Godot properly and have fun doing it (recommended for where you are now)
   b) To actually play it with my friends
   c) To publish it on itch.io or Steam
   d) Portfolio / showing it off

4. **Mood, one letter each:**
   cozy (a) or tense (b) · funny (a) or dark (b) · some story (a) or pure gameplay (b)

5. **Optional: any game you already have in your head?** One or two titles and *what* about them (the combat, the look, the loot, the co-op chaos).

Shortcut: answer like "1a 2a 3b 4 b b b", or just tell me what feels off.

---

## Round 2

**User:**

> 1a 2b 3b 4 b b b. combat like hades

**EazyPromptin:**

Got it: roguelite runs, couch co-op on one PC, made to play with your friends, tense, dark, pure gameplay, and Hades-style combat. That fits together well. Local co-op is the cheap kind of multiplayer, but it still has to be in from the first milestone (two players, one shared camera, two input devices), so I'll treat it as core, not an add-on.

**Your pitch, sharpened:**
> A dark, tense top-down pixel-art roguelite for 1-2 players on one PC. You fight through a dungeon room by room with fast, Hades-style combat: attack, special, dash. After every cleared room each player picks an upgrade, so your builds snowball over a 15-20 minute run. Die and the run is over, but you keep a little something for the next attempt. No story to speak of; the fun is the fights and the builds.

Anchors: **Hades** (dash-heavy combat, room → reward → room structure), **Enter the Gungeon / Soul Knight** (top-down dungeon rooms, couch co-op feel).

**Phase 2/5: Gameplay.** Here's how I picture the first two minutes. Tell me what's wrong:

1. Main menu → "Press a button to join". Player 2 presses a button on their controller and pops in.
2. You both spawn in a small safe room at the dungeon entrance. You can test your attack, special and dash on a training dummy.
3. Walk through the door → first combat room. The doors lock, 6-8 skeletons and bats come at you in two waves.
4. Combat: basic attack combo, a slower heavy special, a short dash with invincibility frames to dodge through enemies. Hits have small knockback and screen shake.
5. Room cleared → doors open, a reward appears. Each player picks 1 of 3 upgrades (e.g. "attacks set enemies on fire", "dash leaves a damaging trail").
6. Choose the next door (each shows its reward type) → next room. Every few rooms a harder elite room, at the end of the floor a boss.
7. If one player goes down, the other can revive them by standing next to them for a few seconds. Both down → run over → short summary → back to the entrance with your earned currency.

**Core loop:** enter room → fight → pick upgrade → choose door → … → boss → die or win → spend meta currency → new run.

1. **Does the walkthrough match what you imagine?**
   a) Yes, that's it
   b) Mostly, but… (tell me what to change)

2. **Controls for co-op?** (Hades-style combat plays best on controller; two keyboards on one PC don't work)
   a) Controller for both players, keyboard + mouse also works when you play solo (recommended)
   b) Player 1 on keyboard + mouse, player 2 on controller
   c) Both on controllers only

3. **What carries over between runs?** (This is where the "keep getting stronger" feeling lives long-term)
   a) A currency you spend on small permanent upgrades, like Hades' mirror: more HP, one extra dash, a reroll (recommended)
   b) Unlocking new weapons or characters to start runs with
   c) Both a and b
   d) Nothing, every run starts from zero

4. **Weapons in version 1?** (Each weapon is its own moveset plus upgrades, so this is the biggest scope lever in combat)
   a) One weapon per player with a fixed moveset, upgrades change how it behaves (recommended for v1, more weapons later)
   b) 2-3 weapons to choose from at the start of a run
   c) Each player picks a character with its own weapon and abilities

5. **Co-op details, decide for me?** My proposal: each player picks their own upgrades, enemies scale up a bit with 2 players, downed players can be revived, the run ends when both are down, no friendly fire.
   a) Sounds right (recommended)
   b) Change something (tell me what)

Run length I'm setting to 15-20 minutes with 1 floor + boss for v1; say so if you want it different.

Shortcut: "1a 2a 3a 4a 5a", **go** to skip ahead with defaults, or just describe what's off.

---

## Round 3

**User:**

> 1a 2a 3a 4a 5a. i have no art, decide for me

**EazyPromptin:**

Locked in: controller co-op (keyboard + mouse solo), meta currency for permanent upgrades, one weapon per player in v1, and my co-op rules. Art is now my call too.

**Status after phase 2:**
- **Decided:** top-down roguelite, 1-2 players couch co-op, Hades-style combat (attack, special, dash), pick 1 of 3 upgrades per room, meta currency between runs, one weapon in v1, revive downed players, run ends when both are down, controllers + keyboard/mouse solo
- **Assumed:** runs of 15-20 min, 1 floor + boss in v1
- **Open:** setting, content volume, upgrade system, tech details

**Phase 3/5: World & look.** Here's what I decided on art, and why:

- **Placeholders first, real art at milestone 4.** For the first milestones Claude Code uses coloured shapes (blue square = player 1, red = player 2, enemies by colour). Tuning combat feel with final sprites wastes time, and it keeps you from getting stuck on art before the game is fun.
- **Then one free pixel-art pack, 16x16: "16x16 DungeonTileset II" by 0x72 on itch.io.** It has dungeon tiles, several heroes and a good set of monsters (skeletons, orcs, demons, slimes), all animated, all in one style. That matters: an agent can't draw a consistent sprite set, and mixing packs looks cheap right away. Backup if it's missing something: Kenney's "Tiny Dungeon" (same 16x16 size). Check the licence on the pack page before you publish anything.
- **Game feel: punchy and arcadey,** like Hades. Hit-stop on heavy hits, screen shake, knockback, damage numbers, enemies flash white when hit, dash with a short afterimage.
- **Camera:** shared camera that follows the midpoint between both players and zooms out a bit when they move apart, but rooms are sized so it never has to zoom far.
- **Audio:** none at first, then a free SFX pack (Kenney) in the polish milestone, one looping dungeon track later.
- **Rooms:** hand-built room layouts that get shuffled each run, no procedural generation. Procedural dungeons are a project of their own, and with 8-10 good layouts the runs already feel different.

1. **Setting / flavour?** (Gives the agent a theme for enemies, rooms and upgrade names)
   a) Cursed crypt: catacombs full of undead, bone piles, candles, green flames (recommended: fits the asset pack perfectly)
   b) Abandoned mine: corrupted creatures, rails, crystals glowing in the dark
   c) Demon fortress: lava, chains, imps and demons, red and black

2. **How much content in version 1?** (The biggest scope lever; everything else goes on a "later" list)
   a) 1 floor, 8-10 room layouts, 4 enemy types + elite variants, 1 boss, 12-15 upgrades (recommended)
   b) Smaller: 5 rooms, 2-3 enemy types, 1 boss, 8 upgrades, so you're playing together sooner
   c) Bigger: 2 floors with 2 bosses, 6+ enemy types, 25 upgrades

3. **How should upgrades work?** (This is what makes runs different from each other)
   a) 3-4 themed families like Hades' gods, e.g. fire, frost, poison, lightning. Each upgrade changes your attack, special or dash, and families combine (frozen enemies take double lightning damage) (recommended)
   b) Simple stat upgrades: +damage, +speed, +HP, +crit chance
   c) Items you find, like Enter the Gungeon: passive items with weird effects

4. **On screen during a run, decide for me?** My proposal: HP bar and dash charges per player in the corners, meta currency counter, room counter, boss HP bar at the bottom during the boss. Menus in v1: main menu with "press to join", pause, run summary. Settings menu later.
   a) Fine (recommended)
   b) Change something (tell me what)

Next up is phase 4 (Tech), which will be short since you already know Godot.

Shortcut: "1a 2a 3a 4a", **go** to skip ahead with defaults, or just describe what's off.

---

## Round 4

**User:**

> 1a 2a 3a 4a. go

**EazyPromptin:**

All set: cursed crypt, the recommended v1 content, Hades-style upgrade families, and my HUD proposal. You said **go**, so I've filled the Tech and Production phases with defaults. Each one is marked 🔶 in the brief, so you can veto anything before Claude Code starts.

What I picked for those two phases, in short: **Godot 4 + GDScript** (you know a bit of it, and the text-based scene files are easy for an agent to read and edit). Code stays **readable with comments**, since you want to understand and tweak it. **Claude Code builds, you play-test after every milestone.** The **first playable** is two coloured squares fighting one enemy in one room. The working title **"Crypt Run"** is a placeholder.

Here's your Blueprint package: three parts, each in its own block. Save them as `BRIEF.md`, `PROMPT.md` and `MILESTONES.md` in a `docs/` folder of your new Godot project, then paste the master prompt into Claude Code.

---

### 1. BRIEF.md

````markdown
# Crypt Run (working title): Brief

> Status legend: ✅ decided · 🔶 assumed (default, not yet confirmed) · ❓ open

## 1. Vision & why
A dark, tense top-down pixel-art roguelite for 1-2 players on one PC. You fight through a cursed crypt room by room with fast, Hades-style combat: attack, special, dash. After every cleared room each player picks an upgrade, so builds snowball over a 15-20 minute run. Death ends the run, but meta currency buys small permanent upgrades for the next attempt. No real story; the fun is the fights, the builds and the couch co-op chaos. ✅
Made to play with friends on one PC. ✅
Reference anchors:
- Hades: dash-heavy, responsive combat; room → reward → next room structure; upgrade families that combine; mirror-style meta upgrades. ✅
- Enter the Gungeon / Soul Knight: top-down dungeon rooms, couch co-op feel. 🔶
Anti-goals: no grinding, no story cutscenes, no stiff or floaty controls, no mixed art styles. 🔶

## 2. Audience
The person and their friends, playing together on one PC with controllers. Mostly gamers who know Hades-style games, so no long tutorial needed; a training dummy in the start room is enough. 🔶

## 3. Scope
**Version 1:**
- 1-2 players local co-op, drop-in "press to join" ✅
- One weapon per player, fixed moveset: attack combo, heavy special, dash with i-frames ✅
- 1 floor: start room + 8-10 hand-built combat room layouts, shuffled per run, elite rooms, 1 boss room 🔶
- 4 enemy types + elite variants, 1 boss ✅
- 12-15 upgrades in 3-4 families (fire, frost, poison, lightning) with cross-family synergies ✅
- Pick 1 of 3 upgrades per player after each room; door choice shows reward type ✅
- Meta currency + permanent upgrades between runs (more HP, extra dash, reroll) ✅
- Revive downed teammate; run ends when all players are down ✅
- HUD, main menu, pause, run summary ✅
- Save meta progression locally 🔶

**Later:** more weapons, characters, more floors and bosses, settings menu with keybinds, music, online co-op, achievements, Steam release.
**Out:** procedural level generation (shuffled hand-built rooms instead), story/dialogue, friendly fire, online multiplayer in v1.

## 4. Experience

### Core loop
Enter room → doors lock → fight 2-3 waves → room cleared → each player picks 1 of 3 upgrades → choose next door (shows reward) → … → elite rooms → boss → win or die → summary → spend meta currency in the start room → new run. ✅
- 30 seconds: dodge, hit, dash through enemies, stay alive.
- 5 minutes: build synergies through upgrade picks, survive an elite room.
- Session: one 15-20 min run, then "one more".

### First two minutes ✅
1. Main menu → "Press a button to join". Player 2 joins with a button press.
2. Both spawn in a safe start room at the crypt entrance, with a training dummy.
3. Through the door → first combat room, doors lock, 6-8 skeletons and bats in two waves.
4. Combat: attack combo, slower heavy special, short dash with invincibility frames. Hits have knockback and screen shake.
5. Room cleared → doors open → each player picks 1 of 3 upgrades.
6. Pick the next door → next room. Elite rooms every few rooms, boss at the end of the floor.
7. A downed player can be revived by standing next to them for ~3 seconds. All down → run over → summary → back to the start room with earned currency.

### Player verbs & controls ✅
| Action | Controller | Keyboard + mouse (solo) |
|---|---|---|
| Move | Left stick | WASD |
| Aim | Right stick (falls back to move direction) | Mouse |
| Attack | X / Square | Left click |
| Special | Y / Triangle | Right click |
| Dash | A / Cross | Space |
| Interact / revive | B / Circle (hold) | E (hold) |
| Pause | Start | Esc |
Two players: both on controllers, or one on keyboard + mouse and one on controller. Two keyboards on one PC are not supported.

### Run & progression
- Permadeath per run; meta currency (e.g. "bone shards") dropped by enemies and bosses, kept after death. ✅
- Meta upgrades bought in the start room: max HP, extra dash charge, one reroll per run, small damage bonus. 🔶 (exact list and prices: agent proposes, person tunes)
- Upgrades are per player; each player picks their own. ✅
- Enemies get ~1.5× HP with 2 players. 🔶 (tune in playtests)

### Upgrade families 🔶 (names and exact effects are the agent's proposal; the person tunes)
- **Fire:** burn damage over time; e.g. attack ignites, dash leaves a fire trail.
- **Frost:** slow, then freeze after stacks; e.g. special chills an area.
- **Poison:** stacking damage, spreads on death.
- **Lightning:** chain damage between nearby enemies.
- Synergies: e.g. frozen enemies take double lightning damage, poisoned enemies explode when burned.
- Each upgrade modifies attack, special, dash, or is a passive. Upgrades are data (Resources), so new ones can be added without new code.

### Content list v1
- Enemies (4 + elites): skeleton (melee chaser), bat (fast, erratic), skeleton archer (ranged), ghoul/brute (slow, heavy, telegraphed attack). Elite = stronger variant with an extra trait. 🔶
- Boss: one crypt boss with 2 phases and readable, telegraphed attacks. 🔶
- Rooms: start room, 8-10 combat layouts, 1 boss room. ✅
- Upgrades: 12-15 across the families. ✅

### Look & feel
- Setting: cursed crypt. Catacombs, undead, bone piles, candles, green flames. Dark palette with green accent light. ✅
- Art: geometric placeholders until M4 (player 1 blue, player 2 red, enemies by colour), then **one** asset pack: "16x16 DungeonTileset II" by 0x72 (itch.io), backup Kenney "Tiny Dungeon". Never mix packs. Check the licence before publishing. ✅
- Perspective: top-down 2D, 16x16 tiles, pixel-perfect scaling (nearest filter, integer scaling). 🔶
- Camera: shared, follows the midpoint between players, slight zoom-out when they separate; rooms sized so it never zooms far. ✅
- Game feel: punchy and arcadey. Hit-stop on heavy hits, screen shake, knockback, white hit flash, damage numbers, dash afterimage, input buffering for attacks and dash. ✅
- Audio: none until M4, then a free SFX pack (Kenney); one looping track later. ✅

### UI/HUD & menus ✅
- HUD: HP bar + dash charges per player in the corners, meta currency counter, room counter, boss HP bar at the bottom during the boss.
- Menus v1: main menu with "press to join", pause, run summary. Settings menu later.

## 5. Tech & constraints
- Platform: PC (Windows first; Linux/Mac exports if free). ✅
- Engine: Godot 4 (latest stable 4.x), GDScript. 🔶
- The person knows a bit of Godot: code should be readable, typed GDScript, short comments on the "why", one script per clear responsibility. 🔶
- Input: Godot InputMap with per-device handling so two players can use separate devices. 🔶
- Data: enemies, upgrades and rooms defined as Resources / scenes so content can be added without touching core code. 🔶
- Save: meta progression as local JSON in `user://`. 🔶
- Tests: GUT or gdUnit4 for pure logic (damage, upgrade stacking, save/load). 🔶
- Budget: free tools and assets only. 🔶

## 6. Inputs & assets
None yet. No repo, no art. Asset pack is downloaded by the person at M4. ✅

## 7. Decisions & assumptions
| Topic | Choice | Status | Why |
|---|---|---|---|
| Genre | Top-down roguelite runs | ✅ | Constant "getting stronger" feeling with little hand-made content |
| Multiplayer | Local co-op 1-2 players | ✅ | Play with friends without online networking cost |
| Combat | Hades-style attack/special/dash | ✅ | Person's reference |
| Meta progression | Currency + permanent upgrades | ✅ | Long-term motivation |
| Weapons v1 | One fixed moveset | ✅ | Biggest scope lever in combat |
| Art | Placeholders → 0x72 DungeonTileset II | ✅ | Agent can't draw consistent sprites |
| Rooms | Shuffled hand-built layouts | ✅ | Procedural gen is a project of its own |
| Engine | Godot 4 + GDScript | 🔶 | Person knows some Godot; agent-friendly text scenes |
| Run length | 15-20 min, 1 floor | 🔶 | Fits one sitting with friends |
| Collaboration | Agent builds, person tests each milestone | 🔶 | Fun is the person's call |

## 8. Milestones (summary)
- M0 Setup & feel: project, two placeholder players moving and dashing, shared camera
- M1 Core combat slice: attack/special/dash, one enemy, one room, win/lose/restart, revive
- M2 Run structure & upgrades: room sequence, doors, upgrade picks, 1-2 families
- M3 Content pass: all enemies, elites, boss, all room layouts, all upgrade families
- M4 Look & sound: asset pack, animations, game feel, SFX
- M5 Meta & UI flow: meta currency, permanent upgrades, save, HUD, menus, summary
- M6 Ship: Windows export, clean-machine test

## 9. Done criteria & verification
v1 is done when two friends can start the game, join with controllers, play a full run through the crypt to the boss, die or win, spend currency, and want to start another run, without the person explaining anything.
Agent verifies each milestone with a headless build, a smoke run, logic tests and screenshots (details in MILESTONES.md). The person does the fun-check.

## 10. Open questions
- Exact meta upgrade list and prices → agent proposes in M5 → affects pacing.
- Boss design → agent proposes 2-phase crypt boss in M3 for approval → affects M3 scope.
- Final game name → keep "Crypt Run" → affects nothing technical.

## 11. Agent operating rules
- Read this brief before each session; work one milestone at a time.
- Decide reversible things yourself and log them in section 7. Ask before: adding plugins/addons, changing the engine version, changing a ✅ item, deleting the person's files.
- Never mix art styles; placeholders until M4.
- Commit after each milestone with a clear message; keep the project runnable at every commit.
- Code and comments in English, typed GDScript.
````

---

### 2. PROMPT.md (paste this into Claude Code)

````markdown
You are building "Crypt Run" (working title), a top-down pixel-art roguelite with local co-op, in Godot 4 with GDScript, together with me. I know a bit of Godot and want to understand and tweak the code later.

The full brief is in docs/BRIEF.md, and the milestones are in docs/MILESTONES.md. Read both before doing anything and treat the brief as the source of truth. Items marked 🔶 are assumptions: follow them, but tell me if one turns out to be a bad fit. Items marked ❓ are open: use the recommended default and log your choice in the brief's decisions table.

## Goal of this project
A dark, tense roguelite for 1-2 players on one PC: fight through a cursed crypt room by room with fast Hades-style combat (attack, special, dash), pick an upgrade after each room, and get stronger across runs with meta currency. It's for playing with my friends, so co-op and combat feel matter more than content volume.

## How to work
- Work milestone by milestone. Start with the first milestone not marked done.
- Before coding a milestone, give me a short plan (scenes, scripts, approach) and wait for my OK.
- Local co-op is core from M0: every player-related system must work for 1 or 2 players on separate input devices. Don't build single-player first and retrofit.
- Write readable, typed GDScript with short comments explaining why, not what. One clear responsibility per script. Content (enemies, upgrades, rooms) as Resources/scenes so it can be added without touching core code.
- Use coloured geometric placeholders until M4. Don't import or invent art earlier.
- After each milestone: run its Verify steps, update its status and notes in MILESTONES.md, commit with a clear message, and tell me exactly what to try in my fun-check.
- Decide reversible things yourself and log them. Stop and ask before adding addons/plugins, changing the Godot version, changing anything marked ✅, or deleting files you didn't create.
- Fun is my call. Don't claim something feels good; tell me what to test and ask.

## Start now
Read the brief, then propose your plan for M0 (Setup & feel).
````

---

### 3. MILESTONES.md

````markdown
# Milestones: Crypt Run

## M0: Setup & feel  [status: todo]
**Goal:** Two placeholder players that move and dash in a way that already feels good.
**Build:**
- Godot 4 project, git repo with a Godot .gitignore, folder structure (scenes/, scripts/, resources/, tests/, docs/)
- Pixel-perfect settings: 16x16 grid, nearest filtering, integer scaling, a base resolution like 480x270
- Player scene: 8-direction movement with acceleration/deceleration, dash with i-frames and cooldown, dash input buffering
- Device-based input: player 1 on keyboard+mouse or controller 1, player 2 on controller; drop-in "press any button to join"
- Shared camera on the players' midpoint with slight zoom-out when they separate
- A test room with walls and a debug overlay (FPS, player states) on F3
**Not yet:** combat, enemies, art, menus.
**Done when:** both players can join, move and dash independently in one room; the camera keeps both in view; the project runs from a clean checkout.
**Verify:** `godot --headless --quit-after 600` runs without errors; a screenshot of two players in the room; I test movement and dash with a controller.
**Fun-check for me:** Does moving feel responsive, not floaty? Does the dash feel snappy?

## M1: Core combat slice  [status: todo]
**Goal:** One room, one enemy type, a full fight from start to win or lose.
**Build:**
- Attack combo (3 hits), heavy special, both aimed (right stick / mouse, fallback to move direction)
- Health, damage, hurtboxes/hitboxes, knockback, i-frames on hit
- One enemy: skeleton (melee chaser) with a simple state machine (idle, chase, telegraph, attack, hurt, die)
- Room that locks its doors, spawns 2 waves, and unlocks when cleared
- Downed state + revive by holding interact nearby (~3 s); run over when all players are down; restart
- Basic juice placeholders: white hit flash, small screen shake
**Not yet:** upgrades, multiple rooms, art, more enemies.
**Done when:** 1 or 2 players can clear the room or die, revive works, and restart returns to a fresh room.
**Verify:** smoke run without errors; unit tests for the damage and health logic; scripted test that spawns the room and kills all enemies to check that the doors unlock.
**Fun-check for me:** Do hits feel like they land? Do I want to play the room again?

## M2: Run structure & upgrades  [status: todo]
**Goal:** A run of several rooms where upgrade choices change how you play.
**Build:**
- Run manager: start room → sequence of combat rooms from a pool of 3-4 layouts → end
- Doors that show the reward type; choosing one loads the next room
- Upgrade system as Resources: modifiers on attack, special, dash and passives; stacking rules
- Per-player pick screen: 1 of 3 upgrades after each room, both players choose at the same time
- First 2 families (fire, frost), 6-8 upgrades, including one cross-family synergy
- 2-player enemy HP scaling
**Not yet:** boss, other enemy types, meta progression, art.
**Done when:** a run of 5+ rooms is playable and two runs with different picks play noticeably differently.
**Verify:** unit tests for upgrade stacking and synergy logic; smoke run through a scripted run; screenshot of the pick screen with two players.
**Fun-check for me:** Do the picks feel meaningful? Does a good build feel strong?

## M3: Content pass  [status: todo]
**Goal:** The full v1 floor, playable from start room to boss.
**Build:**
- Remaining enemies: bat, skeleton archer, ghoul/brute; elite variants with one extra trait
- Remaining families (poison, lightning), 12-15 upgrades total, 2-3 synergies
- 8-10 room layouts, elite rooms, room shuffling per run
- Boss: 2 phases, telegraphed attacks (propose the design to me before building it)
- Difficulty curve over the floor
**Not yet:** final art, meta progression, menus.
**Done when:** a full run from start to boss kill or death works and takes roughly 15-20 minutes.
**Verify:** smoke run; tests that every room layout is loadable and every upgrade applies without errors; screenshots of each enemy type.
**Fun-check for me:** Is the boss fair but tense? Does the run drag anywhere?

## M4: Look & sound  [status: todo]
**Goal:** Replace placeholders with one consistent pixel-art style and make combat feel punchy.
**Build:**
- Import "16x16 DungeonTileset II" by 0x72 (I'll download it into assets/; ask me if it's missing), TileMap for rooms, animated sprites for players, enemies and boss
- Map any gaps to Kenney "Tiny Dungeon" only if necessary, and tell me which
- Crypt mood: dark palette, green accent lighting (Godot 2D lights), candles/flames
- Game feel: hit-stop on heavy hits, tuned screen shake, damage numbers, dash afterimage, death particles
- SFX from a free Kenney pack for hits, dash, pickups, door, death
**Not yet:** music, settings menu.
**Done when:** screenshots look consistent, with no placeholder shapes left in normal play.
**Verify:** screenshots of the start room, a combat room and the boss; smoke run.
**Fun-check for me:** Does it look like one game? Do hits feel heavier than before?

## M5: Meta progression & UI flow  [status: todo]
**Goal:** The full loop from main menu to "one more run".
**Build:**
- Meta currency drops, kept after death; save/load as JSON in user://
- Permanent upgrades bought in the start room (propose the list and prices to me)
- HUD: HP + dash charges per player in the corners, currency, room counter, boss HP bar
- Main menu with "press to join", pause menu, run summary screen
**Not yet:** settings/keybinds menu, music.
**Done when:** a new player can start, join, play a run, see the summary, buy a meta upgrade and start again, without explanation.
**Verify:** unit test for the save/load roundtrip; scripted menu flow; screenshots of the HUD with two players and of the summary.
**Fun-check for me:** After dying, do we want to go again right away?

## M6: Ship  [status: todo]
**Goal:** A build my friends can run.
**Build:** Windows export preset, icon, version number, performance check with 2 players in the busiest room.
**Done when:** the exported build runs on a different PC without Godot installed.
**Verify:** `godot --headless --export-release "Windows Desktop" build/CryptRun.exe` succeeds; I test it on a friend's PC.
````

---

**Assumptions to veto before you start:** Godot 4 + GDScript · readable code with comments · agent builds, you test each milestone · base resolution 480x270 · meta upgrade list proposed by the agent · working title "Crypt Run".

Next step: put the three files into `docs/` in an empty Godot project and paste the master prompt into Claude Code. Or say **run it** and I'll start with M0 right here.
