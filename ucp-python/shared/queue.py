"""
Redis Streams-based queue — mirrors Apache Pulsar producer/consumer pattern.
"""
import json
import redis


class StreamProducer:
    def __init__(self, redis_url: str, stream: str):
        self.r = redis.from_url(redis_url)
        self.stream = stream

    def publish(self, data: dict):
        self.r.xadd(self.stream, {"payload": json.dumps(data)})


class StreamConsumer:
    def __init__(self, redis_url: str, stream: str, group: str, consumer: str):
        self.r = redis.from_url(redis_url)
        self.stream = stream
        self.group = group
        self.consumer = consumer
        self._ensure_group()

    def _ensure_group(self):
        try:
            self.r.xgroup_create(self.stream, self.group, id="0", mkstream=True)
        except redis.exceptions.ResponseError:
            pass  # group already exists

    def consume(self, count: int = 10, block_ms: int = 1000):
        """Yields (message_id, data) tuples. Call ack() after processing."""
        messages = self.r.xreadgroup(
            self.group, self.consumer, {self.stream: ">"}, count=count, block=block_ms
        )
        if not messages:
            return
        for _, entries in messages:
            for msg_id, fields in entries:
                yield msg_id, json.loads(fields[b"payload"])

    def ack(self, msg_id):
        self.r.xack(self.stream, self.group, msg_id)
