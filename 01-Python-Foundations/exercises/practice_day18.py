print("=================Day 18=========")
print("===Encapsulation========")
class animal:
    def __init__(self):
        self.__salary = 50000
an = animal()
print(an._animal__salary)

print("=========Getter===To read private data====")
class employee:
    def __init__(self):
        self.__salary = 50000
    def get_salary(self):
        return self.__salary
emp = employee()
print(emp.get_salary())

print("====Setters======TO update the private data===")
class employee:
    def __init__(self):
        self.__salary = 50000
    def set_salary(self,salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary
emp = employee()
emp.set_salary(80000)
print(emp.get_salary())

