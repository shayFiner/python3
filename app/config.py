import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "sqlite:///./equipment.db"

    # Security
    SECRET_KEY: str = "your-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # App
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    APP_NAME: str = "Equipment Management System"
    APP_DESCRIPTION: str = "System for managing equipment, inventory, and tasks"

    class Config:
        env_file = ".env"


settings = Settings()
