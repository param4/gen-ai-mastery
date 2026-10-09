# Progress

**Current phase:** P0 (Setup + LLM foundations)
**Week:** 1 (starts 2026-10-12)
**Last updated:** 2026-10-09
**Next step:** watch Karpathy's "Intro to LLMs" (1h), then `/drill target repos`.
**Blocked on:** none

## Metrics so far
| Phase | Metric | Baseline | Best | Date |
|---|---|---|---|---|

## Prior work (from `../ai-upskill`, Apr 2026, TypeScript)
- Done: Messages API basics (system, max_tokens, content blocks, stop_reason, usage). Hand-rolled tool-use loop (`ai-upskill/code/week-1/tool-use.ts`): parallel tool calls, `is_error` results, recursion guard, every stop_reason handled.
- Known bug there: `AnthropicUtil.logResponse` builds the final text but never prints it, so the answer after `end_turn` is silently dropped.
- Credit in this plan: P0 skips API basics. In P4, port that loop to Python as the starting point.

## Log
### 2026-10-09
- Project set up. Capstone chosen: Maintainer Copilot. Stack: Python + Claude. Mode: I write, buddy reviews.
