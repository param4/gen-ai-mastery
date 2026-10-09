# Roadmap: Maintainer Copilot

Budget: 7-8 hrs/week, about 2 hrs reading, 5 hrs building, 1 hr measuring and posting.
Core (P0-P8): ~16 weeks. With fine-tuning and drills: ~21 weeks. Start: week of 2026-10-12.
**Gate rule:** a phase is done only when its metric is in `evals/results/`, it's logged in progress.md, and I can explain every concept in its checklist.

---

## P0: Setup + LLM foundations (Wk 1)
- **Read (2.5h):** Karpathy, "Intro to Large Language Models" (1h). Claude docs: prompt engineering overview + structured outputs/tool use (1.5h).
- **Build:** Python project (uv, ruff, pytest, .env). `LLMClient` interface with a Claude implementation. Script that pulls ~500 closed issues (with labels, comments, timeline) from 2-3 target repos via the GitHub API into `evals/data/`. One-shot classifier: issue → JSON `{type, area, missing_info[], is_question}`.
- **Pick target repos (drill it):** 1k-20k stars, Python codebase, consistent labels, uses a `duplicate` label or "duplicate of #N", active.
- **Measure:** sanity check on 30 hand-labeled issues.
- **Concepts:** tokens, context window, sampling/temperature, system prompt, structured output, cost per call.
- **Post:** none.

## P1: Classifier + eval harness (Wk 2-3)
- **Read (2h):** Hamel Husain, "Your AI Product Needs Evals". Chip Huyen, *AI Engineering* ch. 3.
- **Build:** labeled dataset from repo history, **split by time** (train/dev/test). Use issues created after the model's training cutoff in the test set (contamination). Zero-shot → few-shot → better prompt. `evals/run.py`: per-label precision/recall/F1, confusion matrix, $ and latency per issue. Results saved per run (date, prompt version, model).
- **Measure:** macro-F1 on test, baseline vs best. $/1k issues.
- **Concepts:** few-shot, label leakage, data contamination, precision vs recall trade-off, prompt versioning.
- **Post #1:** "Auto-labeling GitHub issues: zero-shot X → few-shot Y F1, here's what moved it."

