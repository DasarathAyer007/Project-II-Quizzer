# from pymysql import IntegrityError
# from .question import add_new_question
# from quizzer.model import Category
# from html import unescape
# from random import shuffle
# import requests
# from quizzer.extensions import CATEGORIES,db
# import time


# def set_category():
#     for c in CATEGORIES:
#         try:
#             category = Category(category_name=c)
#             db.session.add(category)
#             db.session.commit()
#         except IntegrityError:
#             db.session.rollback()
#             print("Duplicate entry detected! Category already exists.")
     


# def fetch_questions_for_database():
#     category="Entertainment: Film"
    
    
#     question_url = 'https://opentdb.com/api.php?amount=40'
#     question_category = {
#         "General Knowledge": 9,
#         "Entertainment: Books": 10,
#         "Entertainment: Film": 11,
#         "Entertainment: Music": 12,
#         "Entertainment: Musicals & Theatres": 13,
#         "Entertainment: Television": 14,
#         "Entertainment: Video Games": 15,
#         "Entertainment: Board Games": 16,
#         "Science & Nature": 17,
#         "Science: Computers": 18,
#         "Science: Mathematics": 19,
#         "Mythology": 20,
#         "Sports": 21,
#         "Geography": 22,
#         "History": 23,
#         "Politics": 24,
#         "Art": 25,
#         "Celebrities": 26,
#         "Animals": 27,
#         "Vehicles": 28,
#         "Entertainment: Comics": 29,
#         "Science: Gadgets": 30,
#         "Entertainment: Japanese Anime & Manga": 31,
#         "Entertainment: Cartoon & Animations": 32
#     }

#     # category="Sports"
#     # if category!=None:
#     #    question_url+=f'&category={question_category[category]}'
#     #    categorydb = Category.query.filter_by(category_name=category).first()
#     for key, value in question_category.items():
#         question_url+=f'&category={value}'
        
#         response = requests.get(question_url+'&type=multiple')

#         questions = response.json().get('results',[])
#         time.sleep(8)

#         formatted_questions = []
#         for q in questions:
#             question_text = unescape((q["question"]))
#             correct =  unescape(q["correct_answer"])
#             incorrect = unescape(q["incorrect_answers"])
#             options = incorrect + [correct]
#             shuffle(options)

#             formatted_questions.append({
#                 'question_text': question_text,
#                 'correct_answer': correct,
#                 'options': options 
#             })
            
            
#         for question in formatted_questions:
#             options=question.get('options')
            
#             add_new_question(
#             question_text=question.get('question_text'),
#             option_1=options[0],
#             option_2=options[1],
#             option_3=options[2],
#             option_4=options[3],
#             correct_option=question.get('correct_answer'),
#             user_id=1,
#             category_name=key
#             )
            
      
   
        
        
    
      


