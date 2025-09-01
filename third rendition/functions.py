from argon2 import PasswordHasher
import messagebox
from tkinter import * 
from tkinter import ttk 

# FUNCTIONS FOR THE DATABASE
def create_item_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS items1 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL
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
# it finds the user by their username, then it takes the corresponding hashed password and compares it to the password they entered
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

# item functions
def add_item(conn, name, description):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items1 (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    return True

def remove_item(conn, item_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items1 WHERE id = ?", (item_id,))
    conn.commit()
    return True

def update_item(conn, item_id, new_name):
    cursor = conn.cursor()
    cursor.execute("UPDATE items1 SET name = ? WHERE id = ?", (new_name, item_id))
    conn.commit()
    return True

def get_item_list(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items1")
    rows = cursor.fetchall()
    return rows

def get_item_id_by_name(conn, name):
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM items1 WHERE name = ?", (name,))
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        None
    

