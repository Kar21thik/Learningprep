# RAG Learning Index — Theory + Build + Interview Ready

A structured 14-topic curriculum covering Retrieval-Augmented Generation from foundations to production.

---

## Phase 1 — Foundations

| # | Topic | What You'll Build | Key Interview Questions |
|---|-------|-------------------|------------------------|
| 1 | [What is RAG?](phase1-foundations/01-what-is-rag/) | RAG vs fine-tuning comparison, simple pipeline sketch | What is RAG? Why use it over fine-tuning? What are the failure modes of RAG? |
| 2 | [Text Chunking](phase1-foundations/02-text-chunking/) | Chunking strategy comparator (fixed-size, semantic, recursive) | What chunk size is optimal? What is chunk overlap? What is recursive chunking? |
| 3 | [Embeddings](phase1-foundations/03-embeddings/) | Embed sentences, compute cosine similarity manually | What is an embedding? How does cosine similarity work? Which embedding model to choose? |
| 4 | [Vector DB Basics](phase1-foundations/04-vector-db-basics/) | In-memory vector store from scratch, then plug into Weaviate | What is a vector database? How does ANN search work? What is HNSW? |

---

## Phase 2 — Retrieval

| # | Topic | What You'll Build | Key Interview Questions |
|---|-------|-------------------|------------------------|
| 5 | [Semantic Search](phase2-retrieval/05-semantic-search/) | Full semantic search pipeline: embed query → search → return top-K | What is semantic search? Dense vs sparse retrieval? What is top-K? |
| 6 | [Hybrid Search](phase2-retrieval/06-hybrid-search/) | Hybrid search with tunable alpha, compare vs pure semantic | What is BM25? What is hybrid search? When to use it? What does alpha control? |
| 7 | [Reranking](phase2-retrieval/07-reranking/) | Two-stage retrieval: BM25/dense → cross-encoder rerank | What is reranking? Bi-encoder vs cross-encoder? Is reranking worth the latency cost? |
| 8 | [Filters & Metadata](phase2-retrieval/08-filters-metadata/) | Add metadata to chunks, filter by date/source/type | Pre-filter vs post-filter? How do you design a metadata schema? When does filtering hurt recall? |

---

## Phase 3 — Generation

| # | Topic | What You'll Build | Key Interview Questions |
|---|-------|-------------------|------------------------|
| 9 | [Prompt Engineering](phase3-generation/09-prompt-engineering/) | Prompt templates with chunk injection, test formatting variants | How do you format RAG context in a prompt? What is a system prompt? How do you order chunks? |
| 10 | [Answer Generation](phase3-generation/10-answer-generation/) | End-to-end RAG pipeline: retrieve → prompt → generate → return | How do you prevent hallucination in RAG? What is grounding? How do you handle no-context answers? |
| 11 | [Chat History / Follow-up](phase3-generation/11-chat-history/) | Multi-turn RAG chatbot with history-aware retrieval | How do you handle multi-turn RAG? What is query rewriting? How do you manage memory? |

---

## Phase 4 — Production

| # | Topic | What You'll Build | Key Interview Questions |
|---|-------|-------------------|------------------------|
| 12 | [Ingestion Pipeline](phase4-production/12-ingestion-pipeline/) | Async ingestion pipeline with idempotent upsert | How do you design a RAG ingestion pipeline? How do you handle updates/deletes? What is idempotent upsert? |
| 13 | [Evaluation](phase4-production/13-evaluation/) | RAGAS eval on your built pipeline, score retrieval and generation | How do you evaluate a RAG system? What is RAGAS? What is faithfulness vs answer relevance? |
| 14 | [Interview Prep](phase4-production/14-interview-prep/) | Mock Q&A covering all 13 topics, full architecture from memory | Full system design: "Design a RAG system for a 10M document corpus" |

---

## Folder Structure

```
RAG/
├── phase1-foundations/
│   ├── 01-what-is-rag/
│   ├── 02-text-chunking/
│   ├── 03-embeddings/
│   └── 04-vector-db-basics/
├── phase2-retrieval/
│   ├── 05-semantic-search/
│   ├── 06-hybrid-search/
│   ├── 07-reranking/
│   └── 08-filters-metadata/
├── phase3-generation/
│   ├── 09-prompt-engineering/
│   ├── 10-answer-generation/
│   └── 11-chat-history/
└── phase4-production/
    ├── 12-ingestion-pipeline/
    ├── 13-evaluation/
    └── 14-interview-prep/
```
