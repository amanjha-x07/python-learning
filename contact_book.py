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


def update_contact():
    name = input("Enter name to update: ").strip()

    if name in contacts:
        new_phone = input("Enter new phone number: ").strip()

        if new_phone:
            contacts[name] = new_phone
            print("Contact updated.")
        else:
            print("Phone number cannot be empty.")
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
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")