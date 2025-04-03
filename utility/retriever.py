from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from config.embedding import embeddings
import shutil

from langchain_community.vectorstores import FAISS
from langchain_core.embeddings import Embeddings
import os
from pathlib import Path

from utility.load_and_split import load_and_split_docs

# Configuration
VECTORSTORE_DIR = "./faiss_index"
PDF_SOURCE_DIR = "./docs"

def get_retriever():
    """Returns always-available retriever, initializing if needed"""
    # Load existing or create new vectorstore
    if os.path.exists(VECTORSTORE_DIR):
        # When loading existing FAISS index
        vectorstore = FAISS.load_local(
            folder_path=VECTORSTORE_DIR,
            embeddings=embeddings,
            allow_dangerous_deserialization=True
        )
    else:
        # Initialize with empty documents if first run
        from langchain_core.documents import Document
        vectorstore = FAISS.from_documents([Document(page_content="")], embeddings)
        vectorstore.save_local(VECTORSTORE_DIR)
    
    return vectorstore.as_retriever()

def update_vectorstore(new_pdfs_dir: str):
    """Replaces the entire vectorstore with the current PDFs in the folder"""
    
    # Get the list of remaining PDFs
    remaining_pdfs = [os.path.join(new_pdfs_dir, f) for f in os.listdir(new_pdfs_dir) if f.endswith(".pdf")]
    
    if not remaining_pdfs:  # No PDFs left, clear the vector store
        if os.path.exists(VECTORSTORE_DIR):
            shutil.rmtree(VECTORSTORE_DIR)  # Remove the entire FAISS index
        return  # No need to proceed if no PDFs are left
    
    # 1. Load and split remaining PDFs
    new_docs = load_and_split_docs(new_pdfs_dir)
    
    # 2. Remove the old vectorstore
    if os.path.exists(VECTORSTORE_DIR):
        shutil.rmtree(VECTORSTORE_DIR)  # Completely remove old FAISS index
    
    # 3. Create a new FAISS index with the remaining PDFs
    vectorstore = FAISS.from_documents(new_docs, embeddings)
    
    # 4. Save the new FAISS index
    vectorstore.save_local(VECTORSTORE_DIR)