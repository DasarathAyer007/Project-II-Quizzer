from quizzer.extensions import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship

class Category(db.Model ,UserMixin):
    __tablename__ = 'Category'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(80), nullable=False ,unique=True)
    
    questions = relationship("Question", back_populates="category")