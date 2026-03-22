from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

def get_vector_store():
    return Chroma(
        persist_directory="data/chroma",
        embedding_function=OpenAIEmbeddings()
    )