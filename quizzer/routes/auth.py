
from flask import render_template,request,redirect,url_for,jsonify,session,Blueprint
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms import DecimalField, RadioField, SelectField, TextAreaField,FileField
from wtforms.validators import InputRequired,Length,EqualTo
from werkzeug.security import generate_password_hash

from services import create_user


class MyForm(FlaskForm):
    username = StringField('Name', validators=[InputRequired(message="Username is required."), Length(min=3, max=15)])
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )

auth=Blueprint('auth',__name__, static_folder="static",template_folder="templates")


@auth.route('/login')
def login():
   if request.method=='POST':
      username=request.form.get('username')
   return render_template('login.html')


@auth.route('/signup',methods=['GET','POST'] )
def signup():
   form = MyForm()
   if form.validate_on_submit():
        username=form.username.data
        password = form.password.data
        confirm_password= form.confirm_password.data
        email=form.email.data

        print("in routes")
        print(username,email,password)
        

        create_user(username=username,email=email,password=generate_password_hash(password, method='pbkdf2:sha1'))



        return "validate Sucessfull"
        # return f'Name: {username} <br> Password: {generate_password_hash(password)} <br> email:{email}'
   print(form.errors)
   return render_template ("signup.html", form=form)

