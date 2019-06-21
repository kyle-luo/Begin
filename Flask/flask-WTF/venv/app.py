from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt

from config import Config

from forms import RegisterForm

app = Flask(__name__, template_folder='../templates')

bs = Bootstrap(app)

app.config.from_object(Config)
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
@app.route('/')

def go():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = bcrypt.generate_password_hash(form.password.data)
        email = form.mail.data
        print(username, password, email)
        flash("Successfully registered")
    return render_template('register.html', form=form)




if __name__ == '__main__':
    app.run(debug=True, port=3000)