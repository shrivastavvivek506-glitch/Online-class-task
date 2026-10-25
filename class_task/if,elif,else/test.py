age = int(input("Enter your age:"))

if (age >= 18):
    print("Age criteria satisfied")

    salary = int(input("Enter your salary:"))

    if (salary >= 30000):
        print("loan approve")

    else:
        print("Loan Rejected: Salary is too low")

else:
    print("Loan Rejected: Age is below 18")
