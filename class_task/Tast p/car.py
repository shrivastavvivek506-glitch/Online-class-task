from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def start(self):
        pass


class BMW(Car):

    def start(self):
        print("BMW car is starting")


class Audi(Car):

    def start(self):
        print("Audi car is starting")


b = BMW()
a = Audi()

b.start()
a.start()