from fastapi import HTTPException, APIRouter

from app.schemas.google_slide_schema import PresentationResponse, SlideRequest
from app.services.google_slide_service import create_presentation, add_ai_generated_slides, add_ai_generated_slides

router = APIRouter()

@router.post("/create-presentation")
async def create_presentation_route() -> PresentationResponse:
    try:
        presentation_id = create_presentation()

        if presentation_id:
            return PresentationResponse(message="Presentation created successfully", presentation_id=presentation_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@router.post("/add-slide/{presentation_id}")
async def add_slide_route(slide_request: SlideRequest):
    success = add_ai_generated_slides(slide_request.presentation_id, slide_request.subject, slide_request.num_slides)

    if success:
        return {"message": "Slide added successfully", "presentation_id": slide_request.presentation_id}
    else:
        raise HTTPException(status_code=500, detail="An error occurred while adding the slide")
