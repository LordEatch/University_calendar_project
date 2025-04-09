import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

class Moodle(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Moodle calendar URL.
        ttk.Label(self, text="Moodle calendar URL:").pack(anchor="w")
        self.moodle_url_entry = ttk.Entry(self)
        self.moodle_url_entry.pack(fill="x", pady=(5, 20))

        # Subtract/Select Selector.
        ttk.Label(self, text="Subtract/Select:").pack(anchor="w")
        self.select_mode = ttk.Combobox(self, values=["Subtract", "Select"], state="readonly")
        self.select_mode.current(0)
        self.select_mode.pack(fill="x", pady=5)

        # Moodle event filters.
        ttk.Label(self, text="Moodle event filters:").pack(anchor="w")
        self.event_filter_frame = ttk.Frame(self)
        self.event_filter_frame.pack(fill="both", expand=True, pady=(5, 20))

        self.event_filter_text = tk.Text(self.event_filter_frame, height=8, wrap="word")
        self.event_filter_text.pack(fill="both", expand=True)

        # Save button.
        ttk.Button(self, text="Save").pack(anchor="w")

        # Save button.
        ttk.Button(self, text="Save").pack(anchor="w")