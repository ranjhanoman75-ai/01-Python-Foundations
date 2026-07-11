print("===========Day 14 =============")
print("===========Professional OOP============")
print("==========Classes and objects=======")
class student:
    def greet(self):
        print("Welcome student")
student1 = student()
student1.greet()

class Dog:
    def bark(self):
        print("Dog barks")
    def bark(self):
        print("Dog1 barks")
dog = Dog()
dog.bark()

dog1 = Dog()
Dog.bark(dog1)

class student:
    def show(self):
        print(self.name)

std1 = student()
std2 = student()
std2.name = "Noman"
std2.show()

class laptop:
    def info(self):
        print("Brand is: ",self.brand)
        print("Ram is: ", self.ram)
hp = laptop()
hp.brand  = "HP"
hp.ram  = "16GB"
hp.info()