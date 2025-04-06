from ics import Calendar
from tempfile import gettempdir
import os
from file_download import download_https_file
from google_calendar import build_service, add_event


TEST = "https://moodle.gla.ac.uk/calendar/export_execute.php?userid=287433&authtoken=98b8a04f638b0916b19f18e1431e6b58311df1b4&preset_what=all&preset_time=recentupcoming"


def main() -> None:
    def download_moodle_calendar(moodle_calendar_url):
        """Download a file at the url download_moodle_calendar and store it in the OS' default temporary directory for apps.
        
        Return the path of the file."""

        # In future change MOODLE_CALENDAR_FILENAME to include the app name to make the file more recognisable.
        MOODLE_CALENDAR_FILENAME: str = "moodle_calendar.ics"

        # Download the Moodle calendar to the OS' default temporary directory for apps.
        temporary_directory_path: str = gettempdir()
        moodle_calendar_path: str = os.path.join(temporary_directory_path, MOODLE_CALENDAR_FILENAME)
        download_https_file(moodle_calendar_url, moodle_calendar_path)

        # Return the path that the file was downloaded to.
        return moodle_calendar_path

    def get_moodle_calendar_events(moodle_calendar_path):
        with open(moodle_calendar_path) as moodle_calendar:
            text: str = moodle_calendar.read()

        calendar: Calendar = Calendar(text)

        return calendar.events
        

    # Download and get all events from the Moodle calendar.
    moodle_calendar_path: str = download_moodle_calendar(TEST)
    # events TYPE???
    events = get_moodle_calendar_events(moodle_calendar_path)

    # Connect to the Google Calendar API.
    service = build_service()

    # Add all of the Moodle calendar events to Google Calendar.
    
    

    # Also to simplify setup, the url should be entered in a UI and stored either as an
    # environment variable or in a json file in the config folder (see google_calendar.py).

if __name__ == "__main__":
    main()