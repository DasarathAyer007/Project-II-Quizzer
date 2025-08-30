from flask import Blueprint,jsonify,session,request,url_for
from .quiz.quiz_control import question_for_quiz,check_answer_question 
from quizzer.extensions import CATEGORIES

api=Blueprint('api',__name__,static_folder="static",template_folder="templates")


@api.route('/get_question/')
def api_question():

   if 'quiz_ended' in session:
         if session.get('quiz_ended'):
            return jsonify({"status": "quiz has ended", "redirect": url_for("quiz.quiz_stop")})
   
   elif not session.get('quiz_ended'):
      question=question_for_quiz()
      return jsonify(question)
   else:
       return jsonify({"error":"start the quiz"})

   
@api.route('/check_answer',methods=['POST'])
def api_check_question():
   data=request.get_json()
   choosen_answer=data.get('choosen_answer')
   question_text=data.get('question_text')
   
   response=check_answer_question(question_text,choosen_answer)

   session.modified = True
   print('current_questio check answer')
   return jsonify(response)

