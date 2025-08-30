# for manipulating question in database
from quizzer.extensions import db
from quizzer.model import Question,Category,QuestionReport
from sqlalchemy.exc import IntegrityError


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