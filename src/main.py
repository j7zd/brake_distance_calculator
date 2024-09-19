import tkinter as tk
from tkinter import ttk
from tabs import create_tabs
from constants_menu import *
from calculations import average_speed, brake_trails_speed, brake_distance

def update_velocity():
    a, b, input_type = get_values()
    if input_type == 0:
        velocity = average_speed(float(a), float(b))
        velocity_var.set(str(round(velocity, 2)))
        brake_distance_var.set(str(round(brake_distance(velocity, 1.2, 0.2, 0.4, 1.1, 0.9), 2)))
    elif input_type == 1:
        velocity = brake_trails_speed(float(a), float(b), 0.4, 1.1, 0.9)
        velocity_var.set(str(round(velocity, 2)))
        brake_distance_var.set(str(round(brake_distance(velocity, 1.2, 0.2, 0.4, 1.1, 0.9), 2)))
    else:
        velocity_var.set("")

if __name__ == "__main__":
    window = tk.Tk()

    window.title("Break distance calculator")
    #window.geometry("400x400")

    tabs_frame = tk.Frame()
    tabs_frame.grid(row=0, column=0, sticky="nsew")
    style = ttk.Style()
    get_values = create_tabs(tabs_frame, style, update_velocity)
    clicked = tk.StringVar()
    btn = tk.Button(window, text='>', command=lambda: buttonClicked(window, btn), width=3)
    btn.grid(row=0, column=1, sticky="nsew") 

    the_rest = tk.Frame()
    the_rest.grid(row=1, column=0, sticky="nsew")

    speed_label = tk.Label(the_rest, text="Velocity: ")
    speed_label.grid(row=0, column=0)
    velocity_var = tk.StringVar()
    velocity_var.set("")
    speed_entry = tk.Entry(the_rest, textvariable=velocity_var, state="readonly")
    speed_entry.grid(row=1, column=0)

    brake_distance_label = tk.Label(the_rest, text="Brake distance: ")
    brake_distance_label.grid(row=0, column=1)
    brake_distance_var = tk.StringVar()
    brake_distance_var.set("")
    brake_distance_entry = tk.Entry(the_rest, textvariable=brake_distance_var, state="readonly")
    brake_distance_entry.grid(row=1, column=1)

    window.mainloop()