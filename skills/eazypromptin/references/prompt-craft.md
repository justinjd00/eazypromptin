# Prompt craft

How to write the final prompt, whatever the depth. These rules hold for Claude, GPT, Gemini and most other current models.

## Structure

Order the content the way a smart colleague with zero context would want to receive a brief:

1. **Goal and why**: what should exist afterwards and what it's for. The why lets the model make good calls on everything you didn't specify.
2. **Context**: who it's for, what exists already, relevant facts the model can't know.
3. **The ask**: concrete. Steps only if the order genuinely matters.
4. **Output**: format, length, where it goes, who reads it.
5. **Constraints**: must / must not, with reasons.
6. **Done criteria**: how to tell it's finished and good. For agents: how to verify.

Short prompts don't need headers. Past ~15 lines, plain headers (`## Goal`) help both model and person.

## Rules that make the difference

- **Facts beat adjectives.** "Persuasive, creative, professional" produce average output; the product's real benefits, the reader's real problem and the one action you want produce specific output. If the prompt lacks facts, ask for them; don't compensate with adjectives.
- **Explain reasons instead of shouting.** "Under 120 words because it's read on a phone" outperforms "MAX 120 WORDS!!!". Reasons generalise to cases the rule didn't foresee.
- **Be precise where it matters, loose where it doesn't.** Pin down the stack, the audience, the deliverable. Leave the model room on wording and structure unless they matter.
- **Show, don't describe, for unusual formats.** One short example of the desired output beats a paragraph describing it. Mark it as an example so it isn't copied literally.
- **Name what to avoid concretely.** "No filler phrases" is weak; "no sentences like 'I hope this email finds you well'" works.
- **Mark assumptions.** If something in the prompt is a guess, say so, so the model can flag a mismatch instead of building on it.
- **One prompt, one job.** If the prompt asks for research, a plan and the implementation, split it or make it explicitly sequential with checkpoints.

## Cut these

- "You are an expert with 20 years of experience..." persona openers. They add nothing a clear task doesn't; a role is only useful when it carries real context ("You're writing as a founder to restaurant owners, some of whom you know personally").
- Generic quality demands: "be thorough", "pay attention to quality", "think carefully".
- Contradictions: "not too long, but not too short either" → give a number.
- Rules nobody would break anyway.
- Caps-lock and exclamation marks.

## Length check

A good final prompt is usually 3-10× the person's original words for Quick/Standard, and the master prompt in Deep mode is short because the brief carries the detail. If a prompt grows long, check that every sentence changes what the model does.

## Model-specific notes

- **Claude**: responds well to XML-style tags for separating material (`<job_posting>…</job_posting>`) and to explicit "why". Follows instructions literally; say "be ambitious" if you want more than the minimum.
- **GPT models**: similar; explicit output format sections help.
- **Gemini**: put long reference material first, the question last.
- **Small/local models**: shorter prompts, fewer constraints, one example, very explicit output format.

Only mention model specifics if the person says which model will run the prompt.
