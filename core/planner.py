# planner.py
def plan(goal: str):
    tasks = []

    g = goal.lower()

    if "termux" in g and "python" in g:
        tasks = [
            "update termux packages",
            "install python",
            "verify python installation"
        ]
    else:
        tasks = ["analyze request", "answer directly"]

    return tasks
