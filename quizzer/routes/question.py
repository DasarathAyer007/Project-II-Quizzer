from flask import Blueprint,jsonify,session,request,render_template,url_for,redirect,flash
# from services import store_question,check_answer 
from ..services import add_new_question,get_question_by_id,set_question_report,get_all_catogery
from flask_login import  login_required,current_user
from quizzer.extensions import CATEGORIES
from .auth_form import AddQuestionValidate


question=Blueprint('question',__name__,static_folder="static",template_folder="templates")


# @question.route('/add_question',methods=['POST','GET'])
# @login_required
# def add_question():
#     if request.method=='POST':
#         question_text=request.form.get('question_text')
#         option_1=request.form.get('option_1')
#         option_2=request.form.get('option_2')
#         option_3=request.form.get('option_3')
#         option_4=request.form.get('option_4')
#         correct_option=request.form.get('correct_option')
#         category_name=request.form.get('category')
                
#         #validate the question
#         user_id=current_user.id
        
#         add_new_question(question_text=question_text,option_1=option_1,option_2=option_2 ,option_3=option_3,option_4=option_4,correct_option=correct_option,user_id=user_id,category_name=category_name)
        
        
#     return render_template("add_question.html",categories=CATEGORIES)


@question.route('/add_question',methods=['POST','GET'])
@login_required
def add_question():
    
    add_question_form = AddQuestionValidate()
    categories = get_all_catogery()
    add_question_form.category.choices = [('', 'Select a category')]+[(str(c.id), c.category_name) for c in categories]

    if add_question_form.validate_on_submit():
        question_text=add_question_form.question_text.data.strip()
        option_1=add_question_form.option_1.data
        option_2=add_question_form.option_2.data
        option_3=add_question_form.option_3.data
        option_4=add_question_form.option_4.data
        correct_option=add_question_form.correct_option.data
        category_id=int(add_question_form.category.data)
                
        print("in add question")
 
        user_id=current_user.id
        
        print(question_text,option_1,option_2 ,option_3,option_4,correct_option,user_id,category_id)
        message, status= add_new_question(question_text=question_text,option_1=option_1,option_2=option_2 ,option_3=option_3,option_4=option_4,correct_option=correct_option,user_id=user_id,category_id=category_id)
        
        
        flash(message, status)
        if status == 'success':
            # Reset the form only if question was added successfully
            return redirect(url_for('question.add_question'))

    print(add_question_form.errors)
        
        
    return render_template("add_question.html",form=add_question_form)

@question.route('/edit_question/<int:question_id>/<int:user_id>')
@login_required 
def edit_question_by_user(question_id,user_id):
    if user_id!=current_user.id:
        return "user id didn't match"
    
    
        
@question.route('/report_question/<int:id>')
@question.route('/report_question',methods=['POST','GET'])
@login_required 
def report_question(id=None):
    if request.method=='POST':
        question_id=request.form.get('q_id')
        question_text=request.form.get('q_text')
        reason=request.form.get('reason')
        
        set_question_report(user_id=current_user.id,question_id=question_id,reason=reason,question_text=question_text)
        
            
    question=get_question_by_id(id)
    
    return render_template("report_question.html",question=question)