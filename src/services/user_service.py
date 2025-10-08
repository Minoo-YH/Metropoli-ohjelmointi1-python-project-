from src.models.user_model import create_user, verify_user
from src.utils.logger import log_info

def register_user():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    create_user(username, password)

def login_user():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    if verify_user(username, password):
        log_info(f"✅ Welcome back, {username}!")
    else:
        print("❌ Invalid username or password.")

