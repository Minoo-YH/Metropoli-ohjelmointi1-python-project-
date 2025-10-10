import mysql.connector,os
from dotenv import load_dotenv


load_dotenv()

def get_connection():
    return mysql.connector.connect(

        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )




# MariaDB connection (uncomment if using MariaDB instead of MySQL)

"""
import mariadb

def get_connection():
    return mariadb.connect(
        host="127.0.0.1",
        user="root",          
        password="12345",     
        database="flight_game",
        port=3307
    )

"""

