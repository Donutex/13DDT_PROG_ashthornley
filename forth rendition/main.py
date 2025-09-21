"""the main file that runs the program.

this file creates the database tables if they do not exist,
then it opens the login page, all in the main() function.
"""
from LoginPage import LoginPage
import functions
import sqlite3

# setting up the database connection, this connection is passed to each page
conn = sqlite3.connect('forth rendition/Like_A_Knife_Through_Clutter4.db')
cursor = conn.cursor()


def main():
    """main() starts the program.

    main() creates the database tables using a SQL connection only if they
    do not exist, then it opens the login page by creating an instance of
    the LoginPage class before running the main loop.
    """
    functions.create_item_table(conn)
    functions.create_login_table(conn)
    functions.create_declutter_log_table(conn)

    # Initialize the Login Page
    login_page = LoginPage(conn)

    # Start the Tkinter main loop
    login_page.root.mainloop()


main()
conn.close()
