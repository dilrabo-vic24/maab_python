import json
import csv
import os
from abc import ABC, abstractmethod

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return self.__dict__

class StorageStrategy(ABC):
    @abstractmethod
    def save(self, tasks):
        pass

    @abstractmethod
    def load(self):
        pass

class JSONStorage(StorageStrategy):
    FILE_NAME = "tasks.json"

    def save(self, tasks):
        with open(self.FILE_NAME, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

    def load(self):
        if not os.path.exists(self.FILE_NAME):
            return []
        with open(self.FILE_NAME, "r") as file:
            return [Task(**data) for data in json.load(file)]

class CSVStorage(StorageStrategy):
    FILE_NAME = "tasks.csv"

    def save(self, tasks):
        with open(self.FILE_NAME, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self):
        if not os.path.exists(self.FILE_NAME):
            return []
        with open(self.FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            return [Task(**row) for row in reader]

class ToDoApp:
    def __init__(self, storage: StorageStrategy):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if due_date:
                    task.due_date = due_date
                if status:
                    task.status = status
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        filtered = [task for task in self.tasks if task.status.lower() == status.lower()]
        for task in filtered:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks saved successfully!")




    def menu(self):
        while True:
            print("\n1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Filter Tasks\n6. Save Tasks\n7. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                task = Task(
                    input("Enter Task ID: "),
                    input("Enter Title: "),
                    input("Enter Description: "),
                    input("Enter Due Date (YYYY-MM-DD): ") or None,
                    input("Enter Status (Pending/In Progress/Completed): ") or "Pending"
                )
                self.add_task(task)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task(input("Enter Task ID: "),
                                 input("Enter new Title: ") or None,
                                 input("Enter new Description: ") or None,
                                 input("Enter new Due Date (YYYY-MM-DD): ") or None,
                                 input("Enter new Status: ") or None)
            elif choice == "4":
                self.delete_task(input("Enter Task ID: "))
            elif choice == "5":
                self.filter_tasks(input("Enter Status: "))
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                self.save_tasks()
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    storage_type = input("Choose storage (json/csv): ").strip().lower()
    storage = JSONStorage() if storage_type == "json" else CSVStorage()
    app = ToDoApp(storage)
    app.menu()