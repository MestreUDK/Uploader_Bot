from config import AUTHORIZED_USERS
from telegram import Update
from telegram.ext import ContextTypes

def restricted(func):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        if user_id not in AUTHORIZED_USERS:
            await update.message.reply_text("⚙️ Bot em manutenção no momento...")
            return
        return await func(update, context)
    return wrapper