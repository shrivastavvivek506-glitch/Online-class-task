# Multilevel Inheritench Example
class student:
    student_name = "XYZ"
class course(student):
    course_name = "MCA"
class collage(course):
    collage_name = "Shobhit university"

collage_obj = collage()
print(collage_obj.student_name)
print(collage_obj.course_name)
print(collage_obj.collage_name)

print("-----------------------------------------")

class grandfather:
    house = "Grand house"
class father(grandfather):
    car = "BMW"
class child(father):
    bike = "R1"

child_obj = child()
print(child_obj.house)#grandfather
print(child_obj.car)#father
print(child_obj.bike)#child

print("--------------------------------------")

class Vehicle:
    company = "Honda"

class Car(Vehicle):
    model = "City"

class SportsCar(Car):
    color = "White"

sports_obj = SportsCar()

print(sports_obj.company)
print(sports_obj.model)
print(sports_obj.color)