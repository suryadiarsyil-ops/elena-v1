# core/brain.py

from core.offline import offline_response
from core.memory import recall, store_memory
from adapters.openrouter import ask_cloud

def think(user_input, api_key, model):
    # 1. OFFLINE FIRST
    offline = offline_response(user_input)
    if offline:
        return offline, "offline"

    # 2. MEMORY RECALL
    memories = recall(user_input)
    prompt = ""

    if memories:
        prompt += "Relevant past context:\n"
        for m in memories:
            prompt += f"- {m}\n"
        prompt += "\n"

    prompt += user_input

    # 3. CLOUD THINKING
    response = ask_cloud(prompt, api_key, model)

    # 4. MEMORY STORE (HANYA YANG PENTING)
    store_memory(user_input)
    store_memory(response)

    return response, "cloud+memory"
