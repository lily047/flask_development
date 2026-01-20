import os, sys 
import pytest 

#going back to the main folder 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from app import app

#base directory path 
basedir = os.path.abspath(os.path.dirname(__file__))
#navigating to the outside folder 
db_path = os.path.join(".", 'database.sqlite3')
#making it abspath 
db_path = os.path.abspath(db_path)

SQLTE_DB_DIR = os.path.join(basedir, db_path)

def test_db_path(): 

    current_path = app.config['SQLALCHEMY_DATABASE_URI']

    print(f"SQLITE_DB_PATH: {SQLTE_DB_DIR}")

    print(f"current_path: {current_path}")

    assert current_path == f"sqlite:///{SQLTE_DB_DIR}"
