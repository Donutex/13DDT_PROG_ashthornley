"""this file contains all the functions used in the program.

nearly all of the functions here are related to database management but some 
look at the AI and map, both found on the Next Steps page.
"""
from argon2 import PasswordHasher
import re
import messagebox
from openai import OpenAI
from geopy.geocoders import Nominatim
import dotenv
import os

# this loads the .env file to put the key into pythons environment variables
dotenv.load_dotenv()
# this takes the api key from pythons environment variables
api_key = os.getenv("API_KEY")


def create_item_table(conn): # FUNCTIONS FOR THE DATABASE
    """Create the items table in the database.

    Args:
        conn (SQLite3.Connection): The database connection object.
    """
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS items4 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL
    )
    ''')
    conn.commit()


def create_login_table(conn):
    """Create the login table in the database.

    Args:
        conn (SQLite3.Connection): The database connection object.
    """
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS login4 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()


def create_declutter_log_table(conn):
    """Create the decluttering log table in the database.

    Args:
        conn (SQLite3.Connection): The database connection object.
    """
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS decluttering_log4 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        item_id INTEGER NOT NULL,
        item_name TEXT NOT NULL
    )
    ''')
    conn.commit()


def password_strength_check(password):
    """Check the strength of a password.

    based on criteria: at least 8 characters, one uppercase letter,
    one lowercase letter, one digit, and one special character.
    this ensures that the users have strong passwords for security reasons.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password is strong, False otherwise.
    """
    # Check the length of the password
    if len(password) < 8:
        return False
    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False
    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False
    # Check for at least one digit
    if not re.search(r"[0-9]", password):
        return False
    # Check for at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True


def create_login(conn, username, password):
    """Create a new user in the login table.

    The password is hashed using the argon2 algorithm for security.
    The function also checks the strength of the password using
    password_strength_check(). the username must be unique, if the username
    already exists, an error message is shown.

    Args:
        conn (SQLite3.Connection): The database connection object.
        username (str): The username of the new user.
        password (str): The password of the new user.

    Returns:
        bool: True if the user was created successfully, False otherwise.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM login4 WHERE username = ?", (username,))
    if cursor.fetchone() is not None:
        messagebox.showerror(
            "User Exists",
            "Username already taken. Please choose a different username."
        )
        return False

    if not password_strength_check(password):
        messagebox.showerror(
            "Weak Password",
            "Password must be at least 8 characters long "
            "and include at least one uppercase letter, one lowercase letter, "
            "one digit, and one special character."
        )
        return False
    else:
        cursor = conn.cursor()
        # hashing the password before storing it in the database
        hashed_password = PasswordHasher().hash(password)
        cursor.execute(
            "INSERT INTO login4 (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )
        conn.commit()
        return True


def check_login(conn, username, password):
    """Check the login credentials of a user.

    this function takes the username and password entered by the user and
    checks if they match the credentials stored in the database. if there
    are no matching username or password, an error message is shown.
    the stored password is hashed, so the argon2 algorithm is used to verify
    the password entered by the user against the password in the database.

    Args:
        conn (SQLite3.Connection): The database connection object.
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        bool: True if the login is successful, Error msg and False otherwise.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM login4 WHERE username = ?", (username,))
    user = cursor.fetchone()
    if user is None:
        messagebox.showerror(
            "Login Failed", 
            "Incorrect username or password. Please try again or sign up."
        )
    stored_password = user[0]
    try:
        PasswordHasher().verify(stored_password, password)
        return True  # Login successful
    except:
        messagebox.showerror(
            "Login Failed",
            "Incorrect username or password. Please try again or sign up."
        )
        return False  # Login failed


def add_item(conn, name, description):
    """Add a new item to the items table.

    adds an item to the SQL database (to the items4 table), with a name
    and description, an id is then assigned to the item automatically.

    Args:
        conn (SQLite3.Connection): The database connection object.
        name (str): The name of the item.
        description (str): The description of the item.

    Returns:
        bool: True if the item was added successfully.
    """
    if not name or not description:
        messagebox.showerror(
            "Missing Fields",
            "Please enter both item name and description."
        )
        return False

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items4 (name, description) VALUES (?, ?)",
        (name, description)
    )
    conn.commit()
    return True


def remove_item(conn, item_id):
    """Remove an item from the items table.

    finds an item in the SQL database (in the items4 table) by its id number
    and removes it from the database.

    Args:
        conn (SQLite3.Connection): The database connection object.
        item_id (int): The ID of the item to remove.

    Returns:
        bool: True if the item was removed successfully.
    """
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items4 WHERE id = ?", (item_id,))
    conn.commit()
    return True


def declutter_item(conn, item_id):
    """Remove (declutter) an item from the items table.

    finds an item in the SQL database (in the items4 table) by its id number
    and removes it from the database. this was created to differentiate between
    removing an item and decluttering an item. (may not be necessary but this
    allows for more clarity in the code and easier future modifications).

    Args:
        conn (SQLite3.Connection): The database connection object.
        item_id (int): The ID of the item to declutter.

    Returns:
        bool: True if the item was decluttered successfully.
    """
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items4 WHERE id = ?", (item_id,))
    conn.commit()
    return True


