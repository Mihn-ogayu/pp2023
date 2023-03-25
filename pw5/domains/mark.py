from domains.course import Course
from domains.student import Student
class Mark:
    def __init__(self,student,course,mark):
        self.student = student
        self.course = course
        self.mark = mark