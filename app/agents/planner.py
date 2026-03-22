from app.services.llm import gemini_llm

def planner(state):
    
    query = state["user_query"]

    prompt = f"""
    Break the query into tasks.

    Available tasks:
    - knowledge
    - ticket
    - priority

    Query: {query}

    Output only a Python list.
    """

    response = gemini_llm(prompt)

    try:
        tasks = eval(response)
    except:
        tasks = ["knowledge", "priority"]

    return {"tasks": tasks}