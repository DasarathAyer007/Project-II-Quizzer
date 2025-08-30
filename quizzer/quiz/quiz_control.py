from flask import session,redirect,url_for
from .fetch_question import fetch_from_database
from .check_answer import check_answer,check_answer_for_database
from datetime import datetime, timedelta

def question_for_quiz():
    # previous_question=session.get('current_question',[])
   
    category=session.get('category',None)
    question=fetch_from_database(category)
    if question is None:
        session['quiz_ended']=True 
        return ({"status": "quiz has ended", "redirect": url_for("quiz.quiz_stop")})
         
    session["current_question_id"]=question.get('id') 
    
    session['question_asked_time']=datetime.utcnow().isoformat() 
    return question 
   

def check_answer_question(question, answer): 
    id=session.get("current_question_id")
    if is_time_expired():
        result=check_answer_for_database(id,question,None) 
        result.update({"time_expired":True})
    else:
        result=check_answer_for_database(id,question,answer) 
    
    quiz_engine(result.get('is_correct'))
    
    session['asked_question'].append({"id":id,"chosen_option": result['chosen_option']})
     
    session.modified = True
    
    print(session['asked_question'])
    result["current_score"]=session['score']
    print(f"in check anser question{result}")
    
    return result


def is_time_expired():
    if session['mode']=='Timed':
        quiz_start_time=datetime.fromisoformat(session['quiz_start_time'])
        if datetime.utcnow()- quiz_start_time > timedelta(seconds=102):
            session['quiz_ended']=True 
            return True
        else:
            return False
    

    asked_time = datetime.fromisoformat(session['question_asked_time'])    
    if session['mode']=="Classic" or  session['mode']=="Survival":
        if datetime.utcnow() - asked_time > timedelta(seconds=17):
            return True  
        else:
            return False
     
     
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
                 
    if result:
        session['score']+=10

    else:
        score=int(session['score'])
        session['score']=max(0, score-5)
  
def timed(result): 
    if result:
        session['score']+=10
    else:
        pass
     
def surival(result):
    if result:
        session['score']+=10
    else :
        session['quiz_ended']=True 
        
