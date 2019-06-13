import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #Database configuration
    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlist:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False