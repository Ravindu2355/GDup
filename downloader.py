import os
from config import DOWNLOAD_DIR

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

async def download_media(client, message, progress):
    path = await message.download(
        file_name=DOWNLOAD_DIR,
        progress=progress
    )
    return path
