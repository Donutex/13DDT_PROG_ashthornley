import customtkinter as ctk
from tkinter import messagebox, END
import threading 
ctk.set_default_color_theme("forth rendition/theme.json")

class MainPage:
    def __init__(self, conn, username):
        self.conn = conn
        self.username = username
        self.root = ctk.CTk()  # CustomTkinter window
        self.root.title("Main Page")
        self.root.geometry("600x800")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # frames for the page (LabelFrames emulated with CTkFrame + labels inside)
        title_frame = ctk.CTkFrame(self.root, corner_radius=10)
        title_frame.pack(padx=10, pady=10, fill="x")

        body_frame = ctk.CTkFrame(self.root, corner_radius=10)
        body_frame.pack(padx=10, pady=10, fill="both", expand=True)

        text_frame = ctk.CTkFrame(body_frame, corner_radius=10)
        text_frame.pack(padx=10, pady=10, fill="x")

        items_frame = ctk.CTkFrame(body_frame, corner_radius=10)
        items_frame.pack(padx=10, pady=10, fill="x")

        progress_frame = ctk.CTkFrame(body_frame, corner_radius=10)
        progress_frame.pack(padx=10, pady=10, fill="x")

        next_steps_frame = ctk.CTkFrame(body_frame, corner_radius=10)
        next_steps_frame.pack(padx=10, pady=10, fill="x")

        # Label for the title
        title_label = ctk.CTkLabel(
            title_frame,
            text="Like A Knife Through Clutter",
            font=("Papyrus", 24)
        )
        title_label.pack(anchor="center", padx=5)

        # subtitle label
        subtitle_label = ctk.CTkLabel(
            title_frame,
            text=f"Welcome back {self.username}!",
            font=("Arial", 15)
        )
        subtitle_label.pack(anchor="center", padx=5, pady=5)

        # body text
        body_text = ctk.CTkLabel(
            text_frame,
            text=("This is the main page of 'Like A Knife Through Clutter' where you can manage your items in order to help "
                  "with decluttering your home."),
            wraplength=500,
            font=("Arial", 12)
        )
        body_text.pack(anchor="center", padx=5, pady=5)

        # view items section
        view_items_label = ctk.CTkLabel(items_frame, text="View or enter your items here:")
        view_items_label.pack(anchor="center", padx=5, pady=5)

        view_items_button = ctk.CTkButton(items_frame, text="View Items", command=self.view_items_button)
        view_items_button.pack(anchor="center", padx=5, pady=5)

        # progress section
        progress_label = ctk.CTkLabel(progress_frame, text="Your progress will be displayed here.")
        progress_label.pack(anchor="center", padx=5, pady=5)

        progress_button = ctk.CTkButton(progress_frame, text="View Progress", command=self.view_progress_button)
        progress_button.pack(anchor="center", padx=5, pady=5)

        # next steps section
        next_steps_label = ctk.CTkLabel(next_steps_frame, text="Your next steps will be displayed here. WARNING: Loading may take a few seconds.")
        next_steps_label.pack(anchor="center", padx=5, pady=5)

        next_steps_button = ctk.CTkButton(next_steps_frame, text="View Next Steps", command=self.view_next_steps_button)
        next_steps_button.pack(anchor="center", padx=5, pady=5)

    def view_items_button(self):
        self.root.destroy()
        from ItemPage import ItemPage
        ItemPage(self.conn, self.username).run()

    def view_progress_button(self):
        self.root.destroy()
        from ProgressPage import ProgressPage
        ProgressPage(self.conn, self.username).run()

    def view_next_steps_button(self):
        self.root.destroy()
        from NextStepsPage import NextStepsPage
        NextStepsPage(self.conn, self.username).run()

    def run(self):
        self.root.mainloop()
