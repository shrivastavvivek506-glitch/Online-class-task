# Public Member
class employee():
    employee_name = "Vivek"
    department = "IT"
    salary = "75000"

e = employee()
print(e.employee_name)
print(e.department)
print(e.salary)

#--------------------------------------------------

# Protected Member
class employee():
    _employee_name = "Vivek"
    _department = "IT"
    _salary = "75000"

e = employee()
print(e._employee_name)
print(e._department)
print(e._salary)

#-----------------------------------------------------

#Private Member
class employee():
    __employee_name = "Vivek"
    __department = "IT"
    __salary = "75000"

e = employee()
print(e.__employee_name)
print(e.__department)
print(e.__salary)
