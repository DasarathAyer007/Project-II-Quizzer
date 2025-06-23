from flask import session,jsonify
import requests
from random import shuffle
from quizzer.extensions import db
from quizzer.model import Question,Category
from html import unescape
def store_question(category):
    

   if 'store_question' not in session:
        session['store_question']=[]
        session['question_index'] = 0
   
   if not bool(session['store_question']) or session.get('question_index', 0) >= len(session['store_question']):
         session['store_question']=(fetch_questions(category))
         session['question_index'] = 0 
      
 
   question_index = session.get('question_index', 0)
   question_list = session.get('store_question', [])

   # print(question_list)

   if question_index < len(question_list):
      question_data = question_list[question_index]
      session['question_index'] = question_index + 1
      

      return question_data
   else:
      pass
   
   

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
        question_text = unescape((q["question"]))
        correct =  unescape(q["correct_answer"])
        incorrect = unescape(q["incorrect_answers"])
        options = incorrect + [correct]
        shuffle(options)

        formatted_questions.append({
            'question_text': question_text,
            'correct_answer': correct,
            'options': options 
        })


   return formatted_questions


def fetch_from_database(category=None):
   
   used_ids = session.get('used_question_ids', [])
   
   query = Question.query
   query = query.filter(~Question.id.in_(used_ids))
   
   if category is not None:  
      category = Category.query.filter_by(category_name=category).first()
      
      query=query.filter_by(category_id=category.id)
      
      
   questions = query.order_by(db.func.random()).all()
   # print(questions.question_text)
      
   

   
   formatted_questions = []
   for q in questions:
        question_text = q.question_text
        option_a=q.option_a
        option_b=q.option_b
        option_c=q.option_c
        option_d=q.option_d
        correct_option = q.correct_option
        options=[option_a,option_b,option_c,option_d]
   
        
        shuffle(options)

        formatted_questions.append({
            'question_text': question_text,
            'correct_answer': correct_option,
            'options': options 
        })
        
   return formatted_questions[0]
