tasks = []

while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for task in tasks:
                print("-", task)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")