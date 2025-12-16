from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is alive"

@app.route("/health")
def health():
    return {"status": "ok"}

def run():
    app.run(host="0.0.0.0", port=8000)
