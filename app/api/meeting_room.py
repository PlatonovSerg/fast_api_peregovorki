from fastapi import APIRouter, HTTPException

from app.crud.meeting_room import create_meeting_room, get_room_id_by_name
from app.schemas.meeting_room import MeetingRoomCreate

router = APIRouter()


@router.post("/meeting_rooms/")
async def create_new_meeting_room(
    meeting_room: MeetingRoomCreate,
):
    room_id = await get_room_id_by_name(meeting_room.name)
    if room_id is not None:
        raise HTTPException(
            status_code=442,
            detail="Переговорка с таким именем уже существует!",
        )
    new_room = await create_meeting_room(meeting_room)
    return new_room
