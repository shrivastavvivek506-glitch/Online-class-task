# Multilevel Inheritance

class Husband:
    Husband_name = "Vivek Shrivastav"


    def Husband_fxn(self):
        print("Husband Name:", self.Husband_name)


class Wife(Husband):
    Wife_name = "Sonakshi Shrivastav"

    def Wife_fxn(self):
        print("Wife Name:", self.Wife_name)


class Child(Wife):
    child_name = "Javi"

    def child_fxn(self):
        print("Child Name:", self.child_name)


child_obj = Child()

child_obj.Husband_fxn()
child_obj.Wife_fxn()
child_obj.child_fxn()