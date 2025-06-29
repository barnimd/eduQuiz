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
scores_collection = db["scores"]

@app.route("/")
def home():
    username = session.get("username")

    leaderboard_math, extra_math = get_leaderboard("math", username)
    leaderboard_animals, extra_animals = get_leaderboard("animals", username)
    leaderboard_places, extra_places = get_leaderboard("places", username)

    return render_template("index.html",
                           leaderboard_math=leaderboard_math,
                           extra_math=extra_math,
                           leaderboard_animals=leaderboard_animals,
                           extra_animals=extra_animals,
                           leaderboard_places=leaderboard_places,
                           extra_places=extra_places)



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

@app.route("/quiz/<category>", methods=["GET", "POST"])
def quiz(category):
    if 'username' not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        score = int(request.form.get("score", 0))
        simpan_skor(session["username"], category, score)
        flash("Skor kamu berhasil disimpan!", "success")
        return redirect(url_for("home"))

    questions = get_questions(category)
    return render_template("quiz.html", category=category, questions=questions)


@app.route("/submit-score", methods=["POST"])
def submit_score():
    if 'username' not in session:
        return {"error": "Unauthorized"}, 401

    data = request.get_json()
    category = data.get("category")
    score = data.get("score")
    username = session["username"]

    # Simpan skor ke MongoDB
    scores_collection.insert_one({
        "username": username,
        "category": category,
        "score": score
    })

    return {"message": "Score saved successfully"}, 200


def simpan_skor(username, category, score):
    scores_collection.insert_one({
        "username": username,
        "category": category,
        "score": score
    })

def get_leaderboard(category, current_user=None):
    # Ambil 10 skor tertinggi untuk kategori tertentu
    top_scores = list(scores_collection.find(
        {"category": category}
    ).sort("score", -1).limit(10))

    user_score = None
    if current_user:
        user_score = scores_collection.find_one({
            "username": current_user,
            "category": category
        })

        # Cek apakah user sudah masuk 10 besar
        if any(entry["username"] == current_user for entry in top_scores):
            user_score = None  # Tidak perlu ditampilkan terpisah

    return top_scores, user_score

if __name__ == "__main__":
    app.run(debug=True)
