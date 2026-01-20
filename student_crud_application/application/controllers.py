from .models import Student, Course, Enrollments
from flask import render_template, request, redirect, url_for
from app import app 
from application.database import db 
from sqlalchemy import select
from sqlalchemy.orm import Session

@app.route('/', methods = ['GET'])
def home():

    #used to get the file address 
    #sqlite3:///database.sqlite3 is a instance database 
    db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    #DEBUG: print(f"Flask database uri: {db_uri}")

    #students = []
    students = Student.query.all()
    #DEBUG: print(students[0].first_name) #printing the first name of the first student 
    app.logger.debug("Accessed the student table")

    return render_template('index.html', students_data = students)


@app.route('/student/create', methods = ['GET', 'POST'])
def add_student():

    if request.method == 'GET':

        return render_template('add_student.html')
    
    if request.method == 'POST': 

        form = request.form 
        #debug 
        roll_num = form['roll'] ; first_name = form['f_name'] ; last_name = form['l_name'] ; courses = form.getlist('courses')

        #DEBUG: print(courses)

        prev_student_id = Student.query.order_by(Student.student_id.desc()).first()

        details = []

        for course in courses: 

            course_details_list = Course.query.filter(Course.course_id == course[-1]).all()

            for course_details in course_details_list: 

                details.append(course_details)


        for course in details: 

            enrollment = Enrollments(estudent_id = int(prev_student_id.student_id) + 1 , ecourse_id = course.course_id)
            db.session.add(enrollment)
        
        db.session.commit()

        #DEBUG: print(roll_num)

        results = Student.query.filter(Student.roll_number==roll_num).all()

        #DEBUG:print(results)

        if results : 
            return render_template('student_exists.html')
        
        else: 

            new_student = Student(roll_number = roll_num, first_name = first_name, last_name = last_name )

            db.session.add(new_student)
            db.session.commit()

            return redirect(url_for('home'))

@app.route('/student/<int:student_id>/update', methods = ['POST', 'GET'])
def update_student(student_id): 

    #DEBUG: print(f"Method: {request.method}, Student ID: {student_id}") 

    student = Student.query.filter(Student.student_id == student_id).first()

    if request.method == 'GET': 
        return render_template('update_student.html', student = student)

    if request.method == 'POST':

        form = request.form 

        student.roll_number = form.get('roll')
        student.first_name = form.get('f_name')
        student.last_name = form.get('l_name')

        db.session.commit()

        return redirect(url_for('home'))
    
@app.route('/student/<int:student_id>/delete', methods = ['GET'])
def delete_student(student_id):

    student = Student.query.filter(Student.student_id==student_id).first()

    if not student:
        print('Student not found!', 'error')
        return redirect(url_for('home'))
    
    db.session.delete(student)
    db.session.commit()
    
    return redirect(url_for('home'))

@app.route('/student/<int:student_id>', methods = ['GET'])
def student_data(student_id): 

    student = Student.query.filter(Student.student_id==student_id).first()

    enrollments = Enrollments.query.filter(Enrollments.estudent_id == student_id).all()

    course_ids = [enrollment.ecourse_id for enrollment in enrollments]

    courses = []

    for id in course_ids: 

        course_list = Course.query.filter(Course.course_id==id).all()

        for course in course_list:

            courses.append(course)

    return render_template('student_data.html', student=student, courses = courses)
