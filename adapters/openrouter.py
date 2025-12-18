# adapters/openrouter.py

import requests

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def ask_cloud(prompt, api_key, model):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/suryadiarsyil-ops/elena-v1",
        "X-Title": "ELENA AI"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        r = requests.post(
            OPENROUTER_URL,
            headers=headers,
            json=payload,
            timeout=30
        )
    except Exception as e:
        return f"[NETWORK ERROR] {e}"

    try:
        data = r.json()
    except Exception:
        return "[CLOUD ERROR] Response bukan JSON"

    # HARD GUARD: API error / quota / auth / model invalid
    if "choices" not in data:
        return f"[API ERROR] {data}"

    try:
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[PARSE ERROR] {e} | raw={data}"
