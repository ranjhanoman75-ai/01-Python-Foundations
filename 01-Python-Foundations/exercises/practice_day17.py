print("===============Day 17===========")
print("========Multiple Inheritence=======")
print("Child class inherit from multiple parent classes")
class Father:
    def skills(self):
        print("driving")
class Mother:
    def talent(self):
        print("cooking")
class child(Father,Mother):
    pass
ch = child()
ch.skills()
ch.talent()

print("====Multilevel Inheritance=========")
class Animal:
    def eat(self):
        print("Eating")
class mammal(Animal):
    def walk(self):
        print("Walking")
class dog(mammal):
    def bark(self):
        print("Barking")
dg = dog()
dg.eat()
dg.walk()
dg.bark()

print("========Hiererchical inheritance=========")
class animal:
    def eat(self):
        print("eating")
class dog(animal):
    def bark(self):
        print("barking")
class cat(animal):
    def meow(self):
        print("meow")
an = animal()
an.eat()
dg = dog()
dg.bark()
ct = cat()
ct.meow()

print("========Method Resolution Order========")
class A:
    def show(self):
        print("Class A")
class B:
    def show(self):
        print("Class B")
class C(A,B):
    pass
c = C()
c.show()
print(C.__mro__)

print("======Polymorphism=====")
class dog:
    def sound(self):
        print("Barking")
class cat:
    def sound(self):
        print("Meow")
animals = [dog(),cat()]
for animl in animals:
    animl.sound()