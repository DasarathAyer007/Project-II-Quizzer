from quizzer.extensions import db

class QuestionReport(db.Model):
    __tablename__ = 'Question_report'
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('User.id'))
    quiestion_id=db.Column(db.Integer,db.ForeignKey('Question.id'))
    report_reason = db.Column(db.String(100), nullable=False ,unique=True)
    
    

