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


class student:
    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        if marks > 0 and marks <100:
            self.__marks = marks
        else:
            print("Invalid Marks! ")
s = student("Noman ",89)
s.set_marks(12)
print(s.get_marks())

print("=========Bank balance========")
class Bank:
    def __init__(self,balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount>0 :
            self.__balance +=amount
            print("Amount deposited successfully")
        else:
            print("Invalid deposit amount")

    def withdraw(self,amount):
        print("Your current balance is :",self.__balance)
        if amount > self.__balance:
            self.__balance -= amount
            print("Your remaining balance is: ",self.__balance)
        else:
            print("Invalid input amount")

bank = Bank(4500)
bank.deposit(500)
print(bank.get_balance())
            
