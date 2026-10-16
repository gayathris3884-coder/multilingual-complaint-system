"""Application settings and configuration."""

import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Multilingual Complaint System"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./complaints.db")
    DEBUG: bool = True

    class Config:
        case_sensitive = True
        env_file = ".env"
        extra = "ignore"


settings = Settings()
