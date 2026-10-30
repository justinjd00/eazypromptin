# Domain: Mobile App

## Applies when
Route here when the person wants an app that is **installed on a phone or tablet**, typically from the App Store or Google Play, or that depends on device capabilities a browser handles poorly.

Signals:
- Nouns: iPhone app, Android app, App Store, Play Store, "phone app", smartphone, tablet, widget, Apple Watch, push notification, wearable.
- Verbs: install, download, scan, track (location, steps, workouts), notify, take a photo, work offline.
- Artefacts: app icon, store listing, TestFlight, APK/AAB, in-app purchase, HealthKit/Health Connect, Bluetooth device, NFC.
- Phrases: "an app like ... for my phone", "should be in the App Store", "an app our customers can download".

Tell it apart from neighbours:
- **web-app.md**: if the store is not a requirement and the core is managing data (bookings, records, dashboards), a responsive web app or PWA is cheaper and faster. People often say "app" when they just mean "software". Ask the this-or-that "Does it have to be in the App Store, or is a link you can add to the home screen enough?" before committing here. Strong reasons to stay here: push notifications that must be reliable on iOS, background location, camera/scanner-heavy use, offline-first, Bluetooth/NFC, health data, or the store presence itself is a business goal.
- **website.md**: presence and information only; no install.
- **game.md**: the core loop is play (levels, scores, physics), even on mobile. A gamified habit tracker stays here; a puzzle game goes to game.md.
- **design-ui.md**: screens, flows or a clickable Figma prototype without working code.
- **code-change.md**: an existing mobile codebase gets a feature or fix. Borrow the relevant slots (push, store release) from here.
- If the person wants *both* web and mobile clients for the same product, run web-app.md for the backend and product model and this file for the mobile client; recommend the mobile client as a later milestone unless mobile is the core.

## What people leave out
- **Whether it really needs to be native.** Many requests are web apps in disguise; the store adds review cycles, fees and developer accounts for no user benefit.
- **Which platforms, and what devices they test on.** An agent cannot verify iOS without a Mac or a cloud build service; this decides the stack and workflow.
- **Developer accounts and store requirements.** Apple Developer Program (99 USD/year), Google Play Console (25 USD once), privacy labels, data safety form, review guidelines; launch stalls without them.
- **Offline behaviour.** "Should it work without signal?" changes the whole data layer (local DB, sync, conflicts).
- **The backend.** A mobile app almost always needs auth, a database and an API; people describe screens and forget the server.
- **Push notification purpose.** Push needs a backend trigger, permission UX and APNs/FCM setup; vague "with notifications" becomes either spam or nothing.
- **Monetization rules.** Digital goods sold in the app must generally use Apple/Google in-app purchase; physical goods and services use Stripe. Getting this wrong means rejection.
- **Permissions and privacy.** Camera, location, contacts and tracking each need a justification string, a privacy-label entry and, for tracking on iOS, an ATT prompt.

## Discovery map

### Phase 1: Vision & native-or-not
- **One-sentence job**: [Q] "Who opens it, in what moment, to do what?" Mobile apps are used in short bursts in specific situations (on the go, at the gym, in the shop); the moment shapes the UI. Default: derive from the request and confirm. Decide for me: write it and mark it as assumption.
- **Native justification**: prevents building the wrong thing. [Q]
  This-or-that: a) must be in the App Store / Play Store, b) a web app installable to the homescreen (PWA) is fine, c) not sure. Follow with "Which of these does it need?": reliable push, camera/scanner, GPS in background, offline, Bluetooth/NFC, health/fitness data, widgets. Default: if none of the device features apply and the store is not a goal, recommend web-app.md with a PWA and say why. Decide for me: native only if at least one device feature is core.
- **Usage moment & frequency**: drives notifications and retention design. [S]
  Options: a) several times a day (habit, messaging), b) daily (tracker, routine), c) weekly (planning, shopping), d) occasionally when needed (utility, scanner, tickets). Default: b.
- **Success signal**: [D] Options: a) I use it myself daily, b) N installs/active users, c) paying subscribers, d) customers of my business use it instead of calling. Default: a or d.
- **Anti-goals**: [S] Examples: no social feed, no chat, no tablet layout, no Android in v1, no ads. Default: no chat, no social features, phone portrait only.

### Phase 2: Users, screens & flows
- **Account requirement**: affects onboarding drop-off and store rules. [Q]
  Options: a) no account, data stays on the device, b) optional account for sync/backup, c) account required (shared data, multi-device), d) business users invite customers. Default: a or b where possible; Apple requires in-app account deletion if accounts exist, and Sign in with Apple if other social logins are offered.
