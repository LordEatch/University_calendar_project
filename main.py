import os
import file_download

if __name__ == "__main__":
    moodle_calendar_url = 'https://moodle.gla.ac.uk/calendar/export_execute.php?userid=287433&authtoken=98b8a04f638b0916b19f18e1431e6b58311df1b4&preset_what=all&preset_time=recentupcoming'

    # Ensure the temporary folder exists.
    temporary_file_folder_name = 'temporary'
    os.makedirs(temporary_file_folder_name, exist_ok=True)

    # Download the Moodle calendar.
    moodle_calendar_file_name = 'moodle_calendar.ics'
    moodle_calendar_path = os.path.join(temporary_file_folder_name, moodle_calendar_file_name)
    file_download.download_https_file(moodle_calendar_url, moodle_calendar_path)