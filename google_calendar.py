import os.path
from config import app_config_directory_path
import arrow

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ["https://www.googleapis.com/auth/calendar"] # If modifying these scopes, delete the file token.json in the config directory.


def build_service():
  # WARNING NEED TO UPDATE THIS SO THAT IT TAKES A USER AS AN ARGUMENT TO ALLOW MULTIPLE USERS.
  def get_user_credentials():
    """Get the credentials needed to manipulate a user's calendar."""

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

  return build("calendar", "v3", credentials=get_user_credentials())

def add_event(service, calendar_id, event):
  new_event = {
        "summary": event.name,
        "location": event.location,
        "description": event.description,
        "start": {
            "dateTime": event.begin.isoformat(),
        },
        "end": {
            "dateTime": event.end.isoformat(),
        },
    }
  
  print("Attempting to add the following event to Google Calendar:")
  print(new_event)
  new_event = service.events().insert(calendarId=calendar_id, body=new_event).execute()
  print("Event successfully added.")