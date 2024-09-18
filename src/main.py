import tkinter as tk
from tkinter import ttk
from tabs import create_tabs
from widgets.box import Box


if __name__ == "__main__":
    window = tk.Tk()

    window.title("Break distance calculator")
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    box = Box(window, row=0, col=0, bg="green", bd=3, relief="ridge")
    box.add_label(text="hello", row=0, col=0, fg="yellow", bg="green")
    entry = box.add_entry(row=0, col=1)
    box.add_button(text="Submit", row=1, col=0, command=lambda: print(f"Name: {entry.get()}"))
    box.configure_grid(rows=2, columns=2)

    box2 = Box(window, row=0, col=1, bg="yellow", bd=10, relief="ridge")
    box2.add_label(text="hello", row=0, col=1, fg="red", bg="yellow")
    entry2 = box2.add_entry(fg="white", row=0, col=2, bg="yellow")
    box2.add_button(text="Submit", row=0, col=3, fg="white", bg="yellow", command=lambda: print(f"Name: {entry2.get()}"))
    box2.configure_grid(rows=1, columns=1)

    row = ttk.Frame(window)
    row.pack(fill='both', expand=True)


    style = ttk.Style()
    create_tabs(row, style)

    button = ttk.Button(row, text=">")
    button.pack(side='right', padx=10, pady=10)

    window.mainloop()