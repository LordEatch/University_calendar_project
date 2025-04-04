import os
import file_download

def main() -> None:
    MOODLE_CALENDAR_URL: str = "https://moodle.gla.ac.uk/calendar/export_execute.php?userid=287433&authtoken=98b8a04f638b0916b19f18e1431e6b58311df1b4&preset_what=all&preset_time=recentupcoming"
    TEMPORARY_DIRECTORY_NAME: str = "temporary"
    MOODLE_CALENDAR_FILENAME: str = "moodle_calendar.ics"

    os.makedirs(TEMPORARY_DIRECTORY_NAME, exist_ok=True) # Ensure that the temporary folder exists.

    # Download the Moodle calendar to the temporary folder.
    moodle_calendar_path: str = os.path.join(TEMPORARY_DIRECTORY_NAME, MOODLE_CALENDAR_FILENAME)
    file_download.download_https_file(MOODLE_CALENDAR_URL, moodle_calendar_path)

    # Need to change this so that the ics file gets downloaded to a different folder to avoid
    # posting my timetable to github. DO NOT stage a future downloaded calendar!

if __name__ == "__main__":
    main()