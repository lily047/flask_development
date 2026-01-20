from sqlalchemy import inspect 
import os, sys 
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from application.database import db 
from app import app

@pytest.fixture #fixtures cannot be called directly 
def inspector():

    with app.app_context(): 

        print("This test is being executed.")

        inspector = inspect(db.engine)
        #yeilding inspector which can be used outside this function too 
        yield inspector  


#function to test whether the tables even exist 
def test_tables(inspector):

    tables =  inspector.get_table_names()

    if tables: 
        assert 'student' in tables 
        assert 'course' in tables 
        assert 'enrollments' in tables 
    else: 
        assert False 

def get_columns(inspector, table_name):

    columns = inspector.get_columns(table_name)
    column_names = [column['name'] for column in columns]

    return column_names

#test to check if all the columns in the student table exist 
def test_student_table(inspector): 

    columns  = get_columns(inspector, 'student')

    assert 'student_id' in columns 
    assert 'roll_number' in columns 
    assert 'first_name' in columns 
    assert 'last_name' in columns 


#test to check if all the columns in the course table exist 
def test_course_table(inspector): 

    columns  = get_columns(inspector, 'course')

    assert 'course_id' in columns 
    assert 'course_code' in columns 
    assert 'course_name' in columns 
    assert 'course_description' in columns 

#test to check if all the columns in the enrollments table exist 
def test_enrollments_table(inspector): 

    columns  = get_columns(inspector, 'enrollments')

    assert 'enrollment_id' in columns 
    assert 'estudent_id' in columns 
    assert 'ecourse_id' in columns 

