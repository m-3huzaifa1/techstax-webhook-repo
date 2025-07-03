from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import os
from datetime import datetime
import pytz
from bson.json_util import dumps
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = MongoClient(os.getenv('MONGO_URI'))
db = client['techStaXwebhookDB']
collection = db['events']

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.json
    event_type = request.headers.get('X-GitHub-Event')
    data = {}
    india = pytz.timezone('Asia/Kolkata')
    timestamp = datetime.now(india).strftime('%d %B %Y - %I:%M %p %Z')

    if event_type == "push":
        data = {
            "type": "push",
            "author": payload["pusher"]["name"],
            "to_branch": payload["ref"].split("/")[-1],
            "timestamp": timestamp
        }
    elif event_type == "pull_request":
        pr = payload["pull_request"]
        data = {
            "type": "pull_request",
            "author": pr["user"]["login"],
            "from_branch": pr["head"]["ref"],
            "to_branch": pr["base"]["ref"],
            "timestamp": timestamp
        }
    elif event_type == "merge_group":  # Optional simulation
        pr = payload["merge_group"]
        data = {
            "type": "merge",
            "author": payload["sender"]["login"],
            "from_branch": pr["head"]["ref"],
            "to_branch": pr["base"]["ref"],
            "timestamp": timestamp
        }
    if data:
        collection.insert_one(data)

    return jsonify({"status": "success"}), 200

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-updates', methods=['GET'])
def get_updates():
    latest = collection.find().sort('_id', -1).limit(10)
    return dumps(list(latest))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)