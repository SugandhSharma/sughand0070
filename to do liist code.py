# Function to display the to-do list
def show_tasks(tasks):
    print("To-Do List:")
    if not tasks:
        print("No tasks yet.")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")
    print()

# Function to add a task to the to-do list
def add_task(tasks, new_task):
    tasks.append(new_task)
    print(f"Task '{new_task}' added to the to-do list.\n")

# Function to mark a task as completed
def complete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        completed_task = tasks.pop(task_index)
        print(f"Task '{completed_task}' marked as completed.\n")
    else:
        print("Invalid task index. Please try again.\n")

# Main function
def main():
    tasks = []  # Empty list to store tasks

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            new_task = input("Enter the task: ")
            add_task(tasks, new_task)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            task_index = int(input("Enter the task number to mark as completed (0 to cancel): ")) - 1
            if task_index == -1:
                continue
            complete_task(tasks, task_index)
        elif choice == "4":
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
