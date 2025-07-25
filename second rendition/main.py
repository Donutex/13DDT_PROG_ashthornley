from tkinter import * 
from tkinter import ttk 
import tkintermapview

root = Tk()
root.title("Like A Knife Through Clutter")

# functions that will let the buttons do something and lead to new pages
def item_page():
    def back_to_main():
        item_window.withdraw()
        root.deiconify() # this function 'unhides' the main window

    def add_item():
        # function to add an item to your list ---- at the moment it will store this in a text file, this will be changed to a database later
        item_name = item_name_entry.get()
        item_price = item_price_entry.get()
        item_condition = item_condition_entry.get()
        with open("first rendition\items.txt", "a") as file:
            file.write(f"{item_name}, {item_price}, {item_condition}\n")
        item_name_entry.delete(0, END)
        item_price_entry.delete(0, END)
        item_condition_entry.delete(0, END)
        # updating the dropdown menu with the new items
        with open("first rendition\items.txt", "r") as file: 
            items = file.readlines()
        selected_item['values'] = items
        
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


    # Labels and entry boxes for editing an existing item  
    edit_item_label = Label(body_frame_right, text="Edit an existing item", font=("arial", 16, "bold"))
    edit_item_label.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

    # dropdown menu to select an item to edit
    with open("first rendition\items.txt", "r") as file:
        items = file.readlines()
    selected_item = ttk.Combobox(body_frame_right, state="readonly")
    selected_item['values'] = items
    selected_item.grid(row=1, column=0, padx=10, pady=3)

    edit_name_label = Label(body_frame_right, text="new item name: ")
    edit_name_label.grid(row=2, column=0, padx=10, pady=5, sticky="NSEW")
    edit_name_entry = Entry(body_frame_right)
    edit_name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="NSEW")

    edit_price_label = Label(body_frame_right, text="new estimated value: ")
    edit_price_label.grid(row=3, column=0, padx=10, pady=5, sticky="NSEW")
    edit_price_entry = Entry(body_frame_right)
    edit_price_entry.grid(row=3, column=1, padx=10, pady=5, sticky="NSEW")

    edit_condition_label = Label(body_frame_right, text="new condition: ")
    edit_condition_label.grid(row=4, column=0, padx=10, pady=5, sticky="NSEW")
    edit_condition_entry = Entry(body_frame_right)
    edit_condition_entry.grid(row=4, column=1, padx=10, pady=5, sticky="NSEW")

    def edit_item():
        selected = selected_item.get()
        new_name = edit_name_entry.get()
        new_price = edit_price_entry.get()
        new_condition = edit_condition_entry.get()
        if selected and new_name and new_price and new_condition:
            with open("first rendition\items.txt", "r") as file:
                items = file.readlines()
            with open("first rendition\items.txt", "w") as file:
                for item in items:
                    if item.strip() == selected.strip():
                        file.write(f"{new_name}, {new_price}, {new_condition}\n")
                    else:
                        file.write(item)
        edit_name_entry.delete(0, END)
        edit_price_entry.delete(0, END)
        edit_condition_entry.delete(0, END)
        selected_item.set('Successfully edited!')

        # Update the dropdown menu with the new items
        with open("first rendition\items.txt", "r") as file: 
            items = file.readlines()
        selected_item['values'] = items
        selected_item.set('Successfully edited!')

    # button to edit an existing item
    edit_item_button = ttk.Button(body_frame_right, text="edit item", command=edit_item)
    edit_item_button.grid(row=5, column=0, padx=10, pady=5, sticky="NSEW")

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
    text_frame = ttk.LabelFrame(body_frame)
    text_frame.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")

    # button to go back to the main page
    back_button = ttk.Button(header_frame, text="Back", command=back_to_main)
    back_button.grid(row=0, column=1, padx=10, pady=5, sticky="NSEW")

    # Title for the page placed into the header frame
    title = Label(header_frame, text="Like A Knife Through Clutter - next steps", font=("papyrus", 20, "bold"))
    title.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

    # description for the map
    map_description = Label(body_frame, text="If you're struggling to find a place to dispose of your items, use the map below to find nearby stores and places that can help you.")
    map_description.grid(row=0, column=0, padx=10, pady=5, sticky="NSEW")

    # map that shows the location of nearby useful stores / places to help dispose of your items.
    local_map = tkintermapview.TkinterMapView(body_frame, width=600, height=400, corner_radius=0)
    local_map.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")    
    local_map.set_position(-36.852095, 174.763180)
    local_map.set_zoom(10)

    locations = [
    {"name": "Mt Eden Family Store", "lat": -36.8770, "lon": 174.6270},
    {"name": "New Lynn Family Store", "lat": -36.9090, "lon": 174.6840},
    {"name": "Howick Family Store", "lat": -36.8900, "lon": 174.9300},
    {"name": "Mt Wellington Family Store", "lat": -36.9180, "lon": 174.8300},
    {"name": "Royal Oak Family Store", "lat": -36.9060, "lon": 174.7700},
    ]
    for location in locations:
        local_map.set_marker(location["lat"], location["lon"], text=location["name"])

    # instructions for what to do with the users items
    # list with all the items (this is a placeholder and will be improved later)
    with open("items.txt", "r") as file:
        items = file.readlines()
    for index, item in enumerate(items):
        items = item.strip()
        name = item.split(", ")[0]
        item_name = Label(text_frame, text=f"Item {index+1}: {name}")
        item_name.grid(row=index+2, column=0, padx=10, pady=5, sticky="NSEW")

