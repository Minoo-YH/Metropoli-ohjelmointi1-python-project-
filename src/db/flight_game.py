import mariadb

def get_connection():
    return mariadb.connect(
        host="127.0.0.1",
        user="root",          
        password="12345",     
        database="flight_game",
        port=3307
    )


