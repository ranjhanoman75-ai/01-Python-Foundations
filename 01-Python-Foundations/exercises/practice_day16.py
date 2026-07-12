print("==========Day16=====================")
print("============Inheritance=============")
class Animal:
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
dog = Dog()
dog.eat()
dog.bark()
dog.sleep()

print("=============Method Overriding==========")
class animal:
    def sound(self):
        print("Animal sound")
class dog(animal):
    def sound(self):
        print("Dog sound")
janwer = animal()
janwer.sound()
dg = dog()
dg.sound()