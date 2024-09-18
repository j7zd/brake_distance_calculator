import tkinter as tk
from tkinter import ttk
from tabs import create_tabs

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Break Distance Calculator")

    row = ttk.Frame(root)
    row.pack(fill='both', expand=True)


    style = ttk.Style()
    create_tabs(row, style)

    button = ttk.Button(row, text=">")
    button.pack(side='right', padx=10, pady=10)

    root.mainloop()