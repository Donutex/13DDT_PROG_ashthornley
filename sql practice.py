import sqlite3
#print(sqlite3.sqlite_version)

# Connect to or create the database
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students1 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
''')
conn.commit()

# Functions
def add_student(name, age):
    cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print("✅ Student added.")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n📋 Student List:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
    print()

def update_age(student_id, new_age):
    cursor.execute("UPDATE students SET age = ? WHERE id = ?", (new_age, student_id))
    conn.commit()
    print("🔁 Age updated.")

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print("🗑️ Student deleted.")

# CLI Menu
while True:
    print("\nStudent Manager")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student Age")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        add_student(name, age)

    elif choice == '2':
        view_students()

    elif choice == '3':
        student_id = int(input("Enter student ID to update: "))
        new_age = int(input("Enter new age: "))
        update_age(student_id, new_age)

    elif choice == '4':
        student_id = int(input("Enter student ID to delete: "))
        delete_student(student_id)

    elif choice == '5':
        print("👋 Goodbye!")
        break

    else:
        print("❗Invalid option. Please try again.")

# Close connection
conn.close()