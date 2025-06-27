from quizzer.extensions import db

class Leaderboard(db.Model):
    __tablename__ = 'Leaderboard'
    # id = db.Column(db.Integer, primary_key=True)
    rank_positon=db.Column(db.Integer, nullable=False,primary_key=True)
    type=db.Column(db.String(20), nullable=False,primary_key=True)
    mode=db.Column(db.String(20), nullable=False,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('User.id'))
    # user_id=db.Column(db.Integer)
    high_score = db.Column(db.Integer, nullable=False ,)
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id'))
 