from typing import TypedDict, List, Optional

class AgentState(TypedDict):
    user_query: str
    tasks: List[str]
    knowledge: Optional[str]
    ticket: Optional[str]
    priority: Optional[str]
    final_response: Optional[str]