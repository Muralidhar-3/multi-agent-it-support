from app.services.llm import groq_llm
import ast

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

    Only provide the information if the query is related to IT issues. 
    if the user query is not related to IT issues, 
    do not provide any tasks and say I don not have information about it.
    """

    response = groq_llm(prompt)

    try:
        tasks = ast.literal_eval(response)
    except:
        tasks = ["knowledge", "priority"]

    print("planner", tasks)
    return {"tasks": tasks}
    