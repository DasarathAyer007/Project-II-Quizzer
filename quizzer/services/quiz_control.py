from flask import session,redirect,url_for
from .store_question import store_question
from .check_answer import check_answer

def question_for_quiz():
    # previous_question=session.get('current_question',[])




    category=None
    if 'category' in session:
      # number_of_questions = int(request.args.get('no-of-question', 5))
        category=session.get('category',None)
    return store_question(category) 





def check_answer_question(question, answer):
    result=check_answer(question,answer)
    quiz_engine(result.get('is_correct'))
    result["current_score"]=session['score']
    return result

def quiz_engine(check):
    if session['mode']=="classic":
        classic(check)
    elif session['mode']=='timed':
        timed(check)
    elif session['mode']=='survival':
        surival(check)

def catogery():
    pass


def random():
    pass


def classic(result):
    if result:
     
        session['score']+=10

    else:
        score=int(session['score'])
        session['score']=max(0, score-5)


def timed(result):
    if result:
        session['score']+=10
        score=session['score']
   

def surival(result):
    if result:
        session['score']+=10
        score=session['score']

    else :
        session['quiz_ended']=True 
        
        