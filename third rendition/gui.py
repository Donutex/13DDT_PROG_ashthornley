from tkinter import * 
from tkinter import ttk 
import tkintermapview
import functions
import messagebox

class LoginPage:
    def __init__(self, conn):
        self.root = Tk()
        self.conn = conn
        self.root.title("Login Page")
        self.root.geometry("600x800")
        self.root.resizable(False, False)
        self.create_widgets()
    
    def create_widgets(self):
        # Frame for the login stuff
        self.login_frame = ttk.LabelFrame(self.root, text="Login")
        self.login_frame.pack(padx=10, pady=10, fill=BOTH)

        # Frame for the sign-up stuff
        self.signup_frame = ttk.LabelFrame(self.root, text="Sign Up")
        self.signup_frame.pack(padx=10, pady=10, fill=BOTH)

        # title + subtitle
        self.title_label = ttk.Label(self.login_frame, text="Like A Knife Through Clutter", font=("Arial", 16))
        self.title_label.pack(anchor=CENTER, padx=10, pady=10)
        self.subtitle_label = ttk.Label(self.login_frame, text="Login to your account to get started", font=("Arial", 12))
        self.subtitle_label.pack(anchor=CENTER, padx=10, pady=10)

        # Username label and entry
        self.username_label = ttk.Label(self.login_frame, text="Username:")
        self.username_label.pack(anchor=CENTER, padx=10, pady=10)
        self.username_entry = ttk.Entry(self.login_frame)
        self.username_entry.pack(anchor=CENTER, padx=10, pady=10)

        # Password label and entry
        self.password_label = ttk.Label(self.login_frame, text="Password:")
        self.password_label.pack(anchor=CENTER, padx=10, pady=10)
        self.password_entry = ttk.Entry(self.login_frame, show='*')
        self.password_entry.pack(anchor=CENTER, padx=10, pady=10)

        # Login button
        self.login_button = ttk.Button(self.login_frame, text="Login", command=self.login_button)
        self.login_button.pack(anchor=CENTER, padx=10, pady=10)

        # sign up subtitle
        self.signup_subtitle_label = ttk.Label(self.signup_frame, text="Don't have an account? Sign up here", font=("Arial", 12))
        self.signup_subtitle_label.pack(anchor=CENTER, padx=10, pady=10)

        # Sign Up button
        self.signup_button = ttk.Button(self.signup_frame, text="Sign Up", command=self.signup_page_button)
        self.signup_button.pack(anchor=CENTER, padx=10, pady=10)

    def login_button(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        # this function returns true or false so you can use it in an if statement
        if functions.check_login(self.conn, self.username, self.password):
            # Login successful
            self.root.destroy()
            MainPage(self.conn, self.username).run()

        else:
            # Login failed
            messagebox.showerror("Login Failed", "Incorrect username or password. Please try again or sign up.")
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)

    def signup_page_button(self):
        # opening the sign up page also with the same connection
        self.root.destroy()
        SignUpPage(self.conn).run()


class SignUpPage:
    def __init__(self, conn):
        self.root = Tk()
        self.conn = conn
        self.root.title("Sign Up Page")
        self.root.geometry("600x800")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the sign-up form
        signup_frame = ttk.LabelFrame(self.root, text="Sign Up")
        signup_frame.pack(padx=10, pady=10, fill=BOTH)

        # Username label and entry
        self.signup_username_label = ttk.Label(signup_frame, text="Username:")
        self.signup_username_label.pack(anchor=CENTER, padx=10, pady=10)
        self.signup_username_entry = ttk.Entry(signup_frame)
        self.signup_username_entry.pack(anchor=CENTER, padx=10, pady=10)

        # Password label and entry
        self.signup_password_label = ttk.Label(signup_frame, text="Password:")
        self.signup_password_label.pack(anchor=CENTER, padx=10, pady=10)
        self.signup_password_entry = ttk.Entry(signup_frame, show='*')
        self.signup_password_entry.pack(anchor=CENTER, padx=10, pady=10)

        # Sign Up button
        self.signup_button = ttk.Button(signup_frame, text="Sign Up", command=self.signup_button)
        self.signup_button.pack(anchor=CENTER, padx=10, pady=10)

        # back to login button
        self.back_to_login_button = ttk.Button(signup_frame, text="Back to Login", command=self.back_to_login_button)
        self.back_to_login_button.pack(anchor=CENTER, padx=10, pady=10)

    def signup_button(self):
        username = self.signup_username_entry.get()
        password = self.signup_password_entry.get()
        # function from the function py file
        functions.create_login(self.conn, username, password)
        # clearing the entries after sign up
        self.signup_username_entry.delete(0, END)
        self.signup_password_entry.delete(0, END)
        messagebox.showinfo("Sign Up Successful", "You have successfully signed up! You can now log in.")
        if functions.check_login(self.conn, username, password):
            # If the login check is successful, redirect to the main page
            self.root.destroy()
            LoginPage(self.conn).run()
    
    def back_to_login_button(self):
        self.root.destroy()
        LoginPage(self.conn).run()

    def run(self):
        self.root.mainloop()


