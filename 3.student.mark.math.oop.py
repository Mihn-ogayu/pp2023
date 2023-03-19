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
        print(f"-"*40)
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
                        if self.is_float(input_mark) == True and self.is_inrange(input_mark) == True:
                            math.floor(input_mark * 10) / 10
                            mak = Mark(student,course_input,input_mark)
                            # mk = (student,course_input)
                            self.mark[input_mark] = mak
                        else:
                            print("Mark is invalid type or out of 0.0 - 20.0 range")
                    else:
                        print("Student does not exist.")
                        break
            else:
                print("Course does not exist!")
                continue
        print(" ")

    def is_float(self,x):
        while True:
            try:
                float(x)
                return True
            except ValueError:
                self.input_marks(x)
    def is_inrange(self,x):
        while True:
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
                x += 1
                print(f'Course: {self.course[course_input].course_name}, Credits: {self.course[course_input].course_credit}')
                for student in self.mark:
                    mark = self.mark[student]
                    if mark.course == course_input:
                        print(f'Student ID: {mark.student}\t\tMark: {mark.mark}')
                print (" ") 
            else:
                print("Course does not exist! ")
                print("Please re-enter from the beginning")
                self.show_marks(x)
        
#Define a method to calculate GPA
    def calculate_GPA(self):
        temp_credit = []
        for course in self.course:
            print(f'Course: {self.course[course].course_name}, Credits: {self.course[course].course_credit}')
            temp_credit.append(self.course[course].course_credit)
        x = 1
        while x <= len(self.student):
            stu_id = input("Enter student ID you want to calculate GPA for: ")
            if stu_id in self.student:
                x += 1
                temp_mark = []
                for mark in self.mark:
                    mark = self.mark[mark]
                    if stu_id == mark.student:
                        # x += 1
                        temp_mark.append(mark.mark)
                        # temp_mark = []
                        # marks = np.append(temp_mark,[mark.mark])
            else:
                x=1
                print("Student ID not found, please re-enter")           
            temp1 = np.empty(0)
            temp2 = np.empty(0)
            mark_real = np.append(temp1,temp_mark)
            credit_real = np.append(temp2,temp_credit)
            gpa = np.average(mark_real,weights=credit_real)
            math.floor(gpa*10)/10
            print(f'The GPA of student {self.student[stu_id].student_name} is {gpa}')
            print(" ")
# Define a method to show GPA in decending order

    def show_GPA(self):
        pass
#create a teacher Object that manages the student marks
teacher = Data()

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
# teacher.show_GPA()