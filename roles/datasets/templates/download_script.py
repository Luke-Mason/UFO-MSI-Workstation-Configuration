# download_script.py

import hashlib
import requests
import os
import sys
import hashlib
import os.path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Command-line arguments
creds_path = sys.argv[1]
download_path = sys.argv[2]
downloaded_filename = sys.argv[3]

# Path to the file on Google Drive
file_id = 'your_file_id_here'

creds = Credentials.from_authorized_user_file(creds_path, ['https://www.googleapis.com/auth/drive.readonly'])
service = build('drive', 'v3', credentials=creds)

request = service.files().get_media(fileId=file_id)
media = request.execute()

# Check if the file already exists
output_file_path = os.path.join(download_path, downloaded_filename)
if os.path.isfile(output_file_path):
    print(f"File {downloaded_filename} already exists.")
    exit(0)

try:
    # Save the downloaded content to a file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(media)

    print(f"File downloaded and saved to {output_file_path}")
    exit(0)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    exit(1)
