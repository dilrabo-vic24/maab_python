import json
import csv
import os

def create_tasks_json():
    tasks = [
        {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
        {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
        {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
    ]
    
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)
    print("tasks.json created successfully.")

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        print("Error: tasks.json file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in tasks.json.")
        return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    try:
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file, indent=4)
        print("Tasks saved successfully to tasks.json.")
        return True
    except Exception as e:
        print(f"Error saving tasks: {e}")
        return False

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    
    print("\n=== TASK LIST ===")
    print("ID  | Task                | Completed | Priority")
    print("----+---------------------+-----------+---------")
    for task in tasks:
        task_name = task["task"]
        if len(task_name) > 19:
            task_name = task_name[:16] + "..."
        
        completed = "Yes" if task["completed"] else "No"
        
        print(f"{task['id']:<3} | {task_name:<19} | {completed:<9} | {task['priority']}")
    print()

def calculate_stats(tasks):
    if not tasks:
        print("No tasks found. Cannot calculate statistics.")
        return
    
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    
    total_priority = sum(task["priority"] for task in tasks)
    average_priority = total_priority / total_tasks if total_tasks > 0 else 0
    
    print("\n=== TASK STATISTICS ===")
    print(f"Total tasks:      {total_tasks}")
    print(f"Completed tasks:  {completed_tasks}")
    print(f"Pending tasks:    {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")
    print()
    
    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "average_priority": average_priority
    }

def convert_to_csv(tasks, filename="tasks.csv"):
    if not tasks:
        print("No tasks to convert to CSV.")
        return False
    
    try:
        with open(filename, 'w', newline='') as csvfile:
            # Define CSV column headers
            fieldnames = ['ID', 'Task', 'Completed', 'Priority']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header row
            writer.writeheader()
            
            # Write task data
            for task in tasks:
                writer.writerow({
                    'ID': task['id'],
                    'Task': task['task'],
                    'Completed': task['completed'],
                    'Priority': task['priority']
                })
        
        print(f"Tasks successfully converted to {filename}")
        return True
    except Exception as e:
        print(f"Error converting tasks to CSV: {e}")
        return False

def modify_task_demo(tasks):
    if not tasks:
        print("No tasks to modify.")
        return tasks
    
    for task in tasks:
        if not task["completed"]:
            print(f"\nModifying task with ID {task['id']}: '{task['task']}'")
            print(f"Changing completion status from {task['completed']} to True")
            
            task["completed"] = True
            
            print(f"Task {task['id']} has been marked as completed.")
            break
    
    return tasks

def main():
    if not os.path.exists('tasks.json'):
        create_tasks_json()
    
    tasks = load_tasks()
    
    display_tasks(tasks)
    
    stats = calculate_stats(tasks)
    
    convert_to_csv(tasks)
    
    print("\n--- Demonstrating Task Modification ---")
    tasks = modify_task_demo(tasks)
    
    save_tasks(tasks)
    
    print("\n--- After Modification ---")
    display_tasks(tasks)
    calculate_stats(tasks)
    
    convert_to_csv(tasks)
    
    print("\nContents of tasks.csv:")
    try:
        with open('tasks.csv', 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()