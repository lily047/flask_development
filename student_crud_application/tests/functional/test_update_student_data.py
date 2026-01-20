import pytest 
import os, sys 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app import app 
from application.models import Student 

@pytest.fixture
def client(): 

    client = app.test_client()

    yield client 

def test_update_data(client): 

    test_id = Student.query.order_by(Student.roll_number.desc()).first()

    response = client.post(f'/student/{test_id.student_id}/update', 
    data = {'roll':test_id.roll_number, 'f_name':f"tested_{test_id.first_name}", 'l_name':test_id.last_name, 'courses':'course_1'},  follow_redirects = True)

    assert b"tested_" in response.data 