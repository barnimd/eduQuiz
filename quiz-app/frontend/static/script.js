document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('quiz-form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        let score = 0;
        let total = 2; // Jumlah soal per kategori (ubah ini kalau soal ditambah)

        // Jawaban benar sesuai kategori
        const answers = {
            math: {
                q1: 'B',
                q2: 'A'
            },
            animals: {
                q1: 'B',
                q2: 'B'
            },
            places: {
                q1: 'C',
                q2: 'B'
            }
        };

        // Ambil kategori dari URL
        const path = window.location.pathname;
        const category = path.split("/")[2]; // misal /quiz/math → 'math'

        const correct = answers[category];

        // Cek setiap soal
        for (let key in correct) {
            const selected = form.querySelector(`input[name="${key}"]:checked`);
            if (selected && selected.value === correct[key]) {
                score++;
            }
        }

        // Tampilkan hasil
        resultDiv.innerHTML = `
            Kamu menjawab ${score} dari ${total} soal dengan benar.<br>
            Skor kamu: <strong>${Math.round((score / total) * 100)}%</strong>
        `;

        // Scroll ke hasil
        resultDiv.scrollIntoView({ behavior: "smooth" });
    });
});


let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("slide");
    let dots = document.getElementsByClassName("dot");

    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }

    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }

    slides[slideIndex-1].style.display = "block";  
    dots[slideIndex-1].className += " active";
}
