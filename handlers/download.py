# handlers/download.py

from telegram import Update
from telegram.ext import ContextTypes
from utils.restrict import restricted
from modules.baixar.baixar_video import baixar_e_enviar_video
from modules.baixar.baixar_avancado import baixar_com_argumentos
from modules.logs.logger import log_erro

@restricted
async def baixar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("❗ Envie o link do vídeo.\nExemplo: /download https://site.com/video.mp4")

    url = context.args[0]

    try:
        await baixar_e_enviar_video(update, context, url)
    except Exception as e:
        await log_erro(update, e, contexto="baixar vídeo no modo automático")
        await update.message.reply_text(
            "⚠️ Erro ao baixar o vídeo no modo automático.\n"
            "Você pode tentar o modo avançado com argumentos:\n"
            "`/avancado [args do yt-dlp] URL`",
            parse_mode="Markdown"
        )

@restricted
async def avancado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text(
            "❗ Use o comando assim:\n"
            "/avancado -f bestvideo+bestaudio https://link"
        )

    args = context.args
    try:
        await baixar_com_argumentos(update, context, args)
    except Exception as e:
        await log_erro(update, e, contexto="baixar vídeo no modo avançado")
        await update.message.reply_text("⚠️ Ocorreu um erro ao tentar baixar no modo avançado.")