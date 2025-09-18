from LoginPage import LoginPage
import functions
import sqlite3

conn = sqlite3.connect('forth rendition/Like_A_Knife_Through_Clutter4.db')
cursor = conn.cursor()

def main():
    functions.create_item_table(conn)
    functions.create_login_table(conn)
    functions.create_declutter_log_table(conn)

    # Initialize the Login Page
    login_page = LoginPage(conn)
    
    # Start the Tkinter main loop
    login_page.root.mainloop()

main()
conn.close()