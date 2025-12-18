# memory.py
import json, time
from pathlib import Path

MEMORY_FILE = Path("data/memory.json")
MEMORY_FILE.parent.mkdir(exist_ok=True)

def load_memory():
    if MEMORY_FILE.exists():
        return json.loads(MEMORY_FILE.read_text())
    return []

def save_memory(mem):
    MEMORY_FILE.write_text(json.dumps(mem[-200:], indent=2))

def extract_keywords(text):
    blacklist = {"dan", "yang", "untuk", "dengan", "ini", "itu"}
    words = text.lower().split()
    return list({w for w in words if len(w) > 3 and w not in blacklist})

def store_memory(text):
    mem = load_memory()
    mem.append({
        "text": text,
        "keywords": extract_keywords(text),
        "timestamp": time.time()
    })
    save_memory(mem)

def recall(query):
    qkeys = set(extract_keywords(query))
    mem = load_memory()
    scored = []

    for m in mem:
        overlap = qkeys & set(m["keywords"])
        score = len(overlap)
        if score > 0:
            scored.append((score, m["text"]))

    scored.sort(reverse=True)
    return [t for _, t in scored[:3]]
