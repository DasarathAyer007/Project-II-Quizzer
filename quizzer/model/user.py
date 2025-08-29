from quizzer.extensions import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship

class User(db.Model ,UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False ,unique=True)
    email = db.Column(db.String(100), nullable=False,unique=True)
    password = db.Column(db.String(150), nullable=False)
    profile_pic=db.Column(db.String(100))  
    role=db.Column(db.String(20)) 
    
    quiz_states = relationship("QuizState", back_populates="user")
    
    def get_high_score(self, type, mode):
        for qs in self.quiz_states:
            if qs.type.lower() == type.lower() and qs.mode.lower() == mode.lower():
                return qs.high_score or 0
        return 0
    
    def get_attempt(self, type, mode):
        for qs in self.quiz_states:
            if qs.type.lower() == type.lower() and qs.mode.lower() == mode.lower():
                return qs.attempt or 0
        return 0

    # @property
    # def id(self):
    #     return self.user_id
    
    # # def __repr__(self):
    # #     return f"<User {self.user_id} - {self.username}>"

