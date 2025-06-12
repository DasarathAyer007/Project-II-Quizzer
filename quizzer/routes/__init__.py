from flask import Flask,Blueprint
from os import urandom

def create_app():
    app=Flask(__name__ , static_folder='../static',template_folder="../templates")
    app.secret_key=urandom(24) 

    from .view import view
    from .question import question
    from .quiz import quiz
   

    app.register_blueprint(view,url_prefix='/')
    app.register_blueprint(quiz,url_prefix='/quiz')
    app.register_blueprint(question,url_prefix='/question')
    


    return app