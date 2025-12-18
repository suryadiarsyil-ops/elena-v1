# brian.py
from core.offline import offline_response
from adapters.openrouter import ask_cloud

def think(user_input):
    offline = offline_response(user_input)
    if offline:
        return offline, "offline"
    return ask_cloud(user_input), "cloud"
