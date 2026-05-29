from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        # print("Vehicle is running")
        pass

    def login(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("Bike is running")


class Car(Vehicle):
    def start(self):
        print("Car is running")


b1 = Bike()
b1.start()

c1 = Car()
c1.start()
