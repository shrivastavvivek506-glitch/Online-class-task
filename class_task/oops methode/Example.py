print("//Example 1:")

class student():
    name="Vivek Shrivastav"
    course="BCA"
    def student_details(self):
        print("student all info")

s = student()
print(s.name)
print(s.course)
s.student_details

#-------------------------------------

print("// Example 2:")

class car():
    name="BMW"
    model="5x"
    color="black"
    def car_info(self):
        print("all about car")

v = car()
print(v.name)
print(v.color)
v.car_info()