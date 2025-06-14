
from flask import render_template,request,redirect,url_for,jsonify,session,Blueprint


view=Blueprint('view',__name__, static_folder="static",template_folder="templates")

@view.route('/')
@view.route('/home')
def index():
  return render_template('home.html')
  # return render_template('quiz/quizresult.html')




