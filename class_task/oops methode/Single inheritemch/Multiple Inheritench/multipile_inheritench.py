# Multiple Inheritench Example

class Student:
    Student_name = "Alexa"
class course:
    course_name = "BCA"

class collage(Student,course):
    collage_name = "shobhit university"

collage_obj = collage()
print(collage_obj.Student_name)
print(collage_obj.course_name)
print(collage_obj.collage_name)    

#print("------------------------------------")

class employee:
    employee_name = "Rahul"

class department:
    department_name = "Software"
class salary(employee,department):
    salary = "5000000"

salary_obj = salary()
print(salary_obj.employee_name)
print(salary_obj.department_name)
print(salary_obj.salary)

#print("-------------------------------")

class brand:
    brand_name = "Toyota"
class model:
    model_name = "Fortuner"
class car(brand,model):
    coclor = "Black"

car_obj = car()
print(car_obj.brand_name)
print(car_obj.model_name)
print(car_obj.coclor)    