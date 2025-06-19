from telegram import Update
from telegram.ext import ContextTypes
from utils.restrict import restricted

@restricted
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Envie o comando /download <link> para baixar o vídeo.")