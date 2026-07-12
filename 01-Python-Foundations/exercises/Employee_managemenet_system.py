print("=========== Company Employee Management System ===========")
print("============== Class Based System =================")

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"Employee Name : {self.name}")
        print(f"Employee ID   : {self.employee_id}")
        print(f"Salary        : {self.salary}")

    def __str__(self):
        return f"Employee(Name={self.name}, ID={self.employee_id}, Salary={self.salary})"


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department, bonus):
        super().__init__(name, employee_id, salary)
        self.department = department
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus

    def display_info(self):
        super().display_info()

        print(f"Department    : {self.department}")
        print(f"Bonus         : {self.bonus}")
        print(f"Gross Salary  : {self.calculate_salary()}")

emp = Employee("Noman", 34, 45000)
emp.display_info()

print("-" * 40)
manager = Manager("Ali", 23, 50000, "Finance", 4000)
manager.display_info()