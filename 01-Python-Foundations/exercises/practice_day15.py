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
