# modules/baixar_video.py

import aiohttp
import asyncio
import os
from telegram import Update
from telegram.ext import ContextTypes

# Cria a pasta 'temp' se ainda não existir
TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

async def baixar_e_enviar_video(update: Update, context: ContextTypes.DEFAULT_TYPE, url: str):
    chat_id = update.effective_chat.id
    nome_arquivo = os.path.join(TEMP_DIR, f"video_{chat_id}.mp4")

    mensagem = await update.message.reply_text("🔽 Iniciando download...")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resposta:
                tamanho_total = int(resposta.headers.get('Content-Length', 0))
                if resposta.status != 200 or tamanho_total == 0:
                    await mensagem.edit_text("❌ Erro ao acessar o vídeo.")
                    return

                progresso = 0
                bloco = 1024 * 64  # 64KB
                with open(nome_arquivo, 'wb') as com_aberto:
                    async for chunk in resposta.content.iter_chunked(bloco):
                        com_aberto.write(chunk)
                        progresso += len(chunk)
                        porcentagem = int((progresso / tamanho_total) * 100)

                        if porcentagem % 10 == 0:
                            await mensagem.edit_text(f"🔽 Baixando... [{porcentagem}%]")

        await mensagem.edit_text("📤 Enviando vídeo...")
        with open(nome_arquivo, 'rb') as video:
            await context.bot.send_video(
                chat_id=chat_id,
                video=video,
                caption="✅ Aqui está seu vídeo!"
            )

        await mensagem.edit_text("✅ Envio concluído!")

    except Exception as e:
        await mensagem.edit_text(f"❌ Erro: {e}")
    finally:
        if os.path.exists(nome_arquivo):
            os.remove(nome_arquivo)