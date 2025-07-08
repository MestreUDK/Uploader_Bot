# modules/baixar_avancado.py

import os
import subprocess
from telegram import Update
from telegram.ext import ContextTypes

TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

async def baixar_com_argumentos(update: Update, context: ContextTypes.DEFAULT_TYPE, argumentos: list):
    chat_id = update.effective_chat.id
    nome_arquivo = os.path.join(TEMP_DIR, f"yt_{chat_id}.mp4")

    await update.message.reply_text("🔧 Executando yt-dlp no modo avançado...")

    cmd = ["yt-dlp", "-o", nome_arquivo, *argumentos]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        return await update.message.reply_text("⚠️ Erro ao baixar com os argumentos fornecidos.")

    await update.message.reply_text("📤 Enviando vídeo...")
    try:
        await context.bot.send_video(chat_id=chat_id, video=open(nome_arquivo, 'rb'))
    except Exception as e:
        await update.message.reply_text(f"⚠️ Erro ao enviar: {e}")
    finally:
        if os.path.exists(nome_arquivo):
            os.remove(nome_arquivo)
