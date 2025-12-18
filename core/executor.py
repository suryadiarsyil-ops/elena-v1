# executor.py
def execute(task: str):
    if task == "update termux packages":
        return "Run: pkg update && pkg upgrade"

    if task == "install python":
        return "Run: pkg install python"

    if task == "verify python installation":
        return "Check with: python --version"

    return f"Task '{task}' completed conceptually."
