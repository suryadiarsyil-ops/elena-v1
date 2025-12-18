# core/brain.py

from core.offline import offline_response
from core.memory import recall, store_memory
from core.planner import plan
from core.executor import execute
from core.tools import get_pwd, list_files, read_file
from adapters.openrouter import ask_cloud

def think(user_input, api_key, model, autonomous=False):
    # OFFLINE REFLEX
    offline = offline_response(user_input)
    if offline:
        return offline, "offline"

    # TOOL AWARENESS
    if user_input == "/pwd":
        return get_pwd(), "tool"

    if user_input == "/ls":
        return "\n".join(list_files()), "tool"

    if user_input.startswith("/read "):
        path = user_input.split(" ", 1)[1]
        return read_file(path), "tool"

    # AUTONOMOUS MODE
try:
    result = execute(t)
except Exception as e:
    result = f"[EXEC ERROR] {e}"

output += f"\nStep {i}: {t}\n→ {result}\n"
        store_memory(output)
        return output, "autonomous"

    # NORMAL MODE
    context = recall(user_input)
    prompt = ""

    if context:
        prompt += "Relevant context:\n"
        for c in context:
            prompt += f"- {c}\n"
        prompt += "\n"

    prompt += f"Environment:\nPWD: {get_pwd()}\nFiles: {list_files()}\n\n"
    prompt += user_input

    # core/brain.py
    print(f"[DEBUG] mode=cloud | prompt_len={len(prompt)}")
    
    response = ask_cloud(prompt, api_key, model)

    if isinstance(response, str) and len(response) > 50:
    store_memory(user_input)
    store_memory(response)

    return response, "cloud+memory"
