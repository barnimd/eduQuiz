from flask import Flask, render_template, request, redirect, url_for, session
import os
from questions_bank import get_questions

app = Flask(
    __name__,
    template_folder='frontend/templates',
    static_folder='frontend/static'
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz/<category>')
def quiz_page(category):
    questions = get_questions(category)
    return render_template('quiz.html', category=category, questions=questions)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')