# main.py
from telethon import TelegramClient, events
from flask import Flask
import threading
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("user", api_id, api_hash)
app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is running!'

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    print(f"New message from {event.sender_id}: {event.text}")

def start_flask():
    app.run(host="0.0.0.0", port=10000)

def start_telethon():
    with client:
        client.run_until_disconnected()

if __name__ == "__main__":
    threading.Thread(target=start_flask).start()
    start_telethon()
