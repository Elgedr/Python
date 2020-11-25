from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'A2:E'


def get_links_from_spreadsheet(id: str, token: str) -> list:
    """Should get a list of strings from the first column of a Google Spreadsheet with the given ID."""
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token):
        with open(token, 'rb') as tok:
            creds = pickle.load(tok)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                token, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token, 'wb') as tok:
            pickle.dump(creds, tok)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=id,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    res = []

    if not values:
        print('No data found.')
    else:
        for row in values:
            res.append(row[0])
    return res


def get_links_from_playlist(link: str, developer_key: str) -> list:
    """Should get a list of links to songs in the Youtube playlist with the given address."""
    return []
