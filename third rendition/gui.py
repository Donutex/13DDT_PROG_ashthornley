from tkinter import * 
from tkinter import ttk 
import tkintermapview

class LoginPage:
    def __init__(self):
        self.root = Tk()
        self.root.title("Login Page")
        self.root.geometry("600x800")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Frame for the login stuff
        login_frame = ttk.LabelFrame(self.root, text="Login")
        login_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

        # Username label and entry
        ttk.Label(text="Username:").pack(anchor=CENTER, padx=10, pady=10)
        self.username_entry = ttk.Entry(self.root)
        self.username_entry.pack(anchor=CENTER, padx=10, pady=10)

        # Password label and entry
        ttk.Label(text="Password:").pack(anchor=CENTER, padx=10, pady=10)
        self.password_entry = ttk.Entry(self.root, show='*')
        self.password_entry.pack(anchor=CENTER, padx=10, pady=10)

        # Login button
        self.login_button = ttk.Button(text="Login", command=self.login_button)
        self.login_button.pack(anchor=CENTER, padx=10, pady=10)

    def login_button(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # For demonstration, we will just print the credentials
        # In a real application, you would verify these credentials
        print(f"Username: {username}, Password: {password}")
        
        # Clear the entries after login attempt
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

        # Optionally, you can close the login window or proceed to the next page
        self.root.destroy()
        MainPage().run()


class SignUpPage:
    def __init__(self):
        self.root = Tk()
        self.root.title("Sign Up Page")
        self.root.geometry("600x800")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the sign-up form
        signup_frame = ttk.LabelFrame(self.root, text="Sign Up")
        signup_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        # Username label and entry
        ttk.Label(signup_frame, text="Username:").grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = ttk.Entry(signup_frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        # Password label and entry
        ttk.Label(signup_frame, text="Password:").grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = ttk.Entry(signup_frame, show='*')
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Sign Up button
        self.signup_button = ttk.Button(signup_frame, text="Sign Up", command=self.signup_button)
        self.signup_button.grid(row=2, columnspan=2, pady=10)

    def signup_button(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # For demonstration, we will just print the credentials
        # In a real application, you would save these credentials
        print(f"Username: {username}, Password: {password}")
        
        # Clear the entries after sign-up attempt
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

        # Optionally, you can close the sign-up window or proceed to the next page
        self.root.destroy()


class MainPage:
    def __init__(self):
        self.root = Tk()
        self.root.title("Main Page")
        self.root.geometry("600x800")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the main content
        main_frame = ttk.LabelFrame(self.root, text="Main Page")
        main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        # Add a label
        ttk.Label(main_frame, text="Welcome to the Main Page!").grid(row=0, column=0, padx=5, pady=5)

        # Add a button to open a map view
        map_button = ttk.Button(main_frame, text="Open Map", command=self.open_map)
        map_button.grid(row=1, column=0, padx=5, pady=5)

    def open_map(self):
        map_window = Toplevel(self.root)
        map_window.title("Map View")
        
        # Create a map view
        map_widget = tkintermapview.TkinterMapView(map_window, width=600, height=400)
        map_widget.pack(fill=BOTH, expand=True)
        
        # Set a default location
        map_widget.set_position(37.7749, -122.4194)  # Example: San Francisco coordinates
        map_widget.set_zoom(10)

    def run(self):
        self.root.mainloop()


class CreateItemPage:
    def __init__(self):
        self.root = Tk()
        self.root.title("Create Item Page")
        self.root.geometry("600x800")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the item creation form
        item_frame = ttk.LabelFrame(self.root, text="Create Item")
        item_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        # Item name label and entry
        ttk.Label(item_frame, text="Item Name:").grid(row=0, column=0, padx=5, pady=5)
        self.item_name_entry = ttk.Entry(item_frame)
        self.item_name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Item description label and entry
        ttk.Label(item_frame, text="Description:").grid(row=1, column=0, padx=5, pady=5)
        self.item_description_entry = ttk.Entry(item_frame)
        self.item_description_entry.grid(row=1, column=1, padx=5, pady=5)

        # Create Item button
        self.create_item_button = ttk.Button(item_frame, text="Create Item", command=self.create_item_button)
        self.create_item_button.grid(row=2, columnspan=2, pady=10)

    def create_item_button(self):
        item_name = self.item_name_entry.get()
        item_description = self.item_description_entry.get()
        
        # For demonstration, we will just print the item details
        print(f"Item Name: {item_name}, Description: {item_description}")
        
        # Clear the entries after item creation attempt
        self.item_name_entry.delete(0, END)
        self.item_description_entry.delete(0, END)

        # Optionally, you can close the item creation window or proceed to the next page
        self.root.destroy()


class ProgressPage:
    def __init__(self):
        self.root = Tk()
        self.root.title("Progress Page")
        self.root.geometry("600x800")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the progress display
        progress_frame = ttk.LabelFrame(self.root, text="Progress")
        progress_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        # Add a label to show progress
        self.progress_label = ttk.Label(progress_frame, text="Your progress will be displayed here.")
        self.progress_label.grid(row=0, column=0, padx=5, pady=5)

    def run(self):
        self.root.mainloop()


class NextStepsPage:
    def __init__(self):
        self.root = Tk()
        self.root.title("Next Steps Page")
        self.root.geometry("600x800")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the next steps
        next_steps_frame = ttk.LabelFrame(self.root, text="Next Steps")
        next_steps_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        # Add a label to show next steps
        self.next_steps_label = ttk.Label(next_steps_frame, text="Your next steps will be displayed here.")
        self.next_steps_label.grid(row=0, column=0, padx=5, pady=5)

    def run(self):
        self.root.mainloop()
