class Student:

    def __init__(self, name, age, email, course, semester, marks):
        self.name = name
        self.age = age
        self.email = email
        self.course = course
        self.semester = semester
        self.marks = marks

    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Email:{self.email}")
        print(f"Course:{self.course}")
        print(f"Semester:{self.semester}")
        print(f"Marks:{self.marks}")