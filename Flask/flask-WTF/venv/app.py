from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from config import Config

from forms import RegisterForm

app = Flask(__name__, template_folder='../templates')

bs = Bootstrap(app)

app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/')

def go():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    # if form.validate_on_submit():
    #     flash("Successfully registered")
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=3000)