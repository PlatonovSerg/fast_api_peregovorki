from typing import Optional

from pydantic import BaseModel, Field, field_validator


class MeetingRoomCreate(BaseModel):
    name: str = Field(
        ...,
        max_length=100,
    )
    description: Optional[str]

    @field_validator("name")
    def name_validator(cls, value: str):
        if not value:
            raise ValueError("Имя не должно быть пустым")
        return value

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Переговорка номер надцать",
                    "description": "Неведомо существует она или нет не очень"
                    " понятно",
                }
            ]
        },
        "title": "Класс для переговорок",
        "str_max_length": 100,
    }
