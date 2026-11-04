# Multilevel Inheritance

class Grandfather:
    grandfather_name = "Ramesh"

    def grandfather_fxn(self):
        print("Grandfather Name:", self.grandfather_name)


class Father(Grandfather):
    father_name = "Rajesh"

    def father_fxn(self):
        print("Father Name:", self.father_name)


class Child(Father):
    child_name = "Vivek"

    def child_fxn(self):
        print("Child Name:", self.child_name)


child_obj = Child()

child_obj.grandfather_fxn()
child_obj.father_fxn()
child_obj.child_fxn()

child_obj.grandfather_fxn()