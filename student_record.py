students = []


def add_student():
    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()

    if name and course:
        students.append({
            "name": name,
            "course": course
        })
        print("Student added.")
    else:
        print("Name and course cannot be empty.")


def view_students():
    if not students:
        print("No students yet.")
    else:
        for i, student in enumerate(students, start=1):
            print(i, "-", student["name"], ":", student["course"])


def search_student():
    name = input("Enter student name to search: ").strip()

    for student in students:
        if student["name"].lower() == name.lower():
            print("Name:", student["name"])
            print("Course:", student["course"])
            return

    print("Student not found.")


def delete_student():
    name = input("Enter student name to delete: ").strip()

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print("Student deleted.")
            return

    print("Student not found.")


while True:
    print("\n1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")