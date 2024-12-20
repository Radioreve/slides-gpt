from pydantic import BaseModel

class PresentationResponse(BaseModel):
    message: str
    presentation_id: str

class SlideRequest(BaseModel):
    presentation_id: str
    subject: str
    num_slides: int
