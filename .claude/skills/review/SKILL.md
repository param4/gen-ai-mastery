---
name: review
description: Review my latest GenAI code like a senior AI engineer, then quiz me on it. Use when I say "review", "check my code", "is this right", or finish a build task.
---

1. Find what changed (git diff / recent files in `app/`, `evals/`). Read the relevant spec in `docs/specs/` if one exists.
2. Review, ranked by severity, one line each with `file:line`:
   - **Correctness:** API misuse, broken tool_use/tool_result pairing, unhandled stop reasons, retries, parsing.
   - **AI-specific:** prompt quality, context bloat, leakage between train and test data, eval contamination, judge bias, missing citations, injection surface, unbounded loops or cost.
   - **Production:** errors, timeouts, idempotency, logging/tracing, secrets.
   - **Measurement:** is there an eval proving it works? If not, that's the top finding.
3. Don't rewrite the code. Point to the fix; give a snippet only for non-AI boilerplate or after I've tried twice.
4. Ask 2-3 sharp questions that test whether I understand *why* my code works (or doesn't). Log the ones I can't answer in `docs/questions.md`.
5. If something here is post-worthy, say so in one line.
