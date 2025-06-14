
from .config import db 


# MySQL connection (using PyMySQL driver)


class User(db.Model):
    __tablename__ = 'User'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    profile_pic=db.Column(db.String(200))  
    role=db.Column(db.String(20)) 

   


def save_user(username,email,password):
    role="user"
    profile_pic="https://avatar.iran.liara.run/public/boy"
    user=User(username=username,email=email,password=password ,role=role,profile_pic=profile_pic)
    db.session.add(user)
    db.session.commit()
    print(user)

