# elena.py

import os
from core.brain import think

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "openai/gpt-3.5-turbo"

if not API_KEY:
    raise RuntimeError("OPENROUTER_API_KEY belum diset")

print("ELENA AI READY. Commands: /auto /pwd /ls /read <file>")

autonomous = False

while True:
    user = input(">> ").strip()

    if user == "/auto":
        autonomous = not autonomous
        print(f"[MODE] autonomous = {autonomous}")
        continue

    if user in ("/exit", "/quit"):
        break

    out, mode = think(user, API_KEY, MODEL, autonomous)
    print(out)
