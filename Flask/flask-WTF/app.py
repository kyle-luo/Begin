from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
db = SQLAlchemy(app)

app.config.from_object(Config)

@app.route('/')

def go():
    return render_template('render templates.html')

def register():
    return "test"


if __name__ == '__main__':
    app.run(debug=True)