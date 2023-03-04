#function for input student
def input_students(students:list):
    dict = {}   #temp dict to store student info
    print("\n")
    student_id = input("Student ID: ")
    student_name = input("Student Name: ")
    student_dob = input("DoB: ")
    dict["StudentID"] = student_id
    dict["StudentName"] = student_name
    dict["DOB"] = student_dob
    dict["course"] = [ ]
    students.append(dict)   #append temp dict to students[] list

#function for input courses
def input_courses(courses:list):
    dict ={}
    print("\n")
    course_id = input("Course ID: ")
    course_name = input("Course: ")
    dict["CourseID"] = course_id
    dict["Course Name"] = course_name
    courses.append(dict)

#input  student marks for subjects
def input_marks(students:list,courses:list):
    print ("\n")
    course_input = input("Choose course ID:")
    student_input = input("Choose Student ID:")
    dict = {}
    mark = input("Mark:")
    for course in courses:
        if course["CourseID"] == course_input:
            course_name = course["Course Name"]
    for student in students:
        if student["StudentID"] == student_input:
            student["course"].append({"Course Name": course_name, "mark": mark})


# input_marks(students,courses)
students = []
courses = []

stu_no = int(input("Number of students: "))
for i in range(stu_no):
    input_students(students)
course_no = int(input("Number of courses: "))
for j in range(course_no):
    input_courses(courses)
for student in students:
    input_marks(students,courses)
for student in students:
    print("-----------------")
    print(f'Name: {student["StudentName"]}' )
    print(f'ID: {student["StudentID"]}')
    print(f'DoB:  {student["DOB"]}')
for course in student["course"]:
    print(f'Course: {course["Course Name"]}, {course["mark"]}')

print("\n")
for course in courses:
    print(course)
