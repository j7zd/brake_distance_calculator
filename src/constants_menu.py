import tkinter as tk
from tkinter.ttk import *
from main import update_velocity

is_opened = False  
entries = []      
labels = []        
entry_values = []  
default_entry_values = [ "1.2", "0.2", "0.4", "1.1", "0.9", "9.81"]
entry_values = default_entry_values.copy()

def save_value(event, idx, on_change):
    value = entries[idx].get()  
    entry_values[idx] = value   
    print(f"Value saved for {labels[idx * 3].cget('text')} {value}") 
    on_change()

def buttonClicked(window, btn, on_change):
    global is_opened
    
    if not is_opened:
        window.geometry("700x320")
        btn["text"] = '<'
        
        # Create a parent frame to hold all the smaller frames
        parent_frame = tk.Frame(window, borderwidth=2, relief="ridge")
        parent_frame.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

        variables = [
            ["t1", "Driver's reaction time:", "s"],
            ["t2", "Brake activation delay:", "s"],
            ["t3", "Brake delay rise time:", "s"],
            ["k", "Correction factor:", ""],
            ["m", "Coefficient of traction:", ""],
            ["g", "Acceleration of gravity:", "m/s²"]
        ]

        for idx, (var_name, description, unit) in enumerate(variables):
            frame = tk.Frame(parent_frame) 
            frame.grid(row=idx, column=0, sticky="w", padx=5, pady=2)
            
            desc_label = tk.Label(frame, text=description, width=30, anchor="w")
            desc_label.grid(row=0, column=0, columnspan=5, padx=2)
    
            labels.append(desc_label)
            
            var_label = tk.Label(frame, text=var_name)
            var_label.grid(row=1, column=0, columnspan=1, sticky="ew")
            labels.append(var_label)
            
            entry = tk.Entry(frame, width=3)
            entry.grid(row=1, column=1, sticky="ew")    
            entry.insert(0, entry_values[idx])  
            entries.append(entry)
            
            unit_label = tk.Label(frame, text=unit, width=5)
            unit_label.grid(row=1, column=2, sticky="w")
            labels.append(unit_label)
            
            # Bind the "Enter" key to the save_value function for this entry box
            entry.bind('<Return>', lambda event, i=idx: save_value(event, i, on_change))
        
        is_opened = True 
    else:
        window.geometry("500x320")
        btn["text"] = '>'
        
        for widget in window.grid_slaves():
            if int(widget.grid_info()["column"]) >= 2:  # Remove widgets in columns 2 and beyond
                widget.grid_forget()
        
        is_opened = False  