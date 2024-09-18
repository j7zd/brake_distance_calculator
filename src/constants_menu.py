from tkinter import *
from tkinter.ttk import *


is_opened = False  # Global flag for window state
entries = []       # List to store entry widgets
labels = []        # List to store label widgets
entry_values = []  # List to store the values entered in the entry boxes
default_entry_values = [ "1.2", "0.2", "0.4", "1", "0.9", "9.81", "50"]

def save_value(event, idx):
    value = entries[idx].get()  # Get the value from the corresponding entry
    entry_values[idx] = value   # Save the value to the corresponding index in the list
    print(f"Value saved for {labels[idx].cget('text')}: {value}")  # Print the saved value for feedback


def buttonClicked(window, btn):
    global is_opened
    if not is_opened:
        # Make the window wider
        window.geometry("600x400")
        btn["text"] = 'v'
        
        # List of names for the entry boxes
        names = ["t1", "t2", "t3", "k", "m", "g", "SL"]
        
        if not labels and not entries:
            is_default = True
            # Create the entry boxes with labels, placed below each other
            for idx, name in enumerate(names):
                label = Label(window, text = name)
                label.place(x = 420, y = 50 + idx * 40)  # Place labels starting from x=420 and spacing them vertically
                labels.append(label)
                
                txt = Entry(window, width=5)
                txt.place(x = 440, y = 50 + idx * 40)  # Entry boxes aligned to the right of the labels
                entries.append(txt)
                
                # Set the default value in the entry box
                txt.insert(0, default_entry_values[idx])

                # Append the default value to the entry_values list
                entry_values.append(default_entry_values[idx])
                
                # Bind the "Enter" key to the save_value function for this entry box
                txt.bind('<Return>', lambda event, i=idx: save_value(event, i))
            
        # Show the widgets if hidden
        for label in labels:
            label.place(x=420, y=50 + labels.index(label) * 40)
        for txt in entries:
            txt.place(x=440, y=50 + entries.index(txt) * 40)
            
            is_opened = True
    else:
        # Make the window narrower
        window.geometry("400x400")
        btn["text"] = '>'
        
        for label in labels:
            label.place_forget()
        for txt in entries:
            txt.place_forget()
        
        is_opened = False
