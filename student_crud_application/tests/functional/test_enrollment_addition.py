import pytest 
import os, sys 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app import app 
from application.models import Student, Course, Enrollments

@pytest.fixture 
def client(): 

    client = app.test_client()

    yield client 

def test_enrollment_table_data_entry(client): 

    prev_entry = Student.query.order_by(Student.roll_number.desc()).first()

    new_roll_num = (prev_entry.roll_number + 1)

    response = client.post('/student/create', data = {'roll':new_roll_num, 'f_name':f'test_user{new_roll_num}', 'l_name':f"name", 'courses':['course_1', 'course_3']})

    student_id = Student.query.filter(Student.roll_number == new_roll_num).first().student_id

    result = Enrollments.query.filter(Enrollments.estudent_id == student_id ).all()

    assert result is not None

    print(result)

    flag = False
    
    for enrollment in result: 
        print(type(enrollment.ecourse_id))
        if enrollment.ecourse_id in [1, 3]: 
            flag = True 
    
    assert flag == True  