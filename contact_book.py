contacts = {}


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()

    if name and phone:
        contacts[name] = phone
        print("Contact added.")
    else:
        print("Name and phone cannot be empty.")


def view_contacts():
    if not contacts:
        print("No contacts yet.")
    else:
        for name, phone in contacts.items():
            print(name, ":", phone)


def search_contact():
    name = input("Enter name to search: ").strip()

    if name in contacts:
        print("Phone:", contacts[name])
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")


while True:
    print("\n1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")