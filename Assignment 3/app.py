from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient("mongodb+srv://username:password@cluster0.xxxxxx.mongodb.net/?retryWrites=true&w=majority")

db = client["studentdb"]

collection = db["students"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api")
def api():

    with open("data.json","r") as file:
        data=json.load(file)

    return jsonify(data)


@app.route("/submit",methods=["POST"])
def submit():

    try:

        name=request.form["name"]
        email=request.form["email"]

        collection.insert_one({

            "name":name,
            "email":email

        })

        return redirect(url_for("success"))

    except Exception as e:

        return render_template("index.html",error=str(e))


@app.route("/success")
def success():

    return render_template("success.html")


if __name__=="__main__":
    app.run(debug=True)
