location = input("Enter your location:")


if location.lower() == "motihari":
    print("your are eligible:")

    Age = int(input("Enter your age:"))

    if (Age >= 18):
        print("Your are eligible to vote:")

    else:
        print("your age is so low , So your are not elgible to vote:")

else:
    print("your location is note match , So your are not vote in motihari:")