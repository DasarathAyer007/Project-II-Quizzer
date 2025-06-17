def register_blueprints(app):
    from .view import view
    from .question import question
    from .quiz import quiz
    from .auth import auth
    
    app.register_blueprint(view,url_prefix='/')
    app.register_blueprint(quiz,url_prefix='/quiz')
    app.register_blueprint(auth,url_prefix='/auth')
    app.register_blueprint(question,url_prefix='/question')