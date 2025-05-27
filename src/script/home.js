
document.querySelector('#menu-img').addEventListener('click', () => {
  document.querySelector("#side-nav").classList.toggle("hidden");
})

document.querySelector('#cross-snav').addEventListener('click', () => {
  document.querySelector("#side-nav").classList.toggle("hidden");
});




document.querySelector('#catg-btn').addEventListener('click', () => {
  document.querySelector('#catg-opt').classList.toggle("hidden");
  document.querySelector('#arrow-img').classList.toggle("rotate-90");
});

document.querySelector('#non-catg-btn').addEventListener('click', () => {
  document.querySelector('#non-catg-opt').classList.toggle("hidden");
  document.querySelector('#arrow-img-non').classList.toggle("rotate-90");
});


const modeBar = document.querySelector('#mode-bar');
const showModeBar = document.querySelector('#show-mode-bar');
const hideModeBar = document.querySelector('#hide-mode-bar');


document.querySelectorAll('.mode-opt').forEach(el => {
  el.addEventListener('click', () => {
    modeBar.classList.remove('sm:w-[60%]');
    modeBar.classList.add('sm:w-[27%]');
    modeBar.classList.add('max-sm:hidden');
    modeBar.classList.remove('absolute');
    modeBar.classList.add('max-sm:absolute')
    showModeBar.classList.add("sm:hidden");
    document.querySelector('#select-msg').classList.add('hidden');
    document.querySelector('#main').classList.remove("hidden")
    leaderboard.classList.remove('hidden');

  });
});





hideModeBar.addEventListener('click', () => {
  modeBar.classList.add('hidden',)
  showModeBar.classList.remove("hidden", 'sm:hidden')
  

});

showModeBar.addEventListener('click', () => {
  showModeBar.classList.add('hidden', 'sm:hidden');
  modeBar.classList.remove('hidden', 'max-sm:hidden');
  
});


const leaderboard = document.querySelector('#Leaderboard');
const showLeader = document.querySelector('#show-leader');
const hideLeader = document.querySelector('#hide-leader');



hideLeader.addEventListener('click', () => {
  // document.querySelector('#main').classList.add("w-full")
  leaderboard.classList.toggle("hidden");
  showLeader.classList.toggle("hidden");
});

showLeader.addEventListener('click', () => {
  leaderboard.classList.toggle("hidden");
  showLeader.classList.toggle("hidden")
});

const quizFeild=document.querySelector("#quiz-feild");
const modeInfo=document.querySelector("#mode-info");



const options=document.querySelector('#options');
const optBtn=document.querySelectorAll('.opt-btn ')
const selectedCategory = document.querySelector('#catg-select');


document.querySelector("#start").addEventListener('click',()=>{

  if(catogery){
   console.log(selectedCategory)
   if(selectedCategory.value==''){

    alert('select a catogery')
    return false;
    
   }
  }
  modeInfo.classList.add('hidden');  
  const timer=document.querySelector('#quiz-start-timer');
  timer.classList.remove('hidden');
  timer.classList.add('flex')

   quizFeild.classList.remove('hidden');
      quizFeild.classList.add('flex')

  const startCountdown=document.querySelector('#quiz-start-countdown');

  let remaining=3;
  startCountdown.textContent = remaining;
  const interval = setInterval(() => {
    remaining--;
    startCountdown.textContent = remaining;

    if (remaining <= 0) {
      clearInterval(interval);
      //  countdownEl.textContent = "Time!";
        timer.classList.add('hidden');

     
   
    }
  }, 700);

   
})


// function startCountdown(seconds) {
//   const countdownEl = document.getElementById('countdown');
//   let remaining = seconds;

//   countdownEl.textContent = remaining;

//   const interval = setInterval(() => {
//     remaining--;
//     countdownEl.textContent = remaining;

//     if (remaining <= 0) {
//       clearInterval(interval);
//       countdownEl.textContent = "Time!";
//         optBtn.forEach(btn=>{
//     btn.classList.remove('hidden')
//   })

//       // Optionally trigger something when timer ends
//     }
//   }, 1000);
// }




let showQuizInfo=()=>{


  modeInfo.classList.remove('hidden')
  quizFeild.classList.remove('flex');
  quizFeild.classList.add('hidden');
  // startTimer.classList.remove("hidden");

 

}

