import tkinter as tk


class Box(tk.Frame):
    def __init__(self, parent, row, col, bg="white", **kwargs):
        super().__init__(parent, **kwargs)
        self.default_bg = bg
        self.config(bg=bg, **kwargs)
        self.grid(row=row, column=col, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

    def add_button(self, row=0, col=0, bg=None, **kwargs):
        if bg is None:
            bg = self.default_bg
        button = tk.Button(self, bg=bg, **kwargs)
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        return button
    
    def add_label(self, row=0, col=0, bg=None, **kwargs):
        if bg is None:
            bg = self.default_bg
        label = tk.Label(self, bg=bg, **kwargs)
        label.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        return label

    def add_entry(self, row=0, col=0, bg=None, **kwargs):
        if bg is None:
            bg = self.default_bg
        entry = tk.Entry(self, bg=bg, **kwargs)
        entry.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        return entry

    def configure_grid(self, rows, columns):
        for r in range(rows):
            self.grid_rowconfigure(r, weight=1)
        for c in range(columns):
            self.grid_columnconfigure(c, weight=1)