import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

QUERY_FILE = os.path.join(BASE_DIR, "queries.json")

def load_queries():
    try:
        with open(QUERY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading queries: {e}")
        return 


def query(name):
    queries = load_queries()
    q = queries.get(name)
    if not q:
        print(f"Error: Query '{name}' not found in queries.json")
        return None
    return q


