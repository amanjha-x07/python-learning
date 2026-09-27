expenses = []

while True:
    print("\n1. Add expense")
    print("2. Show expenses")
    print("3. Calculate total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))

        expenses.append({
            "name": name,
            "amount": amount
        })

        print("Expense added.")

    elif choice == "2":
        if not expenses:
            print("No expenses yet.")
        else:
            for expense in expenses:
                print(expense["name"], "-", expense["amount"])

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print("Total expense =", total)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")