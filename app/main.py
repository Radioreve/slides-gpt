from fastapi import FastAPI
from app.routers.openai_routes import router as openai_router

app = FastAPI(title="OpenAI API Interaction")

app.include_router(openai_router, prefix="/openai", tags=["OpenAI"])

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
