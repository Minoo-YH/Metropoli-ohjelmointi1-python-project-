<<<<<<< HEAD
import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="flight_game"
    )










=======
import mariadb

def get_connection():
    return mariadb.connect(
        host="127.0.0.1",
        user="nipa",
        password="12345",
        database="flight_game",
        port = 3307
    )
>>>>>>> bf82030 (Solve error)
