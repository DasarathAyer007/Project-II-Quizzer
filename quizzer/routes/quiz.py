from flask import render_template,request,redirect,url_for,jsonify,session,Blueprint
from datetime import datetime, timedelta


quiz=Blueprint('quiz',__name__,static_folder=",static",template_folder="templates")

@quiz.route('/intro/<type>/<mode>')
def quiz_intro(type,mode):
   return render_template(f'quiz_intro/{type}/{mode}.html')


@quiz.route('/start/<type>/<mode>')
def quiz_start(type,mode):
    session.clear()
    session['type']=type
    session['mode']=mode
    session['score']=0
    session['quiz_start_time'] = datetime.utcnow().isoformat()
    session['asked_question']=[]
  

    number_of_questions=0
    category=''
    if type.lower()=='category':
       category = request.args.get('category-name') 
       session['category']=category
  
       return render_template(f'quiz/{type}/{mode}.html', category=category)
       
       
    if type.lower()=='classic':
      number_of_questions = request.args.get('no-of-question', type=int) 
      session['no_of_question']=number_of_questions
      return render_template(f'quiz/{type}/{mode}.html',number_of_questions=number_of_questions)
    
    if type.lower()=='category' and type.lower()=='classic':
       session['category']=category
       session['no_of_question']=number_of_questions
       return render_template(f'quiz/{type}/{mode}.html', category=category, number_of_questions=number_of_questions)
    return render_template(f'quiz/{type}/{mode}.html')


@quiz.route('/stop')
def quiz_stop():

   return redirect(url_for("quiz.quiz_result", type=session.get('type'), mode=session.get('mode')))
  

@quiz.route('/result/<type>/<mode>')
def quiz_result(type, mode):

   if not session:
      print('no sesion')
      return redirect(url_for("quiz.quiz_intro",type=type,mode=mode))

   score=session.get('score')
   questions=session.get('asked_question')
   print(questions)

   session.clear()

   return render_template('quiz/quizresult.html' , type=type,mode=mode,questions=questions)
   
