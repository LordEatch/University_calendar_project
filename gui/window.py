import tkinter as tk
from tkinter import ttk
from ..config import APP_NAME
from pages.moodle import Moodle
from pages.google_calendar import GoogleCalendar

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_NAME)
        self.geometry("800x600")
        
        # Create main container with navigation bar at top and content below.
        main_container = ttk.Frame(self)
        main_container.pack(fill="both", expand=True)
        
        # Navigation bar.
        nav_bar = ttk.Frame(main_container)
        nav_bar.pack(side="top", fill="x", padx=5, pady=5)
        
        # Navigation buttons in the bar
        self.moodle_btn = ttk.Button(nav_bar, text="Moodle", command=lambda: self.show_page(Moodle))
        self.moodle_btn.pack(side="left", padx=5)

        self.google_calendar_btn = ttk.Button(nav_bar, text="Google Calendar", command=lambda: self.show_page(GoogleCalendar))
        self.google_calendar_btn.pack(side="left", padx=5)
        
        # Container for pages below the nav bar
        self.page_container = ttk.Frame(main_container)
        self.page_container.pack(side="top", fill="both", expand=True)
        self.page_container.grid_rowconfigure(0, weight=1)
        self.page_container.grid_columnconfigure(0, weight=1)
        
        # Dictionary to hold all pages
        self.pages = {}
        
        # Create and add all pages to the container
        for PageClass in (Moodle, GoogleCalendar):
            page_name = PageClass.__name__
            page = PageClass(parent=self.page_container, controller=self)
            self.pages[page_name] = page
            page.grid(row=0, column=0, sticky="nsew")
        
        # Show the first page initially
        self.show_page(Moodle)
    
    def show_page(self, PageClass):
        """Show the requested page."""

        page_name = PageClass.__name__
        page = self.pages[page_name]
        page.tkraise()
        
        # Update button states to show current page
        for btn in [self.moodle_btn, self.google_calendar_btn]:
            btn.state(["!disabled"])
        
        if page_name == Moodle.__name__:
            self.moodle_btn.state(["disabled"])
        elif page_name == GoogleCalendar.__name__:
            self.google_calendar_btn.state(["disabled"])

# Run the application
if __name__ == "__main__":
    app = Window()
    app.mainloop()