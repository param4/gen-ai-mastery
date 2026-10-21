# Interview Sprint (started 2026-10-20)
Mini Maintainer Copilot on pydantic/pydantic. Each block: concept (10-15m) → I build → 3 interview questions.

| # | Block | Build | Status |
|---|---|---|---|
| 1 | LLM basics | Issue classifier returning JSON | in progress: dataset |
| 2 | Evals | Score classifier vs real labels (precision/recall/F1) | |
| 3 | RAG | Duplicate finder (embeddings + BM25 + rerank), recall@5 | |
| 4 | Agents | Triage agent with 3 tools | |
| 5 | MCP | Expose tools to Claude Code | |
| 6 | Guardrails | Attack own agent with prompt injection, then defend | |
| 7 | Interview drill | System design + rapid-fire on fine-tuning/LoRA/serving | |

Stack: Python 3.12 (uv), Claude, local embeddings, in-memory BM25. No Docker.
Labels used: bug V2, feature request, question, documentation.

## Findings
- 2026-10-20: first fetch was imbalanced (322 bug / 73 feature / 4 docs / 1 question). Fix: fetch up to 100 per label.
