from app.services.db import conn, cursor

def ticket_agent(state):
    query = state["user_query"]
    
#     check priority
    priority = state.get("priority", "medium")

    cursor.execute(
        "INSERT INTO tickets (query, priority) VALUES (?, ?)",
        (query, priority)
    )
    conn.commit()

    return {"ticket": f"Ticket created with priority {priority}"}