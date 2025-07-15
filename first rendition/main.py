from tkinter import * 
from tkinter import ttk 

def main():
    root.mainloop()

root = Tk() 

# creating the frames 
header_frame = ttk.Frame(root, padding="10")
header_frame.grid(row=0, column=0, sticky=(W, E))
body_frame = ttk.Frame(root, padding="10")
body_frame.grid(row=1, column=0, sticky=(W, E))
body_frame_left = ttk.Frame(body_frame, padding="10")
body_frame_left.grid(row=0, column=0, sticky=(W, E))
body_frame_right = ttk.Frame(body_frame, padding="10")
body_frame_right.grid(row=0, column=1, sticky=(W, E))

# adding labels to the header frame
title_label = ttk.Label(header_frame, text="Like A Knife Through Clutter!", font=("Arial", 16))
title_label.grid(row=0, column=0, sticky=(W, E))
description_label = ttk.Label(header_frame, text="Add items to this program to help with management of your decluttering efforts!", font=("Arial", 12))
description_label.grid(row=1, column=0, sticky=(W, E))

# ADDING AN ITEM TO THE LIST!!!
# adding labels to the body frame
left_label = ttk.Label(body_frame_left, text="Add Items To Your List", font=("Arial", 14))
left_label.grid(row=0, column=0, sticky=(W, E))

item_name_label = ttk.Label(body_frame_left, text="Item Name:")
item_name_label.grid(row=1, column=0, sticky=(W, E))
item_name_entry = ttk.Entry(body_frame_left)
item_name_entry.grid(row=1, column=1, sticky=(W, E))

item_description_label = ttk.Label(body_frame_left, text="Item Description:")
item_description_label.grid(row=2, column=0, sticky=(W, E))
item_description_entry = ttk.Entry(body_frame_left)
item_description_entry.grid(row=2, column=1, sticky=(W, E))

def add_item():
    item_name = item_name_entry.get()
    item_description = item_description_entry.get()
    if item_name and item_description:
        with open("first rendition\items.txt", "a") as file:
            file.write(f"{item_name}: {item_description}\n")
        item_name_entry.delete(0, END)
        item_description_entry.delete(0, END)
        root.destroy()  
        main()
    else:
        print("Please fill in both fields.")

add_button = ttk.Button(body_frame_left, text="Add Item", command=add_item)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# REMOVING AN ITEM FROM THE LIST!!!
# adding labels to the right frame
right_label = ttk.Label(body_frame_right, text="Declutter Items From Your List", font=("Arial", 14))
right_label.grid(row=0, column=0, sticky=(W, E))
remove_item_label = ttk.Label(body_frame_right, text="Select Item to Remove:")
remove_item_label.grid(row=1, column=0, sticky=(W, E))
with open("first rendition\items.txt", "r") as file:
    items = file.readlines()
selected_item = ttk.Combobox(body_frame_right, state="readonly")
selected_item['values'] = items
selected_item.grid(row=1, column=1, sticky=(W, E))

def remove_item():
    selected_item = items.get()
    if selected_item:
        with open("first rendition\items.txt", "r") as file:
            lines = file.readlines()
        with open("first rendition\items.txt", "w") as file:
            for line in lines:
                if selected_item not in line:
                    file.write(line)
        items.set('')
        root.destroy()
        main()
    else:
        print("Please select an item to remove.")

remove_button = ttk.Button(body_frame_right, text="Remove Item", command=remove_item)
remove_button.grid(row=2, column=0, columnspan=2, pady=10)

main()
