from uni_cal_pro.google_calendar import build_service, event_exists, add_event
import uni_cal_pro.gui.window as gui_window
from uni_cal_pro.moodle import get_moodle_calendar_events


TEST = "https://moodle.gla.ac.uk/calendar/export_execute.php?userid=287433&authtoken=98b8a04f638b0916b19f18e1431e6b58311df1b4&preset_what=all&preset_time=recentupcoming"


def main():
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
    events = get_moodle_calendar_events(TEST)

    # Connect to the Google Calendar API.
    service = build_service()

    # Add all of the Moodle calendar events to Google Calendar.
    add_events_to_google_calendar(service, "7a26e32ba78d04c90e76e231e21ee6ceffe3da91a80f049da72475522cf50ff2@group.calendar.google.com", events)

    gui_window.main()

if __name__ == "__main__":
    main()