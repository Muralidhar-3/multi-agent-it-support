import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

DATA_PATH = "data/docs"
CHROMA_PATH = "data/chroma"


def ingest_documents():
    documents = []

    # Load all txt files
    for file in os.listdir(DATA_PATH):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(DATA_PATH, file))
            documents.extend(loader.load())

    print(f"Loaded {len(documents)} documents")

    # Chunking
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    # Free embeddings (HuggingFace)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Store in Chroma
    db = Chroma.from_documents(
        chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )

    db.persist()
    print("✅ Documents ingested successfully!")


# 👇 THIS PART IS IMPORTANT
if __name__ == "__main__":
    ingest_documents()