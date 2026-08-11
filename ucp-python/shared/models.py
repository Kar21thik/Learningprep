from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class RawDocument:
    """Loaded from disk, pushed to raw queue."""
    doc_id: str          # content hash (idempotent)
    source_path: str
    content: str
    doc_type: str        # pdf, html, txt, docx
    ingested_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Chunk:
    """One chunk of a document, stored in MongoDB + embedded into Weaviate."""
    chunk_id: str        # doc_id + chunk index
    doc_id: str
    content: str
    chunk_index: int
    source_path: str
    doc_type: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    embedding: Optional[list[float]] = None


@dataclass
class SearchResult:
    chunk_id: str
    doc_id: str
    content: str
    source_path: str
    score: float
