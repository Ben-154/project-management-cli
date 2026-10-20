import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "database.json")


def load_users():
    from models import User

    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [User.from_dict(u) for u in data.get("users", [])]


def save_users(users):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    data = {"users": [u.to_dict() for u in users]}
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)