from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
import bcrypt
import os
from questions_bank import get_questions

app = Flask(__name__, template_folder='../templates', static_folder='../static')


app.secret_key = "admin123"  # Ganti dengan yang lebih aman di production

client = MongoClient("mongodb://localhost:27017/")  # atau URI Mongo Atlas
db = client.eduquiz
users = db.users

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = bcrypt.hashpw(request.form["password"].encode('utf-8'), bcrypt.gensalt())

        if users.find_one({"username": username}):
            return "Username already exists"
        
        users.insert_one({"username": username, "password": password})
        return redirect(url_for("login"))
    
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"].encode('utf-8')

        user = users.find_one({"username": username})
        if user and bcrypt.checkpw(password, user["password"]):
            session["username"] = username
            return redirect(url_for("home"))
        return "Invalid username or password"
    
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


# Lindungi akses ke quiz
@app.route("/quiz/<category>")
def quiz(category):
    if 'username' not in session:
        return redirect(url_for("login"))
    # Ambil soal dari database atau questions_bank.py
    return render_template("quiz.html", category=category)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')