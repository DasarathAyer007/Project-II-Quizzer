from quizzer.extensions import db
from flask_login import UserMixin

class Questions(db.Model ,UserMixin):
    __tablename__ = 'Questions'
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False ,unique=True)
    option_a=db.Column(db.String(80), nullable=False)
    option_b=db.Column(db.String(80), nullable=False)
    option_c=db.Column(db.String(80), nullable=False)
    option_d=db.Column(db.String(80), nullable=False)
    correct_option=db.Column(db.String(80), nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('User.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id'))


    

    # @property
    # def id(self):
    #     return self.user_id
    
