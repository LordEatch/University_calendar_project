from platformdirs import user_config_dir
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar"] # If modifying these scopes, delete the file token.json.

def main():
  service = None

  # WARNING NEED TO UPDATE THIS SO THAT IT TAKES A USER AS AN ARGUMENT TO ALLOW MULTIPLE USERS.
  def get_user_credentials():
    """Get the credentials needed to manipulate a user's calendar."""

    APP_NAME = "University_calendar_project"

    app_config_directory_path = user_config_dir(appname=APP_NAME, appauthor=False) # Get the OS-specific path of the app in the config directory.

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time. It is stored in the OS' default config directory so that sensitive
    # keys are not added to the git.
    creds = None

    user_signed_in_token_json_path = os.path.join(app_config_directory_path, "token.json")
    if os.path.exists(user_signed_in_token_json_path):
      creds = Credentials.from_authorized_user_file(user_signed_in_token_json_path, SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        credentials_path = os.getenv("University_calendar_project_google_calendar_api_credentials_path")
        flow = InstalledAppFlow.from_client_secrets_file(
            credentials_path, SCOPES
        )
        creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open(user_signed_in_token_json_path, "w") as token:
        token.write(creds.to_json())
    
    return creds

  def add_event():
    event = {
          'summary': 'Sample Event',
          'location': 'University of Glasgow',
          'description': 'A sample event created via the Google Calendar API.',
          'start': {
              'dateTime': '2025-04-07T10:00:00',
              'timeZone': 'Europe/London',
          },
          'end': {
              'dateTime': '2025-04-07T11:00:00',
              'timeZone': 'Europe/London',
          },
      }

    event = service.events().insert(calendarId='primary', body=event).execute()

  service = build("calendar", "v3", credentials=get_user_credentials())

  add_event()

if __name__ == "__main__":
  main()