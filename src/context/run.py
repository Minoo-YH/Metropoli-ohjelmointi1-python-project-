from db.flight_game import get_connection

def run_query(query, params=None, fetchone=False):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    if query.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
        conn.commit()
        result = cursor.rowcount   
    else:
        result = cursor.fetchone() if fetchone else cursor.fetchall()
    cursor.close()
    conn.close()
    return result
