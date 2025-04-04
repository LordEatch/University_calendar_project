from requests import get
from requests.auth import HTTPBasicAuth

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
        # Save the file.
        with open(download_file_location, 'wb') as file:
            file.write(response.content)
        print(f'{download_file_location} downloaded successfully!')
    else:
        print(f'Failed to download the file. Status code: {response.status_code}')