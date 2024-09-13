from app.core.config import settings
from fastapi import FastAPI
from app.api.meeting_room import router

app = FastAPI(title=settings.app_title, description=settings.app_description)

app.include_router(router)
