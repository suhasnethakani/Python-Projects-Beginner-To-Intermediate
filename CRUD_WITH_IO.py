import os

TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        try:
            with open(TASK_FILE, "r") as file:
                tasks = [line.strip() for line in file.readlines()]
        except IOError as e:
            print("Error reading tasks:", e)
    return tasks

def save_tasks(tasks):
    try:
        with open(TASK_FILE, "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except IOError as e:
        print("Error saving tasks:", e)

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nCurrent Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def update_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Enter new task description: ")
            tasks[index] = new_task
            save_tasks(tasks)
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- Task Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting... Tasks saved.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
