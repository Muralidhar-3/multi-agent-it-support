from app.services.llm import groq_llm

def priority_agent(state):
    query = state["user_query"]

    prompt = f"""
    Classify priority: low, medium, high

    Query: {query}
    """

    response = groq_llm(prompt)

    return {"priority": response.strip().lower()}