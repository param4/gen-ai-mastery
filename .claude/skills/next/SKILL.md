---
name: next
description: Tell me exactly what to do right now in my GenAI learning plan. What to read (with a time budget), what to build, and how to measure it. Use when I say "next", "what now", "where are we", or start a session without a clear task.
---

1. Read `docs/progress.md` and the current phase in `docs/roadmap.md`. Check `docs/questions.md` for open items.
2. If progress.md hasn't been updated in 7+ days, say so in one line and shrink the next step to a task under 1 hour.
3. Reply in at most 6 lines:
   - **Where:** phase, week, % of the phase done
   - **Read:** exact resource + section + time (only if this step needs it; max 1h)
   - **Build:** one concrete task, small enough for one 1-2h sitting
   - **Done when:** the check or number that proves it
   - **Blocker/risk:** only if one exists
4. Don't write the code. If the task needs a spec first, suggest `/drill <task>`.
