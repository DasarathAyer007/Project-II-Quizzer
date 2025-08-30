from flask import session
from quizzer.model import Question


def check_answer_for_database(id,question_text,answer):
   question=Question.query.filter_by(id=id).first()
   
   if question_text.strip().lower()==question.question_text.strip().lower():
      if answer==question.correct_option:
         return ({'question_text':question.question_text,'chosen_option':answer,"is_correct":True,'correct_option':question.correct_option,'current_score':session['score']})
      else:
          if  answer is None:
            return ({'question_text':question.question_text,'chosen_option':None,"is_correct":False,'correct_option':question.correct_option,'current_score':session['score']})

          return ({'question_text':question.question_text,'chosen_option':answer,"is_correct":False,'correct_option':question.correct_option,'current_score':session['score']})
       
   else:
      print(session.get('current_question'))
      print(question)
      print("question din't match")
      return "question didn't match"




def check_answer(question, answer):
 
   question_current=session.get('current_question')
   print(question_current)
   

   if question==question_current.get('question_text'):
      if answer == question_current.get('correct_answer'):
         return ({'question_text':question,'chosen_option':answer,"is_correct":True,'correct_option':question_current.get('correct_answer'),'current_score':session['score']})
         
      else:
         if  answer is None:
            return ({'question_text':question,'chosen_option':None,"is_correct":False,'correct_option':question_current.get('correct_answer'),'current_score':session['score']})

         
         return ({'question_text':question,'chosen_option':answer,"is_correct":False,'correct_option':question_current.get('correct_answer'),'current_score':session['score']})
   else:
      print(session.get('current_question'))
      print(question)
      print("question din't match")
      return "question didn't match"