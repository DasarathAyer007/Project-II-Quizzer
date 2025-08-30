from flask import render_template, request, redirect, url_for, Blueprint, flash, session
from .auth_form import *
from werkzeug.security import generate_password_hash
from .auth_services import create_user
from flask_login import login_user, login_required, logout_user, current_user
from .auth_services import verify_login, create_user, send_otp

from werkzeug.security import generate_password_hash

auth = Blueprint("auth", __name__, static_folder="static", template_folder="templates")

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginFormValidate()
    if form.validate_on_submit():
        username_email = form.username_email.data
        password = form.password.data
        stay_login = form.stay_login.data or False

        user = verify_login(identifier=username_email, password=password)
        if not user:
            flash("Wrong Username/Email Or Password")
        else:
            login_user(user, remember=stay_login)
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

        print(username, email, password)

        session["otp"] = send_otp(email)

        print(session["otp"])

        if session.get("otp") is None:
            flash("signup failed Check your Email", category="success")
            return redirect(url_for("auth.signup"))
        else:
            session["signup_user"] = {
                "username": username,
                "email": email,
                "password": password,
            }

            return redirect(url_for("auth.otp_verify"))

    return render_template("signup.html", form=signup_form)


@auth.route("signup/verification", methods=["POST", "GET"])
def otp_verify():
    if request.method == "POST":
        otp_digits = request.form.getlist("opt-code")
        opt_code = "".join(otp_digits)
        
        signup_data = session.get("signup_user")

        if "otp" not in session or not signup_data:
            flash("Signup session expired Try again", category="error")
            return redirect(url_for("auth.signup"))

        

        if int(session["otp"]) == int(opt_code):

            create_user(
                username=signup_data["username"],
                email=signup_data["email"],
                password=generate_password_hash(
                    signup_data["password"], method='pbkdf2:sha256'
                )
            )
            user = verify_login(identifier=signup_data["username"], password=signup_data["password"])
            login_user(user, remember=False)
            session.pop("signup_user", None)
            session.pop("opt", None)
            flash("login SucessFull", category="success")
            return redirect(url_for("view.profile"))
        else:
            flash("Wrong OTP")
            return render_template("otp.html")

    return render_template("otp.html")


@auth.route("/logout")
@login_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for("auth.login"))
