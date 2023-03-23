from domains.student import Student
from domains.course import Course
from domains.mark import Mark
# import input as ip
# import output as op
from input import input_students
from output import list_students
import numpy as np
import math
import os
clear = lambda:os.system('clear')


class Main():
    def __init__(self):
        self.student = {}   
        self.course = {}
        self.mark = {}
        # self.gpa = {}
    def add_student(self):
        self.student = input_students()
    def display_students(self):
        list_students(self.student)

    # def add_student(self):
    #     while True:
    #         try:
    #             no_stu = int(input("Number of students: \n"))
    #             break
    #         except ValueError:
    #             print("Not a valid student number, please try again!")
    #             continue
    #     self.input_students()

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

if __name__ == '__main__':
    teacher = Main()

while True:
    clear()
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
    if choice == 1:
        # teacher.add_student()
        # clear()
        teacher.add_student()
        
    if choice == 2:
        pass
    if choice == 3:
        # teacher.list_students()
        teacher.display_students()

        
        