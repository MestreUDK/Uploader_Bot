# handlers/common.py

"""Comandos básicos do Uploader Bot."""

from telegram import Update
from telegram.ext import ContextTypes

from utils.restrict import restricted


@restricted
async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Apresenta as principais funções do bot."""
    if not update.message:
        return

    await update.message.reply_text(
        "👋 Bem-vindo ao Uploader Bot!\n\n"
        "📥 Use /download para enviar uma lista de links.\n"
        "📄 Também será possível enviar um arquivo .txt.\n"
        "🎬 Links MP4, MKV e M3U8 serão aceitos.\n"
        "⚙️ Os vídeos poderão ser enviados no formato original "
        "ou otimizados antes do upload."
    )