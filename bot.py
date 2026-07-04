import os
import httpx
from dotenv import load_dotenv


load_dotenv()


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_IDS = os.getenv("TELEGRAM_CHAT_IDS", '').split(',')

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"


async def send_telegram_message(text: str) -> bool:
    """
    Отправляет текстовое сообщение всем organizers из TELEGRAM_CHAT_IDS.
    Возвращает True, если все сообщения ушли успешно.
    """
    success = True

    async with httpx.AsyncClient() as client:
        for chat_id in TELEGRAM_CHAT_IDS:
            payload = {
                "chat_id": chat_id.strip(),
                "text": text,
                "parse_mode": "HTML",
            }
            response = await client.post(TELEGRAM_API_URL, json=payload)
            if response.status_code != 200:
                success = False
                print(f"Ошибка для chat_id={chat_id}: {response.status_code} {response.text}")

    return success