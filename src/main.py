import tkinter as tk
from tkinter import ttk
from tabs import create_tabs
from constants_menu import *


if __name__ == "__main__":
    window = tk.Tk()

    window.title("Break distance calculator")
    window.geometry("400x400")

    tabs_frame = tk.Frame()
    tabs_frame.grid(row=0, column=0, sticky="nsew")
    style = ttk.Style()
    create_tabs(tabs_frame, style)
    clicked = tk.StringVar()
    btn = tk.Button(window, text='>', command=lambda: buttonClicked(window, btn), width=3)
    btn.place(x=350, y=50) 


    window.mainloop()