let select=document.querySelector('#select-div');
let type='';
let catogery=false;
let mode=''


document.querySelector('#n-catg-clas').addEventListener('click', () => {
  setLeaderboardName("Random Battle", "Classic")
  select.classList.add('hidden');
  showQuizInfo();
  type='Non-catogery'
  mode='Classic'
  catogery=false;

});

document.querySelector('#n-catg-time').addEventListener('click', () => {
  setLeaderboardName("Random Battle", "Timed")
  select.classList.add('hidden')
   showQuizInfo();
  
  type='Non-catogery'
  mode="Timed"
  catogery=false;
});

document.querySelector('#n-catg-surv').addEventListener('click', () => {
  setLeaderboardName("Random Battle", "Survival")
  select.classList.add('hidden')
   showQuizInfo();
  
  type='Non-catogery'
  mode="Survival"
  catogery=false;
});

document.querySelector('#catg-clas').addEventListener('click', () => {
  setLeaderboardName(`Catogery Battle`, "Classic")
  select.classList.remove('hidden');
   showQuizInfo();
    
    type="Catogery";
    mode='Classic'
    catogery=true;
  

});

document.querySelector('#catg-time').addEventListener('click', () => {
  setLeaderboardName("Catogery Battle", "Timed")
  select.classList.remove('hidden');
   showQuizInfo();
   type="Catogery"
   mode="Timed"
  catogery=true;
});

document.querySelector('#catg-surv').addEventListener('click', () => {
  setLeaderboardName("Catogery Battle", "Survial")
   select.classList.remove('hidden');
   showQuizInfo();
 
   type="Catogery"
   mode="Survival"
    catogery=true;
});



const setLeaderboardName = (type, mode) => {
  document.querySelectorAll(".quiz-type").forEach(el => {
    el.innerText = type;
  });

  document.querySelectorAll(".quiz-mode").forEach(el => {
    el.innerText = mode;
  });

}







// document.querySelector("#start-btn").addEventListener('click',()=>{

//   if(catogery){
//    const selectedCategory = document.querySelector('#catg-select').value;
//    console.log(selectedCategory)
//    if(selectedCategory=='null'){

//     alert('select a catogery')
    
//    }
//   }
//   startQuiz()
// })
let catogeryulr=''
let apiURL=`https://opentdb.com/api.php?amount=10`
//https://opentdb.com/api.php?amount=10&category=11
const film='11';
const mythology='20';
const sport='21'
let allQuestions = []; // Will hold all 10 questions
let currentIndex = 0;  // Tracks which question to show

const startQuiz = () => {
  if (catogery) {
    const selectedCategory = document.querySelector('#catg-select').value;
  

    if (selectedCategory == 'Film') apiURL += '&category=11&type=multiple';
    if (selectedCategory == 'Sport') apiURL += `&category=21&type=multiple`;
    if (selectedCategory == 'Mythology') apiURL += `&category=20&type=multiple`;

    console.log(apiURL)
  }

  fetchQuestion().then((questions) => {
    if (questions.results && questions.results.length > 0) {
      allQuestions = questions.results;
      currentIndex = 0;
      setQuestion(allQuestions[currentIndex]);
    }
  });
};
document.querySelector('#next').addEventListener('click', () => {
  currentIndex++;
  if (currentIndex < allQuestions.length) {
    setQuestion(allQuestions[currentIndex]);
  } else {
    alert("Quiz completed!");
    // Optionally reset UI or show score
  }
});

let correct_answer=''
async function fetchQuestion() {
    try{
    let res = await fetch(apiURL);
    jsonRes = await res.json();
    // ques = jsonRes.results[0].question;
  
 

    // const wrong = jsonRes.results[0].incorrect_answers;
    // correct = jsonRes.results[0].correct_answer;
    // options = suffle([...wrong, correct]);
    return jsonRes
      
    }catch(err){
        ques="TRY AGAIN";
    }
  }

 function setQuestion(ques){
  console.log(ques)
   document.querySelector('#show-question').innerText= ques.question;
   let wrong = ques.incorrect_answers;
    let correct = ques.correct_answer;
    let options = suffle([...wrong, correct]);

    document.querySelector('#option-1').innerText=options[0]
    document.querySelector('#option-2').innerText=options[1]
    document.querySelector('#option-3').innerText=options[2]
    document.querySelector('#option-4').innerText=options[3]

 }

  function suffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}