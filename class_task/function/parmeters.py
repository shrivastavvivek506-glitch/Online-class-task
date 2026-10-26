# 1. without parameters example

def friend_name():
    print("Ashish")
    print("Abhi")

friend_name()

print("--------------------------")

def greet():
    print("Hello, Welcome!")

greet()

print("-------------------------------")

def add():
    a = 1
    b = 99
    print("Sum =", a + b)

add()

print("----------------------------")

# 2. parameters example

def sum_of_number(a,b):
    print("sum", a+b)

sum_of_number(20, 10)

print("---------------------------")

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Vivek", 19)


print("-----------------------------")

def square(num):
    print("Square =", num * num)

square(5)
square(8)

