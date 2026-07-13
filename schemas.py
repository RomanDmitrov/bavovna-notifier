from pydantic import BaseModel
from typing import Optional


class BookingNotification(BaseModel):
    """
    Данные заявки, которые присылает Django при создании
    нового booking request или partnership request.
    """
    request_type: str
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    telegram: Optional[str] = None
    message: Optional[str] = None

    # Поля только для booking (заявка на бронювання)
    category: Optional[str] = None
    guests: Optional[int] = None
    budget: Optional[str] = None

    # Поле только для partnership (заявка на партнерство)
    partnership_type: Optional[str] = None