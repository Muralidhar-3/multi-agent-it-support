from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def get_vector_store():
    embedding_function = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return Chroma(
        persist_directory="data/chroma",
        embedding_function=embedding_function
    )