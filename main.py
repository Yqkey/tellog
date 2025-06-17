from telethon import TelegramClient, events
from flask import Flask
import threading
import os

# Загружаем переменные окружения
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

# Указываем файл сессии
client = TelegramClient("user", api_id, api_hash)

# Flask-приложение
app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is running!'

# Обработка входящих сообщений
@client.on(events.NewMessage(incoming=True))  # добавили incoming=True
async def handler(event):
    sender = await event.get_sender()
    name = sender.username if sender.username else sender.first_name
    print(f"[+] New message from {name} ({event.sender_id}): {event.text}")

# Запуск Flask в отдельном потоке
def start_flask():
    app.run(host="0.0.0.0", port=10000)

# Запуск Telethon
def start_telethon():
    print("[*] Starting Telethon...")
    with client:
        print("[+] Telethon connected.")
        client.run_until_disconnected()

# Основной запуск
if __name__ == "__main__":
    threading.Thread(target=start_flask).start()
    start_telethon()
