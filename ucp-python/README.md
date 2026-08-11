# UCP Python — Production RAG Pipeline (Local)

A Python reimplementation of the ITF Unified Content Pipeline (UCP) for local learning.
Mirrors the real production architecture, replacing Java/Spring with Python equivalents.

---

## Architecture

```
[Extractors / File Watcher]
        │
        ▼
  ucp-data-loader        ← loads raw docs (PDF, HTML, DOCX, text)
        │
        ▼ (in-process queue / Redis Stream / file queue)
  ucp-data-processor     ← cleans, chunks, stores metadata → MongoDB
        │
        ▼ (queue)
  ucp-llm-processor      ← embeds chunks → upserts into Weaviate
        │
        ▼
     Weaviate             ← vector store (embeddings)
     MongoDB              ← document metadata store

        │
        ▼
   ucp-service            ← REST API (FastAPI) backed by MongoDB + Weaviate
        │
        ▼
     ucp-rag              ← RAG search layer: semantic/hybrid search,
                             reranking, context assembly, LLM call, streaming
```

---

## Module Map

| Module | Production Equivalent | What it does |
|--------|----------------------|--------------|
| `ucp-data-loader` | ucp-data-loader | Watches folder / ingests files, pushes to queue |
| `ucp-data-processor` | ucp-data-processor | Cleans + chunks, saves metadata to MongoDB |
| `ucp-llm-processor` | ucp-llm-processor | Consumes queue, embeds chunks, upserts to Weaviate |
| `ucp-rag` | ucp-rag | Semantic/hybrid search, rerank, context assembly, LLM call |
| `ucp-service` | ucp-service | FastAPI REST endpoints over MongoDB + Weaviate |
| `shared` | shared libs | Common models, queue client, config |
| `infra` | Docker Compose | Weaviate + MongoDB + Redis local stack |

---

## Stack (Python equivalents)

| Production (Java) | Python Equivalent |
|-------------------|-------------------|
| Spring Boot | FastAPI |
| Apache Pulsar | Redis Streams (local) |
| Weaviate client | weaviate-client |
| MongoDB | pymongo / motor |
| amazon-nova-lite (Spring AI) | Claude via Anthropic SDK |
| embed-bge-reranker-large | sentence-transformers (BGE reranker) |
| Spring AI embeddings | sentence-transformers / OpenAI embeddings |

---

## Run Order

```bash
# 1. Start infra
cd infra && docker compose up -d

# 2. Start processor services
python ucp-data-loader/main.py
python ucp-data-processor/main.py
python ucp-llm-processor/main.py

# 3. Start API
python ucp-service/main.py

# 4. Query
curl http://localhost:8000/search?q=your+question
```

---

## Learning Goals

- Understand each stage of a production RAG pipeline
- See how documents flow from raw file → chunks → embeddings → answers
- Build and debug each module independently
- Mirror real production patterns: idempotent upsert, async processing, streaming LLM responses

---

## Phases

- [ ] Phase 1 — Infra up (Weaviate + MongoDB + Redis via Docker)
- [ ] Phase 2 — ucp-data-loader (file watcher → queue)
- [ ] Phase 3 — ucp-data-processor (chunk + MongoDB)
- [ ] Phase 4 — ucp-llm-processor (embed + Weaviate upsert)
- [ ] Phase 5 — ucp-rag (search + rerank + LLM)
- [ ] Phase 6 — ucp-service (FastAPI endpoints)
- [ ] Phase 7 — Wire end to end, test full flow
