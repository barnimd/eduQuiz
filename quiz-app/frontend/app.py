from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
import bcrypt
from questions_bank import get_questions

app = Flask(__name__)
app.secret_key = "admin123"  # Ganti di production

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["eduquiz"]
users = db["users"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = bcrypt.hashpw(request.form["password"].encode('utf-8'), bcrypt.gensalt())

        if users.find_one({"username": username}):
            flash("Username already exists", "error")
            return render_template("signup.html")

        users.insert_one({"username": username, "password": password})
        flash("Signup successful. Please login.", "success")
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
        flash("Invalid username or password", "error")
        return render_template("login.html")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

@app.route("/quiz/<category>")
def quiz(category):
    if 'username' not in session:
        return redirect(url_for("login"))

    questions = get_questions(category)
    return render_template("quiz.html", category=category, questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
