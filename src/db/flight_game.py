import mysql.connector
from dotenv import load_dotenv
import os
import sys

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )





sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from db.flight_game import get_connection



if __name__ == "__main__":
    conn = get_connection()
    print("   done")
    conn.close()
