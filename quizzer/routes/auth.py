from flask import render_template, request, redirect, url_for, Blueprint, flash, session
from .auth_form import *

from werkzeug.security import generate_password_hash
from quizzer.services import create_user
from flask_login import login_user, login_required, logout_user, current_user
from quizzer.services import verify_login, create_user, send_otp

from werkzeug.security import generate_password_hash
from quizzer.model import User


auth = Blueprint("auth", __name__, static_folder="static", template_folder="templates")


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginFormValidate()
    if form.validate_on_submit():
        username_email = form.username_email.data
        password = form.password.data
        remember = form.remember.data or False

        user = verify_login(identifier=username_email, password=password)
        print(user)
        if not user:
            flash("Wrong Username/Email Or Password")
            # print("login fail")
        else:
            login_user(user, remember=False)
            # print("login succeesful")
            flash("login SucessFull", category="success")
            return redirect(url_for("view.profile"))

    return render_template("login.html", form=form)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    signup_form = SignUpValidate()
    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data
        confirm_password = signup_form.confirm_password.data
        email = signup_form.email.data

        print("in routes")
        print(username, email, password)

        # session['otp']=send_otp(email)

        # return redirect(url_for('otp',username=username,
        #             email=email,
        #             password=generate_password_hash(password, method="pbkdf2:sha1")))

        create_user(
            username=username,
            email=email,
            password=generate_password_hash(password, method="pbkdf2:sha1"),
        )

        return "validate Sucessfull"
    print(signup_form.errors)
    return render_template("signup.html", form=signup_form)


@auth.route("signup/verification", methods=["POST", "GET"])
def otp(username, email, password):
    if request.method == "POST":
        otp_digits = request.form.getlist("opt-code")
        opt_code = "".join(otp_digits)

        if "otp" in session:
            if otp == opt_code:
                create_user(
                    username=username,
                    email=email,
                    password=password,
                )

    return render_template("otp.html")


@auth.route("/logout")
def logout():

    pass
