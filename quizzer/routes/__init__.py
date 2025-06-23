def register_blueprints(app):
    from .view import view
    from .api import api
    from .quiz import quiz
    from .auth import auth
    from .question import question
    
    app.register_blueprint(view,url_prefix='/')
    app.register_blueprint(quiz,url_prefix='/quiz')
    app.register_blueprint(auth,url_prefix='/auth')
    app.register_blueprint(api,url_prefix='/api')
    app.register_blueprint(question,url_prefix='/question')