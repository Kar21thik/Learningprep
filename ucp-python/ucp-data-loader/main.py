"""
ucp-data-loader
---------------
Watches an input folder for new files, loads them, computes a content hash
(for idempotent dedup), and publishes RawDocument payloads to the raw queue.

Mirrors: ucp-data-loader (Java/Spring)
Queue out: ucp:raw (Redis Stream)
"""
import hashlib
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from shared.config import settings
from shared.queue import StreamProducer

SUPPORTED = {".txt", ".md", ".pdf", ".html", ".docx"}
WATCH_DIR = Path("./data/input")


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def load_file(path: Path) -> str | None:
    ext = path.suffix.lower()
    if ext in (".txt", ".md", ".html"):
        return path.read_text(errors="ignore")
    if ext == ".pdf":
        try:
            import pypdf
            reader = pypdf.PdfReader(str(path))
            return "\n".join(p.extract_text() or "" for p in reader.pages)
        except ImportError:
            print("pypdf not installed — skipping PDF")
            return None
    if ext == ".docx":
        try:
            import docx
            doc = docx.Document(str(path))
            return "\n".join(p.text for p in doc.paragraphs)
        except ImportError:
            print("python-docx not installed — skipping DOCX")
            return None
    return None


def watch(producer: StreamProducer, seen: set):
    WATCH_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Watching {WATCH_DIR.resolve()} ...")
    while True:
        for path in WATCH_DIR.iterdir():
            if path.suffix.lower() not in SUPPORTED or path.name in seen:
                continue
            content = load_file(path)
            if not content:
                continue
            doc_id = content_hash(content)
            producer.publish({
                "doc_id": doc_id,
                "source_path": str(path),
                "content": content,
                "doc_type": path.suffix.lstrip("."),
            })
            seen.add(path.name)
            print(f"  Published: {path.name} → doc_id={doc_id}")
        time.sleep(3)


if __name__ == "__main__":
    producer = StreamProducer(settings.redis_url, settings.raw_stream)
    watch(producer, seen=set())
