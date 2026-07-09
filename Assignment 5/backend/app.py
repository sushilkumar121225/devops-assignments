from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Flask Backend is Running Successfully!"

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json

    print(data)

    return jsonify({
        "status": "success",
        "message": "Data received successfully"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)