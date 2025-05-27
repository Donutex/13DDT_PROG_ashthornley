from tkinter import * 
from tkinter import ttk 

root = Tk()
root.title("Like A Knife Through Clutter")

# functions that will let the buttons do something
def item_page():
    def back_to_main():
        item_window.withdraw()
        root.deiconify() # this function 'unhides' the main window

    def add_item():
        # function to add an item to your list ---- at the moment it will store this in a text file, this will be changed to a database later
        item_name = item_name_entry.get()
        item_price = item_price_entry.get()
        item_condition = item_condition_entry.get()
        with open("items.txt", "a") as file:
            file.write(f"{item_name}, {item_price}, {item_condition}\n")

        item_name_entry.delete(0, END)
        item_price_entry.delete(0, END)
        item_condition_entry.delete(0, END)
        
    root.withdraw()
    item_window = Toplevel(root)
    item_window.title("Item Page")

    # frames for the page
    header_frame = ttk.LabelFrame(item_window) 
    header_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
    body_frame = ttk.LabelFrame(item_window)
    body_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")
    body_frame_left = ttk.LabelFrame(body_frame)
    body_frame_left.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
    body_frame_right = ttk.LabelFrame(body_frame)
    body_frame_right.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")

    # Title for the page placed into the header frame
    title = Label(header_frame, text="Like A Knife Through Clutter - your items", font=("papyrus", 20, "bold"))
    title.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

    # button to go back to the main page
    back_button = ttk.Button(header_frame, text="Back", command=back_to_main)
    back_button.grid(row=0, column=1, padx=10, pady=5, sticky="NSEW")

    # labels and entry boxes for the items details 
    create_item_label = Label(body_frame_left, text="Create a new item", font=("arial", 16, "bold"))
    create_item_label.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

    item_name_label = Label(body_frame_left, text="item name: ")
    item_name_label.grid(row=1, column=0, padx=10, pady=5, sticky="NSEW")
    item_name_entry = Entry(body_frame_left)
    item_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="NSEW")

    item_price_label = Label(body_frame_left, text="estimated value: ")
    item_price_label.grid(row=2, column=0, padx=10, pady=5, sticky="NSEW")
    item_price_entry = Entry(body_frame_left)
    item_price_entry.grid(row=2, column=1, padx=10, pady=5, sticky="NSEW")

    item_condition_label = Label(body_frame_left, text="condition: ")
    item_condition_label.grid(row=3, column=0, padx=10, pady=5, sticky="NSEW")
    item_condition_entry = Entry(body_frame_left)
    item_condition_entry.grid(row=3, column=1, padx=10, pady=5, sticky="NSEW")

    # button and process to add items to your list
    add_item_button = ttk.Button(body_frame_left, text="Add Item", command=add_item) 
    add_item_button.grid(row=4, column=0, padx=10, pady=5, sticky="NSEW")

    def edit_item():
        # function to edit an existing item in your list

        with open("items.txt", "r") as file:
            items = file.readlines()
            for item in items:
                x = item.split(", ")[0] 
                print = x 
            

    # edit an existing item

def next_steps_page():
    def back_to_main():
        next_steps_window.withdraw()
        root.deiconify() # this function 'unhides' the main window

    root.withdraw()
    next_steps_window = Toplevel(root)
    next_steps_window.title("Next Steps Page")

    # frames for the page
    header_frame = ttk.LabelFrame(next_steps_window) 
    header_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
    body_frame = ttk.LabelFrame(next_steps_window)
    body_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

    # button to go back to the main page
    back_button = ttk.Button(header_frame, text="Back", command=back_to_main)
    back_button.grid(row=0, column=1, padx=10, pady=5, sticky="NSEW")

    # Title for the page placed into the header frame
    title = Label(header_frame, text="Like A Knife Through Clutter - next steps", font=("papyrus", 20, "bold"))
    title.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

def progression_page():
    def back_to_main():
        progression_window.withdraw()
        root.deiconify() # this function 'unhides' the main window

    root.withdraw()
    progression_window = Toplevel(root)
    progression_window.title("Item Page")

    # frames for the page
    header_frame = ttk.LabelFrame(progression_window) 
    header_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
    body_frame = ttk.LabelFrame(progression_window)
    body_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")
    body_frame_left = ttk.LabelFrame(body_frame)
    body_frame_left.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
    body_frame_right = ttk.LabelFrame(body_frame)
    body_frame_right.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")

    # button to go back to the main page
    back_button = ttk.Button(header_frame, text="Back", command=back_to_main)
    back_button.grid(row=0, column=1, padx=10, pady=5, sticky="NSEW")

    # Title for the page placed into the header frame
    title = Label(header_frame, text="Like A Knife Through Clutter - progression", font=("papyrus", 20, "bold"))
    title.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

    with open("items.txt", "r") as file:
        items = file.readlines()
        for i in range(len(items)):
            item_summary = Label(body_frame_left, text=f"Item {i+1}: {items[i].strip()}")
            item_summary.grid(row=i, column=0, padx=10, pady=5, sticky="NSEW")

    # written description of your progression
    progression_description = Label(body_frame_right, text="Your progression will be shown here as you add items and complete tasks.")
    progression_description.grid(row=0, column=0, padx=10, pady=5, sticky="NSEW")

    # this opens the items file, reads it line by line, splits each line by the commas, looks at the second item (price), and adds them together
    with open("items.txt", "r") as file:
        items = file.readlines()
        total_value = sum(float(item.split(", ")[1]) for item in items if item.strip())
        total_value_label = Label(body_frame_right, text=f"Total estimated value of items: ${total_value:.2f}") # the :.2f make the number a float with 2 decimals 
        total_value_label.grid(row=1, column=0, padx=10, pady=5, sticky="NSEW")

        removal_status = Label(body_frame_right, text="Items removed: 0")  # Placeholder for removal status ADD THIS IN
        removal_status.grid(row=2, column=0, padx=10, pady=5, sticky="NSEW")

# frames for the page
header_frame = ttk.LabelFrame(root) 
header_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
body_frame = ttk.LabelFrame(root)
body_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

# Title for the page placed into the header frame
title = Label(header_frame, text="Like A Knife Through Clutter", font=("papyrus", 20, "bold"))
title.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

# buttons that lead to other pages in the app
item_page_button = ttk.Button(body_frame, text="Item", command=item_page)
item_page_button.pack(padx=10, pady=5)

next_steps_page_button = ttk.Button(body_frame, text="Next Steps", command=next_steps_page)
next_steps_page_button.pack(padx=10, pady=5)

progression_page_button = ttk.Button(body_frame, text="Progression", command=progression_page)
progression_page_button.pack(padx=10, pady=5)

root.mainloop()