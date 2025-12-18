# executor.py
def execute(task: str):
    if task == "update termux packages":
        return "Run: pkg update && pkg upgrade"

    if task == "install python":
        return "Run: pkg install python"

    if task == "verify python installation":
        return "Check: python --version"

    if task == "identify error source":
        return "Look at the LAST line of traceback."

    if task == "suggest fix":
        return "Fix depends on error message and module."

    return f"Task '{task}' analyzed."
