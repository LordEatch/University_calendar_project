from ics import Calendar
import os
from uni_cal_pro.config import app_temp_directory_path
from uni_cal_pro.file_download import download_https_file
from uni_cal_pro.google_calendar import build_service, event_exists, add_event
import uni_cal_pro.gui.window as gui_window

TEST = "https://moodle.gla.ac.uk/calendar/export_execute.php?userid=287433&authtoken=98b8a04f638b0916b19f18e1431e6b58311df1b4&preset_what=all&preset_time=recentupcoming"


def main():
    def download_moodle_calendar(moodle_calendar_url):
        """Download a file at the url download_moodle_calendar and store it in the app's temporary directory.
        
        Return the path of the file."""

        # In future change MOODLE_CALENDAR_FILENAME to include the app name to make the file more recognisable.
        MOODLE_CALENDAR_FILENAME = "moodle_calendar.ics"

        # Download the Moodle calendar to the app's temp folder.
        moodle_calendar_path = os.path.join(app_temp_directory_path, MOODLE_CALENDAR_FILENAME)
        download_https_file(moodle_calendar_url, moodle_calendar_path)

        # Return the path that the file was downloaded to.
        return moodle_calendar_path

    def get_moodle_calendar_events(moodle_calendar_path):
        with open(moodle_calendar_path) as moodle_calendar:
            text = moodle_calendar.read()

        calendar = Calendar(text)

        return calendar.events
        
    def add_events_to_google_calendar(service, calendar_id, events):
        """Add a list of events to Google Calendar."""

        event_tally = 0

        for event in events:
            # Check if the event already exists.
            if not event_exists(service, calendar_id, event):
                add_event(service, calendar_id, event)
                event_tally += 1
            
        print(f"{event_tally} events added to Google Calendar.")

    # Download and get all events from the Moodle calendar.
    moodle_calendar_path = download_moodle_calendar(TEST)
    events = get_moodle_calendar_events(moodle_calendar_path)

    # Connect to the Google Calendar API.
    service = build_service()

    # Add all of the Moodle calendar events to Google Calendar.
    add_events_to_google_calendar(service, "7a26e32ba78d04c90e76e231e21ee6ceffe3da91a80f049da72475522cf50ff2@group.calendar.google.com", events)

    gui_window.main()

if __name__ == "__main__":
    main()