class MainPage:
    def __init__(self, conn, username):
        self.root = Tk()
        self.conn = conn
        self.username = username
        self.root.title("Main Page")
        self.root.geometry("600x800")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # frames for the page
        title_frame = ttk.LabelFrame(self.root)
        title_frame.pack(padx=10, pady=10, fill=BOTH)
        body_frame = ttk.LabelFrame(self.root)
        body_frame.pack(padx=10, pady=10, fill=BOTH)
        text_frame = ttk.LabelFrame(body_frame)
        text_frame.pack(padx=10, pady=10, fill=BOTH)
        items_frame = ttk.LabelFrame(body_frame)
        items_frame.pack(padx=10, pady=10, fill=BOTH)
        progress_frame =  ttk.LabelFrame(body_frame)
        progress_frame.pack(padx=10, pady=10, fill=BOTH)
        next_steps_frame = ttk.LabelFrame(body_frame)
        next_steps_frame.pack(padx=10, pady=10, fill=BOTH)

        # Label for the title
        title_label = ttk.Label(title_frame, text="Like A Knife Through Clutter", font=("Papyrus", 24))
        title_label.pack(anchor=CENTER, padx=5)

        # subtitle label
        subtitle_label = ttk.Label(title_frame, text=f"Welcome back {self.username}!", font=("Arial", 15))
        subtitle_label.pack(anchor=CENTER, padx=5, pady=5)

        # body text
        body_text = ttk.Label(text_frame, text="This is the main page of 'Like A Knife Through Clutter' where you can manage your items in order to help " \
        " with decluttering your home.", wraplength=500)
        body_text.font=("Arial", 12)
        body_text.pack(anchor=CENTER, padx=5, pady=5)

        # view items button label
        view_items_label = ttk.Label(items_frame, text="View or enter your items here:")
        view_items_label.pack(anchor=CENTER, padx=5, pady=5)
        # view items button
        view_items_button = ttk.Button(items_frame, text="View Items", command=self.view_items_button)
        view_items_button.pack(anchor=CENTER, padx=5, pady=5)

        # progress label
        progress_label = ttk.Label(progress_frame, text="Your progress will be displayed here.")
        progress_label.pack(anchor=CENTER, padx=5, pady=5)
        # progress button
        progress_button = ttk.Button(progress_frame, text="View Progress", command=self.view_progress_button)
        progress_button.pack(anchor=CENTER, padx=5, pady=5)

        # next steps label
        next_steps_label = ttk.Label(next_steps_frame, text="Your next steps will be displayed here.")
        next_steps_label.pack(anchor=CENTER, padx=5, pady=5)
        # next steps button
        next_steps_button = ttk.Button(next_steps_frame, text="View Next Steps", command=self.view_next_steps_button)
        next_steps_button.pack(anchor=CENTER, padx=5, pady=5)

    def view_items_button(self):
        # Open the Create Item Page
        self.root.destroy()
        CreateItemPage(self.conn, self.username).run()

    def view_progress_button(self):
        # Open the Progress Page
        self.root.destroy()
        ProgressPage(self.conn).run()

    def view_next_steps_button(self):
        # Open the Next Steps Page
        self.root.destroy()
        NextStepsPage(self.conn).run()

    def run(self):
        self.root.mainloop()


