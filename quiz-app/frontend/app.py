from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
import bcrypt
from questions_bank import get_questions
from collections import Counter
from datetime import datetime

app = Flask(__name__)
app.secret_key = "admin123"  # Ganti di production

# MongoDB setup
client = MongoClient("mongodb://host.docker.internal:27017/")
db = client["eduquiz"]
users = db["users"]
scores_collection = db["scores"]

@app.route("/")
def home():
    stats = None
    if "username" in session:
        stats = get_user_stats(session["username"])
    
    leaderboard_math, extra_math = get_leaderboard("math", session.get("username"))
    leaderboard_animals, extra_animals = get_leaderboard("animals", session.get("username"))
    leaderboard_places, extra_places = get_leaderboard("places", session.get("username"))

    return render_template("index.html",
                           stats=stats,
                           leaderboard_math=leaderboard_math,
                           leaderboard_animals=leaderboard_animals,
                           leaderboard_places=leaderboard_places,
                           extra_math=extra_math,
                           extra_animals=extra_animals,
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

    # Cek apakah sudah ada skor sebelumnya untuk user + kategori
    existing_score = scores_collection.find_one({
        "username": username,
        "category": category
    })

    if existing_score:
        # Jika skor baru lebih tinggi, update
        if score > existing_score["score"]:
            scores_collection.update_one(
                {"_id": existing_score["_id"]},
                {"$set": {"score": score}}
            )
    else:
        # Jika belum ada, insert
        scores_collection.insert_one({
            "username": username,
            "category": category,
            "score": score
        })

    return {"message": "Score processed"}, 200


def simpan_skor(username, category, score):
    # 1. Simpan ke koleksi 'scores' untuk tracking history
    db.scores.insert_one({
        "username": username,
        "category": category,
        "score": score,
        "timestamp": datetime.utcnow()
    })

    # 2. Update ke koleksi 'best_scores' hanya jika score baru lebih tinggi
    db.best_scores.update_one(
        {"username": username, "category": category},
        {"$max": {"score": score}},
        upsert=True
    )

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

def get_user_stats(username):
    all_attempts = list(db.scores.find({"username": username}))
    total_kuis = len(all_attempts)

    # Hitung jumlah per kategori
    from collections import Counter
    kategori_count = Counter([a['category'] for a in all_attempts])
    kategori_fav = kategori_count.most_common(1)[0][0] if kategori_count else None

    # Hitung rata-rata
    if all_attempts:
        avg_score = sum(a['score'] for a in all_attempts) / len(all_attempts)
    else:
        avg_score = 0

    # Skor tertinggi dari best_scores
    tertinggi = db.best_scores.find({"username": username}).sort("score", -1).limit(1)
    tertinggi_list = list(tertinggi)
    high_score_data = tertinggi_list[0] if tertinggi_list else None


    return {
        "total_kuis": total_kuis,
        "kategori_fav": kategori_fav,
        "avg_score": round(avg_score, 2),
        "skor_tertinggi": high_score_data["score"] if high_score_data else 0,
        "kategori_tertinggi": high_score_data["category"] if high_score_data else "-"
    }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