- **Core screens**: [Q] "Name the 3-5 screens you picture." Help with reference anchors: "Like Duolingo's home with the daily task, like Strava's record button, like Revolut's card list." Default: propose a tab structure (e.g. Home / Add / History / Profile) and let the person edit.
- **First-minute walkthrough**: catches onboarding gaps. [S]
  Scenario walkthrough: "Someone installs it from the store and opens it. What do they see in the first 60 seconds?" Cover permission prompts (ask in context, not all at launch), sign-in, first value moment. Default: the coach narrates; person confirms.
- **Core objects**: [S] the things stored and synced (e.g. Workout, Set, Exercise; Order, Item; Habit, CheckIn). Default: propose from the request.
- **Navigation pattern**: [D] Options: a) bottom tabs (default for 3-5 top areas), b) single stack with a home list, c) drawer (avoid for new apps). Default: a.
- **Accessibility & platform feel**: [D] Options: a) one design on both platforms, b) platform-adaptive (iOS and Material conventions). Default: a with native components where the framework provides them; dynamic type and VoiceOver/TalkBack labels required.

### Phase 3: Device features, data & offline
- **Device features**: each one is a permission, a native module and a test case. [S]
  Checklist: camera/photo library, barcode/QR scan, location (foreground/background), push notifications, biometrics (Face ID), Bluetooth LE, NFC, HealthKit/Health Connect, calendar/contacts, haptics, widgets/Live Activities. Default: only what the one-sentence job needs. Decide for me: camera and push only if mentioned.
- **Offline**: changes the data architecture. [Q]
  Options: a) online only, show a friendly error offline, b) read offline (cached data), c) offline-first, create and edit offline and sync later, d) fully local, no server. Default: b. For c, name the tool (PowerSync or ElectricSQL with Postgres, WatermelonDB, Realm-style sync is retired so do not propose it) and the conflict rule (last write wins by default).
- **Backend**: [Q] Options: a) none (local only, SQLite/MMKV), b) Supabase (Postgres, Auth, Storage, Realtime), c) Firebase (Firestore, Auth, FCM), d) own API (NestJS, Laravel) shared with a web app, e) existing backend (name it). Default: b. Decide for me: a if no account is needed, otherwise b.
- **Push notifications**: [S] "What exactly triggers a push, and how often?" Options: a) none, b) reminders scheduled on device (local notifications, no server), c) server-triggered events (new message, order ready) via Expo Push / FCM / APNs, d) marketing broadcasts (OneSignal). Default: b for habit apps, c for service apps; never d in v1.
- **Data sensitivity**: [S] Options: a) nothing personal, b) personal data (GDPR baseline: EU region, deletion, privacy policy), c) health, location history or children's data (stricter store rules and legal review). Default: b.

### Phase 4: Stack, monetization & release
- **Platforms**: [Q] Options: a) iOS + Android together (recommended), b) iOS first, c) Android first, d) also tablet/web from the same code. Default: a via cross-platform. Ask what phone the person owns; that is the first test device.
- **Framework**: [Q] Offer a committed recommendation:
  a) **React Native with Expo** (Expo Router, EAS Build/Submit/Update, TypeScript). Recommended default: largest ecosystem, cloud builds without a Mac, over-the-air updates, coding agents handle it well, shares TypeScript with a Next.js/NestJS backend.
  b) **Flutter** (Dart, Riverpod or Bloc, go_router). Strong for custom, animation-heavy UI and consistent rendering; good if the person already knows Dart.
  c) **Native** (Swift/SwiftUI for iOS, Kotlin/Jetpack Compose for Android). Choose for one platform only, deep OS integration (widgets, Watch, CarPlay, advanced HealthKit/ARKit) or maximum performance; two codebases if both platforms.
  d) **Kotlin Multiplatform / Compose Multiplatform** for teams with Android/Kotlin background sharing logic.
  e) **Capacitor** wrapping an existing web app when the web app already exists and only store presence + a few plugins are needed.
  Decide for me: a.
- **Existing skills & hardware**: [S] "Which languages do you read? Do you have a Mac and which phones?" No Mac means iOS builds go through EAS Build or Codemagic and testing through TestFlight on a real device. Let skills override the framework default.
- **Monetization**: [S] Options: a) free, b) paid upfront, c) subscription for digital features (StoreKit / Google Play Billing, wired via RevenueCat), d) one-time unlock (in-app purchase), e) selling physical goods or real-world services (Stripe, outside IAP rules), f) ads (AdMob). Default: a for v1, c via RevenueCat when charging for digital features. Flag the store commission (15% under Apple/Google small-business programs) and EU/US external-payment rules as an open question if relevant.
- **Release path**: [S] Options: a) personal use / internal (TestFlight + Play internal testing), b) closed beta, c) public store release. Default: a, then b. Note that new personal Google Play accounts require a closed test with testers before production; plan for it.
- **Store assets**: [D] App name, subtitle, icon (1024 px), screenshots for required sizes, privacy policy URL, support URL, privacy nutrition label / data safety form, age rating. Default: generated as a milestone; screenshots taken from the simulator.

