
from flask import render_template,request,redirect,url_for,jsonify,session,Blueprint


view=Blueprint('view',__name__, static_folder="static",template_folder="templates")

@view.route('/')
@view.route('/home')
def index():
  return render_template('home.html')
  # return render_template('quiz/quizresult.html')

@view.route('/login')
def login():
   return render_template('login.html')


@view.route('/signup')
def signup():
   return "signup"



