from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegisterForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Password', validators=[DataRequired(), EqualTo(password)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')