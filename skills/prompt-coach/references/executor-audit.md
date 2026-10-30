# Executor audit

Before delivering, find out what the agent that receives the brief would still have to guess. Models that execute an underspecified spec rarely vary between interpretations; they collapse onto one confident reading, which may be wrong. Sampling the output several times and checking agreement therefore misses the problem. Asking a reader to *name its assumptions* catches it.

## Procedure

1. **Freeze a draft** of the brief (or the final prompt in Standard mode).
2. **Spawn 2-3 readers** that see *only* the draft, nothing from the conversation:
   - **Executor**: a capable coding agent (or writer, analyst…) with zero context, about to start the first milestone.
   - **Domain expert**: someone who knows this kind of product well (a game designer, a SaaS architect, an editor).
   - **Skeptical QA**: someone who has to decide whether the result is done.
   If a subagent tool exists, run each as a separate subagent with the prompt below. If not, switch roles explicitly in your reasoning, one reader at a time, and don't let knowledge from the conversation leak into the role.
3. **Collect guesses** in the fixed form: *"I would assume X because the brief doesn't say Y."* Each with impact (would a wrong guess cause rework? high / low).
4. **Triage**:
   - Guesses the readers **disagree** on, with high impact → ask the person (one final short round, ≤3 questions, multiple choice).
   - Guesses all readers make the same way and the person would plausibly agree with → write them into the brief as assumptions.
   - Trivial or discoverable-by-the-agent guesses (file names, minor styling) → drop.
5. **Patch the brief** and re-run the audit once if more than a few high-impact guesses were found.
6. **Report in one line**: "Audit: 3 readers, 17 guesses on the first draft, 2 left after your answers, both marked as assumptions."

If the person said "go", skip step 4's questions: turn high-impact divergent guesses into explicit assumptions with the safest default and list them at the top of the brief.

## Reader prompt (for subagents)

```
You are about to execute the brief below as <ROLE>. You have no other context: no chat history, no access to the person who wrote it.
Read it and list every point where you would have to guess to do the work (or, for QA, to decide whether the work is done).
Write each as: "I would assume <X> because the brief doesn't say <Y>." Add impact: HIGH if a wrong guess would cause rework or a result the author doesn't want, LOW otherwise.
Focus on conditional behaviour, edge cases, error handling, scope boundaries, constraints, priorities between conflicting goals, and what "done" means. Ignore wording and formatting.
Then list anything in the brief that is contradictory or impossible.
Return at most 20 items, most important first.

<BRIEF>
...
</BRIEF>
```

## What good audits catch

- Conditional rules nobody wrote down ("what if both players die at the same time?", "what if the CSV has empty rows?").
- Priorities between goals ("fast" vs. "polished": which wins when they conflict?).
- Scope edges ("does 'accounts' include password reset?").
- Verification gaps ("'feels good' according to whom, measured how?").
- Hidden dependencies ("asset pack licence?", "API key from where?").
- Contradictions between sections.
- Broken internal references ("see §7" when there is no §7), sections promised but missing, numbers that don't add up.
- Missing capacity and environment: target hardware, time budget, who maintains it.

## Cost control

Run the audit once per package (twice at most). For Quick mode, do a one-reader inline audit in your head: "What would an agent have to guess here?" and add one or two assumptions; don't spawn anything.
