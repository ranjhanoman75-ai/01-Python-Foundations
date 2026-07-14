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
