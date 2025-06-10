from flask import Blueprint,jsonify,session,request,render_template
from .fetch import fetch_questions


question=Blueprint('question',__name__,static_folder="static",template_folder="templates")

@question.route('add_question')
def add_question():
   return render_template("add_question.html")


@question.route('/get_question/')
def get_question():
   category=None
   
   if 'category' in session:
      # number_of_questions = int(request.args.get('no-of-question', 5))
      category=session.get('category',None)

   if 'question_list' in session:
      if not bool(session['question_list']) or session.get('question_index', 0) >= len(session['question_list']):
         session['question_list']+=(fetch_questions(category))
      
 
   question_index = session.get('question_index', 0)
   question_list = session.get('question_list', [])

   if question_index < len(question_list):
      question_data = question_list[question_index]
      session['question_index'] = question_index + 1
 
      return jsonify(question_data)
   else:
      pass
       
      # return jsonify({'error': 'No more questions available'}), 400
   

@question.route('/check_answer',methods=['POST'])
def check_question():
   data=request.get_json()
   choosen_answer=data.get('choosen_answer')
   question_text=data.get('question_text')
   index=session['question_index']-1
   question_list = session.get('question_list', [])
   question_current=question_list[index]
   score=int(session['score'])

   if question_text==question_current.get('question_text'):
      if choosen_answer == question_current.get('correct_answer'):
         session['score']+=1
         score=session['score']
         return jsonify({'your_answer':choosen_answer,"correct":True,'right_option':question_current.get('correct_answer'),'current_score':score})
         
      else:
         return jsonify({'your_answer':choosen_answer,"correct":False,'right_option':question_current.get('correct_answer'),'current_score':score})
   else:
      pass

   # print(choosen_answer)
   # print(question_text)


   # return "hello"
