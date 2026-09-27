expenses = []

while True:
    print("\n1. Add expense")
    print("2. Show expenses")
    print("3. Calculate total")
    print("4. Delete expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")

        try:
            amount = float(input("Enter expense amount: "))

            if amount < 0:
                print("Amount cannot be negative.")
                continue

            expenses.append({
                "name": name,
                "amount": amount
            })

            print("Expense added.")

        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "2":
        if not expenses:
            print("No expenses yet.")
        else:
            for i, expense in enumerate(expenses, start=1):
                print(i, "-", expense["name"], ":", expense["amount"])

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print("Total expense =", total)

    elif choice == "4":
        if not expenses:
            print("No expenses to delete.")
        else:
            for i, expense in enumerate(expenses, start=1):
                print(i, "-", expense["name"], ":", expense["amount"])

            try:
                number = int(input("Enter expense number to delete: "))

                if 1 <= number <= len(expenses):
                    expenses.pop(number - 1)
                    print("Expense deleted.")
                else:
                    print("Invalid expense number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")