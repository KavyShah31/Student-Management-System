# Student Management System

A simple, menu-driven Student Management System built using **Python** and **SQLite**. This project helps manage student records through a command-line interface.

## Features

* **Add Student:** Save student details in the database.
* **View Students:** Display all registered students.
* **Search Student:** Search by student name or email.
* **Update Student:** Edit existing student details.
* **Delete Student:** Delete a student record after confirmation.
* **Student Statistics:** Display total students, average marks, highest marks, and lowest marks.
* **Data Validation:** Validate numeric inputs and marks.
* **SQLite Database:** Store student records persistently.

## Technologies Used

* Python 3
* SQLite
* SQL
* Visual Studio Code

## Project Structure

```text
Student-Management-System/
│
├── main.py
├── Student_manager.py
├── student.py
├── database.py
├── README.md
├── .gitignore
└── screenshots/
    ├── menu.png
    ├── student-list.png
    └── statistics.png
```

The `students.db` file is created locally when the application initializes the database. It is not included in this example structure because local student data should not be published to GitHub.

## Requirements

* Python 3.10 or a compatible Python 3 version
* No external Python packages are required for the basic application. SQLite support is included with Python.

## How to Run

1. Install Python and verify it in your terminal:

   ```bash
   python --version
   ```

2. Open the project folder in VS Code.

3. Open the terminal in the project directory.

4. Run the application:

   ```bash
   python main.py
   ```

5. Select an option from the menu and follow the prompts.

## Application Menu

The application provides these options:

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Student Statistics
7. Exit

## Screenshots

Screenshots of the application will be added here.

### Main Menu

### Student List

### Student Statistics

## Database

The application uses SQLite to store student information, including name, age, email, course, semester, and marks.

**Privacy note:** Do not upload real or sensitive student records to a public repository.

## Future Improvements

* Add a graphical user interface (GUI).
* Export student records to CSV or Excel.
* Add login and authentication.
* Generate student reports.

## Author

**Kavya Shah**

## License

This project is available for learning and educational purposes.
