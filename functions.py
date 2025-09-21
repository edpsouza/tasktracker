import json

def add_task(filename="tasks.json"):
    task_desc = input("\nEnter the task description: ")
    task = {"task": task_desc, "done": False}
    with open(filename, "r") as f:
        try:
            tasks = json.load(f)
            if not isinstance(tasks, list):
                tasks = []
        except json.JSONDecodeError:
            tasks = []
    tasks.append(task)
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=2)
