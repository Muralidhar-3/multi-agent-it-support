from app.services.llm import gemini_llm

def aggregator(state):
    prompt = f"""
    Combine results into a helpful response.

    Knowledge:
    {state.get('knowledge')}

    Ticket:
    {state.get('ticket')}

    Priority:
    {state.get('priority')}
    """

    response = gemini_llm(prompt)

    return {"final_response": response}