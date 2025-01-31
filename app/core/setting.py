from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    GROQ_API_KEY: str

    class Config:
        env_file = ".env"

# Instantiate the settings
settings = Settings()
