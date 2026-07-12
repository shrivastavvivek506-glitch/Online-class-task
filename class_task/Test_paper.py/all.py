print("hii soan :")
x = int(input("Please Enter the your number :"))
def even_odd(x):
    if x %2 == 0:
        print("This is even number :")

    else:
        print("This is odd number :")

even_odd(x)
print("hii Vivek :")
y = int(input("Please Enter the your number :"))
even_odd(y)

age = int(input("Enter your age:"))
if age >= 18 and age <= 80:
    print("your are eligible for vote:")
elif  age > 80:
        print("your age is very high so, you are not eligible for vote :")

else:
    print("your are not eligible for vote:")