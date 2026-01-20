import pytest 
import os, sys 

#going to the root dir 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from application.models import Student
from app import app 

students = Student.query.all()

@pytest.fixture
def client():

    client = app.test_client()

    yield client 


#in order to run this test, comment student.query.all() in controllers and set students = []
#otherwise this should always fail
def test_no_student_data(client):

    response = client.get('/')

    assert b"No student found" in response.data 

def test_with_student_data(client): 

    response = client.get('/')

    assert b"table" in response.data 
    assert b"SNo" in response.data 
    assert b"Roll Number" in response.data 
    assert b"First Name" in response.data 
    assert b"Last Name" in response.data 
    assert b"Actions" in response.data 
    assert b"Update" in response.data 
    assert b"Delete" in response.data 
