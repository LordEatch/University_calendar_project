from platformdirs import user_config_dir
from tempfile import gettempdir
import os

APP_NAME = "University_calendar_project"

# Get the OS-specific path of the config directory for this app.
app_config_directory_path: str = user_config_dir(appname=APP_NAME, appauthor=False)

# Get the OS-specific path of the temp directory for this app.
temp_directory_path: str = gettempdir()
app_temp_directory_path: str = os.path.join(temp_directory_path, APP_NAME)