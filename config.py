import os

# Telegram
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Allowed users (comma separated Telegram IDs)
AUTHORIZED_USERS = list(map(int, os.getenv("AUTHORIZED_USERS", "").split(",")))

# Google OAuth
CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"

TOKEN_FILE = "token.json"
UPLOAD_METHOD_FILE = "method.txt"
DOWNLOAD_DIR = "downloads"
