import sqlite3
from argon2 import PasswordHasher
import messagebox

# FUNCTIONS FOR THE DATABASE
def create_item_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS items1 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')
    conn.commit()

def create_login_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS login1 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()

# this function is used to create a new user in the login table
def create_login(conn, username, password):
    cursor = conn.cursor()
    # this scrambles the password up using an algorithm called argon2
    hashed_password = PasswordHasher().hash(password)
    cursor.execute("INSERT INTO login1 (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()

# this function checks to see if the user exists in the login info table
# it finds the user by their username, then it checks the hashed password
def check_login(conn, username, password):
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM login1 WHERE username = ?", (username,))
    user = cursor.fetchone()
    if user is None:
        messagebox.showerror("Login Failed", "Incorrect username or password. Please try again or sign up.")
    stored_password = user[0]
    try:
        PasswordHasher().verify(stored_password, password)
        return True  # Login successful
    except:
        messagebox.showerror("Login Failed", "Incorrect username or password. Please try again or sign up.")


def add_item(conn, name):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items1 (name) VALUES (?)", (name,))
    conn.commit()

def remove_item(conn, item_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items1 WHERE id = ?", (item_id,))
    conn.commit()

def update_item(conn, item_id, new_name):
    cursor = conn.cursor()
    cursor.execute("UPDATE items1 SET name = ? WHERE id = ?", (new_name, item_id))
    conn.commit()

def get_item_list(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items1")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}")

