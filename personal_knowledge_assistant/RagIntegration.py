from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader, WebBaseLoader, Docx2txtLoader, UnstructuredMarkdownLoader, TextLoader
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
store_path = BASE_DIR / 'Knowledge_Store'

class RagRetriever:
    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name = "sentence-transformers/all-MiniLM-L6-v2"
        )
        self.vector_store = Chroma(
            collection_name= 'store',
            embedding_function= self.embedding_model,
            persist_directory=store_path
        )

    def data_exists(self, topic, description):
        topic = topic.lower()
        description = description.lower()
        result = self.vector_store._collection.get(
            where={
                "topic": topic,
                "description": description
            },
            limit=1
        )
        return len(result["ids"]) > 0

    def file_loader(self, source):
        if source.startswith("https") or source.startswith("http"):
            loader = WebBaseLoader(source)

        elif source.endswith(".pdf"):
            loader = PyMuPDFLoader(source)

        elif source.endswith(".docx"):
            loader = Docx2txtLoader(source)

        elif source.endswith(".md"):
            loader = UnstructuredMarkdownLoader(source)

        elif source.endswith(".txt"):
            loader = TextLoader(source)

        else:
            raise ValueError("Unsupported source")
        
        self.document = loader.load()

    def text_splitting(self, topic, description):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap = 200
        )
        self.chunks = text_splitter.split_documents(self.document)
        topic = topic.lower()
        description =  description.lower()
        for chunk in self.chunks:
            chunk.metadata['topic'] = topic
            chunk.metadata['description'] = description

        self.vector_store.add_documents(self.chunks)

        return self.chunks

    def vector_embedding(self, question):
        retriever = self.vector_store.max_marginal_relevance_search(
        query=question,
        k=5,
        fetch_k=15
    )
        return retriever