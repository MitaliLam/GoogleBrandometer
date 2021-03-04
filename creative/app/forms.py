"""
Description of QuestionForm: Generates a survey name field input and
5 questions and answers for customers to fill out. It would capture the
input of the customers and create a survey based on user input.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    surveyname = StringField('SurveyName',validators=[DataRequired()])
    question1 = StringField('Question1',validators=[DataRequired()])
    answer1a = StringField('Answer1a', validators=[DataRequired()])
    answer1b = StringField('Answer1b', validators=[DataRequired()])
    answer1c = StringField('Answer1c', validators=[DataRequired()])
    answer1d = StringField('Answer1d', validators=[DataRequired()])
    question2 = StringField('Question2')
    answer2a = StringField('Answer2a')
    answer2b = StringField('Answer2b')
    answer2c = StringField('Answer2c')
    answer2d = StringField('Answer2d')
    question3 = StringField('Question3')
    answer3a = StringField('Answer3a')
    answer3b = StringField('Answer3b')
    answer3c = StringField('Answer3c')
    answer3d = StringField('Answer3d')
    question4 = StringField('Question4')
    answer4a = StringField('Answer4a')
    answer4b = StringField('Answer4b')
    answer4c = StringField('Answer4c')
    answer4d = StringField('Answer4d')
    question5 = StringField('Question5')
    answer5a = StringField('Answer5a')
    answer5b = StringField('Answer5b')
    answer5c = StringField('Answer5c')
    answer5d = StringField('Answer5d')
    submit = SubmitField('Create')
