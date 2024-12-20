import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "null")
    MAX_TOKEN: int = os.getenv("MAX_TOKEN", 100)