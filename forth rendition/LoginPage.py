"""the login page file that runs the login page.

this file has a LoginPage class that creates the login page, the page is the 
classes object, and the functions needed to make the page work are the class's
methods. the page is created using customtkinter to make it look modern 
and cool (similar to all the other pages). the page leads to the main page 
if the login is successful, or to the sign-up page if the user does not have an
account.
"""
import customtkinter as ctk
from tkinter import messagebox, END
import functions
from MainPage import MainPage
from SignUpPage import SignUpPage

# setting the theme for the customtkinter, using a json file 
ctk.set_default_color_theme("forth rendition/theme.json")

class LoginPage:
    def __init__(self, conn):
        """necessary initialization for the login page.

        this part runs immediately when a new LoginPage object is created.
        it sets up the database connection (self.conn), the window(self.root),
        and calls the method to create the widgets create_widgets()

        Args:
            conn (SQLite3 Connection): The database connection object.
        """
        self.conn = conn
        self.root = ctk.CTk()  
        self.root.title("Login Page")
        self.root.geometry("600x570")
        self.root.resizable(False, False)
        self.create_widgets()


    def create_widgets(self):
        """Create the widgets for the login page.
        """
        self.login_frame = ctk.CTkFrame(self.root, corner_radius=10)
        self.login_frame.pack(padx=20, pady=20, fill="both")

        self.login_label = ctk.CTkLabel(
            self.login_frame,
            text="Login",
            font=("Arial", 18, "bold")
        )
        self.login_label.pack(pady=(10, 5))

        self.title_label = ctk.CTkLabel(
            self.login_frame,
            text="Like A Knife Through Clutter",
            font=("Arial", 16)
        )
        self.title_label.pack(padx=10, pady=10)

        self.subtitle_label = ctk.CTkLabel(
            self.login_frame,
            text="Login to your account to get started",
            font=("Arial", 12)
        )
        self.subtitle_label.pack(padx=10, pady=10)

        # Username
        self.username_label = ctk.CTkLabel(self.login_frame, text="Username:")
        self.username_label.pack(padx=10, pady=(10, 2))
        self.username_entry = ctk.CTkEntry(self.login_frame, width=200)
        self.username_entry.pack(padx=10, pady=5)

        # Password
        self.password_label = ctk.CTkLabel(self.login_frame, text="Password:")
        self.password_label.pack(padx=10, pady=(10, 2))
        self.password_entry = ctk.CTkEntry(self.login_frame, show='*', width=200)
        self.password_entry.pack(padx=10, pady=5)

        # Login button
        self.login_button = ctk.CTkButton(
            self.login_frame,
            text="Login",
            command=self.login_button_action
        )
        self.login_button.pack(padx=10, pady=10)

        self.signup_frame = ctk.CTkFrame(self.root, corner_radius=10)
        self.signup_frame.pack(padx=20, pady=20, fill="both")

        self.signup_label = ctk.CTkLabel(
            self.signup_frame,
            text="Sign Up",
            font=("Arial", 18, "bold")
        )
        self.signup_label.pack(pady=(10, 5))

        self.signup_subtitle_label = ctk.CTkLabel(
            self.signup_frame,
            text="Don't have an account? Sign up here",
            font=("Arial", 12)
        )
        self.signup_subtitle_label.pack(padx=10, pady=10)

        # Sign Up button
        self.signup_button = ctk.CTkButton(
            self.signup_frame,
            text="Sign Up",
            command=self.signup_page_button
        )
        self.signup_button.pack(padx=10, pady=10)


    def login_button_action(self):
        """Handle the login button action.

        this method is called when the login button is pressed. is looks at the
        entrys for the username and passwords then checks if they are correct
        using the functions.check_login function. if the login is successful, 
        the main page opens, if not an error message is shown and the entrys
        are cleared. so the user can try again.
        """
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        # Assuming functions.check_login exists
        if functions.check_login(self.conn, self.username, self.password):
            self.root.destroy()
            MainPage(self.conn, self.username).run()
        else:
            messagebox.showerror(
                "Login Failed",
                "Incorrect username or password. Please try again or sign up."
            )
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)


    def signup_page_button(self):
        """Handle the sign-up button action.
        """
        self.root.destroy()
        SignUpPage(self.conn).run()

    def run(self):
        """Start the main loop for itself.
        """
        self.root.mainloop()

