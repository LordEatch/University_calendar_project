import tkinter as tk
from tkinter import ttk
from settings import SettingsWindow

class HomeWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Home")
        self.geometry("300x200")
        self.configure(padx=20, pady=20)

        self.create_widgets()

    def create_widgets(self):
        font = ("Segoe UI", 10)

        # "Execute" Button
        self.execute_btn = ttk.Button(self, text="Execute", command=self.execute)
        self.execute_btn.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # "Settings" Button
        self.settings_btn = ttk.Button(self, text="Settings", command=self.open_settings)
        self.settings_btn.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    def execute(self):
        print("Execute button pressed")

    def open_settings(self):
        pass
        #settings_window = SettingsWindow()  # Create a new SettingsWindow
        #settings_window.mainloop()  # Start the settings window's main loop


if __name__ == "__main__":
    app = HomeWindow()
    app.mainloop()