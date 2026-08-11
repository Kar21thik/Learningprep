# 12 — Ingestion Pipeline

## Subtopics
- Document loading: PDFs, HTML, DOCX, plain text
- Pipeline stages: load → clean → chunk → embed → upsert
- Idempotent upsert (re-ingesting same doc doesn't create duplicates)
- Handling updates and deletes
- Async/batch ingestion for scale
- Mirrors a real production pattern (e.g. ucp-llm-processor style)

## What You'll Build
- Async ingestion pipeline: watch a folder → load new docs → chunk → embed → upsert to vector DB
- Idempotent upsert using content hash as ID

## Interview Angles
- How do you design a RAG ingestion pipeline for production?
- How do you handle document updates and deletes in a vector DB?
- What is idempotent upsert and why does it matter?
- How do you scale ingestion to millions of documents?

## Notes
