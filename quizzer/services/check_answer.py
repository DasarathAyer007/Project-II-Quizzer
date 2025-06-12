from flask import session


def check_answer(question, answer):
 
   question_current=session.get('current_question',[])
   
   print(question_current)
   score=int(session['score'])

   if question==question_current.get('question_text'):
      if answer == question_current.get('correct_answer'):
         return ({'question_text':question,'chosen_option':answer,"is_correct":True,'correct_option':question_current.get('correct_answer'),'current_score':session['score']})
         
      else:
         
         return ({'question_text':question,'chosen_option':answer,"is_correct":False,'correct_option':question_current.get('correct_answer'),'current_score':session['score']})
   else:
      return "question didn't match"
