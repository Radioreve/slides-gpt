from fastapi import HTTPException, APIRouter

from app.schemas.openai_schema import TextSummary, TextRequest
from app.services.openai_service import generate_text_with_ai

router = APIRouter()


@router.post("/generate-text")
async def generate_text(request: TextRequest) -> TextSummary:
    try:
        summary = generate_text_with_ai(request.text)
        return TextSummary(summary=summary)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la génération de texte par GenAI : {e}")
