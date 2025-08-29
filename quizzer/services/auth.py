from quizzer.extensions import db,mail
from sqlalchemy.exc import IntegrityError
from quizzer.model import User
from flask_mail import Message 
from random import randint
from flask import current_app


from werkzeug.security import check_password_hash
import re



def create_user(username,email,password):
    profile_pic=f"https://api.dicebear.com/9.x/initials/svg?seed={username}"
    role="user"
    user=User(username=username,email=email,password=password ,role=role,profile_pic=profile_pic)
    db.session.add(user)

    try:
        db.session.commit()
        return True
    except IntegrityError:
        db.session.rollback()
        return False

def username_exists(username: str) -> bool:
    return User.query.filter_by(username=username.lower()).first() is not None


def email_exists(email: str) -> bool:
    return User.query.filter_by(email=email.lower()).first() is not None



username_pattern = r"^[a-zA-Z][a-zA-Z0-9_]{4,14}$"
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def verify_login(identifier, password):
   
    if re.match(username_pattern, identifier):
        user = User.query.filter_by(username=identifier).first()
        # print(user.username)

    elif re.match(email_pattern, identifier):
        user = User.query.filter_by(email=identifier).first()
    else:
        return False 


    if user and check_password_hash(user.password, password):
        return user

    return False
        
        
def send_otp(email):
    otp=randint(10000,99999)
    print(otp,email)
    subject="OTP for Quizzer Signup"
    try:
        message = Message(subject, sender=current_app.config['MAIL_USERNAME'], recipients=[email])
        message.body = str(otp)
        mail.send(message)
        return otp
        
    except Exception as e:
        return None
  