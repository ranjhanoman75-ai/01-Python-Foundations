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
print("Amount after deposit: ", b.balance)
