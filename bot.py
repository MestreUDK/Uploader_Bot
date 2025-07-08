# bot.py

from telegram.ext import ApplicationBuilder, CommandHandler
from config import BOT_TOKEN, RENDER_EXTERNAL_URL
from handlers.common import start
from handlers.download import baixar, avancado

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("download", baixar))
    app.add_handler(CommandHandler("avancado", avancado))

    # Webhook
    app.run_webhook(
        listen="0.0.0.0",
        port=10000,
        webhook_url=f"{RENDER_EXTERNAL_URL}/{BOT_TOKEN}"
    )

if __name__ == "__main__":
    main()