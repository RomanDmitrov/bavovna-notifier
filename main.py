from fastapi import FastAPI
from schemas import BookingNotification
from bot import send_telegram_message

app = FastAPI()


def build_message_text(data: BookingNotification) -> str:
    """
    Формирует текст уведомления в зависимости от типа заявки.
    """
    if data.request_type == "booking":
        text = (
            f"<b>🎉 Нова заявка на бронювання</b>\n\n"
            f"<b>Ім'я:</b> {data.name}\n"
            f"<b>Email:</b> {data.email or '—'}\n"
            f"<b>Телефон:</b> {data.phone or '—'}\n"
            f"<b>Telegram:</b> {data.telegram or '—'}\n"
            f"<b>Дата події:</b> {data.event_date or '—'}\n"
            f"<b>Тип івенту:</b> {data.event_type or '—'}\n"
            f"<b>Кількість гостей:</b> {data.guests_count or '—'}\n"
            f"<b>Бюджет:</b> {data.budget or '—'}\n"
            f"<b>Повідомлення:</b> {data.message or '—'}"
        )
    else:  # partnership
        text = (
            f"<b>🤝 Нова заявка на партнерство</b>\n\n"
            f"<b>Ім'я/компанія:</b> {data.name}\n"
            f"<b>Email:</b> {data.email or '—'}\n"
            f"<b>Телефон:</b> {data.phone or '—'}\n"
            f"<b>Telegram:</b> {data.telegram or '—'}\n"
            f"<b>Тип співпраці:</b> {data.cooperation_type or '—'}\n"
            f"<b>Повідомлення:</b> {data.message or '—'}"
        )
    return text


@app.post("/notify")
async def notify(data: BookingNotification):
    text = build_message_text(data)
    success = await send_telegram_message(text)
    return {"ok": success}


@app.get("/")
async def health_check():
    return {"status": "bavovna-notifier is running"}