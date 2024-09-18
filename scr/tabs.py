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

    tab1 = ttk.Frame(tabControl)
    tabControl.add(tab1, text='By time and distance')

    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab2, text='By brake marks')

    tabControl.pack(expand=1, fill="both")

    labelTab1 = ttk.Label(tab1, text="Inputs for velocity by time and distance.")
    labelTab1.pack(padx=10, pady=10)

    labelTab2 = ttk.Label(tab2, text="Inputs for velocity by brake marks.")
    labelTab2.pack(padx=10, pady=10)
