from domains.student import Student
from domains.course import Course
from domains.mark import Mark


# Define method to list students
# Output: {Student id, Student Name, DoB}
def list_students(students):
    # if student not in students:
    #     print("No student yet!")
    #     return
    # else:
    #     print("Displaying students:")
    #     print(f"ID \t\tNAME\t\tDOB")
    #     print(f"-"*40)
    #     for student in students:
    #         print(f'{students[student].student_id}\t\t{students[student].student_name}\t\t{self.student[student].student_dob}')
    #     print(" ")

    # print("List of students: ")
    # for stu_id in students:
    #     print(f"ID: {student_id}, Name: {student.name}, DOB: {student.dob}")
    #     # print(f"ID: {students[stu_id].student_id}, Name: {students[stu_id].student.name}, DOB: {students[stu_id].student.dob}")
    # print("-----------------")
    print("List of students: ")
    for student in students():
        print(f"ID: {students[student].student_id}, Name:  {students[student].student_name}, DoB: {students[student].student_dob}" ) #Name: {student}, DOB: {student.dob}")
    print("-----------------")


# Define method to list courses
# Output : {Course ID, Course Name, Credits}
def list_courses(self):
    if course not in self.course:
        print("No courses yet!")
        return
    else:
        print("Displaying courses: ")
        print("-"*20)
        for course in self.course:
            print(f'Course ID: {self.course[course].course_id}\t\t{self.course[course].course_name}\t\t{self.course[course].course_credit}')
            print(" ")

# Define method to show marks
# Output: {course ID, student ID, mark}
def show_marks(self):
    x = 1
    if mark not in self.mark:
        print("No mark yet!")
        return
    else:
        while x <= len(self.course):
            course_input = input("Enter course ID to show mark: ")
            if course_input in self.course:
                x += 1
                print(f'Course: {self.course[course_input].course_name}, Credits: {self.course[course_input].course_credit}')
                for student in self.mark:
                    mark = self.mark[student]
                    if mark.course == course_input:
                        print(f'Student ID: {mark.student}\t\tMark: {mark.mark}')
                print (" ") 
            else:
                print("Course does not exist! ")
                print("Please re-enter from the beginning")
                self.show_marks(x)
