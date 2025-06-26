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

//slideshow
 const slides = document.querySelectorAll('.slide');
  let current = 0;

  function updateSlides() {
    slides.forEach((slide, index) => {
      slide.classList.remove('active', 'prev', 'next');

      if (index === current) {
        slide.classList.add('active');
      } else if (index === (current - 1 + slides.length) % slides.length) {
        slide.classList.add('prev');
      } else if (index === (current + 1) % slides.length) {
        slide.classList.add('next');
      }
    });
  }

  document.getElementById('nextBtn').addEventListener('click', () => {
    current = (current + 1) % slides.length;
    updateSlides();
  });

  document.getElementById('prevBtn').addEventListener('click', () => {
    current = (current - 1 + slides.length) % slides.length;
    updateSlides();
  });

  updateSlides();

