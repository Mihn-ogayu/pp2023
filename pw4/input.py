import math
from domains.student import Student
from domains.course import Course
from domains.mark import Mark


# Define a function that ask for number of student to be inputed and returns
# a dict that store infomation of inputed data 
# ('student_id','student_name','student_dob')
def input_students():
	no_stu = int(input("\nNumber of students: "))
	temp = {}
	for i in range(no_stu):
			print(f"\nInfo of student {i+1}")
			stu_id = input("Student ID: ")
			stu_name = input("Student name: ")
			stu_dob = input("Date of birth: ")

			# New 'student' object to store info
			student = Student(stu_id,stu_name,stu_dob)

			# Store data into 'temp' dict with 'stu_id' key
			temp[stu_id] = student

	# Returns the data of 'temp' dict
	return temp

# Define a function that ask for number of courses to be inputed and returns
# a dict that store infomation of inputed data 
# ('course_id','course_name','course_credits')

def input_courses():
	no_course = int(input("\nNumber of courses: "))
	temp = {}
	for i in range(no_course):
			print(f"\nInformation for course {i+1}")
			course_id = input("Course ID: ")
			course_name = input("Course name: ")
			course_credit = int(input("Credits: "))

			# New 'course' object to store info
			course = Course(course_id,course_name,course_credit)

			# Store data in 'temp' dict with 'course_id' key
			temp[course_id] = course

	# Returns the data of 'temp' dict
	return temp


def input_marks(students,courses):
	x = 1
	temp = {}
	while x <= len(courses):
		course_input = input("Choose course ID for inputing mark: ")
		if course_input in courses:
			x+=1
			print(f'Course: {courses[course_input].course_name} - {course_input} - ETCs {courses[course_input].course_credit}')
			for student in students:
				print(f'\tStudent: {students[student].student_name}')
				input_mark = float(input(f'Mark: '))
				math.floor(input_mark * 10) / 10
				mark = Mark(student,course_input,input_mark)
				# # mk = (student,course_input)
				# self.mark[input_mark] = mak
				# mark[(student,course_input)] = temp_mark
				temp[(student,course_input,input_mark)] = mark
		# else:
		# 	print("Course does not exist!")
	print(" ")
	return temp
