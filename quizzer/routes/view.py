
from flask import render_template,request,redirect,url_for,jsonify,session,Blueprint
from flask_login import login_required,current_user


view=Blueprint('view',__name__, static_folder="static",template_folder="templates")

@view.route('/')
@view.route('/home')
def index():
  return render_template('home.html')



@view.route("/profile")
@login_required 
def profile():
    
    return render_template("profile.html")
  
  
@view.route("/leaderboard")
def leaderboard():
  return render_template("leaderboard.html") 
  


@view.route("profile_picture")
def profile_pic():
    seeds = {
        "Luna", "Max", "Nova", "Orion", "Rex", "Sky", "Toby", "Zara","Sarah","Aiden","Jude"
        "Echo", "Ash", "Juno", "Kai", "Ivy", "Nico", "Leo", "Milo","Caleb","Sawyer","Alexander","Liam","Chase"
    }

    return render_template('choose_profile_pic.html',seeds=seeds, username="username")