import os


# class Config(object):
SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never know'
CSRF_ENABLE = True
USERNAME = 'root'
PASSWORD = 'grandmaz'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'demo_01'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD,
                                                              HOST, PORT, DATABASE)
print(DB_URI)
SQLALCHEMY_DATABASE_URI = DB_URI
print(SQLALCHEMY_DATABASE_URI)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True



