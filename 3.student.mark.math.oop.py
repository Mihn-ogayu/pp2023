import math
import numpy as np

#Define classes for Student, Course, Mark, Data
#Data class is the dictionary data for Students, Courses and Marks

class Student:
    def __init__(self,student_id,student_name,student_dob):
        self.student_id = student_id
        self.student_name = student_name
        self.student_dob = student_dob
class Course:
    def __init__(self,course_id,course_name,course_credit):
        self.course_id = course_id
        self.course_name = course_name
        self.course_credit = course_credit
class Mark:
    def __init__(self,student,course,mark):
        self.student = student
        self.course = course
        self.mark = mark
class Data:
    def __init__(self):
        self.student = {}   
        self.course = {}
        self.mark = {}
        self.gpa = {}

    def input_students(self,x):
        # stu_no = int(input("Number of student: "))
        # print(" ")
        for i in range(x):
            print(f'Enter information for student {i+1}')
            stu_id = input("Student ID: ")
            stu_name = input("Student name: ")
            stu_dob = input("Date of birth: ")
            print(" ")
            student = Student(stu_id,stu_name,stu_dob)
            self.student[stu_id] = student
            #After inputing, store data into student dict

    def input_courses(self,x):
        # co_no = int(input("Number of courses: "))
        # print (" ")
        for i in range(x):
            print(f"Enter information for course {i+1}")
            course_id = input("Course ID: ")
            course_name = input("Course name: ")
            course_credit = int(input("Credits: "))
            print(" ")
            # co = {}
            course = Course(course_id,course_name,course_credit)
            self.course[course_id] = course
            #After inputing, store data into course dict

#Define method to list students
    def list_student(self):
        print("Displaying students:")
        print(f"ID \t\tNAME\t\tDOB")
        for student in self.student:
            print(f'{self.student[student].student_id}\t\t{self.student[student].student_name}\t\t{self.student[student].student_dob}')
            
        #     print(f'Name: {self.student[student].student_name}')
        #     print(f'Date of Birth: {self.student[student].student_dob}')
        print(" ")  
        
#Define method to list courses
    def list_course(self):
        print("Displaying courses: ")
        for course in self.course:
            print(f'Course ID: {self.course[course].course_id}')
            print(f'Course Name: {self.course[course].course_name}')
            print(f'Credits: {self.course[course].course_credit}')
            print(" ")

#Define method to input marks
    def input_marks(self):
        x = 1
        while x <= len(self.course):
            course_input = input("Choose course ID for inputing mark: ")
            if course_input in self.course:
                x+=1
                print(f'Course: {self.course[course_input].course_name} - {course_input}')
                for student in self.student:
                    if student in self.student:
                        print(f'\tStudent: {self.student[student].student_name}')
                        input_mark = float(input(f'Mark: '))
                        while self.is_float(input_mark) == True and self.is_inrange(input_mark) == True:
                            break
                        math.floor(input_mark)
                        mak = Mark(student,course_input,input_mark)
                        mk = (student,course_input)
                        self.mark[mk] = mak
                    else:
                        print("Student does not exist.")
                        break
            else:
                print("Course does not exist!")
                continue
        print(" ")

    def is_float(self,x):
        try:
            float(x)
            return True
        except ValueError:
            self.input_marks(x)
    def is_inrange(self,x):
        try:
            if x in(0.0,20.0):
                pass
            return True
        except IndexError:
            return False
#Define method to show marks
    def show_marks(self):
        x = 1
        while x <= len(self.course):
            course_input = input("Enter course ID to show mark: ")
            if course_input in self.course:
                x+=1
                print(f'Course: {self.course[course_input].course_name}, Credits: {self.course[course_input].course_credit}')
                for student in self.mark:
                    mark = self.mark[student]
                    if mark.course == course_input:
                        print(f'Student ID: {mark.student}\tMark: {mark.mark}')
            else:
                print("Course does not exist! ")
                self.show_marks(x)
        

    def calculate_GPA(self):
        x = 1
        marks = np.array([])
        credits = np.array([])
        for student in self.student:
            for marks in self.mark:
                mark = self.mark[marks]
                if mark.student == student:
                    np.append(marks,mark.mark)
                    np.append(credits,self.course[mark.course].course_credit)
                
        while x <= len(self.student):
            x += 1
            gpa = np.average(marks,xweights=credits)
        
        gpa = dict(sorted(gpa.items(),key=lambda item: item[1], reverse=True))
        for stu_id in gpa:
            print(f'Student ID: {stu_id}, GPA: {gpa[stu_id]}')
        print(" ")
#Define a method to show GPA in decending order

#create a teacher Object that manages the student marks
teacher = Data()
# no_stu = int(input("Number of students: \n"))
while True:
    try:
        no_stu = int(input("Number of students: \n"))
        break
    except ValueError:
        print("Not a valid student number, please try again!")
        continue
teacher.input_students(no_stu)
teacher.list_student()

while True:
    try: 
        no_course = int(input("Number of courses: \n"))
        break
    except ValueError:
        print("Not a valid course number, please try again!")
        continue
# no_course = int(input("Number of courses: \n"))
teacher.input_courses(no_course)
teacher.list_course()

teacher.input_marks()
teacher.show_marks()

teacher.calculate_GPA()