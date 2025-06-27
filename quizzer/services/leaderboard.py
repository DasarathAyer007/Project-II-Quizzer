from quizzer.model import Leaderboard
def get_leaderboard(type, mode):
    
    leaderboard = Leaderboard.query.filter_by(type=type,mode=mode).order_by(Leaderboard.rank_positon).all()
    print(leaderboard)
    
    return leaderboard
    
