import sqlite3

DATABASE_NAME = "students.db"

def create_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection

def create_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL UNIQUE,
            course TEXT NOT NULL,
            semester INTEGER NOT NULL,
            marks REAL NOT NULL
            )
            """)

    connection.commit()
    connection.close()