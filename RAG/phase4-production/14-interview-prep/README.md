# 14 — Interview Prep

## Subtopics
- All 13 concepts consolidated
- Common RAG failure modes and how to fix each
- Tradeoff questions (chunking size, retrieval strategy, reranking)
- System design: RAG for 10M document corpus
- Drawing the full architecture from memory

## What You'll Build
- Mock interview Q&A covering all 13 topics
- Full system design write-up: "Design a RAG system for a 10M document corpus"
- Architecture diagram from memory

## Full System Design Prompt
> "Design a production RAG system that serves 10M documents, handles real-time updates, supports multi-tenant access, and must answer questions in under 2 seconds."

Cover: ingestion pipeline, chunking strategy, embedding choice, vector DB, retrieval strategy (hybrid + rerank), prompt design, LLM, eval, scaling.

## Common Failure Modes
| Failure | Cause | Fix |
|---------|-------|-----|
| Wrong chunks retrieved | Poor chunking or embedding mismatch | Tune chunk size, switch embedding model |
| Hallucination despite good retrieval | Weak grounding prompt | Tighten system prompt, add citation requirement |
| Retrieval miss on keyword queries | Pure semantic search | Add hybrid search (BM25 + dense) |
| Slow response | Reranking + large LLM | Cache embeddings, reduce rerank candidates |
| Follow-up questions retrieve wrong context | No query rewriting | Add condense-question step |

## Notes
