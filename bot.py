"""Ponto de entrada do Uploader Bot."""

import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

from config import BOT_TOKEN
from handlers.common import start
from handlers.download import avancado, baixar


def main() -> None:
    """Inicializa e mantém o bot em execução usando long polling."""
    if not BOT_TOKEN:
        raise RuntimeError(
            "A variável de ambiente BOT_TOKEN não foi configurada."
        )

    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("download", baixar))
    application.add_handler(CommandHandler("avancado", avancado))

    # Inicialização por polling, adequada para bots hospedados na Discloud
    application.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True,
    )


if __name__ == "__main__":
    logging.basicConfig(
        format=(
            "%(asctime)s | %(levelname)s | "
            "%(name)s | %(message)s"
        ),
        level=logging.INFO,
    )

    main()