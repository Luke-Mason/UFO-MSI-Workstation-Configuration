# download_script.py

import hashlib
import requests
import os
import sys
import hashlib
import os.path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Command-line arguments
creds_path = sys.argv[1]
token_path = sys.argv[2]
output_file_path = sys.argv[3]
file_id = sys.argv[4]

# Path to the file on Google Drive
SCOPES =  ['https://www.googleapis.com/auth/drive.readonly']

def main():
    creds = None

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                creds_path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)
        print(f"Downloading file {file_id} from Google Drive...")
        request = service.files().get_media(fileId=file_id)
        media = request.execute()
        print(f"file {file_id} downloaded.")

        # Check if the file already exists
        if os.path.isfile(output_file_path):
            print(f"File {output_file_path} already exists.")
            exit(0)

        try:
            # Save the downloaded content to a file
            with open(output_file_path, 'wb') as output_file:
                output_file.write(media)

            print(f"{file_id} downloaded and saved to {output_file_path}")
            exit(0)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            exit(1)

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')




if __name__ == '__main__':
    main()