from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader, WebBaseLoader, Docx2txtLoader, UnstructuredMarkdownLoader, TextLoader

class RagRetriever:
    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

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
            chunk_size = 1000,
            chunk_overlap = 200
        )

        self.chunks = text_splitter.split_documents(self.document)

    def vector_embedding(self, question):
        vector_store = Chroma.from_documents(
            documents=self.chunks,
            embedding=self.embedding_model
        )

        retriever = vector_store.as_retriever(
            search_kwars={"k":4}
        )

        return retriever