from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader, WebBaseLoader, Docx2txtLoader, UnstructuredMarkdownLoader, TextLoader

class RagRetriever:
    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.vector_store = Chroma(
             collection_name= 'store',
             embedding_function = self.embedding_model,
             persist_directory='./Rag_Store'
        )

    def file_loader(self, source):
        if source.startswith(("http://", "https://")):
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

    def text_splitting(self, policy_type):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 500,
            chunk_overlap = 100
        )

        self.chunks = text_splitter.split_documents(self.document)

        for chunk in self.chunks:
            chunk.metadata["policy"] = policy_type

        self.vector_store.add_documents(self.chunks)

    def vector_embedding(self, question, policy_type):
        retriever = self.vector_store.as_retriever(
            search_kwargs={"k": 4}
        )

        documents = retriever.invoke(question, filter={"policy": policy_type})

        return documents