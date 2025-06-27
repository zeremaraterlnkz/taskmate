import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def list_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {status} {task['title']}")

def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Task added: {title}")

def mark_done(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Task marked as done: {tasks[index]['title']}")
    else:
        print("Invalid task number")

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted task: {removed['title']}")
    else:
        print("Invalid task number")

def main():
    tasks = load_tasks()
    while True:
        command = input("\nCommands: list, add, done, delete, exit\n> ")
        if command == "list":
            list_tasks(tasks)
        elif command == "add":
            title = input("Task title: ")
            add_task(tasks, title)
        elif command == "done":
            index = int(input("Task number: ")) - 1
            mark_done(tasks, index)
        elif command == "delete":
            index = int(input("Task number: ")) - 1
            delete_task(tasks, index)
        elif command == "exit":
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()