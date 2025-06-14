from flask import Flask,Blueprint
from os import urandom

def create_app():
    app=Flask(__name__ , static_folder='../static',template_folder="../templates")
    app.secret_key=urandom(24) 

    

    from .view import view
    from .question import question
    from .quiz import quiz
    from .auth import auth
    from model import db
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/db_quizzer'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(view,url_prefix='/')
    app.register_blueprint(quiz,url_prefix='/quiz')
    app.register_blueprint(auth,url_prefix='/auth')
    app.register_blueprint(question,url_prefix='/question')
    


    return app