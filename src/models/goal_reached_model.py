from src.db.connection import get_connection

def get_goal_reached_by_game(game_id):
    conn = get_connection()
    if not conn:
        return []
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT goal_id FROM goal_reached WHERE game_id = %s", (game_id,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
