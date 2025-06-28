document.addEventListener("DOMContentLoaded", () => {
  showStartCountdown(() => {
    startQuiz(); // mulai quiz setelah countdown
  });
});

// Fungsi countdown awal 3..2..1
function showStartCountdown(callback) {
  const countdownOverlay = document.getElementById("start-countdown");
  const countdownNumber = document.getElementById("countdown-number");

  let count = 3;
  countdownNumber.textContent = count;
  countdownOverlay.style.display = 'flex';

  const interval = setInterval(() => {
    count--;
    if (count === 0) {
      clearInterval(interval);
      countdownOverlay.style.display = 'none';
      callback(); // lanjut ke quiz
    } else {
      countdownNumber.textContent = count;
    }
  }, 1000);
}

// Fungsi utama quiz
function startQuiz() {
  const quizData = window.quizData;
  const container = document.getElementById('quiz-container');
  const countdownEl = document.getElementById('countdown');
  const nextBtn = document.getElementById('next-button');
  const resultDiv = document.getElementById('result');
  const backBtn = document.getElementById("back-button");
  let currentIndex = 0;
  let score = 0;
  let timer;
  let showButtonTimer;

  const path = window.location.pathname;
  const category = path.split("/")[2];

  const correctAnswers = {
    math: { q1: 'B', q2: 'A' },
    animals: { q1: 'B', q2: 'B' },
    places: { q1: 'C', q2: 'B' }
  };

  function showQuestion(index) {
    const question = quizData[index];
    container.innerHTML = `
      <div class="question-box">
        <p><strong>${index + 1}. ${question.text}</strong></p>
        ${question.options.map(opt => `
          <label>
            <input type="radio" name="${question.name}" value="${opt[0]}"> ${opt[0]}. ${opt[1]}
          </label><br>
        `).join("")}
      </div>
    `;

    nextBtn.style.display = "none";
    startQuestionTimer();
  }

  function startQuestionTimer() {
    let timeLeft = 10;
    countdownEl.textContent = timeLeft;

    clearInterval(timer);
    clearTimeout(showButtonTimer);

    timer = setInterval(() => {
      timeLeft--;
      countdownEl.textContent = timeLeft;

      if (timeLeft <= 0) {
        clearInterval(timer);
        handleNext();
      }
    }, 1000);

    // Tampilkan tombol setelah 3 detik
    showButtonTimer = setTimeout(() => {
      nextBtn.style.display = "inline-block";
    }, 3000);
  }

  function handleNext() {
    const selected = document.querySelector('input[name="' + quizData[currentIndex].name + '"]:checked');
    const correct = correctAnswers[category];

    if (selected && selected.value === correct[quizData[currentIndex].name]) {
      score++;
    }

    currentIndex++;
    if (currentIndex < quizData.length) {
      showQuestion(currentIndex);
    } else {
      container.innerHTML = "";
      document.getElementById("timer-container").style.display = "none";
      nextBtn.style.display = "none";
      resultDiv.innerHTML = `
        <h3>Kuis Selesai!</h3>
        <p>Kamu menjawab ${score} dari ${quizData.length} soal dengan benar.</p>
        <strong>Skor kamu: ${Math.round((score / quizData.length) * 100)}%</strong>
      `;
      backBtn.style.display = "inline-block";
    }
  }

  nextBtn.addEventListener("click", () => {
    clearInterval(timer);
    handleNext();
  });

  showQuestion(currentIndex);
}

// ========== Slideshow (jika kamu gunakan di halaman lain) ==========

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

const nextSlideBtn = document.getElementById('nextBtn');
const prevSlideBtn = document.getElementById('prevBtn');

if (nextSlideBtn && prevSlideBtn) {
  nextSlideBtn.addEventListener('click', () => {
    current = (current + 1) % slides.length;
    updateSlides();
  });

  prevSlideBtn.addEventListener('click', () => {
    current = (current - 1 + slides.length) % slides.length;
    updateSlides();
  });

  updateSlides();
}


// Tampilkan hasil
resultDiv.innerHTML = `
    Kamu menjawab ${score} dari ${total} soal dengan benar.<br>
    Skor kamu: <strong>${Math.round((score / total) * 100)}%</strong>
`;

document.getElementById("back-button").style.display = "inline-block";
