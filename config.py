from platformdirs import user_config_dir
from tempfile import gettempdir
import os

# NOTE All of the code below will execute whenever this file is ran but also when it is imported (which is intentional).

APP_NAME = "University_calendar_project"

# Get the OS-specific path of the config directory for this app.
app_config_directory_path: str = user_config_dir(appname=APP_NAME, appauthor=False)

# Get the OS-specific path of the temp directory for this app.
temp_directory_path: str = gettempdir()
app_temp_directory_path: str = os.path.join(temp_directory_path, APP_NAME)

# Create directories at these paths if they don't already exist to allow the rest of the app to put files in them without errors.
os.makedirs(app_config_directory_path, exist_ok=True)
os.makedirs(app_temp_directory_path, exist_ok=True)