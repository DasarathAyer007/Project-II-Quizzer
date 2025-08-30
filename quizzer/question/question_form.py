from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,SubmitField
from wtforms.validators import (
    Length,
    ValidationError,
    DataRequired,
)


class AddQuestionValidate(FlaskForm):
    question_text = StringField('Question', validators=[
        DataRequired(), Length(max=100,message="Question shuould be under 100 character")
    ])

    option_1 = StringField('Option 1', validators=[DataRequired(), Length(max=20)])
    option_2 = StringField('Option 2', validators=[DataRequired(), Length(max=20)])
    option_3 = StringField('Option 3', validators=[DataRequired(), Length(max=20)])
    option_4 = StringField('Option 4', validators=[DataRequired(), Length(max=20)])

    correct_option = StringField('Correct Option', validators=[DataRequired(),Length(max=20)])
    
    category = SelectField('Category', choices=[], validators=[DataRequired()])

    submit = SubmitField('Add Question')
    

    
    def validate_correct_option(self, field):
        options = [
            self.option_1.data.strip(),
            self.option_2.data.strip(),
            self.option_3.data.strip(),
            self.option_4.data.strip()
        ]

        # Ensure all options are unique
        if len(set(options)) < 4:
            raise ValidationError("All options must be unique.")

        # Ensure correct option matches one of the provided options
        if field.data.strip() not in options:
            raise ValidationError("Correct option must match one of the given options.")
        
    