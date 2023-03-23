from domains.student import Student
from domains.course import Course
from domains.mark import Mark


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
    if len(marks) == 0:
        print("No mark yet!")
        return
    else:
        while x <= len(courses):
            course_input = input("Enter course ID to show mark: ")
            if course_input in courses:
                x += 1
                print(f'Course: {courses[course_input].course_name}, Credits: {courses[course_input].course_credit}')
                for student in mark:
                    # mark = self.mark[student]
                    mark = marks[student]
                    if mark.course == course_input:
                        print(f'Student ID: {mark.student}\t\tMark: {mark.mark}')
                print (" ") 
            else:
                print("Course does not exist! ")
                return
