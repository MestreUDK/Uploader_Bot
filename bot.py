from telegram.ext import ApplicationBuilder, CommandHandler
from config import BOT_TOKEN
from handlers.common import start
from handlers.download import baixar

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("download", baixar))
    app.run_polling()

if __name__ == "__main__":
    main()