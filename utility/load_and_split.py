from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config.embedding import embeddings



def load_and_split_docs(pdf_folder: str):
    
    loader = DirectoryLoader(
        pdf_folder,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True
    )
    
    docs_list = loader.load()

    # 2. Split documents
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=250,
        chunk_overlap=0
    )
    doc_splits = text_splitter.split_documents(docs_list)
    
    return doc_splits

