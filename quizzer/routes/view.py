
from flask import render_template,request,redirect,url_for,jsonify,session,Blueprint
from flask_login import current_user,login_required


view=Blueprint('view',__name__, static_folder="static",template_folder="templates")

@view.route('/')
@view.route('/home')
def index():
  return render_template('home.html')



@view.route("/profile")
@login_required 
def profile():
    print(current_user.profile_pic)
    return render_template("profile.html")

