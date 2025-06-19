from flask import Flask,Blueprint
from flask_login import LoginManager
from flask_mail import Mail

def create_app():
    app=Flask(__name__ , static_folder='../static',template_folder="../templates")
    # app.secret_key=urandom(24) 

    from .view import view
    from .question import question
    from .quiz import quiz
    from .auth import auth
    from model import db,User
    
    app.config.from_pyfile('config.py')
    
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/db_quizzer'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    mail = Mail(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login' 

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    app.register_blueprint(view,url_prefix='/')
    app.register_blueprint(quiz,url_prefix='/quiz')
    app.register_blueprint(auth,url_prefix='/auth')
    app.register_blueprint(question,url_prefix='/question')
    
    return app








#   category=''
#     if type.lower()=='category':
#        category = request.args.get('category-name') 
#        session['category']=category
#        return render_template(f'quiz/{type}/{mode}.html', category=category,count_down=time)
       
       
#     if mode.lower()=='classic':
#       number_of_questions = request.args.get('no-of-question', type=int) 
#       session['no_of_question_to_asked']=number_of_questions
#       return render_template(f'quiz/{type}/{mode}.html',number_of_questions=number_of_questions,count_down=time)
    
#     if type.lower()=='category' and mode.lower()=='classic':
#        session['category']=category
#        session['no_of_question_to_asked']=number_of_questions
#        return render_template(f'quiz/{type}/{mode}.html', category=category, number_of_questions=number_of_questions,count_down=time)
    
#     return render_template(f'quiz/{type}/{mode}.html',count_down=time)