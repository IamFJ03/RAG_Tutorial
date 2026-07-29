from langchain_chroma import Chroma
from dotenv import load_dotenv
import os
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader, DirectoryLoader
load_dotenv()

def main():
    print("Hello from rag-beginners!")


if __name__ == "__main__":
    main()
