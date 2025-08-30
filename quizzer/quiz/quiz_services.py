from flask import session
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