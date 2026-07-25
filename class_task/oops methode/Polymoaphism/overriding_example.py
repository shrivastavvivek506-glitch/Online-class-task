print("// Example 1:")

class animal:
    def sound(self):
        print("Animal makes a sound")

class dog:
    def sound(self):
        print("Dog barks")

a = animal()
d = dog()

a.sound()
d.sound()

#---------------------------------------------

print("// Example 2:")

class vehicle:
    def start(self):
        print("Vehicle starts")

# Bike Inheritench for vehicle

class bike(vehicle):
    def start(self):
        print("Bike start with self-start")

b  = bike()

b.start()
