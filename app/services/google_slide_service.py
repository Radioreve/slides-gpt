import uuid

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from app.services.openai_service import generate_text_with_ai

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

def add_ai_generated_slides(presentation_id: str, subject: str, num_slides: int):
    try:
        creds = authenticate_google_api()
        service = build('slides', 'v1', credentials=creds)

        slides_content = generate_slide_content(subject, num_slides)

        requests = prepare_slide_requests(slides_content)

        send_slide_requests(service, presentation_id, requests)

        return True
    except HttpError as err:
        print(f"An error occurred: {err}")
        return False


def generate_slide_content(subject: str, num_slides: int) -> list:
    prompt = (
        f"Crée un plan pour une présentation avec {num_slides} diapositives sur le sujet : {subject}. "
        f"Chaque diapositive doit contenir un titre suivi d'un contenu détaillé. "
        f"Insère un retour à la ligne entre le titre et le contenu, et deux retours à la ligne entre les diapositives. "
        f"Assure-toi que les informations soient claires et organisées."
    )

    ai_response = generate_text_with_ai(prompt)

    slides_content = ai_response.split("\n\n\n")
    slides_content = [slide.strip() for slide in slides_content if slide.strip()]

    return slides_content


def prepare_slide_requests(slides_content: list) -> list:
    requests = []

    for i, slide in enumerate(slides_content):
        parts = slide.split("\n\n", 1)
        title = parts[0].strip() if len(parts) > 0 else f"Slide {i + 1}"
        body = parts[1].strip() if len(parts) > 1 else "Contenu généré automatiquement."

        slide_id = str(uuid.uuid4())
        requests.append(create_blank_slide_request(slide_id))

        title_box_id = str(uuid.uuid4())
        requests.append(create_shape_request(slide_id, title_box_id, 100000, 100000, 4000000, 500000))
        requests.append(create_insert_text_request(title_box_id, title))

        body_box_id = str(uuid.uuid4())
        requests.append(create_shape_request(slide_id, body_box_id, 100000, 700000, 4000000, 2000000))
        requests.append(create_insert_text_request(body_box_id, body))

    return requests


def create_shape_request(slide_id: str, object_id: str, x: int, y: int, width: int, height: int) -> dict:
    return {
        'createShape': {
            'objectId': object_id,
            'shapeType': 'TEXT_BOX',
            'elementProperties': {
                'pageObjectId': slide_id,
                'size': {
                    'width': {'magnitude': width, 'unit': 'EMU'},
                    'height': {'magnitude': height, 'unit': 'EMU'}
                },
                'transform': {
                    'scaleX': 1, 'scaleY': 1,
                    'translateX': x, 'translateY': y,
                    'unit': 'EMU'
                }
            }
        }
    }


def create_insert_text_request(object_id: str, text: str) -> dict:
    return {
        'insertText': {
            'objectId': object_id,
            'insertionIndex': 0,
            'text': text
        }
    }


def create_blank_slide_request(slide_id: str) -> dict:
    return {
        'createSlide': {
            'objectId': slide_id,
            'slideLayoutReference': {
                'predefinedLayout': 'BLANK'
            }
        }
    }

def send_slide_requests(service, presentation_id: str, requests: list):
    service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
