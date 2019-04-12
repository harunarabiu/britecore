import os


MYSQL_USERNAME = os.getenv('MYSQL_USERNAME')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DB = os.getenv('MYSQL_DB')
MYSQL_HOST = os.getenv('MYSQL_HOST')


SECRET_KEY = os.getenv('SECRET_KEY')


class BaseConfig(object):
    DEBUG = False
    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    WTF_CSRF_SECRET_KEY = os.getenv('WTF_CSRF_SECRET_KEY')


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{username}:{password}@{host}/{db}'.format(
        username=MYSQL_USERNAME, password=MYSQL_PASSWORD, host=MYSQL_HOST, db=MYSQL_HOST)


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{username}:{password}@{host}/{db}'.format(
        username=MYSQL_USERNAME, password=MYSQL_PASSWORD, host=MYSQL_HOST, db=MYSQL_HOST)


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{username}:{password}@{host}/{db}'.format(
        username=MYSQL_USERNAME, password=MYSQL_PASSWORD, host=MYSQL_HOST, db=MYSQL_HOST)
