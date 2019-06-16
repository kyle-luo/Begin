from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/')

def go():
    return render_template('render templates.html')

# def register():
#     return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)