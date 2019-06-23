from flask import render_template, flash, redirect, url_for

from app import app, db, bcrypt

from app.model import User
from app.forms import RegisterForm

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    print('start validating')
    if form.validate_on_submit():
        print('validated')
        username = form.username.data
        password = bcrypt.generate_password_hash(form.password.data)
        email = form.email.data
        db.create_all()
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        print(username, password, email)
        flash('register succeed!', category='success')
        redirect(url_for('index'))
    else:
        print('validation failed')
        print(form.errors)
    return render_template('register.html', form=form)
