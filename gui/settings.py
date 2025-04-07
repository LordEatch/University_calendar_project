import tkinter as tk
from tkinter import ttk

class SettingsWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Settings")
        self.geometry("500x450")
        self.configure(padx=20, pady=20)
        self.style = ttk.Style(self)
        self.style.theme_use("clam")  # Use a clean ttk theme

        self.create_widgets()

    def create_widgets(self):
        font = ("Segoe UI", 10)

        # Main vertical frame
        main_frame = ttk.Frame(self)
        main_frame.grid(column=0, row=0, sticky="nsew")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Moodle calendar URL
        ttk.Label(main_frame, text="Moodle calendar URL:", font=font).grid(sticky="w", pady=(0, 5))
        self.moodle_url_entry = ttk.Entry(main_frame, font=font)
        self.moodle_url_entry.grid(sticky="ew", pady=(0, 15))

        # Moodle event filters
        ttk.Label(main_frame, text="Moodle event filters:", font=font).grid(sticky="w", pady=(0, 5))
        self.filters_text = tk.Text(main_frame, height=6, wrap='word', font=font, relief="solid", bd=1)
        self.filters_text.grid(sticky="nsew", pady=(0, 15))

        # Allow text box to expand vertically
        main_frame.rowconfigure(3, weight=1)
        main_frame.columnconfigure(0, weight=1)

        # Google account buttons
        self.forget_btn = ttk.Button(main_frame, text="Forget Google Account", command=self.forget_account)
        self.forget_btn.grid(sticky="ew", pady=(0, 10))

        self.signin_btn = ttk.Button(main_frame, text="Sign Into New Google Account", command=self.signin_account)
        self.signin_btn.grid(sticky="ew", pady=(0, 20))

        # Save Button
        self.save_btn = ttk.Button(main_frame, text="Save", command=self.save)
        self.save_btn.grid(sticky="ew", pady=(0, 10))

        # Back Button
        self.back_btn = ttk.Button(main_frame, text="← Back", command=self.go_back)
        self.back_btn.grid(sticky="ew")

    # Placeholder methods
    def forget_account(self):
        print("Forgot Google account (placeholder)")

    def signin_account(self):
        print("Sign into Google account (placeholder)")

    def save(self):
        print("Save pressed (placeholder)")

    def go_back(self):
        print("Back pressed (placeholder)")
        self.destroy()  # Close the window

if __name__ == "__main__":
    app = SettingsWindow()
    app.mainloop()