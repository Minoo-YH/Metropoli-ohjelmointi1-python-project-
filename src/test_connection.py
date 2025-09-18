import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from db.flight_game import get_connection



if __name__ == "__main__":
    conn = get_connection()
    print("   done")
    conn.close()
