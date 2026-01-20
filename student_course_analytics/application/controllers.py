from flask import Flask, render_template, request 
from flask import current_app as app 
from application.models import  DataManager
from jinja2 import Template, Environment, FileSystemLoader 
import matplotlib.pyplot as plt 

env = Environment(loader = FileSystemLoader('templates'))

#using the DataManager class    
data_manager = DataManager()

#creating the dicts from the data in 'data.csv' 
filename_g = 'db_directory/data.csv'
data_manager.load_from_csv(filename_g)


@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods = ['POST'])
def form_data():

    #retreving the data from the form 
    form = request.form

    #extracting the id_value
    id_val = int(form['id_value'])

    #extracting the id
    id =form['ID'] 

    if id == '' or id_val == '':
        return {'error': 'Missing fields'}, 400
    
    print(f"ID recieved: {id}, id_value recieved: {id_val}" )
    
    if id == 'student_id':
    
        template = env.get_template('student_data.html.jinja2')

        content = template.render(student_id = form['id_value'], id = form['ID'], student_dict = data_manager.get_student_courses(id_val))

    elif id == 'course_id':

        course_marks = data_manager.get_course_students(id_val)

        template = env.get_template('course_data.html.jinja2')

        content = template.render(course_dict = course_marks)

        plt.hist(course_marks.values(), bins = 10)
        plt.savefig('static/chart.png')
        plt.close()

    else: 

        return render_template('wrong_input.html')

    with open('templates/output.html', 'w') as f: 
        f.write(content)

    return render_template('output.html')