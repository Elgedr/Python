"""API."""
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
import os
import googleapiclient.discovery
import googleapiclient.errors
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'A:A'


# def get_links_from_spreadsheet(id: str, token: str) -> list:
#     """Should get a list of strings from the first column of a Google Spreadsheet with the given ID."""
#     creds = None
#     # The file token.pickle stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists(token):
#         with open(token, 'rb') as tok:
#             creds = pickle.load(tok)
#     # # If there are no (valid) credentials available, let the user log in.
#     # if not creds or not creds.valid:
#     #     if creds and creds.expired and creds.refresh_token:
#     #         creds.refresh(Request())
#     #     else:
#     #         flow = InstalledAppFlow.from_client_secrets_file(
#     #             token, SCOPES)
#     #         creds = flow.run_local_server(port=0)
#     #     # Save the credentials for the next run
#     #     with open(token, 'wb') as tok:
#     #         pickle.dump(creds, tok)
#
#     service = build('sheets', 'v4', credentials=creds)
#
#     # Call the Sheets API
#     sheet = service.spreadsheets()
#     result = sheet.values().get(spreadsheetId=id,
#                                 range=SAMPLE_RANGE_NAME).execute()
#     values = result.get('values', [])  # returns an empty list if element does not exist
#     res = []
#     if values == []:
#         print('No data found.')
#     else:
#         for row in values:  # VALUES RETURNS A LIST OF LISTS [[VK.COM],[FACEBOOK.COM],[INSTAGRAM.COM]]
#             res.append(row[0])
#     return res


def get_links_from_playlist() -> list:
    """Should get a list of links to songs in the Youtube playlist with the given address."""
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    # id = link.split('=')[1]
    id = 'PLg5SS_4L6LYu9g-CJ_SwepWE1lAH4xb4o'

    # Get credentials and create an API clientt
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey='AIzaSyA2jR2UH-liBeCVqKGdXo9Ah5xzw0UKtY0')

    request = youtube.playlistItems().list(part='contentDetails', playlistId=id, maxResults=50)
    response = request.execute()
    print(response)
    # res = []
    # for itemz in response['items']:
    #     res.append(f'https://www.youtube.com/watch?v={itemz["snippet"]["resourceId"]["videoId"]}&list={id}')
    # return res


print(get_links_from_playlist())