from app.services.llm import groq_llm

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

    response = groq_llm(prompt)

    print("aggregator", response)

    return {"final_response": response}