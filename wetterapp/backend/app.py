import os
from dotenv import load_dotenv
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

app = Flask(__name__)
CORS(app)


@app.route("/weather",methods=["POST"])
def weather():
    body = request.get_json()
    city = body.get("city")
    if not city:
        return jsonify({"error": "city fehlt"}), 400

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
