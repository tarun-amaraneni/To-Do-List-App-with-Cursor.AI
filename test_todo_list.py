import unittest
import os
import json
from todo_list import TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        """Set up test environment before each test"""
        self.todo = TodoList()
        self.todo.filename = "test_tasks.json"  # Use a test file
        # Clear any existing test file
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

    def test_view_empty_tasks(self):
        """Test viewing tasks when list is empty"""
        # This should not raise an exception
        self.todo.view_tasks()

    def test_view_tasks(self):
        """Test viewing tasks with content"""
        self.todo.add_task("Task 1")
        self.todo.add_task("Task 2")
        # This should not raise an exception
        self.todo.view_tasks()

if __name__ == '__main__':
    unittest.main() 