from functools import lru_cache
from typing import List

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Application settings
    app_name: str = "Python API"
    app_description: str = "A Python API built with FastAPI"
    app_version: str = "0.1.0"
    environment: str = Field("development", env="ENVIRONMENT")
    
    # CORS settings
    cors_origins: List[str] = ["*"]
    
    # Database settings
    database_url: str = Field(..., env="DATABASE_URL")
    db_pool_size: int = Field(5, env="DB_POOL_SIZE")
    db_max_overflow: int = Field(10, env="DB_MAX_OVERFLOW")
    
    # API keys and secrets
    api_key: str = Field("", env="API_KEY")
    
    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Return cached settings instance."""
    return Settings()