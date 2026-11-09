from abc import ABC, abstractmethod

class Student(ABC):

    @abstractmethod
    def course_fxn(self):
        pass


class Course(Student):

    def course_fxn(self):
        print("Python Programming Course")


obj = Course()
obj.course_fxn()