from database import create_table
from Student_manager import(
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    student_statistics
)
from student import Student

def main():
    create_table()

    while True:
        print("\n====== Student Manager ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Student Statistics")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            try:
                name = input("\nEnter Name: ").strip()
                age = int(input("Enter Age: "))
                email = input("Enter email: ").strip()
                course = input("Enter course: ").strip()
                semester = int(input("Enter Semester: "))
                marks = float(input("Enter Marks (0-100): "))

                if not name or not email or not course:
                    print("Name, email and course cannot be empty.")
                    continue

                if age <= 0 or semester <= 0 or not 0 <= marks <= 100:
                    print("Inalid age, semester or marks.")
                    continue

                student = Student(
                    name, age, email, course, semester, marks
                )
                add_student(student)

            except ValueError:
                print("Invalid input! Please enter number where required.")

            except Exception as error:
                print(f"Could not add student: {error}")

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            student_statistics()

        elif choice == "7":
            print("Thank you for student Management Syste!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()