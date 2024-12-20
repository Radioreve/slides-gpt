from fastapi import HTTPException, APIRouter

from app.schemas.google_slide_schema import PresentationResponse
from app.services.google_slide_service import create_presentation

router = APIRouter()

@router.post("/create-presentation")
async def create_presentation_route() -> PresentationResponse:
    try:
        presentation_id = create_presentation()

        if presentation_id:
            return PresentationResponse(message="Presentation created successfully", presentation_id=presentation_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

