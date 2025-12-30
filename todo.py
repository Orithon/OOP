#TO-DO APPLICATION

"""
Project Idea: Create a to-do list application where users can add, edit, and delete tasks.
Each task can be represented as an object with attributes like task name, due date, and priority.
Why It’s Great for Beginners: This project helps you grasp the concept of classes and objects.
You can create a Task class and use instances of this class to manage tasks.
"""

class Task:
    def __init__(self, task_name, due_date, priority):
        self.name= task_name
        self.due_date= due_date
        self.priority= priority
        self.tasks = {}

    def __str__(self):
        return f"{self.name} | Due: {self.due_date} | Priority: {self.priority}"

    def update (self, new_name = None, new_date = None, new_priority= None):
        if new_name:
            self.name= new_name
        if new_date:
            self.due_date= new_date
        if new_priority:
            self.priority= new_priority

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("New Task appended successfully")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def edit_task(self, task_number, name = None, due_date = None, priority = None):
            if 1 <= task_number <= len(self.tasks):
                self.tasks[task_number - 1].update(name, due_date, priority)
                print("Task updated successfully.")
            else:
                print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            print(f"Deleted task: {removed.name}")
        else:
            print("Invalid task number.")


def main():
    todo = ToDoList()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter new task name: ")
            due_date = input("Enter new task due date: ")
            priority = input("Enter new task priority: ")
            todo.add_task(Task(name,due_date,priority))

        elif choice == 2:
            todo.view_tasks()

        elif choice == 3:
            task_number = int(input("Enter new task number: "))
            new_name = input("Enter new task name: ")
            new_due_date = input("Enter new task due date: ")
            new_priority = input("Enter new task priority: ")
            todo.edit_task(task_number,new_name,new_due_date,new_priority)

        elif choice == 4:
            task_number = int(input("Enter new task number: "))
            todo.delete_task(task_number)

        elif choice == 5:
            print("Thank you for using this program.")
            break

        else:
            print("Invalid choice.")


main()

