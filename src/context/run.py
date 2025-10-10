from db.flight_game import get_connection

def run_query(query, params=None, fetchone=False):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(query, params or ())
        first = (query or "").lstrip().split(" ", 1)[0].upper()
<<<<<<< HEAD
=======

>>>>>>> nipa_1
        if first in ("INSERT", "UPDATE", "DELETE"):
            try:
                conn.commit()
            except Exception:
                pass
            return cursor.rowcount
<<<<<<< HEAD
        return cursor.fetchone() if fetchone else cursor.fetchall()
=======

        if first == "SELECT":
            return cursor.fetchone() if fetchone else cursor.fetchall()

        return None
>>>>>>> nipa_1
    finally:
        try:
            cursor.close()
        except Exception:
            pass
<<<<<<< HEAD
        conn.close()
=======
        try:
            conn.close()
        except Exception:
            pass
>>>>>>> nipa_1
