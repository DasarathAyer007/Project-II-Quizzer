
from flask import render_template,Blueprint
from flask_login import login_required,current_user
from .view_services import get_leaderboard,get_question_by_userid
# from quizzer.services import fetch_questions_for_database,set_category

view=Blueprint('view',__name__, static_folder="static",template_folder="templates")

@view.route('/')
@view.route('/home')
def home():
  #set_category()
  # fetch_questions_for_database()
  
  return render_template('home.html')



@view.route("/profile")
@login_required 
def profile():
   print(current_user.quiz_states)    
   return render_template("profile.html",added_question=get_question_by_userid(current_user.id))
  
@view.route("/feedback")
def feedback():
  return render_template('feedback.html')
  
  
@view.route("/leaderboard/<type>/<mode>")
def leaderboard(type,mode):

  data=get_leaderboard(type=type,mode=mode)
  
  return render_template("leaderboard.html" ,data=data,type=type,mode=mode) 


@view.route("/about_us")
def about_us():
  return render_template("about_us.html")
  
@view.route('/account_setting')
def account_setting():
  return render_template("account.html")

@view.route("profile_picture")
def profile_pic():
    seeds = {
        "Luna", "Max", "Nova", "Orion", "Rex", "Sky", "Toby", "Zara","Sarah","Aiden","Jude"
        "Echo", "Ash", "Juno", "Kai", "Ivy", "Nico", "Leo", "Milo","Caleb","Sawyer","Alexander","Liam","Chase"
    }

    return render_template('choose_profile_pic.html',seeds=seeds, username="username")