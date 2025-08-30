def register_blueprints(app):
    from .app.view_routes import view
    from .api import api
    from .quiz.quiz import quiz
    from .auth.auth_routes import auth
    from .question.question import question
    
    app.register_blueprint(view,url_prefix='/')
    app.register_blueprint(quiz,url_prefix='/quiz')
    app.register_blueprint(auth,url_prefix='/auth')
    app.register_blueprint(api,url_prefix='/api')
    app.register_blueprint(question,url_prefix='/question')