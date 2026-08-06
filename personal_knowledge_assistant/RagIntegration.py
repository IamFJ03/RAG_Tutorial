from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader, WebBaseLoader, Docx2txtLoader, UnstructuredMarkdownLoader, TextLoader

class RagRetriever:
    def __init__(self, model_name = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name

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

    def text_splitting(self):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 500,
            chunk_overlap = 200
        )
        self.chunks = text_splitter.split_documents(self.document)
    
    def model_calling(self):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name = self.model_name
        )

    def vector_embedding(self):
        vector_store = Chroma.from_documents(
            documents = self.chunks,
            embedding = self.embedding_model
        )

        retriever = vector_store.as_retriever(
            search_kwargs = {"k":2}
        )

        return retriever