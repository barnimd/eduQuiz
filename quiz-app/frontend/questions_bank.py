import random

def get_questions(category):
    questions = {
        "math": [
            {
                "text": "Berapa hasil dari 2 + 2?",
                "name": "q1",
                "options": [("A", "3"), ("B", "4"), ("C", "5")]
            },
            {
                "text": "Berapa hasil dari 5 x 3?",
                "name": "q2",
                "options": [("A", "15"), ("B", "8"), ("C", "20")]
            }
        ],
        "animals": [
            {
                "text": "Hewan apa yang bisa terbang?",
                "name": "q1",
                "options": [("A", "Kucing"), ("B", "Burung"), ("C", "Ular")]
            },
            {
                "text": "Hewan apa yang hidup di laut?",
                "name": "q2",
                "options": [("A", "Kuda"), ("B", "Ikan"), ("C", "Kambing")]
            }
        ],
        "places": [
            {
                "text": "Gambar ini menunjukkan tempat apa? (anggap ada gambar)",
                "name": "q1",
                "options": [("A", "Sekolah"), ("B", "Rumah"), ("C", "Pasar")]
            },
            {
                "text": "Kota manakah yang merupakan ibu kota Indonesia?",
                "name": "q2",
                "options": [("A", "Bandung"), ("B", "Jakarta"), ("C", "Surabaya")]
            }
        ]
    }

    selected_questions = questions.get(category, [])
    random.shuffle(selected_questions)
    return selected_questions