def update_item(conn, item_id, new_name, new_description):
    """Update an item in the items table.

    finds an item in the SQL database (in the items4 table) by its id number
    and updates its name and description. this is done by replacing the old 
    name and description with the new name and description provided.

    Args:
        conn (SQLite3.Connection): The database connection object.
        item_id (int): The ID of the item to update.
        new_name (str): The new name for the item.
        new_description (str): The new description for the item.

    Returns:
        bool: True if the item was updated successfully.
    """
    if not new_name or not new_description:
        messagebox.showerror(
            "Missing Fields",
            "Please enter both item name and description."
        )
        return False

    cursor = conn.cursor()
    cursor.execute(
        "UPDATE items4 SET name = ?, description = ? WHERE id = ?",
        (new_name, new_description, item_id)
    )
    conn.commit()
    return True


def get_item_list(conn):
    """Retrieve a list of all items in the items table.

    retrieves all items from the SQL database (from the items4 table) and
    returns them as a list of tuples, each tuple contains the id, name, and
    description. This way I can take what information I need from each item.

    Args:
        conn (SQLite3.Connection): The database connection object.

    Returns:
        list: A list of tuples containing the item ID, name, and description.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items4")
    rows = cursor.fetchall()
    return rows


def get_item_id_by_name(conn, name):
    """Retrieve the ID of an item by its name.

    finds an item in the SQL database (in the items4 table) by its name
    and returns its id number. this is used for when the user wants to edit
    or delete a specific item.

    Args:
        conn (SQLite3.Connection): The database connection object.
        name (str): The name of the item.

    Returns:
        int: The ID of the item, or None if not found.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM items4 WHERE name = ?", (name,))
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        None


def log_declutter(conn, username, item_name, item_id):
    """Log a decluttering action.

    records a decluttering action in the decluttering_log4 table, storing
    the username of the user who decluttered, the name of the item, and the
    ID of the item.

    Args:
        conn (SQLite3.Connection): The database connection object.
        username (str): The username of the user performing the decluttering.
        item_name (str): The name of the item being decluttered.
        item_id (int): The ID of the item being decluttered.
    """
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO decluttering_log4 (username, item_name, item_id) VALUES (?, ?, ?)",
        (username, item_name, item_id)
    )
    conn.commit()


def get_declutter_count(conn, username):
    """Retrieve the decluttering count for a user.

    this function looks at the decluttering_log4 table in the SQL database
    and counts how many items the user has decluttered, it returns this count
    to update things like the progress bar.

    Args:
        conn (SQLite3.Connection): The database connection object.
        username (str): The username of the user for whom to retrieve 
                        the decluttering count.

    Returns:
        int: The decluttering count for the user.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM decluttering_log4 WHERE username = ?",
        (username,)
    )
    count = cursor.fetchone()[0]
    return count


def ai_predicted_next_steps(item_names): #  AI FUNCTIONS
    """Predict the next steps for a list of items to declutter.

    this function predicts what to do with the users items by using AI.
    A client is created using OpenAI and my api key. Ive written a long system
    message to tell the AI what its purpose is and how it should act, 
    and a user message to provide the actual context and problems it needs to 
    solve. The messages are sent to the API model (ive chosen a free one) 
    and the first part of the response is returned, the remainder of the 
    response is just useless data.

    Args:
        item_names (list): A list of item names to declutter.

    Returns:
        list: A list of predicted next steps for each item.
    """
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    system_message = (
        "You are a helpful and knowledgeable decluttering assistant."
        "You help users in my app: Like A Knife Through Clutter."
        "You will receive a list of items that a user wants to declutter."
        "You will decide what the user will do with their item, a next step."
        "You choose from either: 'donate', 'sell', 'recycle', 'trash', 'keep'"
        "You will not provide any other options, only these five"
        "Your decisions are trying to help the user declutter effectively"
        "Example: \nShirt: donate\nLaptop: sell\nBottle: recycle"
        "You will not add any extra information, only the one word next step"
        "always assume that the items you receive are items"
        "if the item cannot be identified, you will choose 'trash'"
    )

    user_message = (
        f"Here is a list of items that I own and want to declutter: \
        {item_names} What is the next step for me to do with my items? \
        Choose from either: 'donate', 'sell', 'recycle', 'trash', 'keep'"
    )

    response = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[
            {"role" : "system" , "content" : system_message},
            {"role" : "user" , "content" : user_message}
        ]
    )
    result = response.choices[0].message.content
    print(result)
    return result

# currently not in use, see docstring
def search_nearby_places(query, latitude, longitude, limit=2): #  MAP FUNCTIONS
    """Search for nearby places based on a query (NOT IN USE).

    this function would of searched for nearby places without using a
    predetermined list of places using the geopy library. I could not get this
    to function correctly, so I created a predetermined list of places instead.
    If I were to work on this project further, I would try to get this function
    working correctly.

    Args:
        query (str): The search query (e.g., "donation center").
        latitude (float): The latitude of Auckland city.
        longitude (float): The longitude of Auckland city.
        limit (int): The maximum number of results to return. Defaults to 2.

    Returns:
        list: A list of nearby places matching the query.
    """
    geolocator = Nominatim(user_agent="clutter_app")
    location = geolocator.reverse(f"{latitude}, {longitude}", exactly_one=True)
    city = ""
    if location and "address" in location.raw:
        #city = location.raw["address"].get("city", "") 
        city = 'Auckland'
    results = geolocator.geocode(
        f"{query} near {city}", 
        exactly_one=False, 
        limit=limit
    )
    places = []
    if results:
        for result in results:
            places.append({
                "name": result.address,
                "lat": result.latitude,
                "lon": result.longitude
            })
    return places
