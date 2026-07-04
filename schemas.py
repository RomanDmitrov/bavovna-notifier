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
    event_date: Optional[str] = None
    message: Optional[str] = None

    # Поля только для booking (заявка на бронювання)
    event_type: Optional[str] = None  # Тип івенту
    guests_count: Optional[int] = None  # Кількість гостей
    budget: Optional[int] = None  # Бюджет

    # Поле только для partnership (заявка на партнерство)
    cooperation_type: Optional[str] = None  # Тип співпраці