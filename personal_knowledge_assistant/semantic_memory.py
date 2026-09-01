from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from datetime import datetime
import os

class ConversationMemory:
    def __init__(self):
        self.embedding = HuggingFaceEmbeddings(
            model_name = "sentence-transformers/all-MiniLM-L6-v2"
        )

        store_path = os.getenv("MEMORY_STORE_PATH", "Memory_Store")
        
        self.vector_store = Chroma(
            collection_name="conversation_memory",
            embedding_function=self.embedding,
            persist_directory=store_path
        )

    def save_memory(self, conversation: list, topic: str, description: str):
        timestamp = datetime.now().isoformat()

        memory_text = "\n".join(
            f"{message.type}: {message.content}"
            for message in conversation
        )

        documents = Document(
            page_content=memory_text,
            metadata = {
                "timestamp": timestamp,
                "topic": topic,
                "description": description
            }
        )

        self.vector_store.add_documents([documents])

    def search_memory(self, query: str, k: int = 3):
        results = self.vector_store.similarity_search(
            query,
            k=k
        )

        return results

    def clear_memory(self):
        self.vector_store.delete_collection()
