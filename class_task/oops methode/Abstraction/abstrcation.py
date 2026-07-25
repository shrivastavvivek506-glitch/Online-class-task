from abc import ABC, abstractmethod

class Student_class():
     @abstractmethod
     def course_fxn(self):
         pass
class course(Student_class):
     def course_fxn(self):
         print("This is a very importaint massage")

c_obj = course()

c_obj.course_fxn()
