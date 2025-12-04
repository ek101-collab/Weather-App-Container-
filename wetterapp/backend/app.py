import os
from dotenv import load_dotenv
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

app = Flask(__name__)
CORS(app)

@app.route("/weather", methods=["POST"])
def weather():
    body = request.get_json()
    prompt = body.get("prompt")
    if not prompt:
        return jsonify({"error": "prompt fehlt"}), 400

    url = "https://api.openweathermap.org/assistant/session"
    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": API_KEY
    }
    data = {"prompt": prompt}

    response = requests.post(url, json=data, headers=headers)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)