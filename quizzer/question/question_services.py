# for manipulating question in database
from quizzer.extensions import db
from quizzer.model import Question,Category,QuestionReport
from sqlalchemy.exc import IntegrityError


def add_new_question(
    question_text,
    option_1,
    option_2,
    option_3,
    option_4,
    correct_option,
    user_id,
    category_id=None,
    category_name=None,
):

    category=category_id

    if category_name is not None:
        category_obj = Category.query.filter_by(category_name=category_name).first()
        category=category_obj.id
        print(category)
        
        if category_id is not None:
            if category!=category_id:
                return "category id and name does not match","error"
        
            
    question = Question(
        question_text=question_text,
        option_a=option_1,
        option_b=option_2,
        option_c=option_3,
        option_d=option_4,
        correct_option=correct_option,
        user_id=user_id,
        category_id=category
    )
    db.session.add(question)
    try:
        db.session.commit()
        return "Question added successfully.", "success"
    except IntegrityError as e:
        db.session.rollback()
        error_msg = str(e.orig).lower()

        if "foreign key" in error_msg:
            return "Invalid reference: category or user does not exist.", "error"
        elif "unique" in error_msg:
            return "Duplicate question: this question already exists.", "error"
        elif "not null" in error_msg:
            return "Missing required field: please fill all fields.", "error"
        else:
            return "Database error occurred. Please try again.", "error"
     
    
def set_question_report(user_id,question_id,reason,question_text):
    question=get_question_by_id(question_id)
    
    if question_text!=question.question_text:
        return "question didn't match"
        
    question_report=QuestionReport(user_id=user_id,quiestion_id=question_id,report_reason=reason)
    db.session.add(question_report)
    db.session.commit()
        

def get_question_by_id(id):
    question=Question.query.filter_by(id=id).first()
    return question

def get_question_by_userid(id):
    question=Question.query.filter_by(user_id=id).all()
    return question



def get_all_catogery():
    category=Category.query.all()
    return category

def get_catogery_by_id(id):
    category=Category.query.filter_by(id=id).first()
    return category