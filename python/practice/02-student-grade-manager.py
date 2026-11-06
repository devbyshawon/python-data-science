subjects = ('Math', 'Physics', 'Chemistry', 'Biology', 'English')
pass_mark = 50

students = []


def read_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter {subject} mark (0-100): "))
        except ValueError:
            print("Please enter a number.")
            continue

        mark = round(mark, 2)
        if 0 <= mark <= 100:
            return mark
        print("Mark must be between 0 and 100.")


def find_student(student_id):
    student_id = student_id.strip().upper()
    for student in students:
        if student['id'] == student_id:
            return student
    return None


def calculate_total(student):
    total = 0
    for mark in student['marks']:
        total += mark
    return round(total, 2)


def calculate_average(student):
    total = calculate_total(student)
    average = total / len(subjects)
    return average


def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def get_failed_subjects(student):
    failed = []
    for i in range(len(subjects)):
        if student['marks'][i] < pass_mark:
            failed.append(subjects[i])
    return failed


# Features
def add_student():
    student_id = input("Enter Student ID: ").strip().upper()
    if not student_id:
        print("Student ID cannot be empty")
        return

    if find_student(student_id) is not None:
        print(f"A student with ID {student_id} already exists.")
        return

    student_name = input("Enter Student Name: ").strip()
    if not student_name:
        print("Name cannot be empty.")
        return

    marks = []
    for sub in subjects:
        marks.append(read_mark(sub))

    student = {
        "id": student_id,
        "name": student_name,
        "marks": marks
    }
    students.append(student)

    print(f"Student {student_name} ({student_id}) added successfully.")


def print_student(student):
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    for i in range(len(subjects)):
        print(f"  {subjects[i]}: {student['marks'][i]:g}")


def display_all_students():
    if not students:
        print("No students have been registered yet.")
        return

    print("\nAll Students:")
    for student in students:
        print_student(student)
        show_result(student)
        print()


def search_student():
    student_id = input("Enter Student ID to search: ")
    student = find_student(student_id)

    if student is None:
        print(f"No student found with ID {student_id.strip().upper()}.")
    else:
        print("\nStudent Found")
        print_student(student)
        show_result(student)


def show_result(student):
    total = calculate_total(student)
    average = calculate_average(student)
    grade = get_grade(average)

    print(f"Total: {total:g}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")


def show_top_student():
    if not students:
        print("No students registered yet.")
        return

    highest = calculate_average(students[0])
    for student in students:
        if calculate_average(student) > highest:
            highest = calculate_average(student)

    print("\nTop Performing Student(s):")
    for student in students:
        if calculate_average(student) == highest:
            print_student(student)
            show_result(student)
            print()


def show_failed_students():
    if not students:
        print("No students registered yet.")
        return

    found = False
    print("\nStudents Who Failed a Subject:")
    for student in students:
        failed = get_failed_subjects(student)
        if failed:
            found = True
            print(f"{student['name']} ({student['id']}): {', '.join(failed)}")

    if not found:
        print("No student failed any subject.")


# Menu
def show_menu():
    print("\nStudent Grade Manager")
    print("1. Register a new student")
    print("2. Display all students")
    print("3. Search for a student")
    print("4. Calculate a student's result")
    print("5. Show the highest-performing student")
    print("6. Show students who failed a subject")
    print("7. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            student_id = input("Enter A Student ID: ")
            student = find_student(student_id)
            if student is None:
                print("Student Not Found")
            else:
                print_student(student)
                show_result(student)
        elif choice == "5":
            show_top_student()
        elif choice == "6":
            show_failed_students()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, enter a number from 1 to 7")


main()
