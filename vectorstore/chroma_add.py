from vectorstore.chroma_client import get_chroma_collection


def add_to_chroma(chunk, embedding, metadata):
    collection = get_chroma_collection()

    collection.add(
        ids=[metadata["chunk_id"]],
        documents=[chunk],
        embeddings=[embedding],
        metadatas=[metadata],
    )

    print(f"Saved chunk: {metadata['chunk_id']}")
