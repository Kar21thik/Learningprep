from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Weaviate
    weaviate_host: str = "localhost"
    weaviate_port: int = 8080
    weaviate_class: str = "Document"

    # MongoDB
    mongo_uri: str = "mongodb://localhost:27017"
    mongo_db: str = "ucp"

    # Redis (queue)
    redis_url: str = "redis://localhost:6379"
    raw_stream: str = "ucp:raw"
    chunked_stream: str = "ucp:chunked"

    # Embedding
    embedding_model: str = "BAAI/bge-small-en-v1.5"
    embedding_dim: int = 384

    # Reranker
    reranker_model: str = "BAAI/bge-reranker-large"
    rerank_top_k: int = 20   # candidates to fetch before reranking
    rerank_return_k: int = 5  # final top-K after rerank

    # LLM (Anthropic)
    anthropic_api_key: str = ""
    llm_model: str = "claude-haiku-4-5-20251001"

    # Service
    service_port: int = 8000

    class Config:
        env_file = ".env"


settings = Settings()
