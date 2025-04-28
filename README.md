# To-Do List Application

A simple command-line To-Do List application written in Python that helps you manage your daily tasks efficiently.

## Features
- Add new tasks to the list
- View all tasks with their completion status
- Mark tasks as complete
- Delete tasks from the list
- Task persistence (saves tasks between sessions)
- Simple command-line interface
- Error handling for invalid inputs
- Built-in unit tests

## Requirements
- Python 3.x
- No additional dependencies required

## Installation
1. clone the project from your repository/folder and navigate by using
   ```bash
   cd todo_list.py
   ```

## Usage
Run the application using:
```bash
python3 todo_list.py
```

The application will present you with a menu of options:
1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Delete Task
5. Exit

### Example Usage
1. Adding a task:
   ```
   Enter your choice (1-5): 1
   Enter the task: Buy groceries
   Task added: Buy groceries
   ```

2. Viewing tasks:
   ```
   Enter your choice (1-5): 2
   Current Tasks:
   1. [ ] Buy groceries
   ```

3. Marking a task as complete:
   ```
   Enter your choice (1-5): 3
   Current Tasks:
   1. [ ] Buy groceries
   Enter task number to mark as complete: 1
   Task 'Buy groceries' marked as complete!
   ```

4. Deleting a task:
   ```
   Enter your choice (1-5): 4
   Current Tasks:
   1. [✓] Buy groceries
   Enter task number to delete: 1
   Task 'Buy groceries' deleted successfully!
   ```
## Running Unit Tests
The application includes built-in unit tests

Test Case 1: Adding Tasks
```
This test verifies:
Task is successfully added
Task count is correct
Task content is correct
Task is initially not completed
 ```
Test Case 2: Viewing Empty List
```
This test ensures:
Application doesn't crash when viewing empty list
Empty list is handled gracefully
```
Test Case 3: Marking Tasks Complete
```
This test checks:
Task can be marked as complete
Task status changes correctly
Task remains in the list
```
Test Case 4: Deleting Tasks
```
This test verifies:
Task is successfully deleted
List length decreases correctly
Remaining tasks are preserved
```
Test Case 5: Invalid Input Handling
```
This test ensures:
Application handles non-existent task numbers
Application handles invalid input (non-numeric)
No crashes occur with invalid inputs
```
## To run these tests, you use:
```
export PYTHON_UNITTEST=1
python3 todo_list.py
```
## Deployment
The application is designed to run in any terminal environment:

1. Open your terminal
2. Navigate to the project directory
3. Run the application using `python3 todo_list.py`
4. Your tasks will be automatically saved to `tasks.json` in the same directory

