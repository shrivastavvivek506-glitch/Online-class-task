print("//Example 1:")
class person():
    name = "vivek"
    age = 19
class student(person):
    roll_no = 250110341
    mobile_no = 1234567890

x = student()
print(x.name)
print(x.age)
print(x.roll_no)
print(x.mobile_no)
#----------------------------------

print("//Example 2:")

class vehicle():
    name ="BMW"
    model = "x5"
class car(vehicle):
    color = "black"    
    speed = 200
y = car()
print(y.name)
print(y.model)
print(y.color)
print(y.speed)    

#----------------------------------
print("//Example 3:")

class Employee:
    company = "ABC Corp"
    salary = 50000
class Manager(Employee):
    department = "Sales"
    bonus = 10000
z = Manager()
print(z.company)
print(z.salary)
print(z.department)
print(z.bonus)    