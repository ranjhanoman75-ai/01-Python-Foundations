print("=========Hospital Management System===========")
from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_info(self):
        print("Name of Person: ",self.name)
        print("Age of person: ",self.age)
    @abstractmethod
    def get_role(self):
        pass
    def calculate_payment(self):
        pass
class Patient(Person):
    def display_info(self):
        print("Name of Person: ",self.name)
        print("Age of person: ",self.age)
    def calculate_payment(self,room_charges,medicine_bill):
        Total_Expense=  room_charges+medicine_bill
        print("Total expense of patient: ", Total_Expense)
    def get_role(self):
        print("Its patient")
class Doctor(Person):
    def display_info(self):
        print("Name of Person: ",self.name)
        print("Age of person: ",self.age)
    def calculate_payment(self,salary,bonus):
        return salary+bonus
    def get_role(self):
        print("He is a doctor")
class Nurse(Person):
    def display_info(self):
        print("Name of Person: ",self.name)
        print("Age of person: ",self.age)
    def calculate_payment(self,salary,allowance):
        return salary + allowance
    def get_role(self):
        print("She is a nurse")

        
print("===========Patient Information===============")           
p1 =Patient("Noman",23)
p1.display_info()
p1.calculate_payment(4500,3400)
print("Its role:", p1.get_role())
print("==================Doctor information=============")
dtr = Doctor("Abdul Shakoor",45)
dtr.display_info()
print("Total salary is including bonus:", dtr.calculate_payment(45000,5000))
dtr.get_role()
print("============Nurse Information==============")
nurse = Nurse("Alina ", 22)
nurse.display_info()
print("The total salary with allowance is: " ,nurse.calculate_payment(35000,7000))
nurse.get_role()