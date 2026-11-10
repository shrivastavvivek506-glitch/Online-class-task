# Multiple Inheritance

class Father:
    father_name = "Rajesh"

    def father_fxn(self):
        print("Father Name:", self.father_name)


class Mother:
    mother_name = "Sunita"

    def mother_fxn(self):
        print("Mother Name:", self.mother_name)


class Child(Father, Mother):
    child_name = "Vivek"

    def child_fxn(self):
        print("Child Name:", self.child_name)


child_obj = Child()

child_obj.father_fxn()
child_obj.mother_fxn()
child_obj.child_fxn()

child_obj.child_fxn()