def progression_page():
    def back_to_main():
        progression_window.withdraw()
        root.deiconify() # this function 'unhides' the main window

    def declutter_item():
        selected = selected_item.get()
        if selected:
            with open("items.txt", "r") as file:
                items = file.readlines()
            for i in range(len(items)):
                items[i] = items[i].strip()            
                if items[i].strip() == selected.strip():
                    declutter_value = float(items[i].split(", ")[1])
                    with open("decluttered_items.txt", "a") as decluttered_file:
                        decluttered_file.write(f"{declutter_value}\n")
            with open("items.txt", "w") as file:
                for item in items:    
                    if item.strip() != selected.strip():
                        file.write(item + "\n") 
            # Update the dropdown after removing a item
            with open("items.txt", "r") as file:
                items = file.readlines()
            selected_item['values'] = items
            selected_item.set('Successfully decluttered!')  
        else:
            selected_item.set('Please select an item to declutter.')

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

    progression_declutter_frame = ttk.LabelFrame(progression_window)
    progression_declutter_frame.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")

    # button to go back to the main page
    back_button = ttk.Button(header_frame, text="Back", command=back_to_main)
    back_button.grid(row=0, column=1, padx=10, pady=5, sticky="NSEW")

    # Title for the page placed into the header frame
    title = Label(header_frame, text="Like A Knife Through Clutter - progression", font=("papyrus", 20, "bold"))
    title.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

    # written description of your progression
    progression_description = Label(body_frame_right, text="Your progression will be shown here as you add items and complete tasks.")
    progression_description.grid(row=0, column=0, padx=10, pady=5, sticky="NSEW")

    # List of items that the user owns 
    with open("first rendition\items.txt", "r") as file:
        items = file.readlines()
        for i in range(len(items)):
            item_summary = Label(body_frame_left, text=f"Item {i+1}: {items[i].strip()}")
            item_summary.grid(row=i, column=0, padx=10, pady=5, sticky="NSEW")

    # this opens the items file, reads it line by line, splits each line by the commas, looks at the second item (price), and adds them together
    with open("first rendition\items.txt", "r") as file:
        items = file.readlines()
        total_value = 0
        for i in range(len(items)):
            items[i] = items[i].strip()
            value = float(items[i].split(",")[1])
            total_value += value
        total_value_label = Label(body_frame_right, text=f"Total estimated value of items: ${total_value:.2f}") # the :.2f make the number a float with 2 decimals 
        total_value_label.grid(row=1, column=0, padx=10, pady=5, sticky="NSEW")

    # label for the deculttering section
    declutter_label = Label(progression_declutter_frame, text="Declutter an item", font=("arial", 16, "bold"))
    declutter_label.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

    # dropdown menu to show / select an item to declutter
    with open("first rendition\items.txt", "r") as file:
        items = file.readlines()
    selected_item = ttk.Combobox(progression_declutter_frame, state="readonly")
    selected_item['values'] = items
    selected_item.grid(row=1, column=0, padx=10, pady=3)

    # button to declutter an item
    declutter_button = ttk.Button(progression_declutter_frame, text="Declutter Item", command=declutter_item)
    declutter_button.grid(row=1, column=1, padx=10, pady=5, sticky="NSEW")

# frames for the page
header_frame = ttk.LabelFrame(root) 
header_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
body_frame = ttk.LabelFrame(root)
body_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")
declutter_frame = ttk.LabelFrame(root)
declutter_frame.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")

# Title for the page placed into the header frame
title = Label(header_frame, text="Like A Knife Through Clutter", font=("papyrus", 20, "bold"))
title.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

# buttons that lead to other pages in the app
item_page_button = ttk.Button(body_frame, text="Item", command=item_page)
item_page_button.grid(row = 1, column= 0, padx=10, pady=5)

next_steps_page_button = ttk.Button(body_frame, text="Next Steps", command=next_steps_page)
next_steps_page_button.grid(row = 2, column= 0, padx=10, pady=5)

progression_page_button = ttk.Button(body_frame, text="Progression", command=progression_page)
progression_page_button.grid(row = 3, column= 0, padx=10, pady=5)

root.mainloop()