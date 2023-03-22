from domains import Student
from domains import Course
from domains import Mark
class Input():
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