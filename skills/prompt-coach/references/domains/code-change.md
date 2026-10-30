# Domain: Code Change

## Applies when
The work happens inside an **existing** codebase: fixing a bug, improving performance, refactoring, adding a feature to a running app, migrating a framework/library/database, upgrading dependencies, adding or repairing tests, cleaning up tech debt.

Signals: "fix", "bug", "stopped working", "error", "slow", "refactor", "migrate to", "upgrade", "add X to my app", "write tests for", a stack trace, a GitHub issue link, a repo path, "in my project".

Neighbours and how to tell them apart:
- **New app / greenfield build**: no repo yet, or the person wants to start over. Route to the app/software domain. A rewrite of an existing app that must keep its data and URLs stays here.
- **Design / UI**: if the ask is "make the settings page look better" in an existing app, stay here for implementation but borrow mood/layout slots from design-ui.
- **Content writing**: README or docs prose without code changes goes there.

## What people leave out
- **Reproduction steps**: "the login is broken" without steps means the agent fixes something it guessed. Often it "fixes" a symptom that wasn't the bug.
- **Expected vs actual**: without the expected behavior, the agent cannot tell a bug from a feature.
- **Scope boundary**: which files or modules may be touched. Without it, a bugfix turns into a 40-file refactor that nobody can review.
- **Constraints**: no new dependencies, public API must stay compatible, PHP 8.1 not 8.3, no DB schema change. Guessed constraints break production.
- **How to verify**: which test command, which manual check. Without it, "done" means "it compiles".
- **Environment details**: versions, OS, browser, which environment (local, staging, prod), feature flags.
- **Risk and rollback**: whether this touches payments, auth, data migrations. Determines how careful and incremental the agent must be.
- **Deliverable shape**: direct commit on main, branch plus PR, patch file, or just a plan. Agents default differently.

## Discovery map

