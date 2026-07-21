print("//Example 1")
class animal:
    type = "mammal"
class pet:
    owner = "vivek"
class dog(animal, pet):
    breed = "labrador"

d = dog()
print(d.type)
print(d.breed)
print(d.owner)    
#----------------------------------------

print("//Example 2")
class employee:
    company = "TCM"
class department:
    dept = "IT"
class manager(employee,department):
    salary = 50000
m = manager()
print(m.salary)
print(m.company)
print(m.dept)            
#----------------------------------------

print("//Example 3")

class school:
    school_name = "ABC school"
class student:
    name = "Aman"
class Result(school,student):
    grade = "A"

r = Result()
print(r.name)
print(r.grade)
print(r.school_name)            