from flask import Flask, jsonify
import os
import requests
import time

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
app = Flask(__name__)

@app.route('/')
def index():
    return "cadburys secret santa tracker by xeny yours truly 💯💯💯"

def send(message):
    response = requests.post(DISCORD_WEBHOOK_URL, json={'content': message})
    print("Message sent successfully." if response.status_code == 204 else f"Failed to send message. Status code: {response.status_code}")

def check_link(link):
    print("trying link", link)
    r = requests.get(link)
    if "missed-out" not in r.url:
        if link == "https://bit.ly/StarFreebies-Cadbury-32-ireland":
            pass
        else:
            print(r.url)
            send(f"@everyone\n\n<{link}>\n\n.")#{r.url}

def check_all():
    with open("links.txt", "r") as file:
        links = file.read().splitlines()

    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        executor.map(check_link, links)

while True:
    check_all()

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
