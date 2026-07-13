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