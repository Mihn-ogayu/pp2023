class Student:
    def __init__(self,student_id,student_name,student_dob,GPA):
        self.student_id = student_id
        self.student_name = student_name
        self.student_dob = student_dob
        self.gpa = GPA
class Course:
    def __init__(self,course_id,course_name):
        self.course_id = course_id
        self.course_name = course_name
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

    def input_students(self,x):
        # stu_no = int(input("Number of student: "))
        # print(" ")
        for i in range(x):
            stu_id = input("Enter Student ID: ")
            stu_name = input("Student name: ")
            stu_dob = input("Date of birth: ")
            print(" ")
            student = Student(stu_id,stu_name,stu_dob,None)
            self.student[stu_id] = student

    def input_courses(self,x):
        # co_no = int(input("Number of courses: "))
        # print (" ")
        for i in range(x):
            course_id = input("Enter course ID: ");
            course_name = input("Course name: ")
            print(" ")
            # co = {}
            course = Course(course_id,course_name)
            self.course[course_id] = course

    def list_student(self):
        print("Displaying students:")
        for student in self.student:
            print("-----------------------")
            print(f'ID: {self.student[student].student_id}')
            print(f'Name: {self.student[student].student_name}')
            print(f'Date of Birth: {self.student[student].student_dob}')
        print(" ")  
    def list_course(self):
        print("Displaying courses: ")
        for course in self.course:
            print(f'Course ID: {self.course[course].course_id}')
            print(f'Course Name: {self.course[course].course_name}')
            print(" ")

    def input_marks(self,x):
        for i in range(x):
            course_input = input("Choose course ID for inputing mark: ")
            if course_input in self.course:
                print(f'Course: {self.course[course_input].course_name} - {course_input}')
                for student in self.student:
                    if student in self.student:
                        print(f'\tStudent: {self.student[student].student_name}')
                        input_mark = input(f'Mark: ')
                        mk = Mark(student,course_input,input_mark)
                        key = (student,course_input)
                        self.mark[key] = mk
                    else:
                        print("Student does not exist.")
                        break
            else:
                print("Course does not exist")
                return
        print(" ")
    def show_marks(self,x):
        for i in range(x):
            course_input = input("Enter course ID to show mark: ")
            for student in self.mark:
                mark = self.mark[student]
                if mark.course == course_input:
                    print(f'Student ID: {mark.student}\tMark: {mark.mark}')
teacher = Data()
no_stu = int(input("Number of students: \n"))
teacher.input_students(no_stu)
teacher.list_student()
no_course = int(input("Number of courses: \n"))
teacher.input_courses(no_course)
teacher.list_course()

teacher.input_marks(no_course)
teacher.show_marks(no_course)
