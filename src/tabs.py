import tkinter as tk
from tkinter import ttk

def create_tabs(root, style):
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

    Tab1EntryFrame = ttk.Frame(tab1);
    Tab1EntryFrame.grid(rows=1, columns=4)
    labelEntrySTab1 = ttk.Label(Tab1EntryFrame, text="Distance").grid(row=0, column=0)
    entrySTab1 = ttk.Entry(Tab1EntryFrame).grid(row=0, column=1)
    labelEntryTTab1 = ttk.Label(Tab1EntryFrame, text="Time").grid(row=0, column=2)
    entryTTab1 = ttk.Entry(Tab1EntryFrame).grid(row=0, column=3)

    Tab2EntryFrame = ttk.Frame(tab2);
    Tab2EntryFrame.grid(rows=1, columns=4)
    labelEntrySTab2 = ttk.Label(Tab2EntryFrame, text="Length 1").grid(row=0, column=0)
    entrySTab2 = ttk.Entry(Tab2EntryFrame).grid(row=0, column=1)
    labelEntryTTab2 = ttk.Label(Tab2EntryFrame, text="Length 2").grid(row=0, column=2)
    entryTTab2 = ttk.Entry(Tab2EntryFrame).grid(row=0, column=3)
