"""This is the progress page.

This page allows users to view their decluttering progress via a progress bar
keeping track of a 25 item milestone and more importantly, log decluttering
that they have done by selecting an item from a dropdown menu.
"""
import customtkinter as ctk
from tkinter import messagebox
import functions
ctk.set_default_color_theme("forth rendition/theme.json")


class ProgressPage:
    """Progress page of the application."""
    def __init__(self, conn, username):
        """Necessary initialization for the Progress page.

        This part runs immediately when a new ProgressPage object is created.
        It sets up the database connection (self.conn), remembers who the user
        is (self.username), sets up the window(self.root), prevents attribute
        errors for the progress and decluttering_combobox attributes, and calls
        the method to create the widgets create_widgets()

        Args:
            conn (SQLite3 Connection): The database connection object.
        """
        self.conn = conn
        self.username = username
        self.root = ctk.CTk()
        self.root.title("Progress")
        self.root.geometry("600x800")
        self.root.resizable(False, False)
        self.progress = None
        self.decluttering_combobox = None
        self._create_widgets()

    def _create_widgets(self):
        """Create the widgets for the Progress page."""
        # frames for the page
        title_frame = ctk.CTkFrame(self.root)
        title_frame.pack(padx=10, pady=10, fill="x")

        body_frame = ctk.CTkFrame(self.root)
        body_frame.pack(padx=10, pady=10, fill="both", expand=True)

        text_frame = ctk.CTkFrame(body_frame)
        text_frame.pack(padx=10, pady=10, fill="x")

        progress_bar_frame = ctk.CTkFrame(body_frame)
        progress_bar_frame.pack(padx=10, pady=10, fill="x")

        decluttering_frame = ctk.CTkFrame(body_frame)
        decluttering_frame.pack(padx=10, pady=10, fill="x")

        # back to the main button 
        back_to_main_button = ctk.CTkButton(
            title_frame,
            text="← Back to Main Page",
            command=self._return_to_main
        )
        back_to_main_button.pack(side="left", padx=10, pady=5)

        # title for the page
        title_label = ctk.CTkLabel(
            title_frame,
            text="Like A Knife Through Clutter",
            font=("Papyrus", 24)
        )
        title_label.pack(side="right", padx=10, pady=5)

        # subtitle with the username
        subtitle_label = ctk.CTkLabel(
            title_frame,
            text=f"{self.username}'s Progress!",
            font=("Arial", 15)
        )
        subtitle_label.pack(anchor="center", padx=5, pady=5)

        # body text
        body_text_label = ctk.CTkLabel(
            text_frame,
            text="This is the progress page of 'Like A Knife Through Clutter' "
            "where you can view your progress and log decluttering that you "
            "have done.",
            wraplength=500,
        )
        body_text_label.pack(anchor="center", padx=5, pady=5)

        # progress bar introduction
        progress_bar_intro_label = ctk.CTkLabel(
            progress_bar_frame,
            text="Your progress will be displayed here:"
        )
        progress_bar_intro_label.pack(anchor="center", padx=5, pady=5)

        self.progress = ctk.CTkProgressBar(
            progress_bar_frame,
            width=400
        )
        self.progress.pack(padx=10, pady=10)
        self.progress_text_label = ctk.CTkLabel(progress_bar_frame, text="")
        self.progress_text_label.pack(padx=10, pady=(0, 10))
        self._update_progress_bar()  #  initial update so it isn't empty

        # decluttering info
        decluttering_info_label = ctk.CTkLabel(
            decluttering_frame,
            text="Log your decluttering here:"
        )
        decluttering_info_label.pack(anchor="center", padx=5, pady=5)

        # dropdown menu for items to declutter
        # because of the way info is fetched from the database, we need to
        # just get the names and can ignore all the other info, therefore
        # we get row[1] from each row 
        item_names = [row[1] for row in functions.get_item_list(self.conn)]
        self.decluttering_combobox = ctk.CTkOptionMenu(
            decluttering_frame,
            values=item_names,
            width=400
        )
        self.decluttering_combobox.set("Select an item you have decluttered")
        self.decluttering_combobox.pack(padx=10, pady=10, fill="x")

        # log decluttering button
        self.log_decluttering_button = ctk.CTkButton(
            decluttering_frame,
            text="Log Decluttering",
            command=self._log_decluttering
        )
        self.log_decluttering_button.pack(padx=10, pady=10, fill="x")

    
    def _log_decluttering(self):
        """Log the decluttering action.

        This method retrieves the selected item from the combobox, and gets the
        corresponding item ID from the database using the function
        functions.get_item_id_by_name(). If the item ID is found, it calls
        functions.declutter_item() and functions.log_declutter() to mark the
        item as decluttered in the database and remove it from the users items.
        It then updates the progress bar and shows a success message. If the
        item ID is not found, it shows an error message. Then the combobox
        resets to the default prompt.
        """
        item_name = self.decluttering_combobox.get()
        item_id = functions.get_item_id_by_name(self.conn, item_name)

        if item_id:
            functions.declutter_item(self.conn, item_id)
            functions.log_declutter(
                self.conn,
                self.username,
                item_name,
                item_id
            )
            self._update_progress_bar()
            messagebox.showinfo(
                title="Decluttering Logged",
                message="Your decluttering has been logged successfully."
            )
        else:
            messagebox.showerror(
                title="Decluttering Not Logged",
                message="Failed to log decluttering. Please try again."
            )

        self.decluttering_combobox.set("Select an item you have decluttered")


    def _update_progress_bar(self):
        """Update the progress bar based on the user's decluttering progress.

        This method fetches the number of items the user has decluttered using
        functions.get_declutter_count(). It calculates the progress towards a
        25 item milestone and updates the progress bar and text label. If the
        user has reached or exceeded the milestone, it shows a congratulatory
        message.
        """
        milestone = 25
        count = functions.get_declutter_count(self.conn, self.username)
        progress_percent = (count / milestone)
        self.progress.set(progress_percent)

        # Update progress text
        self.progress_text_label.configure(
            text=f"{count} out of the {milestone} item milestone!"
        )

        if count >= milestone:
            messagebox.showinfo(
                title="Milestone Reached!",
                message="Congratulations! You are doing great, keep it up!"
            )
            # ADD A RESET BUTTON OR SOMETHING TO RESET THE COUNT IF THEY WANT TO DO ANOTHER MILESTONE


    def _return_to_main(self):
        """Return to the main page."""
        self.root.destroy()
        from MainPage import MainPage
        MainPage(self.conn, self.username).run()


    def run(self):
        """Run the main loop of the Progress Page."""
        self.root.mainloop()
