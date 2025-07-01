document.addEventListener("DOMContentLoaded", () => {
  showStartCountdown(() => {
    startQuiz(); 
  });
});

//countdown awal
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
      callback();
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
  
  let userAnswers = [];


  const path = window.location.pathname;
  const category = path.split("/")[2];

const correctAnswers = {
    math: {
      q1: "A",  
      q2: "B",
      q3: "A",
      q4: "B",
      q5: "A",
      q6: "A",
      q7: "A",
      q8: "B",
      q9: "B",
      q10: "A",
      q11: "C",
      q12: "A",
      q13: "A",
      q14: "A",
      q15: "A",
      q16: "A",  
      q17: "B",
      q18: "B",
      q19: "B",
      q20: "A",
      q21: "B",
      q22: "B",
      q23: "A",
      q24: "A",
      q25: "B",
      q26: "C",
      q27: "B",  
      q28: "B",
      q29: "A",
      q30: "A"
    },
    animals: {
      q1: "B",
      q2: "B",
      q3: "A",
      q4: "B",
      q5: "C",
      q6: "A",
      q7: "B",
      q8: "A",
      q9: "B",
      q10: "B",
      q11: "A",
      q12: "A",
      q13: "A",
      q14: "A",
      q15: "A",
      q16: "A",
      q17: "B",
      q18: "B",
      q19: "B",
      q20: "B",
      q21: "A",
      q22: "A",
      q23: "B",
      q24: "B",
      q25: "A",
      q26: "B",
      q27: "A",
      q28: "A",
      q29: "B",
      q30: "A"
    },
    places: {
      q1: 'B',
      q2: 'A',
      q3: 'A',
      q4: 'B',
      q5: 'B',
      q6: 'A',
      q7: 'B',
      q8: 'B',
      q9: 'A',
      q10: 'A',
      q11: 'A',
      q12: 'B',
      q13: 'A',
      q14: 'B',
      q15: 'A',
      q16: 'B',
      q17: 'B',
      q18: 'A',
      q19: 'A',
      q20: 'C',
      q21: 'A',
      q22: 'A',
      q23: 'A',
      q24: 'C',
      q25: 'B',
      q26: 'A',
      q27: 'A',
      q28: 'A',
      q29: 'A',
      q30: 'A'
    }
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

    const progressBar = document.getElementById("progress-bar");
    progressBar.style.width = "100%";

    clearInterval(timer);
    clearTimeout(showButtonTimer);

    timer = setInterval(() => {
        timeLeft--;
        countdownEl.textContent = timeLeft;

        const percentage = (timeLeft / 10) * 100;
        progressBar.style.width = `${percentage}%`;

        if (timeLeft <= 0) {
            clearInterval(timer);
            progressBar.style.width = "0%";
            handleNext();
        }
    }, 1000);

    // tombol muncul setelah 3 detik
    showButtonTimer = setTimeout(() => {
        nextBtn.style.display = "inline-block";
    }, 3000);
}


function handleNext() {
    const selected = document.querySelector('input[name="' + quizData[currentIndex].name + '"]:checked');
    const correct = correctAnswers[category];

    let userAnswer = selected ? selected.value : "Tidak Dijawab";
    let correctAnswer = correct[quizData[currentIndex].name];
    let isCorrect = userAnswer === correctAnswer;

    if (isCorrect) score++;

    userAnswers.push({
      question: quizData[currentIndex].text,
      userAnswer: userAnswer,
      correctAnswer: correctAnswer,
      isCorrect: isCorrect
    });

    currentIndex++;
    if (currentIndex < quizData.length) {
      showQuestion(currentIndex);
    } else {
      showResult();
    }
  }

  function showResult() {
    container.innerHTML = "";
    document.getElementById("timer-container").style.display = "none";
    nextBtn.style.display = "none";

    const finalScore = Math.round((score / quizData.length) * 100);

    let answerReview = userAnswers.map((answer, idx) => {
      let status = answer.isCorrect ? "✅ Benar" : "❌ Salah";
      let userDisplay = answer.userAnswer === "Tidak Dijawab" ? "<i>Tidak Dijawab</i>" : answer.userAnswer;

      return `
        <div class="review-item">
          <strong>${idx + 1}. ${answer.question}</strong><br>
          Jawaban kamu: ${userDisplay}<br>
          Jawaban benar: ${answer.correctAnswer}<br>
          <span style="color:${answer.isCorrect ? 'green' : 'red'}">${status}</span>
          <hr>
        </div>
      `;
    }).join("");

    resultDiv.innerHTML = `
      <h3>Kuis Selesai!</h3>
      <p>Kamu menjawab ${score} dari ${quizData.length} soal dengan benar.</p>
      <strong>Skor kamu: ${finalScore}%</strong>
      <h4>Review Jawaban:</h4>
      ${answerReview}
    `;

    backBtn.style.display = "inline-block";

    fetch("/submit-score", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        category: category,
        score: finalScore
      })
    })
      .then(res => {
        if (!res.ok) {
          console.error("Gagal menyimpan skor");
        }
      })
      .catch(err => console.error("Fetch error:", err));
  }

  nextBtn.addEventListener("click", () => {
    clearInterval(timer);
    handleNext();
  });

  showQuestion(currentIndex);
}

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

