from langgraph.graph import StateGraph
from app.graph.state import AgentState

from app.agents.planner import planner
from app.agents.knowledge import knowledge_agent
from app.agents.ticket import ticket_agent
from app.agents.priority import priority_agent
from app.agents.aggregator import aggregator

def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("planner", planner)
    builder.add_node("knowledge", knowledge_agent)
    builder.add_node("ticket", ticket_agent)
    builder.add_node("priority", priority_agent)
    builder.add_node("aggregator", aggregator)

    builder.set_entry_point("planner")

    builder.add_edge("planner", "knowledge")
    builder.add_edge("planner", "priority")
    builder.add_edge("planner", "ticket")

    builder.add_edge("knowledge", "aggregator")
    builder.add_edge("priority", "aggregator")
    builder.add_edge("ticket", "aggregator")

    return builder.compile()