# 07 — Reranking

## Subtopics
- Why first-stage retrieval is approximate
- Bi-encoder (fast, used for retrieval) vs cross-encoder (slow, accurate)
- Cross-encoder reranking: feed (query, passage) pair → relevance score
- Cohere Rerank / BGE reranker / ms-marco models
- Latency vs accuracy tradeoff, when to rerank

## What You'll Build
- Two-stage retrieval: BM25/dense retrieval → cross-encoder rerank top-20 → return top-5
- Compare ranking order before and after reranking

## Interview Angles
- What is reranking and why is it needed?
- Bi-encoder vs cross-encoder — speed and accuracy tradeoffs?
- Is reranking worth the added latency?
- How do you decide how many candidates to retrieve before reranking?

## Notes
