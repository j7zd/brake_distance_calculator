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
    tabControl.add(tab1, text='Tab 1')

    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab2, text='Tab 2')

    tabControl.pack(expand=1, fill="both")

    labelTab1 = ttk.Label(tab1, text="This is the content of Tab 1")
    labelTab1.pack(padx=10, pady=10)

    labelTab2 = ttk.Label(tab2, text="This is the content of Tab 2")
    labelTab2.pack(padx=10, pady=10)
