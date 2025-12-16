import os
import asyncio
import threading
from pyrogram import Client, filters
from config import *
from auth import get_login_url, exchange_code
from downloader import download_media
from gdrive import upload_file
import server

def is_auth(user_id):
    return user_id in AUTHORIZED_USERS

def get_method():
    if not os.path.exists(UPLOAD_METHOD_FILE):
        return 0
    return int(open(UPLOAD_METHOD_FILE).read().strip())

def set_method(m):
    with open(UPLOAD_METHOD_FILE, "w") as f:
        f.write(str(m))

app = Client(
    "gdrive-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("login"))
async def login(_, m):
    if not is_auth(m.from_user.id):
        return
    await m.reply(f"🔐 Login URL:\n{get_login_url()}")

@app.on_message(filters.command("auth"))
async def auth_cmd(_, m):
    if not is_auth(m.from_user.id):
        return
    if len(m.command) < 2:
        return await m.reply("Usage: /auth <code>")
    exchange_code(m.command[1])
    await m.reply("✅ Google Drive authenticated")

@app.on_message(filters.command("method"))
async def method_cmd(_, m):
    if not is_auth(m.from_user.id):
        return
    if len(m.command) < 2:
        return await m.reply("Usage: /method 0 or 1")
    set_method(int(m.command[1]))
    await m.reply(f"Upload method set to {m.command[1]}")

@app.on_message(filters.command("up") & filters.reply)
async def upload_cmd(client, m):
    if not is_auth(m.from_user.id):
        return

    status = await m.reply("⬇️ Downloading...")

    async def progress(current, total):
        await status.edit(f"⬇️ {current * 100 // total}%")

    path = await download_media(client, m.reply_to_message, progress)

    filename = os.path.basename(path)
    if get_method() == 1:
        filename = filename + ".css"

    await status.edit("⬆️ Uploading to Google Drive...")
    upload_file(path, filename)

    await status.edit("✅ Uploaded successfully")
    os.remove(path)

def start_flask():
    server.run()

if __name__ == "__main__":
    threading.Thread(target=start_flask).start()
    app.run()
