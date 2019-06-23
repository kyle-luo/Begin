from flask import render_template, flash

from app import app, db, bcrypt

from app.forms import RegisterForm
from app.model import User


@app.route('/')

def go():
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
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        print(username, password, email)
        flash('register succeed!')

    else:
        print('validation failed')
        print(form.errors)
    return render_template('register.html', form=form)
