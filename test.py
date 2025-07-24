import tkinter as tk

def draw_spongebob(canvas):
    # Body
    canvas.create_rectangle(100, 60, 300, 260, fill="#ffe135", outline="#d4b200", width=4)
    # Eyes
    canvas.create_oval(140, 90, 190, 140, fill="white", outline="black", width=2)
    canvas.create_oval(210, 90, 260, 140, fill="white", outline="black", width=2)
    canvas.create_oval(160, 110, 180, 130, fill="#00bfff", outline="black", width=2)
    canvas.create_oval(230, 110, 250, 130, fill="#00bfff", outline="black", width=2)
    canvas.create_oval(170, 120, 175, 125, fill="black")
    canvas.create_oval(240, 120, 245, 125, fill="black")
    # Sunglasses (cool!)
    canvas.create_rectangle(145, 110, 185, 130, fill="black", outline="white", width=2)
    canvas.create_rectangle(215, 110, 255, 130, fill="black", outline="white", width=2)
    canvas.create_line(185, 120, 215, 120, fill="white", width=3)
    canvas.create_line(145, 120, 130, 115, fill="black", width=4)
    canvas.create_line(255, 120, 270, 115, fill="black", width=4)
    # Mouth (smirk)
    canvas.create_arc(170, 160, 230, 200, start=200, extent=100, style=tk.ARC, width=3)
    # Gold chain
    canvas.create_oval(170, 250, 230, 270, outline="#FFD700", width=4)
    # Optional: add a little sparkle
    canvas.create_line(200, 255, 205, 260, fill="#FFD700", width=2)
    canvas.create_line(205, 260, 210, 255, fill="#FFD700", width=2)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Cool SpongeBob")
    canvas = tk.Canvas(root, width=400, height=400, bg="#87ceeb")
    canvas.pack()
    draw_spongebob(canvas)
    root.mainloop()