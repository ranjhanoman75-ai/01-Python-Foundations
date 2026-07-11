print("===========Constructors===========")
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Noman",22)

print(student.name)
print(student.age)
print("================Instance Variable===========")
class student:
    def __init__(self , name,age):
        self.name = name
        self.age = age
        print(self.name)
        print(self.age)
s = student("Noman ",22)
s1 = student("Ali raza", 24)

print("========Class Laptop===========")
class laptop:
    def __init__(self,brand,ram):
        self.brand = brand
        self.ram = ram
    def display(self):
        print(self.brand)
        print(self.ram)
hp = laptop("Hp",16)
hp1 = laptop("Dell", 32)
hp.display()
hp1.display()

class student:
    university = "University of Sargodha"
    def __init__(self,name,age,course):
        self.name= name
        self.age = age
        self.course = course
    def display(self):
        print(self.name)
        print(self.age)
        print(self.course)
    def __str__(self):
        return f"Student Name: {self.name}"
s1 = student("Noman",22,"Agentic Ai")
s2 = student("Ali Raza",23,"Ai engineer")
print(s1.university)
s1.display()
s2.university = "Fast University"
print(s2.university)
s2.display()   
print(s1)
print(s2)

print("============Destructor============")
class student:
    def __del__(self):
        print("Object Destroyed")
s = student()
del s

    