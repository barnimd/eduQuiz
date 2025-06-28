import random

quiz_bank = {
    "math": [
        {
            "name": "q1",
            "text": "Berapa hasil dari 2 + 2?",
            "options": [["A", "3"], ["B", "4"], ["C", "5"]]
        },
        {
            "name": "q2",
            "text": "Berapa hasil dari 5 x 3?",
            "options": [["A", "15"], ["B", "8"], ["C", "20"]]
        }
    ],
    "animals": [
        {
            "name": "q1",
            "text": "Hewan apa yang bisa terbang?",
            "options": [["A", "Kucing"], ["B", "Burung"], ["C", "Ular"]]
        },
        {
            "name": "q2",
            "text": "Hewan apa yang hidup di laut?",
            "options": [["A", "Kuda"], ["B", "Ikan"], ["C", "Kambing"]]
        }
    ],
    "places": [
        {
            "name": "q1",
            "text": "Gambar ini menunjukkan tempat apa? (anggap ada gambar)",
            "options": [["A", "Sekolah"], ["B", "Rumah"], ["C", "Pasar"]]
        },
        {
            "name": "q2",
            "text": "Kota manakah yang merupakan ibu kota Indonesia?",
            "options": [["A", "Bandung"], ["B", "Jakarta"], ["C", "Surabaya"]]
        }
    ]
}

def get_questions(category):
    if category in quiz_bank:
        questions = quiz_bank[category][:]
        random.shuffle(questions)  # ⬅️ acak urutan soal setiap kali
        return questions
    return []
