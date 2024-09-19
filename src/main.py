import tkinter as tk
from tkinter import ttk
from tabs import create_tabs
from constants_menu import *
from calculations import average_speed, brake_trails_speed, brake_distance, ms_to_kmh, check_collision, Vmax, kmh_to_ms

break_distance_var = None

def update_velocity():
    a, b, input_type = get_values()
    if input_type == 0:
        velocity = average_speed(float(a), float(b))
        velocity_var.set(str(round(ms_to_kmh(velocity), 2)) + " km/h")
        brake_distance_var.set(str(round(brake_distance(velocity, 1.2, 0.2, 0.4, 1.1, 0.9), 2)) + " m") # TODO
    elif input_type == 1:
        velocity = brake_trails_speed(float(a), float(b), 0.4, 1.1, 0.9) # TODO
        velocity_var.set(str(round(ms_to_kmh(velocity), 2)) + " km/h")
        brake_distance_var.set(str(round(brake_distance(velocity, 1.2, 0.2, 0.4, 1.1, 0.9), 2)) + " m") # TODO
    else:
        velocity_var.set("")

def update_collision_distance():
    try:
        collision_distance = float(collision_distance_entry.get())
        brake_distance = float(brake_distance_var.get().split(" ")[0])
        does_collision = check_collision(collision_distance, brake_distance)
        if does_collision:
            does_collision_var.set("Yes")
        else:
            does_collision_var.set("No")
    except:
        does_collision_var.set("")

def update_speed_limit():
    try:
        speed_limit = kmh_to_ms(float(speed_limit_entry.get()))
        collision_distance = float(collision_distance_entry.get())
        n_speed = Vmax(collision_distance, 1.2, 0.2, 0.4, 1.1, 0.9) # TODO
        if n_speed is not None:
            if n_speed > speed_limit:
                new_speed_limit_var.set(str(ms_to_kmh(speed_limit)) + " km/h")
            else:
                new_speed_limit_var.set(str(ms_to_kmh(n_speed)) + " km/h")
        else:
            new_speed_limit_var.set("Error")
    except:
        new_speed_limit_var.set("")

if __name__ == "__main__":
    window = tk.Tk()

    window.title("Brake distance calculator")

    tabs_frame = tk.Frame()
    tabs_frame.grid(row=0, column=0, sticky="nsew")
    style = ttk.Style()
    get_values = create_tabs(tabs_frame, style, update_velocity)
    clicked = tk.StringVar()
    btn = tk.Button(window, text='>', command=lambda: buttonClicked(window, btn), width=3)
    btn.grid(row=0, column=1, sticky="nsew") 

    the_rest = tk.Frame()
    the_rest.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

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

    collision_distance_label = tk.Label(the_rest, text="Collision distance: ")
    collision_distance_label.grid(row=2, column=0)
    collision_distance_entry = tk.Entry(the_rest)
    collision_distance_entry.grid(row=3, column=0)
    collision_distance_entry.bind('<Return>', lambda event: update_collision_distance())

    does_collision_label = tk.Label(the_rest, text="Does it collide: ")
    does_collision_label.grid(row=2, column=1)
    does_collision_var = tk.StringVar()
    does_collision_var.set("")
    does_collision_entry = tk.Entry(the_rest, textvariable=does_collision_var, state="readonly")
    does_collision_entry.grid(row=3, column=1)

    speed_limit_label = tk.Label(the_rest, text="Speed limit: ")
    speed_limit_label.grid(row=4, column=0)
    speed_limit_entry = tk.Entry(the_rest)
    speed_limit_entry.grid(row=5, column=0)
    speed_limit_entry.bind('<Return>', lambda event: update_speed_limit())

    new_speed_limit_label = tk.Label(the_rest, text="New speed limit: ")
    new_speed_limit_label.grid(row=4, column=1)
    new_speed_limit_var = tk.StringVar()
    new_speed_limit_var.set("")
    new_speed_limit_entry = tk.Entry(the_rest, textvariable=new_speed_limit_var, state="readonly")
    new_speed_limit_entry.grid(row=5, column=1)

    window.mainloop()