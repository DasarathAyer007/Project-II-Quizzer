from flask import session,jsonify
import requests
from random import shuffle
from quizzer.extensions import db
from quizzer.model import Question,Category
from html import unescape


def fetch_from_database(category=None):
   
   used_ids = session.get('used_question_ids', [])
   
   query = Question.query
   query = query.filter(~Question.id.in_(used_ids))
   
   if category is not None:  
      # category = Category.query.filter_by(category_name=category).first()
      query=query.filter_by(category_id=category)
      
      
   questions = query.order_by(db.func.random()).first()
   
   if not questions:
      session['used_question_ids'] = []
      used_ids = []
      query = Question.query
      if category:
         query = query.filter_by(category_id=category)
      questions = query.order_by(db.func.random()).first()

      if not questions:
         return None 
   
   
   option_a=questions.option_a
   option_b=questions.option_b
   option_c=questions.option_c
   option_d=questions.option_d
   correct_option = questions.correct_option
   options=[option_a,option_b,option_c,option_d]
   shuffle(options)
   
   used_ids.append(questions.id)
   session['used_question_ids'] = used_ids
   
   formatted_question={
      'id':questions.id,
      'question_text': questions.question_text,
      'options':options 
   }

   
   return formatted_question


   questions = query.order_by(db.func.random()).all()
   formatted_questions = []
   for q in questions:
        id=q.id
        question_text = q.question_text
        option_a=q.option_a
        option_b=q.option_b
        option_c=q.option_c
        option_d=q.option_d
        correct_option = q.correct_option
        options=[option_a,option_b,option_c,option_d]
   
        
        shuffle(options)

        formatted_questions.append({
            'id':id,
            'question_text': question_text,
            'options': options 
        })
        
   return formatted_questions[0]



