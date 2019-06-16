from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from config import Config

app = Flask(__name__)

bs = Bootstrap(app)

app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/')

def go():
    return render_template('nav.html')

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)