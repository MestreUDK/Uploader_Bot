# handlers/download.py

from telegram import Update
from telegram.ext import ContextTypes
from utils.restrict import restricted
from modules.baixar_video import baixar_e_enviar_video

@restricted
async def baixar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("❗ Envie o link do vídeo.\nExemplo: /download https://site.com/video.mp4")

    url = context.args[0]
    await baixar_e_enviar_video(update, context, url)