---
name: checkpoint
description: Phase gate for my GenAI roadmap. Verify the phase metric, test my understanding, update progress, and draft the build-in-public post. Use when I say "checkpoint", "am I done with this phase", "wrap up the week", or end a working session.
---

1. **Metric check:** find the phase's metric in `evals/results/`. Missing, or worse than the baseline → the phase is not done; say what's missing.
2. **Concept check:** ask me to explain 3 concepts from the phase's checklist in `docs/roadmap.md`, one at a time. Be strict. Log misses in `docs/questions.md`.
3. **Open questions:** review unresolved items in `docs/questions.md` for this phase.
4. **Update (ask first):** `docs/progress.md` (phase, week, next step, metrics table, dated log entry) and `docs/decisions.md` if a design choice was made.
5. **Post (if the phase has one):** read `../blog/STYLE.md` first and follow it exactly. Draft from `docs/journal.md` into `../blog/drafts/<date>-<slug>.md` (blog post, plus LinkedIn and X cuts at the bottom). Use only real numbers from `evals/results/`; never invent results. Leave the title, opening and verdict marked `TODO(Param)` for me to rewrite in my own voice.
6. End with one line: the next phase's first step.
