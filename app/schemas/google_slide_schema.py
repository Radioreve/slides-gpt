from pydantic import BaseModel

class PresentationResponse(BaseModel):
    message: str
    presentation_id: str
