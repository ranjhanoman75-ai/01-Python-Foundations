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

class Book:
    def info(self,author_name ,title,price):
        self.author_name = author_name
        self.title = title
        self.price = price
    def show(self):
        print("Author name is: ",self.author_name)
        print("Title of Book is: ",self.title)
        print("The price of book is: ",self.price)
b1 = Book()
b1.info("John Sen","Machine Learning",230)
b1.show()

class employee:
    def show(self ,name:str,salary:int):
        print("Name is: ",name)
        print("Salary is: ",salary)
emp1 = employee()
emp1.show("Noman",150000)

class mobile:
    def display(self):
        print("Mobile is: ",self.brand)
mb1= mobile()
mb1.brand = "vivoy31"
mb1.display()

class circle:
    def area(self, r):
        return 3.14*r*r
c1= circle()
print(c1.area(12))

class calculator:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b
cal = calculator()
print(cal.add(12,43))
print(cal.subtract(144,24))
print(cal.multiply(14,6))
print(cal.divide(12,3))        