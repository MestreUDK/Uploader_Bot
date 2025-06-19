import os
import subprocess
from telegram import Update
from telegram.ext import ContextTypes
from utils.restrict import restricted

TEMP_FOLDER = "videos"
os.makedirs(TEMP_FOLDER, exist_ok=True)

HEADERS = [
    '--add-header', 'User-Agent: Mozilla/5.0',
    '--add-header', 'Referer: https://4anime.to'
]

@restricted
async def baixar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("❗ Envie o link do vídeo.\nExemplo: /download https://site.com/video.mp4")

    url = context.args[0]
    filename = "video.mp4"
    output_path = os.path.join(TEMP_FOLDER, filename)

    await update.message.reply_text("🔄 Baixando vídeo...")

    cmd = ["yt-dlp", *HEADERS, "-o", output_path, url]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        return await update.message.reply_text("⚠️ Erro ao baixar o vídeo. Link pode estar expirado ou bloqueado.")

    await update.message.reply_text("📤 Enviando vídeo...")
    try:
        await update.message.reply_video(video=open(output_path, "rb"))
    except Exception as e:
        await update.message.reply_text(f"⚠️ Erro ao enviar o vídeo: {e}")
    finally:
        os.remove(output_path)