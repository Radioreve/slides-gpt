from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

class TextSummary(BaseModel):
    summary: str
