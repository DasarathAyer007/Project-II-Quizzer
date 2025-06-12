from flask import session,jsonify
from .fetch import fetch_questions

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