---
name: drill
description: Drill a fuzzy feature or requirement down into a buildable spec with eval criteria before any code is written. Use when I say "drill", "let's spec X", "what exactly should X do", or I'm about to build something without a clear requirement.
---

Act as a tech lead running a requirements session. Ask questions in small batches (max 3 at a time). Don't answer them for me; give a recommended default only when I'm stuck.

Cover, in order:
1. **User + job:** who uses it (maintainer, reporter, me) and what decision it helps them make.
2. **Input/output contract:** exact input fields, exact output shape (JSON schema), what "no answer" looks like.
3. **Ground truth:** where the correct answers come from (labels, duplicate links, closed-as-invalid, hand labels). How many examples, how they're split (by time), how contamination is avoided.
4. **Metric + target:** one primary metric, one guardrail metric (cost/latency/false positives), a baseline to beat.
5. **Failure modes:** empty or garbage input, prompt injection, API failure, ambiguous cases. What the system does in each.
6. **Scope cut:** the smallest version that produces the metric. Explicitly list what's out.
7. **What to read first:** at most 1 resource, if a concept is new.

End by writing the spec to `docs/specs/<feature>.md` (ask first): goal, contract, data, metric + target, failure modes, out of scope, first task. Then stop. I build.
