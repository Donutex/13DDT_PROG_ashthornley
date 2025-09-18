import customtkinter as ctk
from tkinter import messagebox, END
import functions
ctk.set_default_color_theme("forth rendition/theme.json")

class SignUpPage:
    def __init__(self, conn):
        self.conn = conn
        self.root = ctk.CTk()  # CustomTkinter window
        self.root.title("Sign Up Page")
        self.root.geometry("600x800")
        self.root.resizable(False, False)

        self._create_widgets()

    def _create_widgets(self):
        # Sign up frame
        signup_frame = ctk.CTkFrame(self.root, corner_radius=10)
        signup_frame.pack(padx=20, pady=20, fill="x")

        # Username label + entry
        ctk.CTkLabel(signup_frame, text="Username:", font=("Arial", 12)).pack(
            anchor="center", padx=10, pady=10
        )
        self.signup_username_entry = ctk.CTkEntry(signup_frame, width=250)
        self.signup_username_entry.pack(anchor="center", padx=10, pady=10)

        # Password label + entry
        ctk.CTkLabel(signup_frame, text="Password:", font=("Arial", 12)).pack(
            anchor="center", padx=10, pady=10
        )
        self.signup_password_entry = ctk.CTkEntry(signup_frame, show="*", width=250)
        self.signup_password_entry.pack(anchor="center", padx=10, pady=10)

        # Sign Up button
        ctk.CTkButton(signup_frame, text="Sign Up", command=self._signup).pack(
            anchor="center", padx=10, pady=15
        )

        # Back to login button
        ctk.CTkButton(signup_frame, text="Back to Login", command=self._back_to_login).pack(
            anchor="center", padx=10, pady=10
        )

    def _signup(self):
        username = self.signup_username_entry.get().strip()
        password = self.signup_password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Missing Fields", "Please enter both username and password.")
            return

        functions.create_login(self.conn, username, password)
        self.signup_username_entry.delete(0, END)
        self.signup_password_entry.delete(0, END)
        messagebox.showinfo("Sign Up Successful", "You have successfully signed up! You can now log in.")

        # optionally auto-login
        if functions.check_login(self.conn, username, password):
            self.root.destroy()
            from LoginPage import LoginPage
            LoginPage(self.conn).run()

    def _back_to_login(self):
        self.root.destroy()
        from LoginPage import LoginPage  
        LoginPage(self.conn).run()

    def run(self):
        self.root.mainloop()
