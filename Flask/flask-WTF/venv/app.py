from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_wtf import CsrfProtect

from config import Config
from forms import RegisterForm
from model import User

#init app with Flask
app = Flask(__name__, template_folder='../templates')

#flask-bootstrap render
bs = Bootstrap(app)

#implement config settings
app.config.from_object(Config)

#csrfprotect config
CsrfProtect().init_app(app)

#implement database setting
db = SQLAlchemy(app)

#Bcrypt setting for encryption (like for password, etc)
bcrypt = Bcrypt(app)

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




if __name__ == '__main__':
    app.run(debug=True, port=3000)