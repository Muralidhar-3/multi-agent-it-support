from app.services.vector_store import get_vector_store
from app.services.llm import groq_llm, openrouter_llm

def knowledge_agent(state):
    query = state["user_query"]

    db = get_vector_store()
    docs = db.similarity_search(query, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer using context.

    Context:
    {context}

    Query:
    {query}
    """

    try:
        response = groq_llm(prompt)
    except:
        response = openrouter_llm(prompt)

    return {"knowledge": response}