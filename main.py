import os
from ics import Calendar
from tempfile import gettempdir
import file_download

def main() -> None:
    MOODLE_CALENDAR_URL: str = "https://moodle.gla.ac.uk/calendar/export_execute.php?userid=287433&authtoken=98b8a04f638b0916b19f18e1431e6b58311df1b4&preset_what=all&preset_time=recentupcoming"
    MOODLE_CALENDAR_FILENAME: str = "moodle_calendar.ics"

    def get_moodle_events(moodle_calendar_path):
        with open(moodle_calendar_path) as moodle_calendar:
            text: str = moodle_calendar.read()

        calendar: Calendar = Calendar(text)

        return calendar.events
        
    temporary_directory_path: str = gettempdir()

    # Download the Moodle calendar to the temporary folder.
    moodle_calendar_path: str = os.path.join(temporary_directory_path, MOODLE_CALENDAR_FILENAME)
    # Test.
    print("Test: " + moodle_calendar_path)
    file_download.download_https_file(MOODLE_CALENDAR_URL, moodle_calendar_path)

    # Get all events from the calendar.
    events = get_moodle_events(moodle_calendar_path)

    # Test.
    for e in events:
        print(e.name)


    # Need to change this so that the ics file gets downloaded to a different folder to avoid
    # posting my timetable to github. DO NOT stage a future downloaded calendar!

    # Also to simplify setup, the url should be entered in a UI and stored either as an
    # environment variable or in a json file in the config folder (see google_calendar.py).

if __name__ == "__main__":
    main()