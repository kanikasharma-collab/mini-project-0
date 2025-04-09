# To-Do List Application in Python

# Function to display the menu options
def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

# Function to view all tasks
def view_tasks(tasks):
    if tasks:
        print("\n--- Your Tasks ---")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("\nNo tasks in the to-do list.")

# Function to add a new task
def add_task(tasks):
    task = input("\nEnter the task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added.")

# Function to delete a task
def delete_task(tasks):
    if tasks:
        view_tasks(tasks)
        try:
            task_index = int(input("\nEnter the number of the task to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"Task '{removed_task}' has been removed.")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("\nNo tasks to delete.")

# Main function to run the to-do list program
def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nChoose an option (1/2/3/4): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

# Run the application
if __name__ == "__main__":
    main()