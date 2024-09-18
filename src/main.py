import tkinter as tk
from tkinter import ttk
from tabs import create_tabs



if __name__ == "__main__":
    window = tk.Tk()

    window.title("Break distance calculator")


    tabs_frame = tk.Frame() 
    tabs_frame.grid(row=0, column=0, sticky="nsew")
    style = ttk.Style()
    create_tabs(tabs_frame, style)
    button = ttk.Button(tabs_frame, text=">")
    button.pack(side='right', padx=10, pady=10)


    window.mainloop()