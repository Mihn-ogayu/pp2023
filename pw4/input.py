import math
from domains.student import Student
from domains.course import Course
from domains.mark import Mark


def input_students():
        students = {}
        stu_id = input("Student ID: ")
        stu_name = input("Student name: ")
        stu_dob = input("Date of birth: ")
        print(" ")
        student = Student(stu_id,stu_name,stu_dob)
        students[stu_id] = student
        #After inputing, store data into student dict
        return students

# def input_courses():
#     # for i in range(x):
#         courses = {}
#         # print(f"Enter information for course {i+1}")
#         course_id = input("Course ID: ")
#         course_name = input("Course name: ")
#         course_credit = int(input("Credits: "))
#         print(" ")
#         course = Course(course_id,course_name,course_credit)
#         courses[course_id] = course
#         return courses
        
        #After inputing, store data into course dict

# def input_marks(students,courses):
#     x = 1
#     while x <= len(courses):
#         marks = {}
#         course_input = input("Choose course ID for inputing mark: ")
#         if course_input in courses:
#             x+=1
#             print(f'Course: {courses[course_input].course_name} - {course_input}')
#             for student in students:
#                 if student in students:
#                     print(f'\tStudent: {students[student].student_name}')
#                     input_mark = float(input(f'Mark: '))
#                     temp_mark = {
#                         "student": students[student],
#                         "course" : courses[course_input],
#                         "mark" : input_mark
#                     }
#                     # math.floor(input_mark * 10) / 10
#                     mark = Mark(student,course_input,input_mark)
#                     # # mk = (student,course_input)
#                     # self.mark[input_mark] = mak
#                     marks[(student,course_input)] = temp_mark
#                 else:
#                     print("Student does not exist.")
#                     break
#         else:
#             print("Course does not exist!")
#             continue
#     print(" ")
#     return temp_mark

# def add_student(self):
#     while True:
#         try:
#             no_stu = int(input("Number of students: \n"))
#             for i in range (no_stu):
#                 print(f"Entering information for student {i}")
#                 self.input_students()
#             break
#         except ValueError:
#             print("Not a valid student number, please try again!")
#             continue