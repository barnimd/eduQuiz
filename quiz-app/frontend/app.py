from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

# Route homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route untuk masing-masing quiz (belum ada file-nya, tapi nanti bisa ditambahkan)
@app.route('/quiz/<category>')
def quiz_page(category):
    return render_template('quiz.html', category=category)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
