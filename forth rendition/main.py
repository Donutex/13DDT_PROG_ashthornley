from tkinter import * 
from tkinter import ttk 
from PIL import Image, ImageTk

username = 'admin'

root = Tk()
root.title("Like A Knife Through Clutter - Main Page")
root.geometry("600x800")
root.configure(bg="#e6f2ff")

# set ttk styles
style = ttk.Style()
style.configure("TLabelFrame", background="#e6f2ff")
style.configure("TFrame", background="#5a3e02")

# frames for the page
title_frame = ttk.LabelFrame(root)
title_frame.pack(padx=10, pady=10, fill=BOTH)
body_frame = ttk.LabelFrame(root)
body_frame.pack(padx=10, pady=10, fill=BOTH)
text_frame = ttk.LabelFrame(body_frame)
text_frame.pack(padx=10, pady=10, fill=BOTH)
items_frame = ttk.LabelFrame(body_frame)
items_frame.pack(padx=10, pady=10, fill=BOTH)
progress_frame =  ttk.LabelFrame(body_frame)
progress_frame.pack(padx=10, pady=10, fill=BOTH)
next_steps_frame = ttk.LabelFrame(body_frame)
next_steps_frame.pack(padx=10, pady=10, fill=BOTH)

# Load and resize the image using Pillow
original_image = Image.open("forth rendition/logo_cleaned-removebg-preview.png")
resized_image = original_image.resize((250, 240))  # width, height in pixels
logo_image = ImageTk.PhotoImage(resized_image)
logo_label = Label(title_frame, image=logo_image)
logo_label.pack(anchor=CENTER, pady=5)

# subtitle label
subtitle_label = ttk.Label(title_frame, text=f"Welcome back {username}!", font=("Segoe UI", 15))
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
view_items_button = ttk.Button(items_frame, text="View Items",)
view_items_button.pack(anchor=CENTER, padx=5, pady=5)

# progress label
progress_label = ttk.Label(progress_frame, text="Your progress will be displayed here.")
progress_label.pack(anchor=CENTER, padx=5, pady=5)
# progress button
progress_button = ttk.Button(progress_frame, text="View Progress",)
progress_button.pack(anchor=CENTER, padx=5, pady=5)

# next steps label
next_steps_label = ttk.Label(next_steps_frame, text="Your next steps will be displayed here.")
next_steps_label.pack(anchor=CENTER, padx=5, pady=5)
# next steps button
next_steps_button = ttk.Button(next_steps_frame, text="View Next Steps",)
next_steps_button.pack(anchor=CENTER, padx=5, pady=5)


root.mainloop()