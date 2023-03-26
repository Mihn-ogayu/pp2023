import os
import subprocess
import zipfile
from domains.student import Student
from domains.course import Course
from domains.mark import Mark


def delete_txt():
    if os.path.exists("students.txt"):
        os.remove("students.txt")
    if os.path.exists("courses.txt"):
        os.remove("courses.txt")
    if os.path.exists("marks.txt"):
        os.remove("marks.txt")

def compress_data():
    with open("class.dat","wb") as data_file:
        with zipfile.ZipFile('files.zip','w',compression=zipfile.ZIP_DEFLATED) as my_zip:
            for file in os.listdir():
                if file.endswith(".txt"):
                    my_zip.write(file)

def extract_data():
    with open("class.dat","wb") as data_file:
        with zipfile.ZipFile('files.zip','r') as my_zip:
            my_zip.extractall('data')

def load_students():
    pass