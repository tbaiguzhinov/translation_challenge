import os
from dotenv import load_dotenv

from pydantic_settings import BaseSettings


load_dotenv()

class Settings(BaseSettings):
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY")
    MONGODB_URL: str = os.getenv("MONGODB_URL")


settings = Settings()
