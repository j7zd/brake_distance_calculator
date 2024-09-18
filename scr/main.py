import tkinter as tk
from tkinter import ttk
from tabs import create_tabs

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Break Distance Calculator")

    root.geometry("400x300")

    style = ttk.Style()
    create_tabs(root, style)

    root.mainloop()