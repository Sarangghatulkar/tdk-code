import time
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ Directly using your credentials
TELEGRAM_BOT_TOKEN = "7609865041:AAHNSVopzG248fx3Srz5ZjTJkTfiqiJakis"
META_PIXEL_ID = "1480788746524419"
META_ACCESS_TOKEN = "EAATPQEM4wZAUBPhCApW4w0wu1jkJSM37CHrlUTBitZB3ED2N6B3Fl5lzJ75kKtqQzGT5ZBGFzwMMSowN0TfNK2bGtJcvuZCZBcucdT8FsOV4vTP9LUED0Qpg3UBgJIl0gQOZBvvcsSG8g5PZBZCez4v70tJgmcY1gF5XoYgXIliXAANolJUnPX2FnoeRYUThIfJVZAwZDZD"

@app.route(f"/{TELEGRAM_BOT_TOKEN}", methods=["POST"])
def telegram_webhook():
    data = request.json

    # Telegram user ID
    user_id = data.get("message", {}).get("from", {}).get("id")

    # ✅ Send CAPI event to Meta
    payload = {
        "data": [
            {
                "event_name": "TelegramJoinRequest",
                "event_time": int(time.time()),
                "user_data": {},
                "custom_data": {"telegram_id": user_id}
            }
        ],
        "access_token": META_ACCESS_TOKEN
    }

    r = requests.post(
        f"https://graph.facebook.com/v17.0/{META_PIXEL_ID}/events",
        json=payload
    )
    print("Meta CAPI response:", r.status_code, r.text)

    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


