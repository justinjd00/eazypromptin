# Research basis

Prompt Coach v2 is built on 2025-2026 research on clarification, intent discovery, user modelling and specification quality for AI agents. This page maps each design rule to the evidence behind it. Numbers are as reported by the papers; several are preprints, marked as such. If you find a better source or a result that contradicts a rule, please open an issue.

## The core idea

Most assistants either guess too early or ask generic questions. Both fail for the same reason: they don't model what the person might want. The research points to a different loop: keep explicit hypotheses about the person's intent, show concrete options when the intent isn't formed, ask only the questions that best separate the hypotheses, audit the resulting spec by simulating its executor, and hand off one short, selective spec.

## Rule → evidence

### Keep an explicit belief state and rewrite it every turn
- **LLMs Get Lost in Multi-Turn Conversation** (Laban et al., ICLR 2026). Underspecified multi-turn conversations score 39% lower than fully specified single-turn ones; models assume too early and build on wrong attempts. Consolidating everything into one turn recovers most of the loss. https://arxiv.org/abs/2505.06120
- **BED-LLM** (Choudhury et al., ICLR 2026). LLM questioners drift away from earlier answers unless hypotheses are explicit and inconsistent ones are rejected. https://arxiv.org/abs/2508.21184
- **Bayesian Teaching Enables Probabilistic Reasoning in LLMs** (Qiu et al., Nature Communications). LLMs update beliefs about user preferences far worse than a Bayesian observer when the state is implicit. https://arxiv.org/abs/2503.17523
- **ClarifyMT-Bench** (Luo et al., preprint Dec 2025). A slot tracker with filled / unfilled / conflict states lifted accuracy from 66% to 88%. https://arxiv.org/abs/2512.21120

→ `intent-engine.md`: hypotheses, slot table, conflict state, update rules, `STATE.md`.

### Ask the question that best splits the hypotheses
- **BED-LLM**: choosing questions by expected information gain over sampled hypotheses, with balanced multiple-choice splits, gave large gains (up to 5.8× on one preference-elicitation setting). https://arxiv.org/abs/2508.21184
- **Active Task Disambiguation with LLMs** (Kobalczyk et al., ICLR 2025). Reasoning about candidate *solutions* and picking the question that splits them evenly, training-free: HumanEval pass rate 70.8% → 85.6% (GPT-3.5) after four elicited requirements. https://arxiv.org/abs/2502.04485
- **Modeling Future Conversation Turns to Teach LLMs to Ask Clarifying Questions** (Zhang et al., ICLR 2025). A question is good if different answers lead to different outputs; if not, answer directly. https://arxiv.org/abs/2410.13788
- **SAGE-Agent / ClarifyBench** (Suri et al., preprint Nov 2025). Value-of-information question selection over structured slots with a redundancy penalty: 7-39% more coverage with 1.5-2.7× fewer questions. https://arxiv.org/abs/2511.08798
- **Cold-Start Personalization via Training-Free Priors (Pep)** (Bose et al., 2026). Correlations between preference dimensions let one answer update several; 3-5× fewer interactions. https://arxiv.org/abs/2602.15012

→ `question-selection.md` §1 and `intent-engine.md` §4 (correlated dimensions).

### Only ask what's relevant and answerable, and scale the budget to stakes
- **Asking What Matters (CLARITI)** (Vijayvargiya et al., ICML 2026). Relevance and *user answerability* both matter; removing the answerability filter drops performance to almost no-clarification level. Matched GPT-5's resolve rate with 41% fewer questions. https://arxiv.org/abs/2604.14624
- **Value of Information: A Framework for Human-Agent Communication** (Dong et al., preprint Jan 2026). Ask only when expected utility gain beats the person's cognitive cost; adapts to stakes without tuning. https://arxiv.org/abs/2601.06407
- **Ask Precisely, Assume Wisely** (Dutta et al., NeurIPS 2026 workshop). Three dissatisfaction signals: wrong assumptions, repeated clarifications, irrelevant clarifications.
- **Ambig-SWE** (Vijayvargiya et al., ICLR 2026). Interaction recovers up to 74% on underspecified tasks; the best questions are behavioural and answerable; implementation questions to users often go unanswered. https://arxiv.org/abs/2502.13069

→ `question-selection.md` §2-3 and §7.

### Make the ask/assume decision a separate step
- **Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents** (Edwards & Schuster, preprint 2026). A separate intent monitor reached 69.4% on underspecified SWE-bench vs. 61.2% for a self-checking single agent, close to the fully specified 70.8%. https://arxiv.org/abs/2603.26233
- **Knowing but Not Showing** (Su & Cardie, preprint 2026). Models recognise ambiguity when asked to judge it but almost never ask unprompted. https://arxiv.org/abs/2605.25284

→ SKILL.md step 3, `agents/gap-monitor.md`.

