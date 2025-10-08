from src.db.connection import get_connection

from src.utils.logger import log_info, log_error


def get_all_games():
    conn = get_connection()
    if not conn:
        return []
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM game")
        return cursor.fetchall()
    except Exception as e:
        log_error(f"Error fetching games: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def update_location(game_id, new_location):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    sql = "UPDATE game SET location = %s WHERE id = %s"
    cursor.execute(sql, (new_location, game_id))
    conn.commit()
    cursor.close()
    conn.close()