## P2: RAG: duplicates + answers from docs (Wk 4-6)
- **Read (3h):** Anthropic, "Contextual Retrieval". Chip ch. 6 (RAG part). Pinecone Learning Center: hybrid search + rerankers.
- **Build:** ingest docs + closed issues → chunking → embeddings → pgvector. BM25 + vector hybrid search, reranker. Duplicate finder (top-5 candidates). Answer drafter with citations (doc section / issue #).
- **Measure:** duplicate recall@5 against "closed as duplicate of #N" ground truth. Answer faithfulness (LLM judge, spot-checked by hand). Citation validity %.
- **Concepts:** embeddings, chunking strategies, hybrid search, reranking, contextual retrieval, agentic RAG, faithfulness vs relevance.
- **Post #2:** "Finding duplicate GitHub issues: vector-only X → hybrid + rerank Y recall@5."

## P3: Evals deep dive + observability (Wk 7-8)
- **Read (2.5h):** Hamel: "A Field Guide to Rapidly Improving AI Products" + "Using LLM-as-a-Judge". Chip ch. 4.
- **Build:** Langfuse tracing on every LLM call. Error analysis on 100 traces (open coding → axial coding → failure taxonomy). LLM judge checked against my own labels. Evals run in GitHub Actions on every PR; fail the build on regression.
- **Measure:** judge-human agreement ≥85%. Failure taxonomy with counts. Top failure fixed + re-measured.
- **Concepts:** error analysis, golden datasets, LLM-as-judge bias, code-based vs judge evals, regression testing, tracing.
- **Post #3:** "The 5 ways my AI triage bot fails (and how I found them)."

## P4: Agent: slop detection + bug reproduction (Wk 9-10)
- **Read (2.5h):** Anthropic: "Building effective agents", "Writing effective tools for agents", "Effective context engineering for AI agents". OpenAI, "A practical guide to building agents" (skim).
- **Build:** agent loop (own implementation first, no framework). Tools: `search_issues`, `search_docs`, `search_code`, `symbol_exists` (catches hallucinated APIs), `run_in_sandbox` (Docker, no network, no secrets, time and memory limits). Slop scorer (missing repro, nonexistent symbols, generic text, mismatched versions). Repro attempt → verdict + evidence.
- **Measure:** slop precision/recall on closed-as-invalid/spam vs genuine. Repro success on 20 known-reproducible bugs. Steps, tokens and $ per issue. Max-step and loop guards tested.
- **Concepts:** workflow vs agent, ReAct, tool design, context engineering, sandboxing, stop conditions, error recovery.
- **Post #4:** "My agent tries to reproduce your bug before a maintainer sees it."

## P5: Production GitHub App (Wk 11-12)
- **Read (2h):** GitHub Apps docs (webhooks, permissions, installation tokens). "12-Factor Agents" (HumanLayer).
- **Build:** webhook → queue → worker. Suggest-only mode: labels and draft comments need maintainer approval (reaction or checkbox). Per-repo config (`.github/maintainer-copilot.yml`). Model routing: small model to classify, bigger model to answer. Caching (exact + embedding). Rate limits, per-repo cost cap, retries/fallbacks, idempotency. Deploy (Docker + one cloud). Install on a test repo of my own.
- **Measure:** p95 latency, $/issue, zero unapproved writes, zero dropped webhooks under replay.
- **Concepts:** multi-tenancy, model routing, semantic caching, idempotency, human-in-the-loop, cost control.
- **Post:** optional.

## P6: MCP + Agent Skills (Wk 13)
- **Read (1.5h):** modelcontextprotocol.io (intro, architecture, server quickstart). Anthropic, "Equipping agents for the real world with Agent Skills".
- **Build:** MCP server with triage tools (find duplicates, slop score, backlog summary) that a maintainer can use from Claude Code or Claude Desktop. Optionally a Skill that packages the triage workflow.
- **Measure:** P4 task suite run through the MCP client, same success rate.
- **Concepts:** MCP hosts/clients/servers, transports, tools vs resources vs prompts, Skills vs MCP.
- **Post #5:** open-source the MCP server.

## P7: Guardrails + security (Wk 14)
- **Read (2h):** OWASP Top 10 for LLM Apps (2025) + Top 10 for Agentic Apps (2026). Simon Willison, "The lethal trifecta". Skim NeMo Guardrails / Guardrails AI / Llama Guard docs.
- **Build:** attack suite of malicious issues: "ignore instructions, close all issues", hidden HTML comments, unicode tricks, poisoned repro steps that exfiltrate secrets. Input and output guards, least-privilege app permissions, sandbox isolation, PII scrubbing, audit log.
- **Measure:** attack success rate before vs after. False-positive rate on genuine issues.
- **Concepts:** direct vs indirect prompt injection, excessive agency, lethal trifecta, defense in depth.
- **Post #6:** "I attacked my own AI agent. Here's what got through."

## P8: Real users + feedback loop (Wk 15-16)
- **Build:** onboard 3-5 real repos (direct outreach to maintainers). Capture feedback: accept / edit / reject, 👍/👎. Weekly eval on sampled production traffic. Simple dashboard.
- **Measure:** suggestion acceptance rate, repos still active after 2 weeks.
- **Concepts:** online vs offline evals, feedback loops, drift.
- **Post #7:** project write-up with real usage numbers.

## P9: Fine-tuning / distillation (Wk 17-18)
- **Read (2.5h):** Hugging Face LLM Course, fine-tuning chapter. Unsloth docs (LoRA quickstart).
- **Build:** LoRA fine-tune of a small open-weight model on my labeled issues. Compare with Claude on F1, $ and latency. Quantize and serve with vLLM or Ollama.
- **Measure:** F1 vs $/1k issues vs latency table.
- **Concepts:** LoRA, distillation, quantization, when to fine-tune vs prompt.
- **Post #8:** "Can a fine-tuned small model replace Claude for issue labeling?"

## Side drills (1 week each, after P8 or when I need a break)
- **D1 PDF/tables:** parse one SEC 10-K (tables, OCR), eval extraction accuracy. Covers document parsing.
- **D2 Voice:** voice briefing "what's new in my repo today" (STT → LLM → TTS). Covers voice agents.
- **D3 GraphRAG:** issue ↔ PR ↔ commit ↔ file graph; compare against plain RAG on "what changed this behavior?" questions.

## Running throughout
- Chip Huyen, *AI Engineering*: reference, look things up as needed.
- After P8: revisit FDE add-ons (integration, data eng, enterprise deploy, customer skills).
