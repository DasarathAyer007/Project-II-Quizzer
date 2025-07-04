
from flask import render_template,request,redirect,url_for,jsonify,session,Blueprint
from flask_login import login_required,current_user
from quizzer.services import get_leaderboard


view=Blueprint('view',__name__, static_folder="static",template_folder="templates")

@view.route('/')
@view.route('/home')
def home():
  return render_template('home.html')



@view.route("/profile")
@login_required 
def profile():
    
    return render_template("profile.html")
  
@view.route("/feedback")
def feedback():
  return render_template('feedback.html')
  
  
@view.route("/leaderboard")
def leaderboard():
  return render_template("leaderboard/random_leaderboard.html" , data=get_leaderboard(type='Random',mode='Classic')) 


@view.route("/about_us")
def about_us():
  return render_template("about_us.html")
  


@view.route("profile_picture")
def profile_pic():
    seeds = {
        "Luna", "Max", "Nova", "Orion", "Rex", "Sky", "Toby", "Zara","Sarah","Aiden","Jude"
        "Echo", "Ash", "Juno", "Kai", "Ivy", "Nico", "Leo", "Milo","Caleb","Sawyer","Alexander","Liam","Chase"
    }

    return render_template('choose_profile_pic.html',seeds=seeds, username="username")