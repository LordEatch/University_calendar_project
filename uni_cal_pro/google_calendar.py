import os.path
from datetime import timedelta

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from uni_cal_pro.config import app_config_directory_path


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

# WARNING THIS IS NOT FINAL AS NO EVENT WILL BE ADDED AT THE SAME TIME AS ANOTHER, EVEN IF IT IS DIFFERENT! CHANGE event_exists.
def add_events_to_google_calendar(service, calendar_id, events):
  """Add a list of events to Google Calendar. Do not overwrite/duplicate events existing in the same calendar at the same time."""

  def event_exists(service, calendar_id, event):
    events_result = service.events().list(
        calendarId=calendar_id,
        # Add a time delta to these to allow Google Calendar to search within the window.
        timeMin=(event.begin - timedelta(minutes=1)).isoformat(),
        timeMax=(event.end + timedelta(minutes=1)).isoformat(),
        maxResults=1,
        # singleEvents ensures that recurring events are treated as individual events, rather than a single master event happening once.
        singleEvents=True,
    ).execute()
    events = events_result.get('items', [])

    if events:
      return True
    else:
      return False

  def add_event_to_google_calendar(service, calendar_id, event):
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
    
    try:
      service.events().insert(calendarId=calendar_id, body=new_event).execute()
    except:
      print("ERROR. Could not add the following event to Google Calendar:")
      print(new_event)


  event_tally = 0

  for event in events:
      # Check if the event already exists.
      if not event_exists(service, calendar_id, event):
          add_event_to_google_calendar(service, calendar_id, event)
          event_tally += 1
      
  print(f"{event_tally} events added to Google Calendar.")