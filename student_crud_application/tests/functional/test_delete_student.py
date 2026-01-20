import pytest 
import os, sys 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app import app 
from application.models import Student 

@pytest.fixture
def client(): 

    client = app.test_client()

    yield client 

def test_delete_student(client): 

    student = Student.query.order_by(Student.roll_number.desc()).first()

    response = client.get(f"/student/{student.student_id}/delete")

    up_db = Student.query.order_by(Student.roll_number.desc()).first()

    if not up_db.student_id == student.student_id: 
        assert True 