from platformdirs import user_config_dir
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

APP_NAME = "University_calendar_project"

def main():
  """Shows basic usage of the Google Calendar API.

  Prints the start and name of the next 10 events on the user's calendar."""

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

  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()
    print("Getting the upcoming 10 events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return

    # Prints the start and name of the next 10 events
    for event in events:
      start = event["start"].get("dateTime", event["start"].get("date"))
      print(start, event["summary"])

  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()