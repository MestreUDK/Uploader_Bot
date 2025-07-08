# config.py
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Admin principal
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# Lista de IDs autorizados (convertido de string para int)
raw_ids = os.getenv("ALLOWED_IDS", "")
AUTHORIZED_USERS = [int(uid.strip()) for uid in raw_ids.split(",") if uid.strip().isdigit()]