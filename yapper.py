from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CommandHandler, CallbackContext

TOKEN = "7985326913:AAH8vmElP-6ljmKB6vv5yQgvfgTzHRzvVKc"
CHAT_ID = -1002375370559  # ID вашей группы

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Бот запущен! Всё, что вы мне напишите в ЛС, я отправлю в этот чат.")

async def forward_message(update: Update, context: CallbackContext) -> None:
    """Пересылает сообщение в групповой чат"""
    await context.bot.send_message(chat_id=CHAT_ID, text=f"{update.message.from_user.first_name}: {update.message.text}")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()