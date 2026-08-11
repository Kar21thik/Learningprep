# 10 — Answer Generation

## Subtopics
- End-to-end RAG pipeline wiring: retrieve → format → generate → return
- Grounding: ensuring answer only uses retrieved context
- Handling no-context answers (fallback behavior)
- Streaming vs batch generation
- Citation / source attribution in the answer

## What You'll Build
- Complete RAG pipeline: query → retrieve chunks → build prompt → call LLM → return grounded answer
- Fallback path when retrieval returns nothing relevant

## Interview Angles
- How do you prevent hallucination in RAG generation?
- What is grounding and how do you enforce it?
- How do you handle the case where retrieved context doesn't answer the question?
- How do you add source citations to RAG answers?

## Notes
