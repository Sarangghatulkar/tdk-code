from flask import Flask, request
import requests, time

app = Flask(__name__)

# Replace these with your own info
TELEGRAM_BOT_TOKEN = "7609865041:AAHNSVopzG248fx3Srz5ZjTJkTfiqiJakis"
META_PIXEL_ID = "1480788746524419"
META_ACCESS_TOKEN = "EAATPQEM4wZAUBPhCApW4w0wu1jkJSM37CHrlUTBitZB3ED2N6B3Fl5lzJ75kKtqQzGT5ZBGFzwMMSowN0TfNK2bGtJcvuZCZBcucdT8FsOV4vTP9LUED0Qpg3UBgJIl0gQOZBvvcsSG8g5PZBZCez4v70tJgmcY1gF5XoYgXIliXAANolJUnPX2FnoeRYUThIfJVZAwZDZD"

# Function to send event to Meta
def send_event_to_meta(user_id):
    url = f"https://graph.facebook.com/v18.0/{1480788746524419}/events"
    payload = {
        "data": [{
            "event_name": "TelegramJoinRequest",
            "event_time": int(time.time()),
            "user_data": {"external_id": str(user_id)}
        }],
        "access_token": EAATPQEM4wZAUBPhCApW4w0wu1jkJSM37CHrlUTBitZB3ED2N6B3Fl5lzJ75kKtqQzGT5ZBGFzwMMSowN0TfNK2bGtJcvuZCZBcucdT8FsOV4vTP9LUED0Qpg3UBgJIl0gQOZBvvcsSG8g5PZBZCez4v70tJgmcY1gF5XoYgXIliXAANolJUnPX2FnoeRYUThIfJVZAwZDZD
    }
    requests.post(url, json=payload)

# Telegram webhook
@app.route(f"/{7609865041:AAHNSVopzG248fx3Srz5ZjTJkTfiqiJakis}", methods=['POST'])
def telegram_webhook():
    data = request.get_json()
    # Detect join requests
    if "chat_join_request" in data:
        user_id = data["chat_join_request"]["from"]["id"]
        send_event_to_meta(user_id)
    return "ok"

@app.route("/")
def home():
    return "Bot Active!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

