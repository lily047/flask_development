import pytest 
import os 
import sys 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#this line is added to access app.py 
#the current directionary is not the same directory as the one app.py is in 
#so we make the path to go back by one folder 

from app import app 

@pytest.fixture 
def client():
    app.app_context().push()
    client = app.test_client()

    # Disable template caching for testing
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    app.jinja_env.cache = {}

    # If you're in testing/development mode
    app.config['TESTING'] = True

    yield client 

def test_form(client):

    response = client.get('/')

    assert b"submit" in response.data 

def test_student_data(client): 

    response = client.post('/', data = {'ID':'student_id', 'id_value':'1001'})

    assert b"Student Details" in response.data 
    assert b"table" in response.data 
    assert b"Total Marks" in response.data 
    assert b"1001" in response.data 

def test_course_data(client):

    response = client.post('/', data = {'ID':'course_id', 'id_value':'2001'})
    print(response.data)

    assert b"Course Details" in response.data 
    assert b"table" in response.data 
    assert b"Average Marks" in response.data
    assert b"Maximum Marks" in response.data 
    assert b"img" in response.data  