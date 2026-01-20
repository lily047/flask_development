import os 

#seeting up the basic configuration class
class Config:
    Debug = False 
    SQLITE_DB_DIR = None 
    SQLALCHEMY_DATABASE_URI = None 

class LocalDevelopmentConfig:
    Debug = True 
    SQLITE_DB_DIR = None 
    SQLALCHEMY_DATABASE_URI = None 

class TestingConfig:
    Debug = True 
    SQLITE_DB_DIR = None 
    SQLALCHEMY_DATABASE_URI = None 