### Phase 5: Production: scope, milestones, verification, handoff
- **MVP cut**: [Q] Propose MVP / soon / later columns. Default MVP: core screens, local or Supabase data, one device feature, no payments, internal testing release.
- **Update strategy**: [D] Options: a) store releases only, b) OTA updates for JS changes (EAS Update) + store releases for native changes. Default: b with Expo.
- **Analytics & crash reporting**: [S] Options: a) crash reporting only (Sentry), b) + privacy-friendly product analytics (PostHog EU, TelemetryDeck), c) Firebase Analytics. Default: a + TelemetryDeck or PostHog EU; anything with tracking affects the privacy label.
- **Testing depth**: [S] Options: a) typecheck + unit tests, b) + component tests (React Native Testing Library / flutter_test widget tests), c) + end-to-end on simulator (Maestro or Detox / integration_test). Default: c for the primary flow with Maestro.
- **Agent operating rules**: [S] Default: run on simulator/emulator after every milestone, never commit signing keys or `.env`, keep native config in `app.config.ts` (no manual edits to generated native folders with Expo prebuild), ask before adding native modules or paid services, document every permission with its usage string.

## Inspiration anchors
Anchor on interaction patterns, not branding: "Things 3-style quick add", "Duolingo streak and daily goal", "Strava big record button and post-activity summary", "Too Good To Go list + map toggle", "Revolut card stack", "BeReal-style single daily prompt", "Apple Wallet pass for tickets". Ask "Which app on your phone do you open most, and which feels closest to this?"

Pitch-sampler seeds:
- **One-tap tracker**: open, log in two taps, see your streak; local notifications as reminders; works offline.
- **Customer companion for a local business**: digital loyalty card, push when an offer or appointment slot opens, order-ahead link; account via magic link.
- **Field/scan tool**: scan a barcode or QR, see or edit the record, works in a basement without signal, syncs later.
- **Guided routine app**: daily session (workout, language drill, meditation) with progress, subscription unlock for premium content.
- **Event/ticket app**: schedule, map, saved favourites, Wallet pass, push for changes.
- **Photo-first logger**: take a photo, add a note, timeline view, optional AI tagging later.

## Smart defaults
When the person delegates, apply and record:
- Platforms: iOS + Android, phone portrait only.
- Framework: Expo (latest SDK) + React Native + TypeScript + Expo Router; NativeWind or Tamagui/Unistyles for styling; Zustand or TanStack Query for state/data.
- Data: local-first with expo-sqlite (Drizzle) if no account is needed; Supabase (EU region) with Auth (email magic link + Sign in with Apple + Google) when sync is needed; read-offline cache via TanStack Query persistence.
- Push: expo-notifications; local scheduled notifications first, server push via Expo Push Service when the backend needs to notify.
- Payments: none in v1; RevenueCat for subscriptions later; Stripe only for physical goods/services.
- Build & release: EAS Build + EAS Submit, TestFlight and Play internal testing; EAS Update for OTA fixes.
- Quality: TypeScript strict, ESLint, Jest + React Native Testing Library, Maestro flows for the primary path, Sentry for crashes.
- Privacy: no ad SDKs, no tracking, privacy policy page hosted on a simple website, in-app account deletion.
Why: Expo lets a solo builder ship to both stores without a Mac, coding agents produce it reliably, and every step from build to submission can be scripted and verified.

## Scope traps
- **Native for no reason.** Ask the native-justification question first; route to web-app.md if nothing device-specific is core.
- **Both platforms, both form factors, both themes.** Constraint: phone portrait, light + system dark mode only if the component library gives it for free.
- **Social features.** Feeds, follows, chat and comments explode moderation and backend work, and Apple requires reporting/blocking for user-generated content. Ask "Can v1 work for a single user?"
- **Offline-first sync as a side quest.** Bidirectional sync with conflicts is a project in itself. Constraint: read-offline in v1 unless offline editing is the core job.
- **Store review surprises.** Login walls without a demo account, missing account deletion, vague permission strings and IAP violations cause rejections. Constraint: store-readiness checklist is a milestone, not an afterthought.
- **Backend creep.** Admin panels, CMS and analytics dashboards for the app. Constraint: use the Supabase dashboard as the admin in v1.
- **Monetization before retention.** Paywalls before anyone returns daily. Constraint: payments only after the primary flow and a beta round.

