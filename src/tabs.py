import tkinter as tk
from tkinter import ttk

def create_tabs(root, style, on_change):
    style.configure('TNotebook.Tab', font=('Helvetica', '14'))

    style.configure('TNotebook.Tab', padding=[20, 8, 20, 8])

    style.layout("Tab",
    [('Notebook.tab', {'sticky': 'nswe', 'children':
        [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
            [('Notebook.label', {'side': 'top', 'sticky': ''})],
        })],
    })]
    )

    tabControl = ttk.Notebook(root)
    tabControl.pack(side='left')

    tab1 = ttk.Frame(tabControl)
    tabControl.add(tab1, text='By time and distance')

    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab2, text='By brake marks')

    tabControl.pack(expand=1, fill="both")

    Tab1EntryFrame = ttk.Frame(tab1, padding=(10, 10, 10, 10))
    Tab1EntryFrame.grid(rows=1, columns=4)
    labelEntrySTab1 = ttk.Label(Tab1EntryFrame, text="Distance (m)").grid(row=0, column=0)
    entrySTab1 = ttk.Entry(Tab1EntryFrame)
    entrySTab1.grid(row=0, column=1)
    entrySTab1.bind('<Return>', lambda event: on_change())
    labelEntryTTab1 = ttk.Label(Tab1EntryFrame, text="Time (s)").grid(row=0, column=2)
    entryTTab1 = ttk.Entry(Tab1EntryFrame)
    entryTTab1.grid(row=0, column=3)
    entryTTab1.bind('<Return>', lambda event: on_change())

    Tab2EntryFrame = ttk.Frame(tab2, padding=(10, 10, 10, 10))
    Tab2EntryFrame.grid(rows=1, columns=4)
    labelEntrySTab2 = ttk.Label(Tab2EntryFrame, text="Left length (m)").grid(row=0, column=0)
    entrySTab2 = ttk.Entry(Tab2EntryFrame)
    entrySTab2.grid(row=0, column=1)
    entrySTab2.bind('<Return>', lambda event: on_change())
    labelEntryTTab2 = ttk.Label(Tab2EntryFrame, text="Right length (m)").grid(row=0, column=2)
    entryTTab2 = ttk.Entry(Tab2EntryFrame)
    entryTTab2.grid(row=0, column=3)
    entryTTab2.bind('<Return>', lambda event: on_change())

    def get_selected_values():
        try:
            selected_tab = tabControl.index(tabControl.select())
            if selected_tab == 0:
                return entrySTab1.get(), entryTTab1.get(), 0
            elif selected_tab == 1:
                return entrySTab2.get(), entryTTab2.get(), 1
            else:
                return None, None, None
        except:
            return None, None, None

    return get_selected_values