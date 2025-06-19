from quizzer.extensions import db
from flask_login import UserMixin

class User(db.Model ,UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False ,unique=True)
    email = db.Column(db.String(100), nullable=False,unique=True)
    password = db.Column(db.String(100), nullable=False)
    profile_pic=db.Column(db.String(100))  
    role=db.Column(db.String(20)) 
    
    

    # @property
    # def id(self):
    #     return self.user_id
    
    # # def __repr__(self):
    # #     return f"<User {self.user_id} - {self.username}>"

