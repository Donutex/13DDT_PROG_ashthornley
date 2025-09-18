
import customtkinter as ctk
from tkinter import messagebox, END
import functions
# because this is the first page, we can import stuff here to avoid circular imports
from MainPage import MainPage
from SignUpPage import SignUpPage

ctk.set_default_color_theme("forth rendition/theme.json")

class LoginPage:
    def __init__(self, conn):
        self.conn = conn
        self.root = ctk.CTk()  
        self.root.title("Login Page")
        self.root.geometry("600x800")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Login frame
        self.login_frame = ctk.CTkFrame(self.root, corner_radius=10)
        self.login_frame.pack(padx=20, pady=20, fill="both")

        self.login_label = ctk.CTkLabel(
            self.login_frame,
            text="Login",
            font=("Arial", 18, "bold")
        )
        self.login_label.pack(pady=(10, 5))

        # title + subtitle
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

        # Sign-up frame
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
        self.root.destroy()
        SignUpPage(self.conn).run()

    def run(self):
        self.root.mainloop()

