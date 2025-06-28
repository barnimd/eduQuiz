import random

quiz_bank = {
    "math": [
        {
            "name": "q1",
            "text": "Jika 3x = 12, maka berapa nilai dari x + 2?",
            "options": [("A", "6"), ("B", "4"), ("C", "6")]  # A (x = 4, x+2 = 6)
        },
        {
            "name": "q2",
            "text": "Hasil dari 10 - 2 x 3 adalah?",
            "options": [("A", "24"), ("B", "4"), ("C", "6")]  # B (operasi: 2x3 = 6 → 10-6 = 4)
        },
        {
            "name": "q3",
            "text": "Bilangan ganjil terkecil setelah 20 adalah?",
            "options": [("A", "21"), ("B", "23"), ("C", "19")]  # A
        },
        {
            "name": "q4",
            "text": "Jika 5 apel + 2 apel = 7, berapa 5 apel - 2 apel?",
            "options": [("A", "2"), ("B", "3"), ("C", "5")]  # B
        },
        {
            "name": "q5",
            "text": "Sebuah segitiga punya 3 sisi. Kalau ditambah 1 sisi lagi jadi?",
            "options": [("A", "Segiempat"), ("B", "Segilima"), ("C", "Bukan segitiga")]  # C
        },
        {
            "name": "q6",
            "text": "Berapa hasil dari (4 + 4) ÷ 2?",
            "options": [("A", "4"), ("B", "8"), ("C", "2")]  # A
        },
        {
            "name": "q7",
            "text": "Urutan dari kecil ke besar: 0.5, 1/4, 0.75?",
            "options": [("A", "1/4, 0.5, 0.75"), ("B", "0.5, 0.75, 1/4"), ("C", "0.75, 0.5, 1/4")]  # A
        },
        {
            "name": "q8",
            "text": "Jika kamu membagi 100 dengan 0, hasilnya?",
            "options": [("A", "0"), ("B", "Tidak terdefinisi"), ("C", "Tak hingga")]  # B
        },
        {
            "name": "q9",
            "text": "Bilangan 1, 1, 2, 3, 5, ... selanjutnya?",
            "options": [("A", "7"), ("B", "8"), ("C", "6")]  # B (Fibonacci)
        },
        {
            "name": "q10",
            "text": "Jika sebuah kubus memiliki sisi 3 cm, volumenya adalah?",
            "options": [("A", "27 cm³"), ("B", "9 cm²"), ("C", "12 cm³")]  # A
        }
    ],
    "animals": [
        {"name": "q1", "text": "Hewan apa yang bertelur?", "options": [("A", "Kucing"), ("B", "Ayam"), ("C", "Anjing")]},  # B
        {"name": "q2", "text": "Hewan mamalia di bawah ini adalah?", "options": [("A", "Ikan"), ("B", "Sapi"), ("C", "Burung")]},  # B
        {"name": "q3", "text": "Hewan apa yang bisa terbang?", "options": [("A", "Elang"), ("B", "Kuda"), ("C", "Gajah")]},  # A
        {"name": "q4", "text": "Hewan apa yang hidup di air?", "options": [("A", "Kambing"), ("B", "Paus"), ("C", "Ular")]},  # B
        {"name": "q5", "text": "Hewan tercepat di darat adalah?", "options": [("A", "Singa"), ("B", "Macan"), ("C", "Cheetah")]},  # C
        {"name": "q6", "text": "Hewan apa yang memiliki belalai?", "options": [("A", "Gajah"), ("B", "Kerbau"), ("C", "Rusa")]},  # A
        {"name": "q7", "text": "Binatang yang menghasilkan susu adalah?", "options": [("A", "Ayam"), ("B", "Sapi"), ("C", "Bebek")]},  # B
        {"name": "q8", "text": "Apa nama bayi kambing?", "options": [("A", "Anak kambing"), ("B", "Anak sapi"), ("C", "Anak ayam")]},  # A
        {"name": "q9", "text": "Hewan yang dikenal sebagai raja hutan adalah?", "options": [("A", "Harimau"), ("B", "Singa"), ("C", "Beruang")]},  # B
        {"name": "q10", "text": "Burung yang bisa menirukan suara manusia adalah?", "options": [("A", "Merpati"), ("B", "Beo"), ("C", "Elang")]}  # B
    ],
    "places": [
        {"name": "q1", "text": "Ibukota Indonesia adalah?", "options": [("A", "Bandung"), ("B", "Jakarta"), ("C", "Surabaya")]},  # B
        {"name": "q2", "text": "Tempat untuk membeli makanan adalah?", "options": [("A", "Pasar"), ("B", "Sekolah"), ("C", "Rumah")]},  # A
        {"name": "q3", "text": "Tempat untuk belajar adalah?", "options": [("A", "Sekolah"), ("B", "Pasar"), ("C", "Mall")]},  # A
        {"name": "q4", "text": "Tempat ibadah umat Islam adalah?", "options": [("A", "Gereja"), ("B", "Masjid"), ("C", "Vihara")]},  # B
        {"name": "q5", "text": "Tempat untuk menonton film adalah?", "options": [("A", "Perpustakaan"), ("B", "Bioskop"), ("C", "Apotek")]},  # B
        {"name": "q6", "text": "Tempat naik kereta api?", "options": [("A", "Stasiun"), ("B", "Terminal"), ("C", "Pelabuhan")]},  # A
        {"name": "q7", "text": "Tempat menjual obat-obatan adalah?", "options": [("A", "Pasar"), ("B", "Apotek"), ("C", "Toko baju")]},  # B
        {"name": "q8", "text": "Tempat untuk bermain anak-anak adalah?", "options": [("A", "Kantor"), ("B", "Taman"), ("C", "Puskesmas")]},  # B
        {"name": "q9", "text": "Dimana pesawat terbang lepas landas?", "options": [("A", "Bandara"), ("B", "Stasiun"), ("C", "Pelabuhan")]},  # A
        {"name": "q10", "text": "Tempat untuk membaca dan meminjam buku?", "options": [("A", "Perpustakaan"), ("B", "Kantin"), ("C", "Kelas")]}  # A
    ]
}

def get_questions(category):
    if category in quiz_bank:
        questions = quiz_bank[category][:]
        random.shuffle(questions)  # ⬅️ acak urutan soal setiap kali
        return questions
    return []
