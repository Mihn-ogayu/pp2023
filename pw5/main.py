from domains.student import Student
from domains.course import Course
from domains.mark import Mark
from domains import utils
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
        self.gpa = {}
    
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
        # print(self.mark)
    
    def check_if_data_exist(self):
        if os.path.exists("class.dat"):
            if os.path.exists("students.txt") and os.path.exists("courses.txt") and os.path.exists("marks.txt"):
                pass
            else:
                print("Data exists.")
                print("Extracting data")
                utils.extract_data()
                self.student = utils.load_students()
                self.course = utils.load_courses()
                self.mark = utils.load_marks()
        else:
            print("Data does not exist.")

    # def calculate_GPA(self):
    #     # temp_credit = []
    #     # print("Course List:")
    #     # print("Name\t|\tCredits")
    #     # print("-"*50)

    #     # for course in self.course:
    #     #     print(f'{self.course[course].course_name}\t|\t{self.course[course].course_credit}')
    #     #     temp_credit.append(self.course[course] .course_credit)

    #     for stu_id in self.student:
    #         temp_mark = []
    #         for mark in self.mark:
    #             mark = self.mark[mark]
    #             if stu_id == mark.student:
    #                 temp_mark.append(mark.mark)
           
    #         temp1 = np.empty(0)
    #         temp2 = np.empty(0)
    #         mark_real = np.append(temp1,temp_mark)
    #         credit_real = np.append(temp2,temp_credit)

    #         gpa = np.average(mark_real,weights=credit_real)
    #         self.gpa[stu_id] = gpa
    #         self.student[stu_id].student_gpa = gpa
    #         math.floor(gpa*10)/10

    #         print(f'The GPA of student {self.student[stu_id].student_name}- ID: {self.student[stu_id].student_id} is {gpa}')
    #         print(" ")

    def rank_student(self):
        temp_credit = []
        print("Course List:")
        print("Name\t|\tCredits")
        print("-"*50)
        for course in self.course:
            print(f'{self.course[course].course_name}\t|\t{self.course[course].course_credit}')
            temp_credit.append(self.course[course].course_credit)

        # self.calculate_GPA()
        
        # temp_credit = []
        # for course in self.course:
        #     temp_credit.append(self.course[course].course_credit)
        # self.checkType(temp_credit)

        for stu_id in self.student:
            temp_mark = []
            for mark in self.mark:
                mark = self.mark[mark]
                if stu_id == mark.student:
                    temp_mark.append(mark.mark)

            # self.checkType(temp_mark)
            temp1 = np.empty(0)
            temp2 = np.empty(0)
            markreal = np.append(temp1,temp_mark)
            creditreal = np.append(temp2,temp_credit)
            
            mark_real = markreal.astype(np.float64)
            credit_real = creditreal.astype(np.int32)

            gpa = np.average(mark_real,weights=credit_real)
            self.gpa[stu_id] = gpa

        self.gpa = dict(sorted(self.gpa.items(), key=lambda item: item[1], reverse=True))

        print("\nStudent rankings: ")
        print("-"*50)
        print(f'ID\t\tStudent Name \t\tGPA')

        for student in self.gpa:
            print(f'{self.student[student].student_id}\t\t{self.student[student].student_name}\t\t{self.gpa[student]}')

    def checkType(self,a_list):
        for element in a_list:
            if isinstance(element, int):
                print("It's an Integer")
            if isinstance(element, str):
                print("It's an string")
            if isinstance(element, float):
                print("It's an floating number")


def wait():
    m.getch()

def input_choice():
    while True:
        try: 
            x = int(input("Your choice: "))
            return x
        except ValueError:
            print("Not a valid number, try again")
            continue

if __name__ == '__main__':
    teacher = Main()


utils.delete_if_exist()
# teacher.check_if_data_exist()
while True:
    # clear()
    teacher.check_if_data_exist()
    print("\nStudent Management System")
    print("[1]. Input student")
    print("[2]. Input courses")
    print("[3]. List students")
    print("[4]. List courses")
    print("[5]. Input marks")
    print("[6]. Show marks")
    print("[7]. Student rankings")
    print("[8]. Delete existing data")
    print("[9]. Exit program")


    choice = input_choice()
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
        clear = os.system('cls')
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
    elif choice == 7:
        teacher.rank_student()
        print("Press any key to continue")
        wait()
        clear = os.system('cls')
    elif choice == 8:
        utils.delete_data()
        print("Press any key to continue")
        wait()
        clear = os.system('cls')
    elif choice == 9:
        print("Exiting program...")
        utils.compress_data()
        utils.delete_if_exist()
        utils.delete_py_cache()
        break


    