class CreateItemPage:
    def __init__(self, conn, username):
        self.root = Tk()
        self.conn = conn
        self.username = username
        self.root.title("Create Item Page")
        self.root.geometry("600x800")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Frames for the page
        title_frame = ttk.LabelFrame(self.root)
        title_frame.pack(padx=10, pady=10, fill=BOTH)
        text_frame = ttk.LabelFrame(self.root)
        text_frame.pack(padx=10, pady=10, fill=BOTH)
        item_management_frame = ttk.LabelFrame(self.root, text="Item Management")
        item_management_frame.pack(padx=10, pady=10, fill=BOTH)
        item_form_creation_frame = ttk.LabelFrame(self.root, text="Create Item")
        item_form_creation_frame.pack(padx=10, pady=10, fill=BOTH)

        # Label for the title
        title_label = ttk.Label(title_frame, text="Like A Knife Through Clutter", font=("Papyrus", 24))
        title_label.pack(anchor=RIGHT, padx=10, pady=5)

        # back to main page button
        back_to_main_button = ttk.Button(title_frame, text="Back to Main Page", command=self.return_to_main_button)
        back_to_main_button.pack(anchor=LEFT, padx=10, pady=5)

        # subtitle label
        subtitle_label = ttk.Label(title_frame, text=f"{self.username}'s items", font=("Arial", 15))
        subtitle_label.pack(anchor=CENTER, padx=5, pady=5)

        # body text
        body_text = ttk.Label(text_frame, text="This is the item management page of 'Like A Knife Through Clutter' where you can create, edit and view your items." \
        " use the methods below to add items and start.", wraplength=500)
        body_text.font=("Arial", 12)
        body_text.pack(anchor=CENTER, padx=5, pady=5)

        # Item management label
        item_management_label = ttk.Label(item_management_frame, text="Manage your items here:")
        item_management_label.pack(anchor=LEFT, padx=10, pady=5)

        # View created items button
        view_items_button = ttk.Button(item_management_frame, text="View Items", command=view_items_button)
        view_items_button.pack(anchor=RIGHT, padx=10, pady=5)

        # Item name label and entry
        ttk.Label(item_form_creation_frame, text="Item Name:").pack(anchor=CENTER, padx=10, pady=10)
        self.item_name_entry = ttk.Entry(item_form_creation_frame)
        self.item_name_entry.pack(padx=10, pady=10, fill=BOTH)

        # Item description label and entry
        ttk.Label(item_form_creation_frame, text="Description:").pack(anchor=CENTER, padx=10, pady=10)
        self.item_description_entry = ttk.Entry(item_form_creation_frame)
        self.item_description_entry.pack(padx=10, pady=10, fill=BOTH)

        # Create Item button
        self.create_item_button = ttk.Button(item_form_creation_frame, text="Create Item", command=self.create_item_button)
        self.create_item_button.pack(padx=10, pady=10, fill=BOTH)

    def return_to_main_button(self):
        # Return to the main page
        self.root.destroy()
        MainPage(self.conn, self.username).run()

    def view_items_button(self):
        # Open the View Items Page
        self.root.destroy()
        ViewItemsPage(self.conn).run()

    def create_item_button(self):
        item_name = self.item_name_entry.get()
        item_description = self.item_description_entry.get()
        if functions.add_item(self.conn, item_name, item_description):
            messagebox.showinfo("Item Created", f"Item '{item_name}' has been created successfully.")
        else:
            messagebox.showerror("Failed to create item. Please try again.")
        # empty the text boxes
        self.item_name_entry.delete(0, END)
        self.item_description_entry.delete(0, END)

class ViewItemsPage:
    def __init__(self, conn):
        self.conn = conn
        self.root = Tk()
        self.root.title("View Items Page")
        self.root.geometry("600x800")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # frames for this page
        title_frame = ttk.LabelFrame(self.root)
        title_frame.pack(padx=10, pady=10, fill=BOTH)
        items_frame = ttk.LabelFrame(self.root)
        items_frame.pack(padx=10, pady=10, fill=LEFT)
        item_management_frame = ttk.LabelFrame(self.root, text="Item Management")
        item_management_frame.pack(padx=10, pady=10, fill=RIGHT)

        # Label for the title
        title_label = ttk.Label(title_frame, text="Like A Knife Through Clutter", font=("Papyrus", 24))
        title_label.pack(anchor=RIGHT, padx=10, pady=5)

        # back to main page button
        back_to_main_button = ttk.Button(title_frame, text="Back to Main Page", command=self.return_to_main_button)
        back_to_main_button.pack(anchor=LEFT, padx=10, pady=5)


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
