from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Please Enter a Username'), Length(min=6, max=20)])
    password = PasswordField('Password', validators=[DataRequired(message= u'密码不能为空'), Length(min=6, max=20, message= u'密码不能为空')])
    confirm_password = PasswordField('Password', validators=[DataRequired(), EqualTo(password, message= u'密码不能为空')])
    email = StringField('Email', validators=[DataRequired(), Email(message= u'请输入有效的邮箱地址，比如：username@domain.com')])
    submit = SubmitField('Register')