from flask import session,redirect,url_for
from .store_question import store_question
from .check_answer import check_answer
from datetime import datetime, timedelta

def question_for_quiz():
    # previous_question=session.get('current_question',[])

    category=None
    if 'category' in session:
      # number_of_questions = int(request.args.get('no-of-question', 5))
        category=session.get('category',None)
        
    session['quiestion_asked_time']=datetime.utcnow().isoformat()  
    return store_question(category) 



def check_answer_question(question, answer): 
    result=check_answer(question,answer)
    quiz_engine(result.get('is_correct'))
    result["current_score"]=session['score']
    return result

def quiz_engine(check):
    if session['mode']=="Classic":
        classic(check)
    elif session['mode']=='Timed':
        timed(check)
    elif session['mode']=='Survival':
        surival(check)

def catogery():
    pass


def random():
    pass


def classic(result):
    if 'no_of_question_to_asked' in session:
        session['no_of_question_to_asked']-=1
        print(session['no_of_question_to_asked'])
        if session['no_of_question_to_asked']<=0:
            session['quiz_ended']=True 
            
    asked_time = datetime.fromisoformat(session['quiestion_asked_time'])  
    if datetime.utcnow() - asked_time < timedelta(seconds=10):
              
        if result:
            session['score']+=10

        else:
            score=int(session['score'])
            session['score']=max(0, score-5)
    else:
        score=int(session['score'])
        session['score']=max(0, score-5)
        print('in check time')



def timed(result):
    if result:
        session['score']+=10
        

    else:
        pass
     
def surival(result):
    if result:
        session['score']+=10
        score=session['score']

    else :
        session['quiz_ended']=True 
        
        