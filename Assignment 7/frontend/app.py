from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        response = requests.get("http://express-service:3000")
        backend = response.text
    except:
        backend = "Backend Not Reachable"

    return f"""
    <h1>Flask Frontend</h1>
    <h2>{backend}</h2>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)