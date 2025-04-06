from ics import Calendar
import os
from config import app_temp_directory_path
from file_download import download_https_file
from google_calendar import build_service, add_event


TEST: str = "https://moodle.gla.ac.uk/calendar/export_execute.php?userid=287433&authtoken=98b8a04f638b0916b19f18e1431e6b58311df1b4&preset_what=all&preset_time=recentupcoming"


def main() -> None:
    def download_moodle_calendar(moodle_calendar_url: str):
        """Download a file at the url download_moodle_calendar and store it in the app's temporary directory.
        
        Return the path of the file."""

        # In future change MOODLE_CALENDAR_FILENAME to include the app name to make the file more recognisable.
        MOODLE_CALENDAR_FILENAME: str = "moodle_calendar.ics"

        # Download the Moodle calendar to the app's temp folder.
        moodle_calendar_path: str = os.path.join(app_temp_directory_path, MOODLE_CALENDAR_FILENAME)
        download_https_file(moodle_calendar_url, moodle_calendar_path)

        # Return the path that the file was downloaded to.
        return moodle_calendar_path

    def get_moodle_calendar_events(moodle_calendar_path: str):
        with open(moodle_calendar_path) as moodle_calendar:
            text: str = moodle_calendar.read()

        calendar: Calendar = Calendar(text)

        return calendar.events
        
    def add_events_to_google_calendar(service, calendar_id, events):
        for event in events:
            add_event(service, calendar_id, event)

    # Download and get all events from the Moodle calendar.
    moodle_calendar_path: str = download_moodle_calendar(TEST)
    events = get_moodle_calendar_events(moodle_calendar_path) # TYPE???

    # Connect to the Google Calendar API.
    service = build_service() # TYPE???

    # Add all of the Moodle calendar events to Google Calendar.
    add_events_to_google_calendar(service, "7a26e32ba78d04c90e76e231e21ee6ceffe3da91a80f049da72475522cf50ff2@group.calendar.google.com", events)
    

    # Also to simplify setup, the url should be entered in a UI and stored either as an
    # environment variable or in a json file in the config folder (see google_calendar.py).

if __name__ == "__main__":
    main()