import pytest 
import os, sys 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app import app 
from application.models import Student 

@pytest.fixture
def client():

    client = app.test_client()

    yield client 

def test_student_exists(client):

    existing_student_roll_number = Student.query.order_by(Student.roll_number.desc()).first()

    response = client.post('/student/create', data = {'roll':existing_student_roll_number.roll_number, 'f_name':'name', 'l_name':'name', 'courses': 'course_1' }, follow_redirects = True)

    assert b"Go Home" in response.data 
    assert b"Student already exists" in response.data 