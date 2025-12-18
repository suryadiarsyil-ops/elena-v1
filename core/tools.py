# tools.py
import os

def get_pwd():
    return os.getcwd()

def list_files(limit=20):
    items = os.listdir(".")
    return items[:limit]

def read_file(path, max_chars=1500):
    if not os.path.isfile(path):
        return "File not found."
    try:
        with open(path, "r", errors="ignore") as f:
            return f.read(max_chars)
    except Exception as e:
        return f"Error reading file: {e}"
