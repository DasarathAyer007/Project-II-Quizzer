from flask import Blueprint,jsonify,session,request,render_template,url_for,redirect
# from services import store_question,check_answer 
from ..services import question_for_quiz,check_answer_question 
from quizzer.extensions import CATEGORIES

import html

question=Blueprint('question',__name__,static_folder="static",template_folder="templates")

@question.route('add_question')
def add_question():
   return render_template("add_question.html",categories=CATEGORIES)

@question.route('report_question')
def report_question():
    return render_template("report_question.html")


@question.route('/get_question/')
def api_question():

   if 'quiz_ended' in session:
         if session.get('quiz_ended'):
            return jsonify({"status": "quiz has ended", "redirect": url_for("quiz.quiz_stop")})
   
   elif not session.get('quiz_ended'):
      question=question_for_quiz()
      
      session["current_question"]=question
      # print('current_questio')
      # print(session["current_question"])

      if question is not None: 
         question["question_text"]=html.unescape(question["question_text"])

       
      return jsonify(question)
   else:
       return jsonify({"error":"start the quiz"})

   
   
@question.route('/check_answer',methods=['POST'])
def api_check_question():
   data=request.get_json()
   choosen_answer=data.get('choosen_answer')
   question_text=data.get('question_text')
   
   response=check_answer_question(question_text,choosen_answer)
   print(f"response{response}")
   session['asked_question'].append(response)
   session.modified = True
   print('current_questio check answer')
   print(session["current_question"])

      
   return jsonify(response)

