import os
import logging
import telegram
import asyncio
from dotenv import load_dotenv
# Загрузка переменных окружения из .env файла
load_dotenv()
# Настройка логирования
logging.basicConfig(level=logging.DEBUG)
async def send_telegram_message(token, chat_id, message, parse_mode="Markdown"):
    try:
        bot = telegram.Bot(token=token)
        await bot.send_message(chat_id=chat_id, text=message, parse_mode=parse_mode)
        logging.info(f'Сообщение "{message}" отправлено в чат {chat_id}')
    except Exception as e:
        logging.error(f"Ошибка отправки сообщения в чат {chat_id}: {e}")
        raise
# Тестируем отправку прямо тут
if __name__ == "__main__":
    load_dotenv()
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    YOUR_PERSONAL_CHAT_ID = os.getenv("YOUR_PERSONAL_CHAT_ID")
    message = "Привет, у тебя появился новый заказ! Посмотри на сайте"
    asyncio.run(send_telegram_message(TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID, message))