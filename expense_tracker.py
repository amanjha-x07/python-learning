expenses = []

while True:
    print("\n1. Add expense")
    print("2. Show expenses")
    print("3. Calculate total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        expense = float(input("Enter expense amount: "))
        expenses.append(expense)
        print("Expense added.")

    elif choice == "2":
        print("Expenses:", expenses)

    elif choice == "3":
        total = sum(expenses)
        print("Total expense =", total)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")