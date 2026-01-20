from flask import Flask 
from flask_cors import CORS 
import os 

def create_app():
    
    #initialises flask application 
    app = Flask(__name__, template_folder = 'templates')

    #enables cross-origin resource sharing. it allows requests from different origins 
    CORS(app)

    #pushing the application 
    app.app_context().push()

    return app 

app = create_app()

from application.controllers import * 

if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = '8000')
