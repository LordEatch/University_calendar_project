import uni_cal_pro.gui.window as gui_window
from uni_cal_pro.sync import sync_moodle_to_google_calendar


TEST = "https://moodle.gla.ac.uk/calendar/export_execute.php?userid=287433&authtoken=98b8a04f638b0916b19f18e1431e6b58311df1b4&preset_what=all&preset_time=recentupcoming"


sync_moodle_to_google_calendar(TEST)

# Launch GUI.
gui_window.main()