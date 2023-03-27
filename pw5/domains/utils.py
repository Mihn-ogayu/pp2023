import os
import subprocess
import zipfile
from domains.student import Student
from domains.course import Course
from domains.mark import Mark
import shutil

def delete_if_exist():
    if os.path.exists("students.txt"):
        os.remove("students.txt")
    else:
        pass
    if os.path.exists("courses.txt"):
        os.remove("courses.txt")
    else:
        pass
    if os.path.exists("marks.txt"):
        os.remove("marks.txt")
    else:
        pass
    # if os.path.exists("files.zip"):
    #     os.remove("files.zip")
    # if os.path.exists("class.dat"):
    #     choice = input("Do you want to delete the database? ")
    #     if choice == 'Y':
    #         os.remove("class.dat")
    #     else:
    #         pass
def delete_data():
    delete_if_exist()
    if os.path.exists("class.dat") and os.path.exists("data.zip"):
        os.remove("class.dat")
    # if os.path.exists("data.zip"):
        os.remove("data.zip")
    else:
        print("There is no data to be deleted")
        pass


def compress_data():
    with open("class.dat","wb") as data_file:
        with zipfile.ZipFile('data.zip','w',compression=zipfile.ZIP_DEFLATED) as my_zip:
            for file in os.listdir():
                if file.endswith(".txt"):
                    my_zip.write(file)

def extract_data():
    with open("class.dat","wb") as data_file:
        with zipfile.ZipFile('data.zip','r') as my_zip:
            my_zip.extractall()



def load_students():
    temp = {}
    with open("students.txt") as student_file:
        lines = student_file.readlines()
        for line in lines:
            data = line.strip().split(",")
            student = Student(data[0],data[1],data[2])
            temp[data[0]] = student
    return temp

def load_courses():
    temp = {}
    with open("courses.txt") as course_file:
        lines = course_file.readlines() 
        for line in lines:
            data = line.strip().split(",")
            course = Course(data[0],data[1],data[2])
            temp[data[0]] = course
    return temp

def load_marks():
    temp = {}
    with open("marks.txt") as mark_file:
        lines = mark_file.readlines()
        for line in lines:
            data = line.strip().split(",")
            mark = Mark(data[0],data[1],data[2])

            temp[(data[0],data[1],data[2])] = mark
    return temp

def delete_py_cache():
    if os.path.exists("__pycache__"):
        shutil.rmtree('__pycache__')