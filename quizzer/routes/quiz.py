from flask import render_template,request,redirect,url_for,session,Blueprint
from datetime import datetime


quiz=Blueprint('quiz',__name__,static_folder=",static",template_folder="templates")

@quiz.route('/intro/<type>/<mode>')
def quiz_intro(type,mode):
   type=type.lower()
   mode=mode.lower()
   return render_template(f'quiz_intro/{type}/{mode}.html')


@quiz.route('/start/<type>/<mode>')
def quiz_start(type,mode):
    keys_to_remove = [
        'type', 'mode', 'score', 'quiz_start_time',
        'asked_question', 'quiz_ended', 'no_of_question_to_asked', 'category'
    ]
    for key in keys_to_remove:
        session.pop(key, None) 
    
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
       session['category']=category.title()
       
       
    if mode.lower()=='classic':
      number_of_questions = request.args.get('no-of-question', type=int) 
      session['no_of_question_to_asked']=number_of_questions
      print(session['no_of_question_to_asked'])
      
    
    if type.lower()=='category' and mode.lower()=='classic':
       session['category']=category.title()
       session['no_of_question_to_asked']=number_of_questions
    
    return render_template('quiz/quizbase.html',count_down=time,mode=session['mode'],type=session['type'],category=session.get('category',None))


@quiz.route('/stop')
def quiz_stop():

   return redirect(url_for("quiz.quiz_result", type=session.get('type'), mode=session.get('mode')))
  

@quiz.route('/result/<type>/<mode>')
def quiz_result(type, mode):

   if 'mode' not in session:
      print('no sesion')
      return redirect(url_for("quiz.quiz_intro",type=type,mode=mode))

   score=session.get('score')
   questions=session.get('asked_question')
   print(questions)

   keys_to_remove = [
        'type', 'mode', 'score', 'quiz_start_time',
        'asked_question', 'quiz_ended', 'no_of_question_to_asked', 'category'
    ]
   for key in keys_to_remove:
        session.pop(key, None) 

   return render_template('quiz/quizresult.html' , type=type.lower(),mode=mode.lower(),questions=questions,score=score)
   
