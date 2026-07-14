print("============Day 19================")
print("============Decorators and Pythonic way of setters and getters=======")
class employee:
    def __init__(self):
        self.__salary = 50000
    @property
    def salary(self):
        return self.__salary
emp = employee()
print(emp.salary)