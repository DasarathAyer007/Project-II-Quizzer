from os import urandom

SECRET_KEY=urandom(24) 
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/db_quizzer'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/db_quizzer'

SQLALCHEMY_TRACK_MODIFICATIONS = False



# Email configuration
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'dasarathayer007@gmail.com'
MAIL_PASSWORD = 'vnix rcnm kgwj cwgs'