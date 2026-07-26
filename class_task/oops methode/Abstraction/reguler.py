from abc import ABC, abstractmethod
class student:
    @abstractmethod
    def course_fxn(self):
        pass

    def regular_fxn(self):
        print("This is very important massage:")

class collage_name(student):
    def course_fxn(self):
        print("Shobhit unversity:")

collage_obj = collage_name()

collage_obj.course_fxn()
collage_obj.regular_fxn()