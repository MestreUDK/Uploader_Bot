# bot.py

from telegram.ext import ApplicationBuilder, CommandHandler
from config import BOT_TOKEN, RENDER_EXTERNAL_URL
from handlers.common import start
from handlers.download import baixar, avancado
from flask import Flask, request
from telegram import Update

# 🔹 Servidor Flask que receberá o webhook
web_app = Flask(__name__)
telegram_app = ApplicationBuilder().token(BOT_TOKEN).build()

# 🔹 Rota para o Telegram enviar as atualizações (webhook)
@web_app.route(f"/{BOT_TOKEN}", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.process_update(update)
    return "ok"

# 🔹 Rota padrão para teste
@web_app.route('/')
def home():
    return 'Uploader bot rodando com Webhook!'

def main():
    # Adiciona os comandos
    telegram_app.add_handler(CommandHandler("start", start))
    telegram_app.add_handler(CommandHandler("download", baixar))
    telegram_app.add_handler(CommandHandler("avancado", avancado))

    # 🔹 Inicia o webhook
    telegram_app.run_webhook(
        listen="0.0.0.0",
        port=10000,
        webhook_url=f"{RENDER_EXTERNAL_URL}/{BOT_TOKEN}",
        web_app=web_app,
    )

if __name__ == "__main__":
    main()