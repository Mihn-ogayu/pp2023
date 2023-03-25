from domains.student import Student
from domains.course import Course
from domains.mark import Mark
import numpy as np
import math


# Define method to list students
# Output: {Student id, Student Name, DoB}
def list_students(students):
    if len(students) == 0:
        print("No students yet! ")
    else:
        print("List of students: ")
        print("ID\t|\tName\t|\tDate of birth")
        print("-"*50)
        for student in students:
            print(f"{students[student].student_id}\t|\t{students[student].student_name}\t|\t{students[student].student_dob}")
        print("-"*50)


# Define method to list courses
# Output : {Course ID, Course Name, Credits}
def list_courses(courses):
    if len(courses) == 0:
        print("No courses yet!")
        return
    else:
        print("Displaying courses: ")
        print("ID\t|\tName\t|\tECTs")
        print("-"*50)
        for course in courses:
            print(f'{courses[course].course_id}\t|\t{courses[course].course_name}\t|\t{courses[course].course_credit}')
        print("-"*50)

# Define method to show marks
# Output: {course ID, student ID, mark}
def show_marks(marks,courses):
    x = 1
    while x <= len(courses):
        course_input = input("Enter course ID to show mark: ")
        if course_input in courses:
            x += 1
            print(f'\tCourse: {courses[course_input].course_name}, Credits: {courses[course_input].course_credit}')
            print("ID\t|\tMark")
            for student in marks:
                mark = marks[student]
                if mark.course == course_input:
                    print(f'{mark.student}\t|\t{mark.mark}')
            print(" ")


# gpa = {}

# def calculate_GPA(students,courses,marks):
#     temp_credit = []
#     for course in courses:
#         print(f'Course: {courses[course].course_name}, Credits: {courses[course].course_credit}')
#         temp_credit.append(courses[course] .course_credit)
#     # x = 1
#     # while x <= len(self.student):
#     #     stu_id = input("Enter student ID you want to calculate GPA for: ")
#     #     if stu_id in self.student:
#     #         x += 1
#     for stu_id in students:
#         temp_mark = []
#         for mark in marks:
#             mark = marks[mark]
#             if stu_id == mark.student:
#                 # x += 1
#                 temp_mark.append(mark.mark)
#                 # temp_mark = []
#                 # marks = np.append(temp_mark,[mark.mark])
#         # else:
#         #     x=1
#         #     print("Student ID not found, please re-enter")           
#         temp1 = np.empty(0)
#         temp2 = np.empty(0)
#         mark_real = np.append(temp1,temp_mark)
#         credit_real = np.append(temp2,temp_credit)
#         gpa = np.average(mark_real,weights=credit_real)
#         gpa[stu_id] = gpa
#         students[stu_id].student_gpa = gpa
#         math.floor(gpa*10)/10
#         print(f'The GPA of student {students[stu_id].student_name}- ID: {students[stu_id].student_id} is {gpa}')
#         print(" ")
# def show_GPA(students,courses,marks):
#     calculate_GPA(students,courses,marks)
#     temp_gpa 
#     temp_credit = []
#     for course in courses:
#         temp_credit.append(courses[course].course_credit)

#     for student in students:
#         if student in students:
#             temp_mark = []
#             for mark in marks:
#                 mark = marks[mark]
#                 if student == mark.student:
#                     temp_mark.append(mark.mark)
    
#     temp1 = np.empty(0)
#     temp2 = np.empty(0)
#     mark_real = np.append(temp1,temp_mark)
#     credit_real = np.append(temp2,temp_credit)
#     temp_gpa = np.average(mark_real,weights=credit_real)

#     temp_gpa = dict(sorted(temp_gpa.items(),key=lambda item: item[1],reverse=True))
#     print("Student rankings:")
#     print("-"*50)
#     print("ID\t|\tName\t|\tGPA")
#     for student in temp_gpa:
#         print(f'{students[student].student_id}\t|\t{students[student].student_name}\t|\t{temp_gpa[student]}')
#     # for a,b in marks.items():
#     #     # mark = self.mark[student]
#     #     # mark = marks[student]
#     #     # if course.id == course_input:
#     #     #     print(f'Student ID: {student.id}\t\tMark: {mak}')
#     #     print(f'Student ID: {student.student_id}, Student Name: {student.student_name}, Course {course.course_name}, Mark: {mak}')
#     # print (" ") 
#     # # else:
#     # #     print("Course does not exist! ")
#     # #     return
    