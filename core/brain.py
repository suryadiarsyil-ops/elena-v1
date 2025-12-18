# core/brain.py

from core.offline import offline_response
from core.memory import recall, store_memory
from core.planner import plan
from core.executor import execute
from core.tools import get_pwd, list_files, read_file
from adapters.openrouter import ask_cloud


def think(user_input, api_key, model, autonomous=False):
    # 1. OFFLINE REFLEX
    offline = offline_response(user_input)
    if offline:
        return offline, "offline"

    # 2. TOOL AWARENESS
    if user_input == "/pwd":
        return get_pwd(), "tool"

    if user_input == "/ls":
        return "\n".join(list_files()), "tool"

    if user_input.startswith("/read "):
        path = user_input.split(" ", 1)[1]
        return read_file(path), "tool"

    # 3. AUTONOMOUS MODE
    if autonomous:
        tasks = plan(user_input)
        output = "Autonomous plan:\n"

        for i, t in enumerate(tasks, 1):
            try:
                result = execute(t)
            except Exception as e:
                result = f"[EXEC ERROR] {e}"

            output += f"\nStep {i}: {t}\n→ {result}\n"

        store_memory(output)
        return output, "autonomous"

    # 4. NORMAL MODE (CLOUD)
    context = recall(user_input)
    prompt = ""

    if context:
        prompt += "Relevant context:\n"
        for c in context:
            prompt += f"- {c}\n"
        prompt += "\n"

    prompt += (
        f"Environment:\n"
        f"PWD: {get_pwd()}\n"
        f"Files: {list_files()}\n\n"
    )

    prompt += user_input

    print(f"[DEBUG] mode=cloud | prompt_len={len(prompt)}")

    try:
        response = ask_cloud(prompt, api_key, model)
    except Exception as e:
        return f"[CLOUD ERROR] {e}", "cloud-error"

    if not isinstance(response, str):
        response = str(response)

    if len(response) > 50:
        store_memory(user_input)
        store_memory(response)

    return response, "cloud+memory"
