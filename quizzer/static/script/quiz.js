const showQuestion = document.getElementById("show-question");
const option1 = document.getElementById("option-1");
const option2 = document.getElementById("option-2");
const option3 = document.getElementById("option-3");
const option4 = document.getElementById("option-4");
const score = document.getElementById("score");
const quizMode=document.getElementById("quiz-mode")
const timeExpired=document.getElementById("time-expired-error")
let interval


async function getQuestion() {
    let url = "/api/get_question/";
    let response = await fetch(url);
    let question = await response.json();
    if (question.redirect) {
        window.location.href = question.redirect;  // Redirecting to quiz_stop
    }
    showQuestion.innerText = question.question_text;
    option1.innerText = question.options[0];
    option2.innerText = question.options[1];
    option3.innerText = question.options[2];
    option4.innerText = question.options[3];

    console.log(question);


    if(quizMode.innerText.toLowerCase()!='timed'){
        quizCountDown();
    }
  
}




document.addEventListener("DOMContentLoaded", () => {
    [option1, option2, option3, option4].forEach((element) => {
        element.addEventListener("click", () => {
            submitAnswer(element);
        });
    });
});

function disableOptions(disabled = true) {
    [option1, option2, option3, option4].forEach((el) => {
        el.disabled = disabled;
    });
}


async function submitAnswer(option) {
  disableOptions(true);

    const url = "/api/check_answer";
    if (option ==null){
        choosenAnswer=null
    }else{
     choosenAnswer = option.innerText;
    }

    response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            choosen_answer: choosenAnswer,
            question_text: showQuestion.innerText,
        }),
    });

    answerinfo = await response.json();

       if (answerinfo.time_expired) {
         timeExpired.classList.remove('hidden')
        //  alert('timed Expired')
         option=null
        }
    
    done = await setRightWrong(answerinfo, option);
    console.log(answerinfo);

     if (answerinfo.time_expired) {
         timeExpired.classList.add('hidden')
    }

    getQuestion();
    
    disableOptions(false);
}

 getQuestion();
function setRightWrong(answerinfo, option) {
    let correct
    return new Promise((resolve, reject) => {
        // originBackgrounnd = option1.style.backgroundColor;
        newScore=answerinfo.current_score
        if (answerinfo.is_correct) {
            // option.style.backgroundColor = "green";
            option.classList.add('opt-btn-correct')
            updateScoreFromBackend(newScore)
            score.innerText = String(answerinfo.current_score).padStart(4, '0');
             
        } else {
            // option.style.backgroundColor = "red";
            if(option !=null){
                option.classList.add('opt-btn-wrong')
            }
            updateScoreFromBackend(newScore)
            score.innerText = String(answerinfo.current_score).padStart(4, '0');
            [option1, option2, option3, option4].forEach((element) => {
                if (element.innerText === answerinfo.correct_option) {
                    element.classList.add('opt-btn-correct');
                    correct = element
                }
            });
             
        }
        setTimeout(() => {
              if(option !=null){
                
                option.classList.remove('opt-btn-correct')
                option.classList.remove('opt-btn-wrong')
            }
           
            if (correct != undefined) {
                correct.classList.remove('opt-btn-correct')
            }

            resolve("done");
        }, 1000);
    });

}

const countDown = document.getElementById('countdown')
const quizTimerValue = countDown.innerText
console.log(quizTimerValue)

 

const countdownText = document.getElementById("countdown");
const progressCircle = document.getElementById("progress-ring");
// const quizMode = document.getElementById("quizMode");

const radius = 45;
const circumference = 2 * Math.PI * radius;
progressCircle.style.strokeDasharray = `${circumference}`;
progressCircle.style.strokeDashoffset = `0`;

// declare globally so it can be cleared


quizCountDown();
function quizCountDown() {
  clearInterval(interval);
let timer = quizTimerValue
const totalTime = timer;


  interval = setInterval(() => {
    if (timer <= 1) {
      clearInterval(interval);

        if(quizMode.innerText.toLowerCase()=='timed'){
        
//   const quizStopUrl = "{{ url_for('quiz.quiz_stop') | tojson }}";
  // or, shorter (safe when URL has no quotes):
  // const quizStopUrl = "{{ url_for('quiz.quiz_stop') }}";

  window.location.href = '/quiz/stop';


        }
 countDown.innerText = 15
//             submitAnswer(null)
     countDown.innerText = 15
      setProgress(0, totalTime);

      submitAnswer(null); // or custom logic
      return;
    }

    timer -= 1;
    countDown.innerText = timer;
    setProgress(timer, totalTime);
  }, 1000);

  countDown.innerText = timer;
  setProgress(timer, totalTime);
}

function setProgress(timeLeft, totalTime) {
  const offset = circumference - (timeLeft / totalTime) * circumference;
  progressCircle.style.strokeDashoffset = offset;

  // Update color
  if (timeLeft <= totalTime * 0.3) {
    progressCircle.setAttribute("class", "text-red-500 transition-all duration-500");
  } else if (timeLeft <= totalTime * 0.6) {
    progressCircle.setAttribute("class", "text-yellow-400 transition-all duration-500");
  } else {
    progressCircle.setAttribute("class", "text-green-500 transition-all duration-500");
  }
}















const scoreEl = document.getElementById('score');
const scoreChangeEl = document.getElementById('score-change');

let currentScore = 0; // keep track of current score locally

function updateScoreFromBackend(newScore) {
  newScore = Number(newScore);
  if (isNaN(newScore)) return; // invalid score

  const change = newScore - currentScore;
  if (change === 0) return; // no change, no animation

  // Update displayed score
  currentScore = newScore;
//   scoreEl.textContent = currentScore.toString().padStart(4, '0');

  // Show animated + or - change below score
  scoreChangeEl.textContent = (change > 0 ? '+' : '') + change;
  scoreChangeEl.style.color = change > 0 ? '#4F46E5' : '#DC2626'; // indigo or red

  // Animate: fade in and move up
  scoreChangeEl.style.opacity = '1';
  // scoreChangeEl.style.transform = 'translate(-50%, -20px)';

  // Fade out after 800ms
  setTimeout(() => {
    scoreChangeEl.style.opacity = '0';
    scoreChangeEl.style.transform = 'translate(-50%, 0)';
  }, 800);
}
