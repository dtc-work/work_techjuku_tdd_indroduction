from os import getenv

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_PATH: str = "/api/v1"
    # LOG LEVEL
    LOG_LEVEL_INFO: str = "APP_INFO"
    LOG_LEVEL_ERROR: str = "APP_ERROR"

    class Config:
        case_sensitive = True


settings = Settings()
