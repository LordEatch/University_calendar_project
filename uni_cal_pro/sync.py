from uni_cal_pro.google_calendar import build_service, add_events
from uni_cal_pro.moodle import get_moodle_calendar_events

# WARNING change this to also have a google calendar token as a parameter.
def sync_moodle_to_google_calendar(moodle_calendar_url):
    # Download and get all events from the Moodle calendar.
    events = get_moodle_calendar_events(moodle_calendar_url)

    # Connect to the Google Calendar API.
    service = build_service()

    # Add all of the Moodle calendar events to Google Calendar.
    add_events(service, "7a26e32ba78d04c90e76e231e21ee6ceffe3da91a80f049da72475522cf50ff2@group.calendar.google.com", events)