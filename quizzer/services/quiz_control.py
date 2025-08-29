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
        


from quizzer.extensions import db
from quizzer.model import QuizState,Category,Question
from .leaderboard import update_leaderboard

def set_quiz_state(user_id,mode,type,score,category=None):
    print("in set quiz state method")
    
    category_id=category
    # if category is not None:
    #     category_id=Category.query.filter_by(category_name=category).first()
    #     category_id=category_id.id
    
    quiz_state = QuizState.query.filter_by(user_id=user_id, mode=mode, type=type).first()
    
    if quiz_state is None:
        quiz_state=QuizState(user_id=user_id,type=type,mode=mode,category_id=category_id,high_score=score,attempt=1)
        update_leaderboard(type=type,mode=mode,score=score,user_id=user_id,category_id=category_id)
        db.session.add(quiz_state)
    
    else:
        quiz_state.attempt+=1
        if quiz_state.high_score < score:
            update_leaderboard(type=type,mode=mode,score=score,user_id=user_id,category_id=category_id)
            quiz_state.high_score=score
    
    db.session.commit()


def generate_quiz_result():

    asked_question=session.get('asked_question')
    print(asked_question)
    
    result_list=[]
    for q in asked_question:
        question=Question.query.filter_by(id=q.get('id')).first()
        format_result={
            'id':question.id,
            'question_text':question.question_text,
            'correct_option': question.correct_option,
            'chosen_option':q.get('chosen_option')
        }
        result_list.append(format_result)
    
    return result_list
        
        
        
def check_quiz_start(type, mode ,no_of_question,catogery):
    
    if type != "timed" and type !="category" :
        return False
    
    if mode=="classic":
        if no_of_question not in range(5,50):
            return False
    
    if type == 'category':
        pass