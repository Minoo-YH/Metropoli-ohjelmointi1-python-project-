from src.db.flight_game import get_connection

try:
    conn = get_connection()
    print("✅ Connected to database successfully!")
    conn.close()
except Exception as e:
    print("❌ Database connection failed:", e)
