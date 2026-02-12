import chromadb
from chromadb.config import Settings
import os

class SemanticMemory:
    """
    Manages the long-term semantic memory using ChromaDB.
    """
    def __init__(self, persist_directory="./memory_db"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(name="jarvis_memory")

    def store_memory(self, content: str, metadata: dict = None):
        """
        Stores a memory fragment with optional metadata.
        """
        # In production, we'd use a real ID generator
        mem_id = f"mem_{int(time.time() * 1000)}"
        self.collection.add(
            documents=[content],
            metadatas=[metadata] if metadata else [{"timestamp": time.time()}],
            ids=[mem_id]
        )
        print(f"[*] Memory stored: {content[:50]}...")

    def query_memory(self, query: str, n_results: int = 5):
        """
        Retrieves relevant memories based on semantic similarity.
        """
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results

# Initialize singleton
import time
memory = SemanticMemory()
