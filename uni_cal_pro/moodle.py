from requests import get
from requests.auth import HTTPBasicAuth
import os

from ics import Calendar

from uni_cal_pro.config import app_temp_directory_path
from uni_cal_pro.file_download import download_https_file


def get_moodle_calendar_events(moodle_calendar_url):
    """Return a list of events from an ics file endpoint."""

    def download_temporary_file(file_url, new_file_name):
        """Download a file at the url file_url and store it in the app's temporary directory.
        
        Return the path of the file."""

        def download_https_file(file_url, download_file_location, credentials=None):
            """Download a file from an endpoint at file_url. Store the downloaded file locally at download_file_location. Optionally pass credentials: a string tuple (username, password) for a password-protected endpoint.
            
            Only use this function to download files from endpoints over HTTPS and not HTTP as a plaintext password is passed."""

            if credentials == None:
                print(f'Attemping to download, using no credentials, the file at: {file_url}')
                response = get(file_url)
            else:
                print(f'Attemping to download, using the given username and password, the file at: {file_url}')
                username = credentials[0]
                password = credentials[1]
                response = get(file_url, auth=HTTPBasicAuth(username, password)) # Make a GET request with authentication.

            if response.status_code == 200: # If the request was successful...
                try:
                    # Save the file.
                    with open(download_file_location, 'wb') as file:
                        file.write(response.content)
                    print(f'{download_file_location} downloaded successfully!')
                except:
                    print(f"ERROR. Could not save downloaded file to {download_file_location}. Does the path contain an incorrect or missing directory?")
            else:
                print(f'Failed to download the file. Status code: {response.status_code}')


        # Download the Moodle calendar to the app's temp folder.
        temp_file_path = os.path.join(app_temp_directory_path, new_file_name)
        download_https_file(file_url, temp_file_path)

        # Return the path that the file was downloaded to.
        return temp_file_path


    moodle_calendar_path = download_temporary_file(moodle_calendar_url, "moodle_calendar.ics")

    with open(moodle_calendar_path) as moodle_calendar:
        text = moodle_calendar.read()

    calendar = Calendar(text)

    return calendar.events