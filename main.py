from tkinter import * 
from tkinter import ttk 

root = Tk()
root.title("Like A Knife Through Clutter")

# functions that will let the buttons do something
def item_page():
    root.withdraw()
    item_window = Toplevel(root)
    item_window.title("Item Page")

    # frames for the page
    header_frame = ttk.LabelFrame(item_window) 
    header_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
    body_frame = ttk.LabelFrame(item_window)
    body_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

    # Title for the page placed into the header frame
    title = Label(header_frame, text="Like A Knife Through Clutter - your items", font=("papyrus", 20, "bold"))
    title.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

def next_steps_page():
    root.withdraw()
    next_steps_window = Toplevel(root)
    next_steps_window.title("Next Steps Page")

    # frames for the page
    header_frame = ttk.LabelFrame(next_steps_window) 
    header_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
    body_frame = ttk.LabelFrame(next_steps_window)
    body_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

    # Title for the page placed into the header frame
    title = Label(header_frame, text="Like A Knife Through Clutter - next steps", font=("papyrus", 20, "bold"))
    title.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

def progression_page():
    root.withdraw()
    progression_window = Toplevel(root)
    progression_window.title("Item Page")

    # frames for the page
    header_frame = ttk.LabelFrame(progression_window) 
    header_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
    body_frame = ttk.LabelFrame(progression_window)
    body_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

    # Title for the page placed into the header frame
    title = Label(header_frame, text="Like A Knife Through Clutter - progression", font=("papyrus", 20, "bold"))
    title.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")


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
item_page_button.grid(row=0, column=0, padx=10, pady=5, sticky="NSEW")

next_steps_page_button = ttk.Button(body_frame, text="Next Steps", command=next_steps_page)
next_steps_page_button.grid(row=1, column=0, padx=10, pady=5, sticky="NSEW")

progression_page_button = ttk.Button(body_frame, text="Progression", command=progression_page)
progression_page_button.grid(row=2, column=0, padx=10, pady=5, sticky="NSEW")




root.mainloop()