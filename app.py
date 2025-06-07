from flask import Flask ,render_template,request,redirect,url_for,jsonify,session
import requests
from random import shuffle

app=Flask(__name__)


app.secret_key='jkjfdkjfiejir'

@app.route('/')
@app.route('/home')
def index():
  return render_template('home.html')
   
@app.route('/login')
def login():
   return render_template('login.html')


@app.route('/quiz-intro/<type>/<mode>')
def quiz_intro(type,mode):
   return render_template(f'quiz_intro/{type}/{mode}.html')



@app.route('/quiz-start/<type>/<mode>')
def quiz_start(type,mode):
    session.clear()
    session['type']=type
    session['mode']=mode
    

    number_of_questions=0
    category=''
    if type.lower()=='category':
       category = request.args.get('category-name') 
       session['category']=category
  

       return render_template(f'quiz/{type}/{mode}.html', category=category)
       
    

    if type.lower()=='classic':
      number_of_questions = request.args.get('no-of-question', type=int) 
      session['no_of_question']=number_of_questions
      return render_template(f'quiz/{type}/{mode}.html',number_of_questions=number_of_questions)
    
    if type.lower()=='category' and type.lower()=='classic':
       session['category']=category
       session['no_of_question']=number_of_questions
       return render_template(f'quiz/{type}/{mode}.html', category=category, number_of_questions=number_of_questions)

    return render_template(f'quiz/{type}/{mode}.html')


#temporay for demo
def fetch_questions(category):

   question_url='https://opentdb.com/api.php?amount=5'
   question_category={
   'Film':11,
   'Mythology':20,
   'Sport':21
   }
   if category!=None:
      question_url+=f'&category={question_category[category]}'

   response = requests.get(question_url+'&type=multiple')

   questions = response.json().get('results',[])


   formatted_questions = []
   for q in questions:
        question_text = q["question"]
        correct = q["correct_answer"]
        incorrect = q["incorrect_answers"]
        options = incorrect + [correct]
        shuffle(options)

        formatted_questions.append({
            'question_text': question_text,
            'correct_answer': correct,
            'options': options
        })

   session['question_list'] = formatted_questions
   session['question_index'] = 0
   session['available_no_of_question']=5


   




#@app.route('/api/get_question/<type>/<mode>')
@app.route('/api/get_question/')
def get_question():
   category=None
   if 'category' in session:
      # number_of_questions = int(request.args.get('no-of-question', 5))
      category=session.get('category',None)

   if 'question_list' not in session or session.get('question_index', 0) >= len(session['question_list']):
      if session['type'].lower()=='category':
         fetch_questions(category)
      else:
         fetch_questions(None)
 
   question_index = session.get('question_index', 0)
   question_list = session.get('question_list', [])

   if question_index < len(question_list):
      question_data = question_list[question_index]
      session['question_index'] = question_index + 1
      return jsonify(question_data)
   else:
        # In case something goes wrong, return fallback message
      return jsonify({'error': 'No more questions available'}), 400
   

@app.route('/api/check_question')
def check_question():
   pass





if __name__=='__main__':
    app.run(debug=True)
