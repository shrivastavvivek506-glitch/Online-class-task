class even_odd:
    my_number = int(input("Enter the numebr :"))
    def check_even_odd(self):
        if(self.my_number % 2==0):
            print("This is even number :")
        else:
            print("This is odd number :")

number = even_odd()
print("hii, Vivek")
print(number.my_number)
number.check_even_odd()               
