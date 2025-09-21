import mysql.connector,os,sys
from dotenv import load_dotenv


load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )





sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))




