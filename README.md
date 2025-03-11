# Task Tracker CLI

## About
This is a simple Task Tracker Command-Line Interface (CLI) application built using Python. It allows users to manage tasks by adding, listing, updating, deleting, and marking them as in-progress or done. Tasks are stored in a JSON file (`data.json`).

## Features
- Add new tasks
- List all tasks (filtered by status if needed)
- Update task descriptions
- Delete tasks
- Mark tasks as "in-progress" or "done"

## Requirements
Before using the application, ensure you have the required dependencies installed:

```sh
pip install tabulate
```

## How to Use

### 1. Add a Task
```sh
python main.py add "Buy groceries"
```

### 2. List All Tasks
```sh
python main.py list
```

### 3. List Tasks by Status
```sh
python main.py list done
```

### 4. Update a Task
```sh
python main.py update 1 "Buy groceries and cook dinner"
```

### 5. Delete a Task
```sh
python main.py delete 1
```

### 6. Mark a Task as In-Progress
```sh
python main.py mark-in-progress 1
```

### 7. Mark a Task as Done
```sh
python main.py mark-done 1
```

## File Structure
```
.
├── main.py  # Main script
├── data.json        # Stores tasks
├── README.md        # Documentation
```

## Notes
- The application uses `data.json` to persist tasks.
- Ensure `data.json` exists or will be created when running the program.
- Tasks are identified by a unique ID.

## License
This project is open-source and available for personal or educational use.


https://roadmap.sh/projects/task-tracker
