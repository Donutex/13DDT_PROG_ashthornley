"""This is the Item page.

This page allows users to create, view, edit, and delete items. Users can enter
item names and descriptions, view a list of their items, and manage them using
the edit and delete buttons and functions.
"""
import customtkinter as ctk
from tkinter import messagebox, END
import functions
ctk.set_default_color_theme("forth rendition/theme.json")

class ItemPage:
    def __init__(self, conn, username):
        """necessary initialization for the Item page.

        this part runs immediately when a new ItemPage object is created.
        it sets up the database connection (self.conn), remembers who the user
        is (self.username), sets up the window(self.root),and calls the method
        to create the widgets create_widgets()

        Args:
            conn (SQLite3 Connection): The database connection object.
        """
        self.conn = conn
        self.username = username
        self.root = ctk.CTk()  # CustomTkinter window
        self.root.title("Create Item Page")
        self.root.resizable(True, True)
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the item page.
        """
        # Frames for the page (LabelFrames emulated with CTkFrame + header label)
        title_frame = ctk.CTkFrame(self.root, corner_radius=10)
        title_frame.pack(padx=10, pady=10, fill="x")

        text_frame = ctk.CTkFrame(self.root, corner_radius=10)
        text_frame.pack(padx=10, pady=10, fill="x")

        item_viewing_frame = ctk.CTkFrame(self.root, corner_radius=10)
        item_viewing_frame.pack(padx=10, pady=10, fill="both", expand=True)

        item_tweaking_frame = ctk.CTkFrame(self.root, corner_radius=10)
        item_tweaking_frame.pack(padx=10, pady=10, fill="x")

        item_form_creation_frame = ctk.CTkFrame(self.root, corner_radius=10)
        item_form_creation_frame.pack(padx=10, pady=10, fill="x")

        # Back to main page button
        back_to_main_button = ctk.CTkButton(
            title_frame,
            text="Back to Main Page",
            command=self.return_to_main_button
        )
        back_to_main_button.pack(anchor="w", padx=10, pady=5)

        # Title label
        title_label = ctk.CTkLabel(
            title_frame,
            text="Like A Knife Through Clutter",
            font=("Papyrus", 24)
        )
        title_label.pack(anchor="e", padx=10, pady=5)

        # Subtitle label
        subtitle_label = ctk.CTkLabel(
            title_frame,
            text=f"{self.username}'s items",
            font=("Arial", 15)
        )
        subtitle_label.pack(anchor="center", padx=5, pady=5)

        # Body text
        body_text = ctk.CTkLabel(
            text_frame,
            text=(
                "This is the item management page of Like A Knife Through Clutter"
                "where you can create, edit and view your items. "
                "Use the methods below to add items."
            ),
            wraplength=500,
            font=("Arial", 12)
        )
        body_text.pack(anchor="center", padx=5, pady=5)

        # Item name label and entry
        self.item_name_label = ctk.CTkLabel(
            item_form_creation_frame, 
            text="Item Name:"
        )
        self.item_name_label.pack(anchor="center", padx=10, pady=5)

        self.item_name_entry = ctk.CTkEntry(
            item_form_creation_frame, 
            width=400,
            placeholder_text="Enter item name"
        )
        self.item_name_entry.pack(padx=10, pady=5)

        # Item description label and entry
        self.item_description_label = ctk.CTkLabel(
            item_form_creation_frame,
            text="Description:"
        )
        self.item_description_label.pack(anchor="center", padx=10, pady=5)

        self.item_description_entry = ctk.CTkEntry(
            item_form_creation_frame,
            width=400,
            placeholder_text="Enter description"
        )
        self.item_description_entry.pack(padx=10, pady=5)

        # Create Item button
        self.create_item_button_widget = ctk.CTkButton(
            item_form_creation_frame,
            text="Create Item",
            command=self.create_item_button
        )
        self.create_item_button_widget.pack(padx=10, pady=10, fill="x")

        # Item management label
        item_management_label = ctk.CTkLabel(
            item_viewing_frame, 
            text="View your items here:"
        )
        item_management_label.pack(anchor="w", padx=10, pady=5)

        # Scrollable area for items
        self.scrollable_frame = ctk.CTkScrollableFrame(
            item_viewing_frame, 
            width=600, 
            height=200
        )
        self.scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Item tweaking label
        item_tweaking_label = ctk.CTkLabel(
            item_tweaking_frame,
            text=("Edit or delete your items here "
                  "(this does not count towards your progress):\n"
                  "To edit: select it, then write the new name and description"
                  " in the boxes above and click Edit.\n"
                  "To delete: select it, then click Delete."),
            justify="left"
        )
        item_tweaking_label.pack(anchor="w", padx=10, pady=5)

        # Item selection dropdown (CustomTkinter OptionMenu)
        rows = functions.get_item_list(self.conn)
        item_name = [row[1] for row in rows]
        self.selected_item = ctk.StringVar(
            value="Select an item you want to edit or delete"
        )
        self.item_editing_combobox = ctk.CTkOptionMenu(
            item_tweaking_frame,
            variable=self.selected_item,
            values=item_name if item_name else ["No items available"]
        )
        self.item_editing_combobox.pack(padx=10, pady=10, fill="x")
        self.update_item_list()  # initial population

        # Edit Item button
        self.edit_item_button_widget = ctk.CTkButton(
            item_tweaking_frame,
            text="Edit Item",
            command=self.edit_item_button
        )
        self.edit_item_button_widget.pack(padx=10, pady=10, fill="x")

        # Delete Item button
        self.delete_item_button_widget = ctk.CTkButton(
            item_tweaking_frame,
            text="Delete Item",
            command=self.delete_item_button
        )
        self.delete_item_button_widget.pack(padx=10, pady=10, fill="x")

    def update_item_list(self):
        """Update the list of items displayed on the item page.

        This method clears the current list of items, find the new list using
        the function functions.get_item_list, and repopulates the display area
        with the updated items. It also refreshes the dropdown menu
        """
        # Clear current
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        items = functions.get_item_list(self.conn)
        if items:
            for row in items:
                item_info = f"Name: {row[1]}, Description: {row[2]}"
                ctk.CTkLabel(
                    self.scrollable_frame,
                    text=item_info, anchor="w"
                ).pack(anchor="w", padx=10, pady=2)
        else:
            ctk.CTkLabel(
                self.scrollable_frame,
                text="No items found."
            ).pack(anchor="w", padx=10, pady=2)

        # refresh dropdown
        rows = functions.get_item_list(self.conn)
        item_name = [row[1] for row in rows]
        if item_name:
            self.item_editing_combobox.configure(values=item_name)
        else:
            self.item_editing_combobox.configure(values=["No items available"])

    def return_to_main_button(self):
        """Return to the main page.
        """
        self.root.destroy()
        from MainPage import MainPage
        MainPage(self.conn, self.username).run()

    def create_item_button(self):
        """Create a new item.

        This method retrieves the item name and description from the entrys,
        then uses the function functions.add_item to add the item to the 
        database. If everything works then a success message is shown, if not
        an error message is shown. then the entrys are cleared and the item 
        list is updated.
        """
        item_name = self.item_name_entry.get()
        item_description = self.item_description_entry.get()
        if functions.add_item(self.conn, item_name, item_description):
            messagebox.showinfo(
                "Item Created",
                f"Item '{item_name}' has been created successfully."
            )
        else:
            messagebox.showerror(
                "Item Not Created",
                "Failed to create item. Please try again."
            )
        self.item_name_entry.delete(0, END)
        self.item_description_entry.delete(0, END)
        self.update_item_list()

    def edit_item_button(self):
        """Edit an existing item.

        This method retrieves the selected item from the dropdown, and the new
        name and description from the entrys. it then uses the function 
        functions.get_item_id_by_name to convert the name to an id, and then
        uses the function functions.update_item to update the item in the
        """
        selected_item_name = self.selected_item.get()
        new_name = self.item_name_entry.get()
        new_description = self.item_description_entry.get()
        item_id = functions.get_item_id_by_name(self.conn, selected_item_name)
        if item_id and functions.update_item(self.conn, item_id, new_name, new_description):
            messagebox.showinfo(
                "Item Edited",
                f"Item '{selected_item_name}' has been edited successfully."
            )
        else:
            messagebox.showerror(
                "Item Not Edited",
                "Failed to edit item. Please try again."
            )
        self.item_name_entry.delete(0, END)
        self.item_description_entry.delete(0, END)
        self.update_item_list()

    def delete_item_button(self):
        """Delete an existing item.

        This method retrieves the selected item from the dropdown, then uses
        the function functions.get_item_id_by_name to convert the name to an 
        id, and then uses the function functions.remove_item to delete the 
        item. if everything works then a success message is shown, if not an 
        error message is shown. then the entrys are cleared and the item list 
        is updated.
        """
        selected_item_name = self.selected_item.get()
        item_id = functions.get_item_id_by_name(self.conn, selected_item_name)
        if item_id and functions.remove_item(self.conn, item_id):
            messagebox.showinfo(
                "Item Deleted", 
                f"Item '{selected_item_name}' has been deleted successfully."
            )
        else:
            messagebox.showerror(
                "Item Not Deleted", 
                "Failed to delete item. Please try again."
            )
        self.item_name_entry.delete(0, END)
        self.item_description_entry.delete(0, END)
        self.update_item_list()

    def run(self):
        """Start the main loop for itself.
        """
        self.root.mainloop()
