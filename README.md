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
1. Clone this repository:
   ```bash
   git clone https://github.com/tarun-amaraneni/To-Do-List-App-with-Cursor.AI.git
   ```
2. Navigate to the project directory:
   ```bash
   cd To-Do-List-App-with-Cursor.AI
   ```

## Usage
Run the application using:
```bash
python todo_list.py
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
The application includes built-in unit tests. To run the tests:

1. Set the environment variable for testing:
   ```bash
   export PYTHON_UNITTEST=1
   ```

2. Run the application:
   ```bash
   python todo_list.py
   ```

The tests will automatically execute and show the results.

## Deployment
The application is designed to run in any terminal environment:

1. Open your terminal
2. Navigate to the project directory
3. Run the application using `python todo_list.py`
4. Your tasks will be automatically saved to `tasks.json` in the same directory

## Contributing
Feel free to submit issues and enhancement requests! 

## License
This project is open source and available under the MIT License. 