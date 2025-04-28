class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list"""
        self.tasks.append({"task": task, "completed": False})
        print(f"Task added: {task}")

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
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    todo_list = TodoList()
    
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 