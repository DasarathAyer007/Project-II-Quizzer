from quizzer.extensions import db
from sqlalchemy.orm import relationship

class QuizState(db.Model):
    __tablename__ = 'Quiz_state'
    user_id=db.Column(db.Integer,db.ForeignKey('User.id'),primary_key=True)
    type=db.Column(db.String(15) ,primary_key=True)
    mode=db.Column(db.String(15),primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id'))
    high_score = db.Column(db.Integer)
    attempt = db.Column(db.Integer)

   
    user = relationship("User", back_populates="quiz_states")