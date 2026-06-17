age = int(input("Enter your age :"))
if (age>=18):
    print("You are eligible for loan :")

    salary = int(input("Enter your salary :"))
    if (salary>=50000):

        print("You are approved for loan :")
    else:
        print("You are not approved for loan :")
        print("Please try again later.")
else:
    print("You are not eligible for loan :")