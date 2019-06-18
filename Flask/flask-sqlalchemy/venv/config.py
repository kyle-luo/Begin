import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #Secret key configuration
    SECRET_KEY = 'This is a secret key'

    #Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlist:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False