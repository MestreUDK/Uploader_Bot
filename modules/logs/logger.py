# modules/logs/logger.py

from telegram import Update
from config import ADMIN_ID
import traceback

async def log_erro(update: Update, erro: Exception | str, contexto: str = ""):
    """Loga o erro: envia para o usuário e para o admin."""
    user_id = update.effective_user.id
    erro_texto = (
        str(erro) if isinstance(erro, str)
        else "".join(traceback.format_exception(type(erro), erro, erro.__traceback__))
    ).strip()

    mensagem = f"❗ <b>Erro ao {contexto or 'executar ação'}:</b>\n\n<code>{erro_texto}</code>"

    # Tenta enviar para o usuário que executou
    try:
        if update.message:
            await update.message.reply_text(mensagem, parse_mode="HTML")
        elif update.callback_query:
            await update.callback_query.message.reply_text(mensagem, parse_mode="HTML")
    except:
        pass  # ignora erros ao tentar alertar o usuário

    # Se o usuário não for o admin, envia o erro para o ADMIN_ID também
    if user_id != ADMIN_ID:
        try:
            await update.get_bot().send_message(chat_id=ADMIN_ID, text=mensagem, parse_mode="HTML")
        except:
            pass