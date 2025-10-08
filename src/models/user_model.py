import bcrypt
from src.db.connection import get_connection
from src.utils.logger import log_error, log_info

def create_user(username, password):
    conn = get_connection()
    if not conn:
        return
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    cursor = conn.cursor()
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    try:
        cursor.execute(sql, (username, hashed_pw))
        conn.commit()
        log_info(f"✅ User created: {username}")
    except Exception as e:
        log_error(f"Error creating user: {e}")
    finally:
        cursor.close()
        conn.close()

def verify_user(username, password):
    conn = get_connection()
    if not conn:
        return False
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user and bcrypt.checkpw(password.encode(), user["password"].encode()):
        return True
    return False

