print("=============Abstract classes=============")
from abc import ABC, abstractmethod
class Animal(ABC):
    def eat(self):
        print("Animal is eating")
    @abstractmethod
    def sound(self):
        pass 
class dog(Animal):
    def sound(self):
        print("Dog is barking")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
class Lion(Animal):
    def sound(self):
        print("Lion is roaring")
dg = dog()
dg.eat()
dg.sound()
cat = Cat()
cat.eat()
cat.sound()
lion = Lion()
lion.eat()
lion.sound()
print("==========2 program========")
class vehicle(ABC):
    def show_company(self):
        print("Vehicle company")
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        pass
    def fuel(self):
        pass
class Car(vehicle):
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stopped")
    def fuel(self):
        print("Fuel: petrol")
class Bike(vehicle):
    def start(self):
        print("Bike started")
    def stop(self):
        print("Bike stopped")
    def fuel(self):
        print("Fuel: petrol")
class Truck(vehicle):
    def start(self):
        print("Truck started")
    def stop(self):
        print("Truck stopped")
    def fuel(self):
        print("Fuel: petrol")
print("==========Car=======")
car = Car()
car.show_company()
car.start()
car.stop()
car.fuel()
print("============Bike=========")
bike = Bike()
bike.show_company()
bike.start()
bike.stop()
bike.fuel()
print("========Truck===========")
truck = Truck()
truck.show_company()
truck.start()
truck.stop()
truck.fuel()