from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional, Literal


class Settings(BaseSettings):
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI Lambda Test Deploy"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "FastAPI application for AWS Lambda deployment"

    # CORS Settings
    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    # Environment
    ENVIRONMENT: Literal["development", "staging", "production"] = "development"
    DEBUG: bool = True

    # AWS Settings (for when you deploy to Lambda)
    AWS_REGION: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )


@lru_cache()
def get_settings() -> Settings:
    """
    Creates a cached instance of settings.
    Use this function to get settings throughout the app.
    """
    return Settings()


# Create a settings instance
settings = get_settings()
