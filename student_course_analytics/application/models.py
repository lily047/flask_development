import csv 

#the problem statement asked to deal witht the data o students and courses so i created classes for each of the objects to function properly. 

#student class with student_id as a variable, courses as a dict
class Student:

    def __init__(self, student_id):
        self.student_id = student_id 
        self.courses= {}

    def add_courses(self, course_id, marks):
        self.courses[course_id] = marks 

    def get_marks(self, course_id):
        return self.courses[course_id]
    
    def __repr__(self):
        return f"Student({self.student_id})"
    
    def display_courses(self):
        return self.courses
    

#course class with course-id as a variable, students as a dict
class Course:

    def __init__(self, course_id):
        self.course_id = course_id 
        self.students= {}

    def add_students(self, student_id, marks):
        self.students[student_id] = marks 

    def get_marks(self, student_id):
        return self.students[student_id]
    
    def __repr__(self):
        return f"Student({self.course_id})"
    
    def display_students(self):
        return self.students
    

#a class to manage the data od each of the classes 
# method load_from_csv loads the data from the csv into the particular dicts in student and courses classes  
class DataManager:

    def __init__(self):
        self.students = {}
        self.courses = {}

    def load_from_csv(self, filename):

        with open(filename, newline='') as f:
            #When you use newline='', you're telling Python: "Don't do any automatic newline translation - let the csv module handle it."
            reader = csv.DictReader(f)

            for row in reader:

                row_modified = {k.strip():v.strip() for k,v in row.items()}

                student_id = int(row_modified['Student id'])
                course_id = int(row_modified['Course id'])
                marks = int(row_modified['Marks'])

                if student_id not in self.students:
                    self.students[student_id] = Student(student_id)

                if course_id not in self.courses:
                    self.courses[course_id] = Course(course_id)

                self.students[student_id].add_courses(course_id, marks)
                self.courses[course_id].add_students(student_id, marks)

    def get_student_courses(self, student_id):
        return self.students[student_id].display_courses()
    
    def get_course_students(self, course_id):
        return self.courses[course_id].display_students()
