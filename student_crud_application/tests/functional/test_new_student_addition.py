import pytest 
import os, sys 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app import app 
from application.models import Student 

@pytest.fixture
def client():

    client = app.test_client()

    yield client 

def test_add_students_to_db(client):

    existing_student_roll_number = Student.query.order_by(Student.roll_number.desc()).first()

    new_roll = int(existing_student_roll_number.roll_number) + 1

    new_name = f"test_user{new_roll}"

    response = client.post('/student/create', data = {'roll':new_roll, 'f_name': new_name, 'l_name' : 'name', 'courses':'course_1' })

    roll_check = Student.query.filter(Student.roll_number == new_roll).first()

    if roll_check: 
        assert True 
    else: 
        assert False 

    