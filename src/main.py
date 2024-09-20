import tkinter as tk
from tkinter import ttk
from tabs import create_tabs
from constants_menu import *
from calculations import average_speed, brake_trails_speed, brake_distance, ms_to_kmh, check_collision, Vmax, kmh_to_ms

break_distance_var = None
ROUNDING = 4

def update_velocity(get_values):
    try:
        a, b, input_type = get_values()
        t1 = float(entry_values[0])
        t2 = float(entry_values[1])
        t3 = float(entry_values[2])
        j = entry_values[3]
        if j == "":
            k = float(entry_values[4])
            m = float(entry_values[5])
        else:
            j = float(j)
            k = 1.1
            m = j / 9.81 / 1.1
        if input_type == 0:
            velocity = average_speed(float(a), float(b))
            velocity_var.set(str(round(ms_to_kmh(velocity), ROUNDING)))
        elif input_type == 1:
            velocity = brake_trails_speed(float(a), float(b), t3, k, m)
            velocity_var.set(str(round(ms_to_kmh(velocity), ROUNDING)))
        else:
            velocity_var.set("")
    except:
        pass
    update_brake_distance()

def update_brake_distance():
    try:
        t1 = float(entry_values[0])
        t2 = float(entry_values[1])
        t3 = float(entry_values[2])
        j = entry_values[3]
        if j == "":
            k = float(entry_values[4])
            m = float(entry_values[5])
        else:
            j = float(j)
            k = 1.1
            m = j / 9.81 / 1.1
        velocity = kmh_to_ms(float(speed_entry.get()))
        brake_distance_var.set(str(round(brake_distance(velocity, t1, t2, t3, k, m), ROUNDING)) + " m")
    except:
        brake_distance_var.set("")
    update_collision_distance()

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
    update_speed_limit()

def update_speed_limit():
    try:
        t1 = float(entry_values[0])
        t2 = float(entry_values[1])
        t3 = float(entry_values[2])
        j = entry_values[3]
        if j == "":
            k = float(entry_values[4])
            m = float(entry_values[5])
        else:
            j = float(j)
            k = 1.1
            m = j / 9.81 / 1.1
        speed_limit = kmh_to_ms(float(speed_limit_entry.get()))
        collision_distance = float(collision_distance_entry.get())
        n_speed = kmh_to_ms(Vmax(collision_distance, t1, t2, t3, k, m))
        if n_speed is not None:
            if n_speed > speed_limit:
                new_speed_limit_var.set(str(ms_to_kmh(speed_limit)))
            else:
                new_speed_limit_var.set(str(round(ms_to_kmh(n_speed), ROUNDING)))
        else:
            new_speed_limit_var.set("Error")
    except:
        new_speed_limit_var.set("")

get_values_1 = None

if __name__ == "__main__":
    window = tk.Tk()

    window.title("Brake distance calculator")

    tabs_frame = tk.Frame()
    tabs_frame.grid(row=0, column=0, sticky="nsew")
    style = ttk.Style()
    get_values_1 = create_tabs(tabs_frame, style, lambda: update_velocity(get_values_1))
    clicked = tk.StringVar()
    btn = tk.Button(window, text='>', command=lambda: buttonClicked(window, btn, lambda: update_velocity(get_values_1)), width=3)
    btn.grid(row=0, column=1, rowspan=2, sticky="nsew") 

    the_rest = tk.Frame()
    the_rest.grid(row=0, column=0, sticky="nsew", padx=10, pady=100)

    speed_label = tk.Label(the_rest, text="Velocity (km/h): ")
    speed_label.grid(row=0, column=0)
    velocity_var = tk.StringVar()
    velocity_var.set("")
    speed_entry = tk.Entry(the_rest, textvariable=velocity_var)
    speed_entry.grid(row=1, column=0)
    speed_entry.bind('<Return>', lambda event: update_brake_distance())

    brake_distance_label = tk.Label(the_rest, text="Brake distance (m): ")
    brake_distance_label.grid(row=0, column=1)
    brake_distance_var = tk.StringVar()
    brake_distance_var.set("")
    brake_distance_entry = tk.Entry(the_rest, textvariable=brake_distance_var, state="readonly")
    brake_distance_entry.grid(row=1, column=1)

    collision_distance_label = tk.Label(the_rest, text="Collision distance (m): ")
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

    speed_limit_label = tk.Label(the_rest, text="Speed limit (km/h): ")
    speed_limit_label.grid(row=4, column=0)
    speed_limit_entry = tk.Entry(the_rest)
    speed_limit_entry.grid(row=5, column=0)
    speed_limit_entry.bind('<Return>', lambda event: update_speed_limit())

    new_speed_limit_label = tk.Label(the_rest, text="New speed limit (km/h): ")
    new_speed_limit_label.grid(row=4, column=1)
    new_speed_limit_var = tk.StringVar()
    new_speed_limit_var.set("")
    new_speed_limit_entry = tk.Entry(the_rest, textvariable=new_speed_limit_var, state="readonly")
    new_speed_limit_entry.grid(row=5, column=1)

    window.mainloop()