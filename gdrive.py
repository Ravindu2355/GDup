import os
import requests
from auth import get_access_token

UPLOAD_URL = "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart"

def upload_file(file_path, filename):
    token = get_access_token()
    if not token:
        raise Exception("Not authenticated")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    metadata = {
        "name": filename
    }

    files = {
        "metadata": ("metadata", str(metadata), "application/json"),
        "file": open(file_path, "rb")
    }

    r = requests.post(UPLOAD_URL, headers=headers, files=files)
    r.raise_for_status()
    return r.json()
