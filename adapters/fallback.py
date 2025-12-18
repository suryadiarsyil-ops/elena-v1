# fallback.py
MODELS = [
    "deepseek/deepseek-chat",
    "qwen/qwen-2.5-32b-instruct:free",
    "mistralai/mistral-7b-instruct:free",
]

def next_model(current):
    i = MODELS.index(current)
    return MODELS[(i + 1) % len(MODELS)]
