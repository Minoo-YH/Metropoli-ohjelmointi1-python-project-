import json
from context import config


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def get_users():
    return load_json(config.USERS_FILE)["users"] 

def update_user(users):
    data = {"users": users} 
    save_json(config.USERS_FILE, data)
    return users