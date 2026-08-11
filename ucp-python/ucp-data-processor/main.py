"""
ucp-data-processor
------------------
Consumes raw documents from the raw queue, cleans text, splits into chunks,
saves chunk metadata to MongoDB, then publishes each chunk to the chunked queue.

Mirrors: ucp-data-processor (Java/Spring)
Queue in:  ucp:raw      (Redis Stream)
Queue out: ucp:chunked  (Redis Stream)
Store:     MongoDB (ucp.chunks)
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from shared.config import settings
from shared.queue import StreamProducer, StreamConsumer
from pymongo import MongoClient

CHUNK_SIZE = 512      # characters
CHUNK_OVERLAP = 64


def clean(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    chunks, start = [], 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start += size - overlap
    return chunks


def process(msg: dict, producer: StreamProducer, collection):
    doc_id = msg["doc_id"]
    content = clean(msg["content"])
    chunks = chunk_text(content)

    for i, chunk in enumerate(chunks):
        chunk_id = f"{doc_id}_{i}"
        doc = {
            "chunk_id": chunk_id,
            "doc_id": doc_id,
            "content": chunk,
            "chunk_index": i,
            "source_path": msg["source_path"],
            "doc_type": msg["doc_type"],
        }
        # Idempotent upsert — replace if same chunk_id already exists
        collection.replace_one({"chunk_id": chunk_id}, doc, upsert=True)
        producer.publish(doc)

    print(f"  Processed doc_id={doc_id} → {len(chunks)} chunks")


if __name__ == "__main__":
    mongo = MongoClient(settings.mongo_uri)[settings.mongo_db]["chunks"]
    mongo.create_index("chunk_id", unique=True)

    consumer = StreamConsumer(settings.redis_url, settings.raw_stream, "processor-group", "processor-1")
    producer = StreamProducer(settings.redis_url, settings.chunked_stream)

    print("ucp-data-processor running ...")
    while True:
        for msg_id, data in consumer.consume():
            process(data, producer, mongo)
            consumer.ack(msg_id)
