from jinja2 import Template, Environment, FileSystemLoader
import csv 
import sys 
import matplotlib.pyplot as plt 

#initializing dicts to store the data 
student = {}
course = {}

env = Environment(loader = FileSystemLoader('templates'))
#Environment - engine which proccesses your templates 
#loader is the paramenter to tell how to load the files 
#FileSystemLoader loads templates from the filesystem 

def main():

    #didn't do this on my own but this is smart af took it from a senior's repo 
    def dict_update(dict_name, primary_id, secondary_id, marks):
        
        if primary_id not in dict_name.keys():
            dict_name[primary_id] = {}
            dict_name[primary_id][secondary_id] = {}
        dict_name[primary_id][secondary_id] = marks

    with open('data.csv', newline='') as datafile:
        #reding the data from the csv file 
        reader = csv.DictReader(datafile)

        for row in reader:
            #there is an extra space in the column titles, like ' Course id' removing that space 
            row_modified = {k.strip():v.strip() for k,v in row.items()}
            
            #adding data to the corresponding dictionaries 
            dict_update(student, int(row_modified['Student id']), int(row_modified['Course id']), int(row_modified['Marks']) )
            dict_update(course, int(row_modified['Course id']), int(row_modified['Student id']),  int(row_modified['Marks']) )


    if sys.argv[1] == '-s':
        #extracting the student id from the sys args 
        student_id = int(sys.argv[2])

        if student_id not in student.keys():
            
            template = env.get_template('Wrong_input.html')

            content = template.render()

        else: 
        
            #getting the template from the folder 
            template = env.get_template('Student_Data.html.jinja2')
            #rendering the jinja2 template into html 
            content = template.render(student_data = student[student_id], ID = student_id)

    elif sys.argv[1] == '-c':
        course_id = int(sys.argv[2])

        if course_id not in course.keys():

            template = env.get_template('Wrong_input.html')

            content = template.render()
        
        else:
    
            template = env.get_template('Course_Data.html.jinja2')

            content = template.render(course_data = course[course_id], course_id = course_id)

            plt.hist( course[course_id].values(), bins = 10)
            plt.savefig('static/chart.png')
            plt.close()

    else:
        template = env.get_template('Wrong_input.html')

        content = template.render()


    print("printing the content to be written in the ouput file: ")
    print(content)

    with open('output.html', 'w') as output_file:
            #writing the output html file 
            output_file.write(content)

if __name__=='__main__':
    main()
    debug = True
   