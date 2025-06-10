from flask import Flask,Blueprint
from os import urandom

def create_app():
    app=Flask(__name__)
    # app.secret_key=urandom
    app.secret_key = 'mysecretkey' 

    from .view import view
    from .question import question
    from .quiz import quiz
    from .auth import auth

    app.register_blueprint(view,url_prefix='/')
    app.register_blueprint(auth,url_prefix="/auth")
    app.register_blueprint(quiz,url_prefix='/quiz')
    app.register_blueprint(question,url_prefix='/question')
    


    return app