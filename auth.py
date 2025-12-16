import json
import os
import requests
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, TOKEN_FILE

AUTH_URL = (
    "https://accounts.google.com/o/oauth2/v2/auth"
    "?scope=https://www.googleapis.com/auth/drive.file"
    "&access_type=offline"
    "&prompt=consent"
    f"&client_id={CLIENT_ID}"
    f"&redirect_uri={REDIRECT_URI}"
    "&response_type=code"
)

def get_login_url():
    return AUTH_URL

def exchange_code(code):
    data = {
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code"
    }
    r = requests.post("https://oauth2.googleapis.com/token", data=data)
    r.raise_for_status()

    with open(TOKEN_FILE, "w") as f:
        json.dump(r.json(), f)

def get_access_token():
    if not os.path.exists(TOKEN_FILE):
        return None

    with open(TOKEN_FILE) as f:
        token = json.load(f)

    if "access_token" in token:
        return token["access_token"]

    return None
