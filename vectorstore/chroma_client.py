import chromadb
from chromadb.config import Settings


def get_chroma_collection():
    client = chromadb.Client(
        Settings(persist_directory="./data/chroma_db", anonymized_telemetry=False)
    )

    collection = client.get_or_create_collection(
        name="notices", metadata={"hnsw:space": "cosine"}
    )

    return collection
