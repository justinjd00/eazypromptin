# Question selection

How to pick what to ask. The goal is the fewest questions that remove the most uncertainty about what to build, each one easy to answer.

## 1. The selection procedure

Run this silently before every question round:

1. **List candidate questions** for the open, high-impact slots and the remaining hypotheses (aim for 4-6 candidates).
2. **Simulate the answers.** For each candidate, write in one line how each surviving hypothesis would answer it.
3. **Score the split.** A question is valuable if its answers divide the hypotheses into groups that would lead to different builds. Best: each option corresponds to a different hypothesis (an even split). Worthless: every hypothesis gives the same answer, or every answer leads to the same brief.
4. **Apply the filters** (section 2). Drop anything that fails.
5. **Prefer coverage.** Between two good questions, take the one whose answer settles more correlated slots (`intent-engine.md` §4).
6. **Order by stage.** Goal and success criteria before inputs and constraints before details. Conflicts first of all.
7. Ask the top 1-3.

Shortcut when you're short on time: "Which question would most change what I'd write if I knew the answer?"

## 2. Filters every question must pass

- **Relevance**: different answers lead to different builds. If not, assume and state it.
- **Answerability**: the person can answer from what they know or can show. Ask about behaviour ("what should happen when two players grab the same upgrade?"), examples, preferences, observable facts, errors they see. Never ask a non-expert to design the solution, choose between implementation techniques they don't understand, or know internals. If a technical decision matters, make it yourself and explain it in half a sentence.
- **Not recoverable**: you can't find the answer in the context, files or repo.
- **Not already answered**: including indirectly, via a correlated dimension.
- **Worth the effort**: the cost of a wrong guess outweighs the person's effort to answer. Low-stakes, reversible → assume.

## 3. Budgets

Scale to stakes, not to a fixed count. Returns plateau after about three well-chosen questions while the person's effort keeps rising.

| Situation | Questions |
|---|---|
| Quick, reversible | 0-2 total |
| Standard | up to 3 per round, ~6-8 total |
| Deep | 3-5 in the first two rounds, then ≤3 per round; stop when the audit finds no high-impact guesses |
| Person is terse or tiring | Halve it; switch to stronger defaults and offer "go" |

## 4. Formats

- **Multiple choice by default**: 2-4 concrete, genuinely different options, the recommended one marked, and always an escape: "other, because…". Present each as a named decision and show what it changes: "**Co-op**: a) local, same screen (cheap) b) online (3-5× the work, must be built in from day one)".
- **Open questions only for facts the person holds**: a name, a link, an error message, an example they have, a number.
- **Edge-case probes** to elicit conditional rules: "If a player disconnects mid-run, should the run end, pause, or continue solo?" Concrete scenarios surface rules people would never list.
- **Alternative-seeking** at least once per major decision: "Would X also be fine?" Models skip this, and it's where hidden flexibility (or a hidden hard constraint) shows up.
- **This-or-that bundles** for taste: "cozy (a) or tense (b) · funny (a) or dark (b)", answered "b b".
- **Readback confirmation** at the end of each phase: "So: X, Y, Z. Right?" One word to confirm or correct.

## 5. Question types (rotate between them)

From requirements-elicitation research, the useful follow-up moves are:
1. **Probe the answer**: dig into something they just said ("'stronger' how: numbers going up or new abilities?").
2. **Confirm**: check an inference ("So it's for playing with friends rather than publishing?").
3. **Seek alternatives**: "Would a shorter version also work?"
4. **Seek preferences**: "Which of these feels closer?"
5. **Clarify**: resolve a vague term ("'modern' meaning minimal, or meaning bold colours?").
6. **Change topic**: move to the next high-impact slot when the current one is settled.
7. **Edge case**: "What should happen when…?"

## 6. Interviewer mistakes to avoid

These are the documented failures of human and LLM interviewers. Check each round against them:
- Generic questions ("any other requirements?", "any preferences?").
- Two or more topics in one question.
- Jargon the person didn't use.
- Asking the person to propose the technical solution.
- Not considering alternatives (always asking about the first idea).
- Missing tacit assumptions (the thing "everyone knows" in their domain).
- Asking about something already answered or inferable.
- Long questions; anything over two lines is too long.
- Leading questions that smuggle your preference in as the only reasonable answer (mark your recommendation openly instead).
- Inventing facts (prices, deadlines, user numbers) instead of asking or marking an assumption.
- Asking personal data that isn't needed.

## 7. Self-check signals

Track three failure signals over the session and correct course when one appears:
- **Wrong assumption**: the person corrects something you stated as inferred. Lower confidence in related inferences; ask instead of assuming in that area.
- **Repeated clarification**: you asked about something twice. Your state isn't being carried forward; rewrite it.
- **Irrelevant clarification**: an answer didn't change anything. Tighten the relevance filter.
