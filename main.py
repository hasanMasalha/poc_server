from fastapi import FastAPI, Request
from pydantic import BaseModel
from telegram import Bot

app = FastAPI()

TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = Bot(token=TELEGRAM_TOKEN)

class Message(BaseModel):
    chat_id: int
    text: str

@app.post("/send_message/")
async def send_message(message: Message):
    bot.send_message(chat_id=message.chat_id, text=message.text)
    return {"status": "message sent"}

@app.post("/webhook/")
async def webhook(request: Request):
    update = await request.json()
    chat_id = update["message"]["chat"]["id"]
    text = update["message"]["text"]

    # Here you can add your custom logic
    response_text = f"Echo: {text}"

    bot.send_message(chat_id=chat_id, text=response_text)
    return {"status": "ok"}
