"""This is the signup page.

This page allows users to create a new account by providing a username and
password. It includes input validation to ensure that both fields are filled
and that the password meets strength requirements.
"""

import customtkinter as ctk
from tkinter import messagebox, END
import functions
ctk.set_default_color_theme("forth rendition/theme.json")


class SignUpPage:
    """Sign Up page of the application."""
    def __init__(self, conn):
        """Necessary initialization for the Sign Up page.

        This part runs immediately when a new SignUpPage object is created.
        It sets up the database connection (self.conn),
        sets up the window(self.root), and calls the method to create the
        widgets create_widgets()

        Args:
            conn (SQLite3 Connection): The database connection object.
        """
        self.conn = conn
        self.root = ctk.CTk()  # CustomTkinter window
        self.root.title("Sign Up Page")
        self.root.geometry("600x450")
        self.root.resizable(False, False)
        self._create_widgets()


    def _create_widgets(self):
        """Create the widgets for the Sign Up page."""
        # Sign up frame
        signup_frame = ctk.CTkFrame(self.root, corner_radius=10)
        signup_frame.pack(padx=20, pady=20, fill="x")

        # instructions for user label
        instructions_label = ctk.CTkLabel(
            signup_frame,
            text="Sign Up for an account to get started\n"
                 "Passwords must contain a minimum of 8 characters,\n"
                 "at least one uppercase letter, one lowercase letter, \n"
                 "one digit, and one special character.",
            font=("Arial", 16),
            wraplength=400  # Wrap text at 400 pixels
        )
        instructions_label.pack(anchor="center", padx=10, pady=10)

        # Username label + entry
        username_label =ctk.CTkLabel(
            signup_frame,
            text="Username:",
            font=("Arial", 12)
        )
        username_label.pack(anchor="center", padx=10, pady=10)
        
        self.signup_username_entry = ctk.CTkEntry(signup_frame, width=250)
        self.signup_username_entry.pack(anchor="center", padx=10, pady=10)

        # Password label + entry
        password_label = ctk.CTkLabel(
            signup_frame,
            text="Password:",
            font=("Arial", 12)
        )
        password_label.pack(anchor="center", padx=10, pady=10)

        self.signup_password_entry = ctk.CTkEntry(
            signup_frame,
            show="*",
            width=250
        )
        self.signup_password_entry.pack(anchor="center", padx=10, pady=10)

        # Sign Up button
        sign_up_button = ctk.CTkButton(
            signup_frame,
            text="Sign Up",
            command=self._signup
        )
        sign_up_button.pack(anchor="center", padx=10, pady=15)

        # Back to login button
        back_to_login_button = ctk.CTkButton(
            signup_frame,
            text="Back to Login",
            command=self._back_to_login
        )
        back_to_login_button.pack(anchor="center", padx=10, pady=10)


    def _signup(self):
        """Handle the sign-up process.

        This method retrieves the username and password from the entry fields,
        checks for missing fields, and attempts to create a new login. If the
        password does not meet strength requirements, an error message is shown
        and the process is aborted. If the sign-up is successful,
        the entry fields are cleared and the user is told they can now log in.

        Returns:
            _type_: _description_
        """
        username = self.signup_username_entry.get().strip()
        password = self.signup_password_entry.get().strip()

        if not username or not password:
            messagebox.showerror(
                "Missing Fields",
                "Please enter both username and password."
            )
            return

        if functions.create_login(self.conn, username, password) is False:
            return  # Password strength check failed inside create_login
        else:
            self.signup_username_entry.delete(0, END)
            self.signup_password_entry.delete(0, END)
            messagebox.showinfo(
                "Sign Up Successful",
                "You have successfully signed up! You can now log in."
            )

        # optionally auto-login
        if functions.check_login(self.conn, username, password):
            self.root.destroy()
            from LoginPage import LoginPage
            LoginPage(self.conn).run()


    def _back_to_login(self):
        """Return to the login page."""
        self.root.destroy()
        from LoginPage import LoginPage
        LoginPage(self.conn).run()


    def run(self):
        """Run the main loop of the Sign Up Page."""
        self.root.mainloop()
