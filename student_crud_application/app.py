from flask import Flask 
from flask_cors import CORS 
import os 
#for logging 
import logging 
from application import config 
from application.config import LocalDevelopmentConfig, TestingConfig
from application.database import db 
from flask_migrate import Migrate

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format = "%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s")
#asctime = timestamp 
#levelname indicates the level of logging 
#name is the placeholder for the logger's name, usually the module's name 
#threadName is the placeholder for the thread which generated the logging message. 
#meesage is the placeholder for the actual log message 

def create_app():

    #creating the app 
    app = Flask(__name__, template_folder= 'templates')

    #making it accessible from everywhere 
    CORS(app)

    #getting the exported environment 
    env = os.getenv("ENV", 'development')

    #if-else block to activate the environment 
    if env == 'production':
        app.logger.info("currently no production environment is set up")
        raise Exception ("No priduction configuration setup")
    
    elif env == 'testing': 

        app.logger.info("Starting testing")
        #DEBUG: print("starting testing ")
        app.config.from_object(TestingConfig)

    else: 
        app.logger.info("starting local development")
        #DEBUG: print("Starting local development")
        app.config.from_object(LocalDevelopmentConfig)

    db.init_app(app) #binds your flask app and db 
    migrate = Migrate(app, db) #connects flask app and SQLAlchemy database 
    app.app_context().push()

    from application.models import Student, Course, Enrollments #loading all the models here so flask-migrate can create them 

    return app 

app = create_app()

from application.controllers import *

if __name__ == '__main__': 
    #DEBUG: print(app.url_map) #prints all registered urls 
    app.run(host='127.0.0.1', port='8000')

    