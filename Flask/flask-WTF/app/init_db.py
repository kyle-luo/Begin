from flask_sqlalchemy import SQLAlchemy

from app import app

#implement database setting
db = SQLAlchemy(app)

from app.model import User

db.create_all()
user = User(username='dbinit', password='dbinit', email='dbinit@init.com')
db.session.add(user)

print('db created')