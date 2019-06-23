from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20), EqualTo('confirm_password')])
    confirm_password = PasswordField('Re-enter Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')