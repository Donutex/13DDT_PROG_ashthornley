from argon2 import PasswordHasher
import messagebox
from tkinter import * 
from tkinter import ttk 
from openai import OpenAI
from geopy.geocoders import Nominatim

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

def create_declutter_log_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS decluttering_log1 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        item_id INTEGER NOT NULL,
        item_name TEXT NOT NULL,
        date_decluttered TEXT NOT NULL
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

# item sql functions
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

def declutter_item(conn, item_id):
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
    
# milestone bar functions
def log_declutter(conn, username, item_name, item_id):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO decluttering_log1 (username, item_name, item_id) VALUES (?, ?, ?)", (username, item_name, item_id))
    conn.commit()

def get_declutter_count(conn, username):
    cursor =  conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM decluttering_log1 WHERE username = ?", (username,))
    count = cursor.fetchone()[0]
    return count

# ai functions for next steps
def ai_predicted_next_steps(conn):
    item_list = []
    item_list = get_item_list(conn)

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
    )

    system_message = (
        "You are a helpful and knowledgeable decluttering assistant for my app: Like A Knife Through Clutter."
        "You will receive a list of items that a user owns and wants to declutter"
        "You will provide an appropriate next step for the user, you will decide what the user will do with their item"
        "When you provide the next step, you choose from either: 'donate', 'sell', 'recycle', 'trash', 'keep' "
        "You will not provide any other options, only these five"
        "You will not add any extra information, only the one word next step"
        "You will not add any punctuation, only the one word next step"
    )

    user_message = (
        f"Here is a list of items that the user owns and wants to declutter: {item_list}"
        "What is the next step for the user to take with their items? Choose from either: 'donate', 'sell', 'recycle', 'trash', 'keep' "
    )

    response = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[
            {
            "role":"system","content":system_message},
            {"role":"user","content":user_message}
        ]
    )
    result = response.choices[0].message.content
    print(result)

# map functions for donation locations etc
def search_nearby_places(query, latitude, longitude, limit=5):
    #initialize geolocator with a user agent, nothing would work without this
    geolocator = Nominatim(user_agent="like_a_knife_through_clutter_app")
    #converts the latitude and longitude into a human readable address, heh 
    location = geolocator.reverse(f"{latitude}, {longitude}", exactly_one=True)
    #if the location is found and it has an address...
    if location and "address" in location.raw:
        # get the city name from the address, if it exists
        city = location.raw["address"].get("city", "")
        #searching for a location using the human readable address and the user's query
    # searching for places matching the details, gets 5 places
    results = geolocator.geocode(f"{query}, {city}", exactly_one=False, limit=limit)
    places = []
    # making a list of results to return
    if results:
        for result in results:
            places.append({
                "name": result.address,
                "latitude": result.latitude,
                "longitude": result.longitude
            })
    return places
