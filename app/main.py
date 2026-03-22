from fastapi import FastAPI
from app.graph.builder import build_graph

app = FastAPI()
graph = build_graph()

@app.post("/query")
def handle_query(query: str):
    result = graph.invoke({
        "user_query": query
    })

    return {"response": result["final_response"]}