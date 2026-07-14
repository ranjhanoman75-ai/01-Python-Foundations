print("============Day 19================")
print("============Decorators and Pythonic way of setters and getters=======")
print("=====Property Decorator==========")
class employee:
    def __init__(self):
        self.__salary = 50000
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,amount):
        if amount>0:
            self.__salary = amount
        else:
            print("Invalid amount")
emp = employee()
emp.salary = 60000
print(emp.salary)

class student:
    def __init__(self):
        self.__marks = 67
    @property 
    def marks(self):
        return self.__marks
    @marks.setter
    def marks(self,value):
        if value >0:
            self.__marks = value
        else:
            print("Invalid marks")
s = student()
s.marks = 89
print(s.marks)

class employee:
    def __init__(self):
        self.__salary = 23000
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,new_Salary):
        if new_Salary>15000:
            self.__salary = new_Salary
        else:
            print("Invalid salary")
emp = employee()
emp.salary = 45000
print(emp.salary)

class Bank:
    def __init__(self):
        self.__balance= 3000
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,new_amount):
        if new_amount >0:
            self.__balance += new_amount
            print("Amount that you want to deposit: ",new_amount)
            print("Amount deposited successfully")
        else:
            print("Invalid amount")
b = Bank()
print("Your current balance is: ", b.balance)
b.balance = 4000
print("Balance after deposit: ", b.balance)


class circle:
    def __init__(self,radius):
        self.__radius = radius
    @property
    def calculate_area(self):
        return self.__radius*2*3.14
c = circle(4)
print(c.calculate_area)

class car:
    def __init__(self):
        self.__speed = 180
    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self,new_Speed):
        if new_Speed >250:
            print("invalid speed")
        else:
            self.__speed = new_Speed
            print("Speed set successfully")
c = car()
print("Speed before setting the speed: ", c.speed)
c.speed = 200
print("Speed after setting the speed: ", c.speed)

print("========Employee Payroll Management System==========")
class Employee:
    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self.__department = department
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            print("Name should not be empty")
        else:
            self.__name = value
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 25000:
            self.__salary = new_salary
        else:
            print("Invalid Salary")
    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        if value.strip() == "":
            print("Department cannot be empty")
        else:
            self.__department = value
    def display_info(self):
        print("Name      :", self.name)
        print("Salary    :", self.salary)
        print("Department:", self.department)


emp = Employee("Noman", 36000, "Finance")

emp.display_info()

print()

emp.salary = 45000
emp.department = "IT"

emp.display_info()