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

print("==========super()========")
class animal:
    def sound(self):
        print("Animal sound")
    def eat(self):
        print("Animal eats")
class son(animal):
    def sound(self):
        super().sound()
        super().eat()
        print("Bark")
dg = son()
dg.sound()

print("========constructor inheritence========")
class animal:
    def __init__(self,name):
        self.name = name
class dog(animal):
    pass
dg = dog("Tommy")
print(dg.name)

print("======Child Constructor======")
class teacher:
    def __init__(self,name):
        self.name = name
class student(teacher):
    def __init__(self,name,course):
        super().__init__(name)
        self.course = course
s1 = student("Noman","Agentic Ai")
print(s1.name)
print(s1.course)