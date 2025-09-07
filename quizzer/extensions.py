from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager

db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()

from functools import wraps
from flask import abort
from flask_login import current_user

def role_required(*roles):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if current_user.role not in roles:
                return abort(403)  # Forbidden access
            return func(*args, **kwargs)
        return decorated_view
    return wrapper

CATEGORIES = [
    "General Knowledge",
    "Science & Nature",
    "Science: Computers",
    "Science: Mathematics",
    "Mythology",
    "Sports",
    "Geography",
    "History",
    "Politics",
    "Art",
    "Celebrities",
    "Animals",
    "Vehicles",
    "Entertainment: Books",
    "Entertainment: Film",
    "Entertainment: Music",
    "Entertainment: Musicals & Theatres",
    "Entertainment: Television",
    "Entertainment: Video Games",
    "Entertainment: Comics",
    "Entertainment: Japanese Anime & Manga",
    "Entertainment: Cartoon & Animations",
]

MODE=[
    "Classic","Timed","Survival"
]

TYPE=["Catogery","Random"]