## Brief sections
Add these to the universal brief:
- **Native justification**: why a store app (device features, store presence) rather than a web app.
- **Platforms & devices**: target OS versions, form factors, test devices, Mac availability.
- **Screen map & navigation**: tabs/stacks with each screen's purpose, plus the first-run flow including permission prompts.
- **Device capabilities & permissions**: each capability, when it is requested, the usage-description text, fallback if denied.
- **Data & offline strategy**: local storage, backend, sync approach, conflict rule, what works without network.
- **Notifications**: each notification type, trigger, frequency cap, local or server.
- **Monetization & store compliance**: model, IAP vs Stripe reasoning, RevenueCat setup, review-guideline risks.
- **Release plan**: developer accounts, bundle IDs, build/submit pipeline, testing tracks, OTA policy.
- **Store listing**: name, subtitle, keywords, icon, screenshots, privacy label / data safety answers, age rating, support and privacy URLs.

## Milestones
- **M0 Setup**: Expo (or chosen) project, TypeScript, linting, tests, Expo Router tabs, app runs on the person's phone via a development build. Done when: CI is green and the app opens on simulator and on one real device.
- **M1 Screens & navigation**: all core screens with static data, navigation, empty states, design tokens. Done when: every screen in the screen map is reachable and renders on iOS and Android.
- **M2 Data layer**: local DB or Supabase schema, auth if needed, CRUD for core objects, offline read cache. Done when: data survives app restart and (if accounts) syncs between two devices.
- **M3 Primary flow & device feature**: the core job end to end incl. the one key device feature with permission handling. Done when: a Maestro flow completes the primary path on both simulators, and denying the permission shows the fallback.
- **M4 Notifications**: local reminders and/or server push with token registration and deep linking into the right screen. Done when: a test notification opens the target screen on a real device.
- **M5 Monetization** (if in scope): RevenueCat offerings, paywall, restore purchases, sandbox testing. Done when: a sandbox purchase unlocks the feature and restore works after reinstall.
- **M6 Store readiness**: icon, splash, app config, privacy policy, account deletion, permission strings, store listing texts, screenshots, crash reporting. Done when: the store-readiness checklist is fully ticked.
- **M7 Beta release**: EAS Build production profile, submission to TestFlight and Play internal/closed testing, OTA channel configured. Done when: a tester installs the build from TestFlight and Play and completes the walkthrough script.

## Verification
- Commands: `npx tsc --noEmit && npx eslint . && npx jest` (or `flutter analyze && flutter test`); `npx expo-doctor` for dependency health; `npx expo prebuild --clean` must succeed if native config changed.
- E2E: Maestro flows (`maestro test .maestro/`) for onboarding, primary flow and permission denial, run on iOS simulator and Android emulator (locally or in EAS Workflows / Maestro Cloud).
- Builds: `eas build --profile preview --platform all` completes; the agent reports build URLs. Production builds only when the person has developer accounts set up.
- Device checks the person performs (agents cannot): install on own phone, test push, camera, background behaviour, airplane mode. Provide a numbered 10-step script.
- Offline check: enable airplane mode, open app, verify cached data shows and the error states are friendly; re-enable and confirm sync.
- Store-readiness checklist: account deletion reachable in-app, every permission string specific, privacy policy URL live, demo account for reviewers if login is required, no placeholder text, IAP uses StoreKit/Play Billing for digital goods.
- Acceptance pattern: "On a fresh install, a new user reaches [first value moment] in under 60 seconds and at most [N] taps, with permissions requested only when needed."

## Example opening
Request:
> "wanna make a phone app where you log your gym workouts, sets and weights, and see yourself getting better. should run on iphone and android and work without signal too"

Excerpt of a good Deep-mode round-1 reply:
> Got it: a workout app for your phone, you log exercises, sets and weights at the gym and see your progress, on iPhone and Android and without signal too. Offline plus both platforms clearly point to a real app instead of a web app.
>
> Three directions, pick one or mix:
> **A) "Quick logger"**: gym mode with big buttons, last value already pre-filled, rest timer, done in seconds.
> **B) "Progress coach"**: focus on charts and personal records, a nudge when you should increase a weight.
> **C) "Plan follower"**: you create workout plans (push/pull/legs), the app guides you through every session.
>
> 1. **Does it need an account?** a) No, everything stays on the phone (recommended for v1) b) Optional, for backup and switching devices c) Required
> 2. **Notifications?** a) None b) Rest timer alert and workout reminder, local on the device (recommended) c) More, e.g. a weekly summary
> 3. **Make money?** a) Free for now (recommended) b) Premium subscription for stats c) One-time purchase
> 4. **Tech:** a) Expo + React Native, builds iOS even without a Mac (recommended) b) Flutter c) Decide for me
> 5. **Which phone do you have?** a) iPhone b) Android c) Both
>
> A short answer is enough, e.g. "A+B, 1a 2b 3a 4a 5a" or "decide for me".
