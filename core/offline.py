# offline.py
import re

OFFLINE_RULES = [
    (r"(ls|cd|pwd)", "Itu perintah dasar Linux untuk navigasi direktori."),
    (r"(python error|traceback)", "Cek baris error terakhir, itu sumber masalah."),
    (r"(git clone)", "Gunakan: git clone <url> untuk mengambil repo."),
]

def offline_response(text: str):
    for pattern, answer in OFFLINE_RULES:
        if re.search(pattern, text, re.I):
            return answer
    return None
