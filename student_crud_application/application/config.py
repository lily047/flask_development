import os 

#base directory path 
basedir = os.path.abspath(os.path.dirname(__file__))
#navigating to the outside folder 
db_path = os.path.join(".", 'database.sqlite3')
#making it abspath 
db_path = os.path.abspath(db_path)

#Base config 
#setting up the variables 
class Config(): 
    DEBUG = False
    SQLITE_DB_DIR = None 
    SQLALCHEMY_DATABASE_URI = None 

#setting up the database location 
class LocalDevelopmentConfig(Config): 
    DEBUG = True 
    SQLITE_DB_DIR = os.path.join(basedir, db_path)
    SQLALCHEMY_DATABASE_URI= f'sqlite:///{SQLITE_DB_DIR}'
    #SQLALCHEMY_DATABASE_URI= 'sqlite:///database.sqlite3'

#setting up the testing database 
class TestingConfig(Config): 
    DEBUG = True 
    SQLITE_DB_DIR = os.path.join(basedir, db_path)
    SQLALCHEMY_DATABASE_URI= f'sqlite:///{SQLITE_DB_DIR}'
    #SQLALCHEMY_DATABASE_URI= 'sqlite:///database.sqlite3'