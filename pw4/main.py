from domains.student import Student
from domains.course import Course
from domains.mark import Mark
# import input as ip
# import output as op
from input import input_students,input_courses,input_marks
from output import list_students,list_courses,show_marks
import numpy as np
import math
import os
import time
import msvcrt as m
clear = os.system('cls')


class Main():
    def __init__(self):
        self.student = {}   
        self.course = {}
        self.mark = {}
        # self.gpa = {}
    
    # Adding students
    def add_student(self):
        self.student = input_students()

    # Displaying student info
    def display_students(self):
        list_students(self.student)

    # Adding courses
    def add_course(self):
        self.course = input_courses()

    # Displaying course info
    def display_courses(self):
        list_courses(self.course)

    # Adding mark 
    def add_mark(self):
        self.mark = input_marks(self.student,self.course)

    def display_marks(self):
        show_marks(self.mark,self.course)

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
            self.gpa[stu_id] = gpa
            self.student[stu_id].student_gpa = gpa
            math.floor(gpa*10)/10
            print(f'The GPA of student {self.student[stu_id].student_name}  ID: {self.student[stu_id].student_id} is {gpa}')
            print(" ")

    def show_GPA(self):
        temp_credit = []
        for course in self.course:
            temp_credit.append(self.course[course].course_credit)
        for stu_id in self.student:
            if stu_id in self.student:
                temp_mark = []
                for mark in self.mark:
                    mark = self.mark[mark]
                    if stu_id == mark.student:
                        temp_mark.append(mark.mark)
            else:
                x=1
                print("Student ID not found, please re-enter")           
        temp1 = np.empty(0)
        temp2 = np.empty(0)
        mark_real = np.append(temp1,temp_mark)
        credit_real = np.append(temp2,temp_credit)
        self.gpa = np.average(mark_real,weights=credit_real)
        self.gpa = dict(sorted(self.gpa.items(), key=lambda item: item[1], reverse=True))
        # for stu_id in self.gpa:
        #     print(f"StudentID: {stu_id.gpa}, GPA: {gpa}")
        print("Student rankings: ")
        print("-"*30)
        print(f'Student ID\t\tStudent Name \t\tGPA')
        for student in self.gpa:
            print(f'{self.student[student].student_id}\t\t{self.student[student].student_name}\t\t{self.gpa[student]}')

def wait():
    m.getch()

if __name__ == '__main__':
    teacher = Main()

while True:
    # clear()
    print("\nStudent Management System")
    print("[1]. Input student")
    print("[2]. Input courses")
    print("[3]. List students")
    print("[4]. List courses")
    print("[5]. Input marks")
    print("[6]. Show marks")
    print("[7]. Calculate GPA")
    print("[8]. Student rankings")

    
    choice = int(input("Your choice: "))
    print(" ")
    if choice == 1:
        teacher.add_student()
        print("\nInput complete")
        print("Press any key to continue")
        wait()
        clear = os.system('cls')
    elif choice == 2:
        teacher.add_course()
        print("\nInput complete")
        print("Press any key to continue")
        wait()
        clear = os.system('cls')
    elif choice == 3:
        clear = os.system('cls')
        teacher.display_students()
        print("Press any key to continue")
        wait()
        clear = os.system('cls')
    elif choice == 4:
        clear = os.system('cls')
        teacher.display_courses()
        print("Press any key to continue")
        wait()
    elif choice == 5:
        teacher.add_mark()
        print("\nInput complete")
        print("Press any key to continue")
        wait()
        clear = os.system('cls')
    elif choice == 6:
        teacher.display_marks()
        print("Press any key to continue")
        wait()
        clear = os.system('cls')
    else:
        break