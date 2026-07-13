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