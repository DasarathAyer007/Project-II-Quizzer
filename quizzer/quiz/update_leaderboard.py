from quizzer.model import Leaderboard,User,Category
from sqlalchemy.orm import joinedload
from quizzer.extensions import db

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
    


def update_leaderboard(type,mode,score,user_id,category_id):    
    #if user already exits in leaderboard
    existing_entry = Leaderboard.query.filter_by(type=type, mode=mode, user_id=user_id).first()

    if existing_entry:
        if score > existing_entry.high_score:
            existing_entry.high_score = score
            rerank_leaderboard(type, mode)
            db.session.commit()
        return    

    leaderboard_entries = (
        Leaderboard.query
        .filter_by(type=type, mode=mode)
        .order_by(Leaderboard.high_score.desc(), Leaderboard.rank_positon.asc())
        .all()
    )


    if len(leaderboard_entries) < 20:
        print('here')
        new_entry = Leaderboard(
            type=type,
            mode=mode,
            user_id=user_id,
            high_score=score,
            category_id=category_id,
            rank_positon=0  # will be updated in rerank
        )
        db.session.add(new_entry)
        rerank_leaderboard(type, mode)
        db.session.commit()
        return

    # check if score is better than the lowest
    lowest_entry = leaderboard_entries[-1]
    if score > lowest_entry.high_score:
        db.session.delete(lowest_entry)
        new_entry = Leaderboard(
            type=type,
            mode=mode,
            user_id=user_id,
            high_score=score,
            category_id=category_id,
            rank_positon=0
        )
        db.session.add(new_entry)
        rerank_leaderboard(type, mode)
        db.session.commit()


def rerank_leaderboard(type_, mode):
    entries = (
        Leaderboard.query
        .filter_by(type=type_, mode=mode)
        .order_by(Leaderboard.high_score.desc(), Leaderboard.user_id.asc())
        .all()
    )

    for idx, entry in enumerate(entries, start=1):
        entry.rank_positon = idx
    
