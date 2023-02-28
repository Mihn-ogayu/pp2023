#function for input student
def input_students():
    no_st = int(input("Number of students: "))
    if no_st <= 0:
        print("Invalid number")
        exit()
    else:
        stu_list = [[0 for i in range(3)] for j in range(no_st)]
        for i in range(no_st):
            stu_list[i][0] = input("Student ID: ")
            stu_list[i][1] = input("Student Name: ")
            stu_list[i][2] = input("DOB:")
    return stu_list

#function for input corse
def input_courses():
    no_co = int(input("Number of courses: "))
    if no_co <= 0:
        print("Invalid course")
        exit()
    else:
        co_list = [[0 for i in range (2)] for j in range(no_co)]
        for i in range(no_co):
            co_list[i][0] = input("Course ID: ")
            co_list[i][1] = input("Course name: ")
    return co_list

#List the students
def list_students():
    for i in range(len(student_list)):
        print("Student ID: ",student_list[i][0])
        print("Name: ",student_list[i][1])
        print("DOB: ",student_list[i][2])

#List the courses
def list_courses():
    for i in range(len(course_list)):
        print("Course ID: ",course_list[i][0])
        print("Name: ",course_list[i][1])

#input  student marks for subjects
def input_marks(co,stu):
    mark = [[0 for i in range(len(stu))] for j in range(len(co))]
    for i in range(len(co)):
        for j in range(len(stu)):
            mark [i][j] = int(input("Mark for student",stu[i][1],"for subject",co[i][1]))
    return mark

#Show student marks function
def show_student_marks(stu,co):
    courseID = input("Course ID")
    for i in range(len(co)):
        if courseID == co[i][1]:
            print("Student ",stu[i][1],"Course:",co[i][1],"Mark: ",mark[i][j])  
        else:
            exit()

#define student and course lists
student_list = input_students()
course_list = input_courses()

list_students()
list_courses()

