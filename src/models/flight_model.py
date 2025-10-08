from src.db.connection import get_connection


from src.utils.logger import log_info, log_error


def get_all_flights():
    conn = get_connection()
    if not conn:
        return []
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM flights ORDER BY depart_at DESC")
        result = cursor.fetchall()
        return result
    except Exception as e:
        log_error(f"Error getting flights: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def add_flight(flight):
    conn = get_connection()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        sql = """
        INSERT INTO flights (flight_no, airline, origin, destination, depart_at, arrive_at, price, status)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(sql, (
            flight["flight_no"],
            flight["airline"],
            flight["origin"],
            flight["destination"],
            flight["depart_at"],
            flight["arrive_at"],
            flight["price"],
            flight.get("status", "SCHEDULED")
        ))
        conn.commit()
        log_info(f"Flight added: {flight['flight_no']}")
        return True
    except Exception as e:
        log_error(f"Error adding flight: {e}")
        return False
    finally:
        cursor.close()
        conn.close()
