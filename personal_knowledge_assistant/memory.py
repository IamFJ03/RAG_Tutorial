from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from datetime import datetime

class ConversationMemory:
    def __init__(self):
        self.embedding = HuggingFaceEmbeddings(
            model_name = "sentence-transformers/all-MiniLM-L6-v2"
        )

        self.vector_store = Chroma(
            collection_name="conversation_memory",
            embedding_function=self.embedding,
            persist_directory="./memory_db"
        )

    def save_memory(self, question: str, answer: str):
        timestamp = datetime.now().isoformat()

        memory_text = (
            f"Question: {question}\n"
            f"Answer: {answer}"
        )

        documents = Document(
            page_content=memory_text,
            metadata = {
                "question": question,
                "answer": answer,
                "timestamp": timestamp
            }
        )

        self.vector_store.add_documents([documents])

    def search_memory(self, query: str, k: int = 3):
        results = self.vector_store.similarity_search(
            query,
            k=k
        )

        return results
