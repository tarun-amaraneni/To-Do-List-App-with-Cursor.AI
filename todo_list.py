import json
import os
import unittest

class TodoList:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()

    def add_task(self, task):
        """Add a new task to the list"""
        self.tasks.append({"task": task, "completed": False})
        print(f"Task added: {task}")
        self.save_tasks()

    def edit_task(self, task_number, new_task):
        """Edit an existing task"""
        try:
            task_index = int(task_number) - 1
            if 0 <= task_index < len(self.tasks):
                old_task = self.tasks[task_index]["task"]
                self.tasks[task_index]["task"] = new_task
                print(f"Task '{old_task}' updated to '{new_task}'")
                self.save_tasks()
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

    def view_tasks(self):
        """Display all tasks in the list"""
        if not self.tasks:
            print("No tasks in the list!")
            return
        
        print("\nCurrent Tasks:")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"{i}. [{status}] {task['task']}")

    def mark_complete(self, task_number):
        """Mark a task as complete"""
        try:
            task_index = int(task_number) - 1
            if 0 <= task_index < len(self.tasks):
                self.tasks[task_index]["completed"] = True
                print(f"Task '{self.tasks[task_index]['task']}' marked as complete!")
                self.save_tasks()
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

    def delete_task(self, task_number):
        """Delete a task from the list"""
        try:
            task_index = int(task_number) - 1
            if 0 <= task_index < len(self.tasks):
                deleted_task = self.tasks.pop(task_index)
                print(f"Task '{deleted_task['task']}' deleted successfully!")
                self.save_tasks()
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

    def save_tasks(self):
        """Save tasks to a JSON file"""
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        """Load tasks from a JSON file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    self.tasks = json.load(f)
            else:
                # Create an empty tasks file if it doesn't exist
                self.tasks = []
                self.save_tasks()
        except json.JSONDecodeError:
            print("Error: Tasks file is corrupted. Starting with empty task list.")
            self.tasks = []
            self.save_tasks()

def main():
    todo_list = TodoList()
    
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Edit Task")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks()
            if todo_list.tasks:
                task_num = input("Enter task number to mark as complete: ")
                todo_list.mark_complete(task_num)
        elif choice == "4":
            todo_list.view_tasks()
            if todo_list.tasks:
                task_num = input("Enter task number to delete: ")
                todo_list.delete_task(task_num)
        elif choice == "5":
            todo_list.view_tasks()
            if todo_list.tasks:
                task_num = input("Enter task number to edit: ")
                new_task = input("Enter new task description: ")
                todo_list.edit_task(task_num, new_task)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# 
# 
# 
# Tests
class TestTodoList(unittest.TestCase):
    def setUp(self):
        """Set up test environment before each test"""
        self.todo = TodoList()
        self.todo.filename = "test_tasks.json"  # Use a test file
        if os.path.exists(self.todo.filename):
            os.remove(self.todo.filename)

    def tearDown(self):
        """Clean up after each test"""
        if os.path.exists(self.todo.filename):
            os.remove(self.todo.filename)

    def test_add_task(self):
        """Test adding a new task"""
        self.todo.add_task("Test task")
        self.assertEqual(len(self.todo.tasks), 1)
        self.assertEqual(self.todo.tasks[0]["task"], "Test task")
        self.assertFalse(self.todo.tasks[0]["completed"])

    def test_edit_task(self):
        """Test editing a task"""
        self.todo.add_task("Original task")
        self.todo.edit_task("1", "Updated task")
        self.assertEqual(self.todo.tasks[0]["task"], "Updated task")
        self.assertFalse(self.todo.tasks[0]["completed"])

    def test_view_empty_tasks(self):
        """Test viewing tasks when list is empty"""
        self.todo.view_tasks()  # Should not raise an exception

    def test_mark_complete(self):
        """Test marking a task as complete"""
        self.todo.add_task("Test task")
        self.todo.mark_complete("1")
        self.assertTrue(self.todo.tasks[0]["completed"])

    def test_delete_task(self):
        """Test deleting a task"""
        self.todo.add_task("Task 1")
        self.todo.add_task("Task 2")
        initial_length = len(self.todo.tasks)
        self.todo.delete_task("1")
        self.assertEqual(len(self.todo.tasks), initial_length - 1)

    def test_invalid_task_number(self):
        """Test handling of invalid task numbers"""
        self.todo.add_task("Test task")
        # Test with non-existent task number
        self.todo.mark_complete("999")
        self.todo.delete_task("999")
        self.todo.edit_task("999", "New task")
        # Test with invalid input
        self.todo.mark_complete("invalid")
        self.todo.delete_task("invalid")
        self.todo.edit_task("invalid", "New task")

if __name__ == "__main__":
    # If running tests
    if os.environ.get('PYTHON_UNITTEST') == '1':
        unittest.main()
    else:
        # Run the normal application
        main() 
