from quizzer.extensions import db

class QuizState(db.Model):
    __tablename__ = 'Quiz_state'
    user_id=db.Column(db.Integer,db.ForeignKey('User.id'),primary_key=True)
    type=db.Column(db.String(20) ,primary_key=True)
    mode=db.Column(db.String(20),primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id'))
    high_score = db.Column(db.Integer)
    attempt = db.Column(db.Integer)

   
