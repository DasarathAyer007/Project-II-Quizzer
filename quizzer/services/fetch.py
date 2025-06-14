import requests
from random import shuffle
#temporay for demo
def fetch_questions(category):

   question_url='https://opentdb.com/api.php?amount=5'
   question_category={
   'Film':11,
   'Mythology':20,
   'Sport':21,
   'History':23,
   'Geography':22,
  'Computers':18
   }
   if category!=None:
      question_url+=f'&category={question_category[category]}'

   response = requests.get(question_url+'&type=multiple')

   questions = response.json().get('results',[])
  

   formatted_questions = []
   for q in questions:
        question_text = (q["question"])
        correct = q["correct_answer"]
        incorrect = q["incorrect_answers"]
        options = incorrect + [correct]
        shuffle(options)

        formatted_questions.append({
            'question_text': question_text,
            'correct_answer': correct,
            'options': options 
        })


   return formatted_questions


   