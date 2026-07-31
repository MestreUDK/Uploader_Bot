# config.py

"""Configurações do Uploader Bot carregadas pelas variáveis de ambiente."""

import os


BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()

# Admin principal
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# IDs autorizados separados por vírgula.
# Exemplo: ALLOWED_IDS=123456789,987654321
_raw_ids = os.getenv("ALLOWED_IDS", "")

AUTHORIZED_USERS = {
    int(user_id.strip())
    for user_id in _raw_ids.split(",")
    if user_id.strip().isdigit()
}

# Configurações iniciais do sistema de downloads
MAX_BATCH_ITEMS = int(os.getenv("MAX_BATCH_ITEMS", "20"))
MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", "2000"))

# Quantidade máxima de operações simultâneas
MAX_CONCURRENT_DOWNLOADS = int(
    os.getenv("MAX_CONCURRENT_DOWNLOADS", "2")
)
MAX_CONCURRENT_ENCODINGS = int(
    os.getenv("MAX_CONCURRENT_ENCODINGS", "1")
)
MAX_CONCURRENT_UPLOADS = int(
    os.getenv("MAX_CONCURRENT_UPLOADS", "1")
)

# Diretório usado para arquivos temporários
TEMP_DIR = os.getenv("TEMP_DIR", "temp")