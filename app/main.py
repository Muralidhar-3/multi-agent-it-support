from fastapi import FastAPI
from app.graph.builder import build_graph
from pydantic import BaseModel

app = FastAPI()
graph = build_graph()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def handle_query(request: QueryRequest):
    result = graph.invoke({
        "user_query": request.query
    })

    return {"response": result["final_response"]}