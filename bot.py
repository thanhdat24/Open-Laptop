from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import requests
import os

TOKEN = "7834270003:AAGiLVUPAeCcjKpUgbXT3SLyfgTBoNxw4v0"
WAKE_SERVER = os.getenv("WAKE_SERVER", "https://open-laptop-production.up.railway.app/wake")


app = Application.builder().token(TOKEN).build()

async def wake(update: Update, context: CallbackContext) -> None:
    try:
        response = requests.get(WAKE_SERVER)
        await update.message.reply_text(f"🔹 Gửi lệnh đến: {WAKE_SERVER}\n\n{response.text}")
    except Exception as e:
        await update.message.reply_text(f"❌ Lỗi khi gửi lệnh: {e}")

app.add_handler(CommandHandler("wake", wake))

if __name__ == '__main__':
    print(f"🤖 Bot đang chạy trên Railway...\n🔹 Wake Server: {WAKE_SERVER}")
    app.run_polling()
