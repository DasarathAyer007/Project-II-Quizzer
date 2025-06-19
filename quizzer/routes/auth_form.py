from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, EmailField, IntegerField
from wtforms.validators import (
    InputRequired,
    Length,
    EqualTo,
    ValidationError,
    Regexp,
    NumberRange,
)
from werkzeug.security import generate_password_hash
from quizzer.services import username_exists, email_exists
import re


class LoginFormValidate(FlaskForm):
    username_email = StringField("UserName or Email", validators=[InputRequired()])
    password = PasswordField(
        "Password",
        validators=[
            InputRequired(),
            Length(min=6, message="Password must be at least 6 characters."),
        ],
    )
    stay_login = BooleanField("Stayed Login")

    def validate_username_email(self, field):
        username_pattern = r"^[a-zA-Z][a-zA-Z0-9_]{4,14}$"
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if not re.match(username_pattern, field.data) and not re.match(
            email_pattern, field.data
        ):
            raise ValidationError("Must be a valid username or email.")


class SignUpValidate(FlaskForm):
    username = StringField(
        "User Name",
        validators=[
            InputRequired(),
            Length(min=5, max=15),
            Regexp(r"^[a-zA-Z][a-zA-Z0-9_]{4,14}$", message="Invalid UserName"),
        ],
    )
    email = EmailField(
        "Email",
        validators=[
            InputRequired(),
            Regexp(
                r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
                message="Invalid Email",
            ),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            InputRequired(),
            Length(min=8, max=30, message="Password must be at least 6 characters."),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            InputRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )

    def validate_username(self, field):
        if username_exists(field.data):
            raise ValidationError("Username already exists.")

    def validate_email(self, field):
        if email_exists(field.data):
            raise ValidationError("Email already registered.")


class OTPValidate(FlaskForm):
    value = StringField(
        validators=[
            InputRequired(message="OTP is required"),
            Regexp(r"^\d{5}$", message="Invalid OTP, must be exactly 5 digits"),
        ]
    )