### Show options when intent isn't formed
- **DiscoverLLM** (Kim et al., ICML 2026). Users can't answer questions about intents they haven't formed; alternating divergent turns (concrete options) with convergent ones improved task performance by over 10% and shortened conversations by up to 40%. https://arxiv.org/abs/2602.03429
- **GATE: Eliciting Human Preferences with Language Models** (Li et al., ICLR 2025). Model-driven elicitation (including generated edge cases) beats user-written prompts and labelled examples, with less effort. https://arxiv.org/abs/2310.11589
- **Luminate** (Suh et al., CHI 2024) and **DesignWeaver** (Tao et al., 2025). Name the dimensions first, then generate variants that differ on them; picks become informative. https://arxiv.org/abs/2502.09867
- **Dynamic Prompt Middleware** (Drosos et al., CHIWORK 2025). Task-specific option controls beat generic ones; show what each option changes, or users misread it.
- **Bridging the Gulf of Envisioning** (Subramonyam et al., CHI 2024). Capability, instruction and intentionality gaps; "provide multiple outputs" as a design pattern. https://arxiv.org/abs/2309.14459
- Design fixation from AI examples (Wadinambiarachchi et al., CHI 2024) → wildcards and "none, because…". https://arxiv.org/abs/2403.11164

→ `probes.md`, formedness in `intent-engine.md` §3.

### Mine context and implicit cues first
- **UserBench** (Qian et al., NeurIPS 2025). Users reveal preferences indirectly; frontier models uncover only 27-34% of them and commit too early. https://arxiv.org/abs/2507.22034
- **π-Bench** (Zhang et al., preprint 2026). Hidden requirements are rarely resolved; recoverable context from earlier sessions is ignored. https://arxiv.org/abs/2605.14678
- **Understanding and Supporting How Developers Prompt for LLM-Powered Code Editing** (Nam et al., Google). Five categories developers omit (specifics, how, where, hidden context, intent); filling them from context or asking raised edit correctness by 27%. https://arxiv.org/abs/2504.20196

→ SKILL.md step 1, cue table in `intent-engine.md` §6.

### Audit the spec by simulating its readers
- **Retrieval-Augmented Detection of Pragmatic Ambiguities in Requirements** (Nair & Anish, EASE 2026). Simulated novice/intermediate/expert readers; flag requirements where interpretations diverge. https://arxiv.org/abs/2607.04436
- **Underspecification does not imply Incoherence** (Richter & Papadakis, preprint 2026). Coding models collapse onto one consistent but wrong interpretation; agreement-based checks miss it. https://arxiv.org/abs/2607.01953
- An Accenture Labs tutor (preprint 2607.06074) uses a similar hidden "consequence preview".

→ `executor-audit.md`, `agents/executor-auditor.md`.

### Write short, selective, contract-style specs
- **What Prompts Don't Say** (Yang et al., CMU). Models guess format requirements well but conditional ones badly; unspecified requirements regress twice as often across model updates; simply listing everything degrades accuracy; selective specification used 41-45% fewer tokens and did better. https://arxiv.org/abs/2505.13360
- **ROPE: What Should We Engineer in Prompts?** (Ma et al., TOCHI 2025). Omissions are the dominant defect; requirement quality correlates 0.71 with output quality. https://arxiv.org/abs/2409.08775
- **When the Specification Emerges** (Yan et al., preprint 2026). Specs revealed gradually lose faithfulness; a persistent tracked spec recovers about 90% of the gap. https://arxiv.org/abs/2603.17104
- **Spec-Driven Development as Prescribed and as Practiced** (Agarwal et al., preprint 2026). Specs full of implementation detail go stale; agents drift from specs with no detection → keep what/why separate from how, add drift checks. https://arxiv.org/abs/2608.25202
- **Grounding AI Agents in Contracts** (Tufano et al., SpecOps 2026). Pre/post-conditions and undefined-behaviour contracts raised bug detection from 53.4% to 63.2%. https://arxiv.org/abs/2608.17177
- **Evaluating AGENTS.md** (Gloaguen et al., 2026). Repo overviews in context files don't help and cost >20% more; non-obvious conventions do. https://arxiv.org/abs/2602.11988

→ `brief-format.md` compiling rules, milestones with spec sections, tests first, drift check.

### Interview discipline
- **Requirements Elicitation Follow-Up Question Generation** (Shen et al., RE 2025). Naming interviewer mistakes in the prompt makes LLM follow-ups beat human interviewers; seven follow-up types; models skip alternative-seeking. https://arxiv.org/abs/2507.02858
- **LLMREI** (Korn et al., RE 2025). One question at a time, read-back summaries, never invent facts. https://arxiv.org/abs/2507.02564
- **Ask Early, Ask Late, Ask Right** (Gulati et al., preprint 2026). Goal clarification loses nearly all value after the start; front-load it. https://arxiv.org/abs/2605.07937

→ `question-selection.md` §4-6.

### Don't let mind-reading turn into agreeing
- **Interaction Context Often Increases Sycophancy in LLMs** (Jain et al., CHI 2026). User memory profiles raised agreement sycophancy by up to 45%. https://arxiv.org/abs/2509.12517
- **Recalling Too Well** (Bensal et al., preprint 2026). Memory raises sycophancy when beliefs are stored without their correcting context.

→ "Disagree when it matters" principle; beliefs stored with source in `intent-engine.md` §7.

### Evaluate with difficult simulated users
- **Mind the Sim2Real Gap in User Simulation** (Zhou et al., preprint 2026) and **Flipping the Dialogue** (Naous et al.). LLM-simulated users are too cooperative and polished, inflating success. https://arxiv.org/abs/2603.11245
- **SWE-Together** (Wu et al., Meta, preprint 2026). Simulators anchored to a hidden ground-truth intent. https://arxiv.org/abs/2606.29957

→ `benchmark/`: vague, terse personas with hidden intent cards; scored on what the executor still has to guess.
