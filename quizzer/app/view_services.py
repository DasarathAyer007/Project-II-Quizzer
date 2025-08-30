from quizzer.model import Leaderboard,User,Category
from sqlalchemy.orm import joinedload
from quizzer.extensions import db
from quizzer.model import Question,Category
def get_leaderboard(type, mode):
    
    #leaderboard = Leaderboard.query.filter_by(type=type, mode=mode).order_by(Leaderboard.rank_positon).all()

    # print(leaderboard)
    print(type,mode)
    leaderboard=Leaderboard.query.join(User).outerjoin(Category).add_columns(
        Leaderboard.rank_positon,
        Leaderboard.type,
        Leaderboard.mode,
        Leaderboard.high_score,
        User.username,
        Category.category_name
    ).filter(
            Leaderboard.type == type,
            Leaderboard.mode == mode
        ).order_by(Leaderboard.rank_positon).all()
    

    return leaderboard
    

def get_question_by_userid(id):
    question=Question.query.filter_by(user_id=id).all()
    return question