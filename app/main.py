from core.config import settings
from fastapi import FastAPI

app = FastAPI(title=settings.app_title, description=settings.app_description)
