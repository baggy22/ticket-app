from flask import Flask
#from flask_appconfig import AppConfig
from flask import config

app = Flask(__name__)
app.config.from_pyfile('config_default.py')

from app import views
