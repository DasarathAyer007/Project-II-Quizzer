# for manipulating question in database
from quizzer.extensions import db
from quizzer.model import Question,Category


def add_new_question(
    question_text,
    option_1,
    option_2,
    option_3,
    option_4,
    correct_option,
    user_id,
    category_name,
):
#     print(
#     question_text,
#     option_1,
#     option_2,
#     option_3,
#     option_4,
#     correct_option,
#     user_id,
#     category_name,
#  )
        
    category = Category.query.filter_by(category_name=category_name).first()
    if not category:
        category = Category(category_name=category_name)
        db.session.add(category)
        db.session.commit() 
            
            
    question = Question(
        question_text=question_text,
        option_a=option_1,
        option_b=option_2,
        option_c=option_3,
        option_d=option_4,
        correct_option=correct_option,
        user_id=user_id,
        category_id=category.id
    )
    db.session.add(question)
    db.session.commit()
