from flask import Blueprint,render_template

auth=Blueprint('auth',__name__,template_folder='templates',static_folder="static")

@auth.route('/login')
def login():
   return render_template('login.html')


@auth.route('/signup')
def signup():
   return "signup"