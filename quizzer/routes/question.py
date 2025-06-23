from flask import Blueprint,jsonify,session,request,render_template,url_for,redirect
# from services import store_question,check_answer 
from ..services import add_new_question
from flask_login import  login_required, current_user
from quizzer.extensions import CATEGORIES


question=Blueprint('question',__name__,static_folder="static",template_folder="templates")


@question.route('/add_question',methods=['POST','GET'])
@login_required
def add_question():
    if request.method=='POST':
        question_text=request.form.get('question_text')
        option_1=request.form.get('option_1')
        option_2=request.form.get('option_2')
        option_3=request.form.get('option_3')
        option_4=request.form.get('option_4')
        correct_option=request.form.get('correct_option')
        category_name=request.form.get('category')
        
        
        
        
        #validate the question
        user_id=current_user.id
        
        add_new_question(question_text=question_text,option_1=option_1,option_2=option_2 ,option_3=option_3,option_4=option_4,correct_option=correct_option,user_id=user_id,category_name=category_name)
        
        
    return render_template("add_question.html",categories=CATEGORIES)

@question.route('/report_question')
def report_question():
    return render_template("report_question.html")