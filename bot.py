from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("8384962152:AAE-U5ItxVzrVNPeZQncEDe5XhbS5jBzO9I")
TEXTO_CHAVE = os.environ.get("TEXTO_CHAVE", "cupom")

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data and "text" in data["message"]:
        texto = data["message"]["text"]
        chat_id = data["message"]["chat"]["id"]

        if TEXTO_CHAVE.lower() in texto.lower():
            enviar_mensagem(chat_id, f"🔔 Texto-chave detectado: {texto}")

    return "OK"

def enviar_mensagem(chat_id, texto):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": texto}
    requests.post(url, json=payload)

@app.route("/", methods=["GET"])
def root():
    return "Bot ativo!"


