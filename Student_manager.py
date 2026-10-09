from django.db.backends import sqlite3

from database import create_connection

def add_student(student):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students
        (name, age, email, course, semester, marks)
        VALUES (?,?,?,?,?,?)""",
        (
            student.name,
            student.age,
            student.email,
            student.course,
            student.semester,
            student.marks
        ))

    connection.commit()
    connection.close()

    print("\nstudent added successfully!")


def view_students():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    connection.close()

    if not students:
        print("\nNo students found.")
        return

    print("\n====== Students List ======")

    for student in students:

        print(
            f"ID: {student[0]} | "
            f"Name: {student[1]} | "
            f"Age: {student[2]} | "
            f"Email: {student[3]} | "
            f"Course: {student[4]} | "
            f"Semester: {student[5]} | "
            f"Marks: {student[6]}"
        )

def search_student():

    keyword = input("\nEnter student name or email:").strip()

    if not keyword:
        print("\nPlease enter a name or email.")
        return

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM students
        WHERE name LIKE ? OR email LIKE ?
        """, (f"%{keyword}%", f"%{keyword}%"))

    students = cursor.fetchall()

    connection.close()

    if not students:
        print("\nNo students found.")
        return

    print("\n====== Search Results ======")

    for student in students:
        print(
            f"ID: {student[0]} | "
            f"Name: {student[1]} | "
            f"Age: {student[2]} | "
            f"Email: {student[3]} | "
            f"Course: {student[4]} | "
            f"Semester: {student[5]} | "
            f"Marks: {student[6]}"
        )

def update_student():
    try:
        student_id = int (input("\nEnter Student ID to update: "))
    except ValueError:
        print("\nPlease enter a valid numeric ID.")
        return

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )
    student = cursor.fetchone()

    if student is None:
        print("\nStudent not found!")
        connection.close()
        return

    print("\nEnter new details:")
    print(f"Name: {student[1]}")
    print(f"Age: {student[2]}")
    print(f"Email: {student[3]}")
    print(f"Course: {student[4]}")
    print(f"Semester: {student[5]}")
    print(f"Marks: {student[6]}")

    print("\nEnter new details (press Enter to keep the current value).")

    name = input(f"Name: [{student[1]}]:").strip() or student[1]
    age_input = input(f"Age: [{student[2]}]:").strip()
    email = input(f"Email: [{student[3]}]:").strip() or student[3]
    course = input(f"Course: [{student[4]}]:").strip() or student[4]
    semester_input = input(f"Semester [{student[5]}]: ").strip()
    marks_input = input(f"Marks [{student[6]}]: ").strip()

    try:
        age = int(age_input) if age_input else student[2]
        semester = int(semester_input) if semester_input else student[5]
        marks = float(marks_input) if marks_input else student[6]

        if age <= 0 or semester <= 0 or not 0 <= marks <= 100:
            print("\nAge and semester must be positive; marks must be between 0 and 100.")
            connection.close()
            return

        cursor.execute("""
            UPDATE students
            SET name = ?, age = ?, course = ?, semester = ?, marks = ?
            WHERE id = ?
        """, (name, age, email, course, semester, marks, student_id))

        
        connection.commit()
        print("\nStudent updated successfully!")

    except ValueError:
        print("\nInvalid input! Check age, semester, and marks.")
    except sqlite3.IntegrityError:
        print("\nThis email is already used by another student.")
    finally:
        connection.close()