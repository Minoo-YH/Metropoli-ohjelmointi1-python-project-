from src.db.connection import get_connection

def get_all_goals():
    conn = get_connection()
    if not conn:
        return []
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM goal")
    goals = cursor.fetchall()
    cursor.close()
    conn.close()
    return goals

