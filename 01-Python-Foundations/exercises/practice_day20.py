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
dg = dog()
dg.eat()
dg.sound()
cat = Cat()
cat.sound()