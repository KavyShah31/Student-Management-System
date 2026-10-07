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