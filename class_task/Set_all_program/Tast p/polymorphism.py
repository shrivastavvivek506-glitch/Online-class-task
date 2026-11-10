# Polymorphism

class Father:
    def show(self):
        print("This is Father class")

class Son:
    def show(self):
        print("This is Son class")

father_obj = Father()
father_obj.show()

son_obj = Son()
son_obj.show()