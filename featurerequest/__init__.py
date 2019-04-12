import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

app = Flask(__name__)
csrf = CSRFProtect(app)

APP_STATUS = os.getenv('BRITECORE_APP_STATUS')


if APP_STATUS == 'development':
    app.config.from_object('featurerequest.config.DevelopmentConfig')
    print("Development")
elif APP_STATUS == 'production':
    app.config.from_object('featurerequest.config.ProductionConfig')
else:
    app.config.from_object('featurerequest.config.TestingConfig')



db = SQLAlchemy(app)
migrate = Migrate(app, db)

from featurerequest.views import *




