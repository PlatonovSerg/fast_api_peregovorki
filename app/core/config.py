# core/config.py
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    app_title: str = "Бронирование переговорок"
    app_description: str = "Приложение для бронирования переговорок"
    database_url: str

    class Config:
        env_file = ".env"


settings = Settings()
