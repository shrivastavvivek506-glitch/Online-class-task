# Single Inheritance
# Example

class owner():
    owner_name = "Vivek shrivastav"
    owner_age = "19"

class business(owner):
    business_name = "transport"
    member_ship = "16 Years"

business_obj = business()
print(business_obj.business_name)
print(business_obj.owner_age)
print(business_obj.owner_name)
print(business_obj.member_ship)

#print("--------------------------------------------------")

class job():
    employe_name = "ADCA"
    department_name = "software devloper"

class salary(job):
    salary = "45000"
    member_ship = "42 Years"

salary_obj = salary()
print(salary_obj.department_name)
print(salary_obj.employe_name)
print(salary_obj.salary)
print(salary_obj.member_ship)

#print("--------------------------------------------------")

class student():
    student_name = "Sona"
    course = "BCA"

class Result(student):
    marks = "85%"
    grade = "A" 

result_obj = Result()
print(result_obj.student_name)
print(result_obj.course)
print(result_obj.marks)
print(result_obj.grade)