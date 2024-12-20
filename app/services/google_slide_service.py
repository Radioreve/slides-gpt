from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/presentations']

def authenticate_google_api():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES
    )
    creds = flow.run_local_server(port=0)

    return creds

def create_presentation():
    try:
        creds = authenticate_google_api()
        service = build('slides', 'v1', credentials=creds)

        presentation = service.presentations().create().execute()
        presentation_id = presentation['presentationId']

        return presentation_id
    except HttpError as err:
        print(f"An error occurred: {err}")
        return None