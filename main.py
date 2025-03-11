import argparse
import json
from datetime import datetime
from tabulate import tabulate

# Load existing tasks from file
def load_tasks():
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  

# Save tasks to file
def save_tasks(data):
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# Add a new task
def add_task(task, data):
    new_task = {
        "id": data[-1]["id"] + 1,  
        "description": task,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }
    data.append(new_task)
    save_tasks(data)
    print(f"Task added successfully (ID: {new_task['id']})")


def list_tasks(data, filter=None):
    if filter:
        data = [task for task in data if task["status"] == filter]
    if data:
        print(tabulate(data, headers="keys", tablefmt="grid"))
    else:
        print("No tasks found.")

def update_task(task_id, new_task, data):
    for task in data:
        if task["id"] == int(task_id):
            task["description"] = new_task
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(data)
            print(f"Task updated successfully (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found.")

def delete_task(task_id,data):
    for task in data:
        if task["id"] == int(task_id):
            data.remove(task)
            save_tasks(data)
            print(f"Task deleted successfully (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found.")

def update_task_status(task_id, new_status, data):
    for task in data:
        if task["id"] == int(task_id):
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(data)
            print(f"Task status changed successfully (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found.")

def main():
    parser = argparse.ArgumentParser(description="A simple Task tracker app")
    parser.add_argument("command", choices=["add","list","update","delete","mark-in-progress","mark-done"], help="Command to run")
    parser.add_argument("arg1", type=str, nargs="?", help="")
    parser.add_argument("arg2", type=str, nargs="?", help="")

    args = parser.parse_args()

    # Load existing data
    data = load_tasks()

    if args.command == "add":
        if not args.arg1:
            print("Error: You must provide a task description.")
            return
        add_task(args.arg1, data)
    if args.command == "list":
        list_tasks(data,args.arg1)
    if args.command == "update":
        if not args.arg1:
            print("Error: You must provide a task ID.")
        if not args.arg2:
            print("Error: You must provide a new task.")
        update_task(args.arg1, args.arg2, data)
    if args.command == "delete":
        if not args.arg1:
            print("Error: You must provide a task ID.")
        delete_task(args.arg1, data)
    if args.command == "mark-in-progress":
        if not args.arg1:
            print("Error: You must provide a task ID.")
        update_task_status(args.arg1, "in-progress", data)
    if args.command == "mark-done":
        if not args.arg1:
            print("Error: You must provide a task ID.")
        update_task_status(args.arg1, "done", data)
        

if __name__ == "__main__":
    main()
