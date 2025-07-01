import random

all_questions = {
        "math": [
            {"name": "q1", "text": "Jika 3x = 12, maka berapa nilai dari x + 2?", "options": [["A", "6"], ["B", "4"], ["C", "8"]]},
            {"name": "q2", "text": "Hasil dari 10 - 2 x 3 adalah?", "options": [["A", "24"], ["B", "4"], ["C", "6"]]},
            {"name": "q3", "text": "Bilangan ganjil terkecil setelah 20 adalah?", "options": [["A", "21"], ["B", "23"], ["C", "19"]]},
            {"name": "q4", "text": "Jika 5 apel + 2 apel = 7, berapa 5 apel - 2 apel?", "options": [["A", "2"], ["B", "3"], ["C", "5"]]},
            {"name": "q5", "text": "Sebuah segitiga punya 3 sisi. Kalau ditambah 1 sisi lagi jadi?", "options": [["A", "Segiempat"], ["B", "Segilima"], ["C", "Bukan segitiga"]]},
            {"name": "q6", "text": "Berapa hasil dari (4 + 4) ÷ 2?", "options": [["A", "4"], ["B", "8"], ["C", "2"]]},
            {"name": "q7", "text": "Urutan dari kecil ke besar: 0.5, 1/4, 0.75?", "options": [["A", "1/4, 0.5, 0.75"], ["B", "0.5, 0.75, 1/4"], ["C", "0.75, 0.5, 1/4"]]},
            {"name": "q8", "text": "Jika kamu membagi 100 dengan 0, hasilnya?", "options": [["A", "0"], ["B", "Tidak terdefinisi"], ["C", "Tak hingga"]]},
            {"name": "q9", "text": "Bilangan 1, 1, 2, 3, 5, ... selanjutnya?", "options": [["A", "7"], ["B", "8"], ["C", "6"]]},
            {"name": "q10", "text": "Jika sebuah kubus memiliki sisi 3 cm, volumenya adalah?", "options": [["A", "27 cm³"], ["B", "9 cm²"], ["C", "12 cm³"]]},
            {"name": "q11", "text": "Nilai dari |−7| adalah?", "options": [["A", "-7"], ["B", "0"], ["C", "7"]]},
            {"name": "q12", "text": "Hasil dari 2² + 2 adalah?", "options": [["A", "6"], ["B", "8"], ["C", "4"]]},
            {"name": "q13", "text": "Berapa 25% dari 80?", "options": [["A", "20"], ["B", "25"], ["C", "15"]]},
            {"name": "q14", "text": "Bilangan prima terkecil lebih dari 10?", "options": [["A", "11"], ["B", "13"], ["C", "9"]]},
            {"name": "q15", "text": "Hasil dari 3 x (2 + 4) adalah?", "options": [["A", "18"], ["B", "12"], ["C", "21"]]},
            {"name": "q16", "text": "Nilai dari 10 mod 3 adalah?", "options": [["A", "1"], ["B", "3"], ["C", "2"]]},
            {"name": "q17", "text": "Akar kuadrat dari 64?", "options": [["A", "6"], ["B", "8"], ["C", "7"]]},
            {"name": "q18", "text": "Jika x = 5, maka nilai dari 2x + 1?", "options": [["A", "10"], ["B", "11"], ["C", "9"]]},
            {"name": "q19", "text": "Berapa hasil dari 100 ÷ 25?", "options": [["A", "2"], ["B", "4"], ["C", "5"]]},
            {"name": "q20", "text": "Hasil dari 9² adalah?", "options": [["A", "81"], ["B", "18"], ["C", "72"]]},
            {"name": "q21", "text": "Jika 2 jam = x menit, x adalah?", "options": [["A", "100"], ["B", "120"], ["C", "90"]]},
            {"name": "q22", "text": "Bilangan genap antara 10 dan 20?", "options": [["A", "15"], ["B", "14"], ["C", "19"]]},
            {"name": "q23", "text": "Berapa hasil dari 1/2 + 1/4?", "options": [["A", "3/4"], ["B", "2/4"], ["C", "5/4"]]},
            {"name": "q24", "text": "Jika 7x = 35, maka x adalah?", "options": [["A", "5"], ["B", "7"], ["C", "6"]]},
            {"name": "q25", "text": "10 pangkat 0 sama dengan?", "options": [["A", "0"], ["B", "1"], ["C", "10"]]},
            {"name": "q26", "text": "Luas persegi dengan sisi 4 cm adalah?", "options": [["A", "12 cm²"], ["B", "8 cm²"], ["C", "16 cm²"]]},
            {"name": "q27", "text": "Sisa bagi 22 dengan 5 adalah?", "options": [["A", "3"], ["B", "2"], ["C", "4"]]},
            {"name": "q28", "text": "Bilangan ganjil antara 30 dan 34?", "options": [["A", "32"], ["B", "33"], ["C", "34"]]},
            {"name": "q29", "text": "Berapa hasil dari -3 + 7?", "options": [["A", "4"], ["B", "-10"], ["C", "5"]]},
            {"name": "q30", "text": "Nilai dari 6 x 6 - 6 adalah?", "options": [["A", "30"], ["B", "36"], ["C", "42"]]}
        ],


    "animals": [
        {"name": "q1", "text": "Hewan apa yang bertelur?", "options": [["A", "Kucing"], ["B", "Ayam"], ["C", "Anjing"]]},
        {"name": "q2", "text": "Hewan mamalia di bawah ini adalah?", "options": [["A", "Ikan"], ["B", "Sapi"], ["C", "Burung"]]},
        {"name": "q3", "text": "Hewan apa yang bisa terbang?", "options": [["A", "Elang"], ["B", "Kuda"], ["C", "Gajah"]]},
        {"name": "q4", "text": "Hewan apa yang hidup di air?", "options": [["A", "Kambing"], ["B", "Paus"], ["C", "Ular"]]},
        {"name": "q5", "text": "Hewan tercepat di darat adalah?", "options": [["A", "Singa"], ["B", "Macan"], ["C", "Cheetah"]]},
        {"name": "q6", "text": "Hewan apa yang memiliki belalai?", "options": [["A", "Gajah"], ["B", "Kerbau"], ["C", "Rusa"]]},
        {"name": "q7", "text": "Binatang yang menghasilkan susu adalah?", "options": [["A", "Ayam"], ["B", "Sapi"], ["C", "Bebek"]]},
        {"name": "q8", "text": "Apa nama bayi kambing?", "options": [["A", "Anak kambing"], ["B", "Anak sapi"], ["C", "Anak ayam"]]},
        {"name": "q9", "text": "Hewan yang dikenal sebagai raja hutan adalah?", "options": [["A", "Harimau"], ["B", "Singa"], ["C", "Beruang"]]},
        {"name": "q10", "text": "Burung yang bisa menirukan suara manusia adalah?", "options": [["A", "Merpati"], ["B", "Beo"], ["C", "Elang"]]},
        {"name": "q11", "text": "Hewan berkaki dua yang bisa berenang adalah?", "options": [["A", "Itik"], ["B", "Kucing"], ["C", "Sapi"]]},
        {"name": "q12", "text": "Hewan yang bisa hidup di darat dan air?", "options": [["A", "Katak"], ["B", "Elang"], ["C", "Semut"]]},
        {"name": "q13", "text": "Hewan bertanduk biasanya berjenis kelamin?", "options": [["A", "Jantan"], ["B", "Betina"], ["C", "Keduanya"]]},
        {"name": "q14", "text": "Hewan yang mengeluarkan tinta untuk bertahan diri?", "options": [["A", "Gurita"], ["B", "Ikan"], ["C", "Kepiting"]]},
        {"name": "q15", "text": "Hewan yang dikenal sebagai hewan pemalas?", "options": [["A", "Sloth"], ["B", "Macan"], ["C", "Zebra"]]},
        {"name": "q16", "text": "Hewan apa yang bisa hidup tanpa air lama?", "options": [["A", "Unta"], ["B", "Ikan"], ["C", "Kerbau"]]},
        {"name": "q17", "text": "Serangga yang menghasilkan madu adalah?", "options": [["A", "Lalat"], ["B", "Lebah"], ["C", "Semut"]]},
        {"name": "q18", "text": "Binatang yang bisa berubah warna?", "options": [["A", "Cicak"], ["B", "Bunglon"], ["C", "Tokek"]]},
        {"name": "q19", "text": "Hewan yang bernapas dengan insang adalah?", "options": [["A", "Kucing"], ["B", "Ikan"], ["C", "Bebek"]]},
        {"name": "q20", "text": "Hewan berkaki 8 adalah?", "options": [["A", "Ular"], ["B", "Laba-laba"], ["C", "Kupu-kupu"]]},
        {"name": "q21", "text": "Hewan yang tidur di siang hari dan aktif di malam?", "options": [["A", "Burung hantu"], ["B", "Ayam"], ["C", "Kelinci"]]},
        {"name": "q22", "text": "Hewan yang hidup di kutub adalah?", "options": [["A", "Penguin"], ["B", "Harimau"], ["C", "Jerapah"]]},
        {"name": "q23", "text": "Hewan yang sering dijadikan hewan peliharaan kecil?", "options": [["A", "Kuda"], ["B", "Hamster"], ["C", "Sapi"]]},
        {"name": "q24", "text": "Hewan dengan leher paling panjang?", "options": [["A", "Zebra"], ["B", "Jerapah"], ["C", "Singa"]]},
        {"name": "q25", "text": "Hewan yang bisa berjalan mundur?", "options": [["A", "Kepiting"], ["B", "Ayam"], ["C", "Bebek"]]},
        {"name": "q26", "text": "Hewan laut yang memiliki cangkang keras?", "options": [["A", "Ular laut"], ["B", "Kepiting"], ["C", "Ubur-ubur"]]},
        {"name": "q27", "text": "Hewan yang berjalan dengan perutnya?", "options": [["A", "Ular"], ["B", "Gajah"], ["C", "Bebek"]]},
        {"name": "q28", "text": "Mamalia laut terbesar adalah?", "options": [["A", "Ikan Paus"], ["B", "Lumba-lumba"], ["C", "Anjing laut"]]},
        {"name": "q29", "text": "Hewan yang paling terkenal dengan sisik keras?", "options": [["A", "Landak"], ["B", "Trenggiling"], ["C", "Cicak"]]},
        {"name": "q30", "text": "Hewan berkaki empat yang bisa meloncat jauh?", "options": [["A", "Kanguru"], ["B", "Kucing"], ["C", "Rusa"]]}
    ],


    "places": [
        {"name": "q1", "text": "Ibukota Indonesia adalah?", "options": [["A", "Bandung"], ["B", "Jakarta"], ["C", "Surabaya"]]},
        {"name": "q2", "text": "Tempat untuk membeli makanan adalah?", "options": [["A", "Pasar"], ["B", "Sekolah"], ["C", "Rumah"]]},
        {"name": "q3", "text": "Tempat untuk belajar adalah?", "options": [["A", "Sekolah"], ["B", "Pasar"], ["C", "Mall"]]},
        {"name": "q4", "text": "Tempat ibadah umat Islam adalah?", "options": [["A", "Gereja"], ["B", "Masjid"], ["C", "Vihara"]]},
        {"name": "q5", "text": "Tempat untuk menonton film adalah?", "options": [["A", "Perpustakaan"], ["B", "Bioskop"], ["C", "Apotek"]]},
        {"name": "q6", "text": "Tempat naik kereta api?", "options": [["A", "Stasiun"], ["B", "Terminal"], ["C", "Pelabuhan"]]},
        {"name": "q7", "text": "Tempat menjual obat-obatan adalah?", "options": [["A", "Pasar"], ["B", "Apotek"], ["C", "Toko baju"]]},
        {"name": "q8", "text": "Tempat untuk bermain anak-anak adalah?", "options": [["A", "Kantor"], ["B", "Taman"], ["C", "Puskesmas"]]},
        {"name": "q9", "text": "Dimana pesawat terbang lepas landas?", "options": [["A", "Bandara"], ["B", "Stasiun"], ["C", "Pelabuhan"]]},
        {"name": "q10", "text": "Tempat untuk membaca dan meminjam buku?", "options": [["A", "Perpustakaan"], ["B", "Kantin"], ["C", "Kelas"]]},
        {"name": "q11", "text": "Tempat tinggal presiden disebut?", "options": [["A", "Istana Negara"], ["B", "Kantor Camat"], ["C", "Gedung DPR"]]},
        {"name": "q12", "text": "Tempat untuk membeli obat resep dokter?", "options": [["A", "Supermarket"], ["B", "Apotek"], ["C", "Warung"]]},
        {"name": "q13", "text": "Tempat untuk menginap saat berlibur?", "options": [["A", "Hotel"], ["B", "Bioskop"], ["C", "Bandara"]]},
        {"name": "q14", "text": "Tempat untuk berenang secara umum?", "options": [["A", "Perpustakaan"], ["B", "Kolam renang"], ["C", "Stadion"]]},
        {"name": "q15", "text": "Dimana kita bisa melihat hewan liar dari dekat?", "options": [["A", "Kebun Binatang"], ["B", "Museum"], ["C", "Terminal"]]},
        {"name": "q16", "text": "Tempat untuk naik bus antarkota?", "options": [["A", "Stasiun"], ["B", "Terminal"], ["C", "Pelabuhan"]]},
        {"name": "q17", "text": "Tempat ibadah umat Kristen adalah?", "options": [["A", "Masjid"], ["B", "Gereja"], ["C", "Pura"]]},
        {"name": "q18", "text": "Tempat melihat benda-benda bersejarah adalah?", "options": [["A", "Museum"], ["B", "Stasiun"], ["C", "Restoran"]]},
        {"name": "q19", "text": "Tempat untuk mendapatkan layanan kesehatan dasar?", "options": [["A", "Klinik"], ["B", "Mall"], ["C", "Bank"]]},
        {"name": "q20", "text": "Tempat berbelanja pakaian dan elektronik disebut?", "options": [["A", "Terminal"], ["B", "Pasar malam"], ["C", "Mall"]]},
        {"name": "q21", "text": "Tempat untuk mengambil atau menabung uang?", "options": [["A", "Bank"], ["B", "Kantor Pos"], ["C", "Apotek"]]},
        {"name": "q22", "text": "Tempat orang mengurus surat-surat kependudukan?", "options": [["A", "Kantor Kelurahan"], ["B", "Rumah Sakit"], ["C", "Taman"]]},
        {"name": "q23", "text": "Dimana nelayan biasa berlabuh?", "options": [["A", "Pelabuhan"], ["B", "Stasiun"], ["C", "Bandara"]]},
        {"name": "q24", "text": "Tempat naik kapal laut?", "options": [["A", "Terminal"], ["B", "Bandara"], ["C", "Pelabuhan"]]},
        {"name": "q25", "text": "Tempat bermain bola kaki profesional?", "options": [["A", "Gelanggang"], ["B", "Stadion"], ["C", "Taman kota"]]},
        {"name": "q26", "text": "Tempat umum untuk acara seni dan pertunjukan?", "options": [["A", "Gedung Kesenian"], ["B", "Ruang kelas"], ["C", "Puskesmas"]]},
        {"name": "q27", "text": "Tempat untuk potong rambut?", "options": [["A", "Salon"], ["B", "Apotek"], ["C", "Koperasi"]]},
        {"name": "q28", "text": "Tempat jual beli hewan ternak biasanya di?", "options": [["A", "Pasar hewan"], ["B", "Kebun binatang"], ["C", "Klinik"]]},
        {"name": "q29", "text": "Tempat untuk pelatihan militer disebut?", "options": [["A", "Markas TNI"], ["B", "Sekolah"], ["C", "Kantor pos"]]},
        {"name": "q30", "text": "Dimana kamu bisa membeli tiket bioskop dan popcorn?", "options": [["A", "Bioskop"], ["B", "Warung"], ["C", "Perpustakaan"]]}
    ]

}

def get_questions(category):
    if category in all_questions:
        questions = all_questions[category][:]
        random.shuffle(questions)  # Acak urutan soal
        limited = questions[:10]   # Ambil 10 soal saja
        return limited  # Tidak ubah q["name"] agar cocok dengan correctAnswers
    return []

