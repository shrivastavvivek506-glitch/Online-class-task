class Member_ship:

    def __init__(self):
        # Taking user input
        self.Name = input("Enter Your Name: ")
        self.Age = input("Enter Your Age: ")

        # Private Members
        self.__Member_ship_number = input("Enter Membership Number: ")
        self.__Licence_number = input("Enter Licence Number: ")

        # Protected Members
        self._Owner_ship = input("Enter Ownership Name: ")
        self._Owner_number = input("Enter Owner Number: ")

    def Important_details(self):
        print("\n----- Important Details -----")
        print("Membership Number:", self.__Member_ship_number)
        print("Licence Number:", self.__Licence_number)


# Creating Object
Member_ship_obj = Member_ship()

# Printing Public Members
print("\n----- Public Details -----")
print("Name:", Member_ship_obj.Name)
print("Age:", Member_ship_obj.Age)

# Printing Protected Members
print("\n----- Protected Details -----")
print("Ownership Name:", Member_ship_obj._Owner_ship)
print("Owner Number:", Member_ship_obj._Owner_number)

# Calling Method to Access Private Members
Member_ship_obj.Important_details()