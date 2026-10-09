# Decisions

| Date | Decision | Why |
|---|---|---|
| 2026-10-09 | Capstone: Maintainer Copilot (GitHub triage + slop filter + repro) | Covers ~90% of the syllabus; free labeled data and ground truth; real 2026 pain (AI slop); built-in user feedback; enough data for fine-tuning |
| 2026-10-09 | Python | GenAI eval/RAG/fine-tuning tooling is Python-first |
| 2026-10-09 | Claude primary, behind an `LLMClient` interface | Matches the reading list; can swap providers for comparisons |
| 2026-10-09 | No agent framework until after P4 | Learn the loop by hand first |
| 2026-10-09 | pgvector as the vector store | Postgres I already know; one less service |
| 2026-10-09 | Suggest-only mode by default | Maintainers distrust bots; human approves every write |
