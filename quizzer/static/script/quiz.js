const showQuestion = document.getElementById("show-question");
const option1 = document.getElementById("option-1");
const option2 = document.getElementById("option-2");
const option3 = document.getElementById("option-3");
const option4 = document.getElementById("option-4");
const score = document.getElementById("score");
const quizMode=document.getElementById("quiz-mode")
let interval


async function getQuestion() {
    let url = "/question/get_question/";

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

getQuestion();


document.addEventListener("DOMContentLoaded", () => {
    [option1, option2, option3, option4].forEach((element) => {
        element.addEventListener("click", () => {
            submitAnswer(element);
        });
    });
});

async function submitAnswer(option) {

    const url = "/question/check_answer";
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
    done = await setRightWrong(answerinfo, option);
    console.log(answerinfo);

    getQuestion();
}

function setRightWrong(answerinfo, option) {
    let correct
    return new Promise((resolve, reject) => {
        originBackgrounnd = option1.style.backgroundColor;
        if (answerinfo.is_correct) {
            // option.style.backgroundColor = "green";
            option.classList.add('opt-btn-correct')
            score.innerText = String(answerinfo.current_score).padStart(4, '0');
        } else {
            // option.style.backgroundColor = "red";
            if(option !=null){
                option.classList.add('opt-btn-wrong')
            }
            
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

 quizCountDown();

function quizCountDown() {

    clearInterval(interval)

    let timer = quizTimerValue

    interval = setInterval(() => {
        if (timer <= 1) {
            clearInterval(interval)
             if(quizMode.innerText.toLowerCase()=='timed'){
        
//   const quizStopUrl = "{{ url_for('quiz.quiz_stop') | tojson }}";
  // or, shorter (safe when URL has no quotes):
  // const quizStopUrl = "{{ url_for('quiz.quiz_stop') }}";

  window.location.href = '/quiz/stop';


        }
            countDown.innerText = 15
            submitAnswer(null)

        }

        timer -= 1
        countDown.innerText = timer
    }, 1000)

}