### Before round 1: look in the repo
If the coach or the downstream agent has repo access, reading beats asking. Every question answered by the repo is a question the person doesn't have to answer. Before round 1, check and summarise in one line:
- `README.md`, `CONTRIBUTING.md`, `CLAUDE.md` / `AGENTS.md`: setup, conventions, agent rules already written down.
- `package.json`, `composer.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, `*.csproj`, `Gemfile`: stack, versions, scripts (`test`, `lint`, `build`).
- Lockfiles: whether to use npm, pnpm, yarn, bun, composer, uv, poetry.
- `git log --oneline -20` and `git status`: commit style, active areas, uncommitted work.
- Test directories and CI config (`.github/workflows`, `.gitlab-ci.yml`): how verification already runs.
- Linters/formatters (`.eslintrc*`, `biome.json`, `phpstan.neon`, `ruff.toml`, `.editorconfig`).
Then ask only what the repo cannot tell: intent, priorities, risk tolerance, what "fixed" means to the user.

Without repo access, write these checks into the master prompt as the agent's first step, and ask the person only for the stack in one line.

### Phase 1: Goal and type of change
- **Change type** [Q]: each type has a different workflow.
  "What kind of change is this?" Options: (a) bugfix, (b) performance, (c) refactor without behavior change, (d) new feature in existing code, (e) migration/upgrade, (f) tests only. Default: infer from the request. Decide-for-me: infer and state it in the understanding line.
- **Why it matters now** [S]: sets priority and acceptable risk.
  Options: production is broken for users, blocks a release/demo, annoying but has a workaround, groundwork for a later feature, learning/cleanup. Default: annoying with workaround.
- **Definition of fixed / done** [Q]: one observable outcome.
  "When is this done for you?" Offer two concrete phrasings based on the request, e.g. "login with a valid email lands on /dashboard without the 500" or "the product list renders under 300 ms with 5,000 items". Decide-for-me: write the most literal observable outcome and mark it as an assumption.

### Phase 2: Current behavior (bugfix and performance)
- **Reproduction** [Q]: the agent's starting point.
  "How do I trigger it?" Options: (a) exact steps you give, (b) a failing test or curl command, (c) only happens in prod/sometimes, (d) don't know, agent should find out. Default: (a). Decide-for-me: agent writes a failing test or script that reproduces it first; if it can't, it stops and reports.
- **Expected vs actual** [Q]: one line each.
  "What should happen, what happens instead?" Ask for error messages, stack traces, screenshots, log lines verbatim.
- **Since when** [S]: shortcut to the cause.
  Options: always, since a specific commit/deploy/upgrade, since data grew, unknown. If known, suggest `git bisect` or reading the diff of that range.
- **Environment** [S]: versions and where it happens.
  Options: local only, staging, production, specific browser/device/OS. Ask for runtime versions only if the repo doesn't pin them.
- **Measurement** [S] (performance): a number to beat.
  "What is slow, measured how?" Options: page load (Lighthouse/LCP), API latency (p95), query time (EXPLAIN), build time, memory. Default: a before/after measurement of the specific path, recorded in the PR.

### Phase 3: Target behavior (feature, refactor, migration)
- **Behavior spec** [Q] (feature): use a scenario walkthrough.
  "Walk me through it once as a user: who clicks what, what appears?" Then confirm edge cases with this-or-that: empty state, error state, permissions, mobile.
- **Refactor goal** [S]: what improves.
  Options: readability, testability, split a god class/component, remove duplication, prepare for feature X, type safety. Hard rule to confirm: behavior stays identical. Default: identical behavior, smaller units, existing tests still green.
- **Migration target** [S]: exact from and to.
  Options with current examples: Vue 2 to Vue 3 (Composition API), Laravel 10 to 12, PHP 8.1 to 8.4, Next.js Pages Router to App Router, Jest to Vitest, JavaScript to TypeScript, MySQL 5.7 to 8.4, CRA/Webpack to Vite, Python 3.9 to 3.13. Ask whether the migration may be incremental (both coexisting) or must be big-bang.
- **Anti-goals** [S]: what must not change.
  "What must stay exactly as it is?" Options: public API/URLs, DB schema, UI look, response formats, config files, performance of other paths.

### Phase 4: Scope and constraints
- **Files and modules in scope** [S]: protects reviewability.
  Options: (a) only the files the agent finds necessary, keep diff minimal, (b) this module/folder, (c) anything, broad cleanup welcome. Default: (a). Decide-for-me: (a) and a diff budget, e.g. "if more than ~10 files or ~300 lines change, stop and propose a plan first".
- **Dependencies** [S]: new packages are a long-term cost.
  Options: no new dependencies, dev dependencies only, allowed if well-maintained and justified in PR. Default: no new runtime dependencies.
- **Compatibility** [S]: who depends on this code.
  Options: public API used by clients/mobile app, internal only, library published to npm/Packagist. Default: keep public signatures and response shapes backwards compatible.
- **Conventions** [D]: repo style beats agent style.
  Confirm: follow existing patterns, formatter and lint config, commit message style seen in git log, naming. Default: match surrounding code.
- **Off-limits areas** [D]: generated code, vendor folders, migrations already run in prod, secrets, CI config.

### Phase 5: Tests, risk, production
- **Test strategy** [Q]: the agent's proof.
  Options: (a) add a failing test first, then fix (recommended for bugs), (b) extend existing tests, (c) characterization tests before refactor, (d) manual check only because no test setup exists, (e) set up a minimal test harness first. Default: (a) for bugs, (c) for refactors. Decide-for-me: use the repo's existing framework (PHPUnit/Pest, Vitest/Jest, pytest, xUnit, Playwright for E2E).
- **Risk level** [S]: decides how incremental to work.
  Options: low (UI copy, isolated util), medium (shared component, API endpoint), high (auth, payments, data migration, concurrency). Default: medium. High risk adds: feature flag, migration dry run, backup step, staged rollout.
- **Rollback** [D]: how to undo.
  Options: revert the PR, feature flag off, down-migration, restore backup. Default: single revertable PR, reversible migrations.
- **Deliverable** [Q]: what lands where.
  Options: (a) branch plus PR with description (recommended), (b) commits on current branch, (c) patch/diff only, (d) plan only, no code. Default: (a), branch named `fix/<short-desc>` or `feat/<short-desc>`.
- **Milestone split** [D]: for larger work, agree on PR-sized steps (see Milestones).

## Inspiration anchors
References in this domain are patterns and prior art rather than products:
- "Do it the way `<existing similar feature in this repo>` does it" is the strongest anchor. Ask for or find one.
- Known patterns: strangler fig migration, expand-and-contract DB changes, feature flags, characterization tests (Michael Feathers), "make the change easy, then make the easy change" (Kent Beck).
- Upstream migration guides (Vue 3 migration build, Laravel upgrade guide, Next.js codemods, `npx @next/codemod`, Rector for PHP, `pyupgrade`).

Pitch-sampler seeds (offer as strategies when the person can't decide how to approach it):
1. **Surgical fix**: smallest diff that makes a failing test pass, nothing else touched.
2. **Fix plus guardrail**: the fix, a regression test, and a log/assertion so it can't silently return.
3. **Refactor then fix**: first a behavior-preserving cleanup PR, then the fix on clean ground.
4. **Spike first**: agent investigates for a bounded time, writes findings and 2 options, no code merged.
5. **Incremental migration**: old and new coexist behind an adapter; move module by module.
6. **Big-bang upgrade**: one branch, all at once, only for small codebases with good tests.

## Smart defaults
When the person says "just do it" or "decide for me":
- Read repo docs, manifests, git log and tests before changing anything; report the stack in one line.
- Reproduce first: a failing test or script. If reproduction fails, stop and report instead of guessing.
- Minimal diff, match existing style, no new runtime dependencies, public APIs unchanged.
- Run the repo's own test, lint and type-check commands; all must pass before and after (note pre-existing failures separately).
- Work on a new branch, one focused PR with: problem, cause, fix, how verified, risks.
- Stop and ask if: the change exceeds ~10 files/~300 lines, touches auth/payments/migrations, or requires a new dependency.
Why: an AI agent's most expensive failure in an existing codebase is a large, confident, unreviewable diff. Small, verified, reversible changes are cheap to accept or reject.

## Scope traps
- **Drive-by refactoring**: the agent "improves" unrelated code. Prevent with an explicit scope rule and diff budget.
- **Symptom fixing**: catching the exception instead of fixing the cause. Require a root-cause line in the PR description.
- **Upgrade cascade**: one package upgrade pulls ten others. Ask up front whether transitive upgrades are allowed; otherwise pin and report.
- **Untestable legacy**: no tests exist, so every change feels risky. Make "add characterization tests for the touched area" its own first milestone.
- **Moving target feature**: requirements grow during implementation. Freeze the scenario walkthrough in the brief; new ideas go to Open questions.
- **Flaky reproduction**: intermittent bugs eat time. Time-box the investigation and require logging/instrumentation as a deliverable if not reproduced.
- **Migration halfway**: a big-bang migration stalls at 70%. Prefer incremental plans with a working app after every milestone.

## Brief sections
- **Repo Snapshot**: stack, versions, package manager, test/lint/build commands, conventions found (or "to be discovered by agent").
- **Problem Statement**: change type, expected vs actual, reproduction steps, error output, since when.
- **Target Behavior**: scenario walkthrough or refactor/migration goal, edge cases, anti-goals.
- **Scope & Constraints**: files/modules in scope, off-limits areas, dependency rule, compatibility requirements, diff budget.
- **Test & Verification Plan**: test strategy, commands, manual checks, performance measurements.
- **Risk & Rollback**: risk level, flags, migration safety, rollback path.
- **Deliverable**: branch name, PR format, commit style, what to include in the description.

## Milestones
- **M0 Recon**: read repo, run existing tests and build, record baseline (passing/failing, timings). Done when the repo snapshot is written and the baseline is known.
- **M1 Reproduce / characterize**: failing test or script for the bug, or characterization tests for the refactor area, or a measured baseline for performance. Done when the problem is demonstrated by a command.
- **M2 Plan**: short plan of the change, files to touch, risks. Done when approved (Deep/high risk) or auto-approved under the diff budget.
- **M3 Implement**: the change itself, in small commits. Done when the M1 test passes and all pre-existing tests still pass.
- **M4 Harden**: edge cases, error handling, regression tests, lint and type check clean. Done when the verification checklist is green.
- **M5 Deliver**: branch pushed, PR opened with problem, cause, fix, verification evidence, risks, rollback. Done when the PR link exists.

For migrations, repeat M3-M4 per module, each ending with a working app.

## Verification
- The reproduction from M1 fails before and passes after (show both outputs).
- Full test suite, linter and type checker pass: e.g. `npm test && npm run lint && npx tsc --noEmit`, `composer test` / `vendor/bin/phpunit` / `vendor/bin/phpstan analyse`, `pytest && ruff check`, `dotnet test`.
- Build succeeds (`npm run build`, `php artisan optimize`, `dotnet build`).
- Performance: before/after numbers for the same measurement, same environment.
- Refactor: no test changed its assertions; public signatures unchanged (diff check).
- Diff review: only in-scope files changed, no debug output, no commented-out code, no secrets, no unrelated formatting churn.
- Manual check script written in the PR for anything not covered by automated tests (steps, expected result).

## Example opening
Request (~30 words):
> "The password reset link in my Laravel app doesn't work anymore, you end up on a 419 page. Can you fix it? It's a Vue frontend, running on a Hetzner server."

Excerpt of a good Deep-mode round-1 reply:
> Understood: bugfix in an existing Laravel app with a Vue frontend. The link from the password reset email leads to a 419 (Page Expired), so most likely CSRF, session or domain. I'll look at the repo first (composer.json, .env.example, routes, recent commits) before asking more.
>
> Possible approaches:
> **A Surgical:** find the cause, smallest fix, one regression test. (recommended)
> **B Fix plus guardrail:** like A, plus logging for 419s so it can't silently come back.
> **C Investigate first:** the agent delivers only the cause and two possible solutions, no code yet.
>
> 1. Since when? a) always b) since a deploy or update (which one?) c) don't know
> 2. Where does it happen? a) production only b) locally too c) only in certain browsers or mail apps
> 3. When is it solved for you? a) click the link, set a new password, logged in on the dashboard (recommended) b) additionally, an expired link should show a clear message
> 4. Deliverable: a) own branch plus pull request with explanation (recommended) b) directly on the current branch c) just a plan
> 5. Boundaries: no new packages, no database changes. OK?
>
> Short is fine: "A, 1b 2a 3a 4a, ok". Or "decide for me".
