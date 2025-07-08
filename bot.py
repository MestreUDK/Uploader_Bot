# bot.py

from telegram.ext import ApplicationBuilder, CommandHandler
from config import BOT_TOKEN
from handlers.common import start
from handlers.download import baixar, avancado

import threading
from flask import Flask

# 🔹 Servidor web fictício para satisfazer o Render
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return 'Uploader bot está rodando!'

def run_web():
    web_app.run(host="0.0.0.0", port=10000)

def main():
    # 🔹 Inicia o web server em uma thread separada
    threading.Thread(target=run_web).start()

    # 🔹 Inicia o bot normalmente com polling
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("download", baixar))
    app.add_handler(CommandHandler("avancado", avancado))
    app.run_polling()

if __name__ == "__main__":
    main()

