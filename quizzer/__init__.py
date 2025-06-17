from flask import Flask
from .extensions import db, mail, login_manager
from .routes import register_blueprints
from .model import User

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_pyfile('config.py')

    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    
    register_blueprints(app)
    
    with app.app_context():
         db.create_all()

    return app