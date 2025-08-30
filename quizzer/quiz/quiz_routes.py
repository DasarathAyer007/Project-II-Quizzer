from flask import render_template,request,redirect,url_for,session,Blueprint
from datetime import datetime
from .quiz_services import set_quiz_state,generate_quiz_result
from ..services import get_all_catogery,get_catogery_by_id
from flask_login import  current_user
from quizzer.extensions import CATEGORIES  #make read this categories form database

quiz=Blueprint('quiz',__name__,static_folder=",static",template_folder="templates")

@quiz.route('/intro/<type>/<mode>')
def quiz_intro(type,mode):
   type=type.lower()
   mode=mode.lower()
   category=get_all_catogery()
   return render_template(f'quiz_intro/{type}/{mode}.html',categories=category)


@quiz.route('/start/<type>/<mode>')
def quiz_start(type,mode):
    pop_quiz_session()
    
       
    session['type']=type.title()
    session['mode']=mode.title()
    session['score']=0
    session['quiz_start_time'] = datetime.utcnow().isoformat()
    session['asked_question']=[]
    
    print(session['mode'])
    if mode=="timed":
       time=100
    else:
       time=15
    
    number_of_questions=0
    category=''
    if type.lower()=='category':
       category = request.args.get('category-name') 
       session['category']=category
       
       
    if mode.lower()=='classic':
      number_of_questions = request.args.get('no-of-question', type=int) 
      session['no_of_question_to_asked']=number_of_questions
      print(session['no_of_question_to_asked'])
      
    
    return render_template('quiz/quizbase.html',count_down=time,mode=session['mode'],type=session['type'],category=get_catogery_by_id(category))


@quiz.route('/stop')
def quiz_stop():
   type=session.get('type')
   mode=session.get('mode')
   score=session.get('score')
   category=session.get('category')
   
   if current_user.is_authenticated:
      set_quiz_state(user_id=current_user.id,mode=mode,type=type,score=score,category=category)
   
   return redirect(url_for("quiz.quiz_result", type=type, mode=mode))
  

@quiz.route('/result/<type>/<mode>')
def quiz_result(type, mode):
   if 'mode' not in session:
      print('no sesion')
      return redirect(url_for("quiz.quiz_intro",type=type,mode=mode))

   score=session.get('score')
   questions = generate_quiz_result() #D

   pop_quiz_session()     


   return render_template('quiz/quizresult.html' ,type=type.lower(),mode=mode.lower(),questions=questions,score=score)
   


def pop_quiz_session():
   keys_to_remove = [
        'type', 'mode', 'score', 'quiz_start_time',
        'asked_question', 'quiz_ended', 'no_of_question_to_asked', 'category'
    ]
   for key in keys_to_remove:
        session.pop(key, None)