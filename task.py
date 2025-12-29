# A simple To-Do List program
tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-3): ")

    if choice == '1':
        print("\nYOUR TASKS:")
        if not tasks:
            print("Your list is empty!")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == '2':
        new_task = input("Enter the task: ")
        tasks.append(new_task)
        print("Task added!")

    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
