print("==========Day 13 =====Advanced Functions=======")
def add(*numbers):
    print(numbers)
add(1,2,3,4)

def add(*numbers):
    total = 0
    for num in numbers:
        total += num

    return total
print(add(1,2,3))
print(add(1,35,5,6))
print(add(100,199))

def student_info(name, *marks):
    total = 0
    print(name)
    print(marks)
    for i in marks:
        total += i
    
    return total

# call student_info and print the returned total
result = student_info("Noman", 26, 45, 63)

print("Sum of marks: ",result)

print("=========**kwargs========")
def info(**data):
    print(data)
    print(data["name"])

info(name ="Noman", age = 22, Course = "Ai engineer")


def info(**data):
     
    for key ,value in data.items():
        print(key,value)
info(name="Noman", age = 22)


print("========Lambda Function=========")
print("Normal Function")
def square(x):
    return x*x
print(square(5))

print("====Lambda Function====")
Square = lambda x: x*x
print(Square(5))

add = lambda a,b:a+b
print(add(2,4))

students = [
    ("Ali",85),
    ("Bilal",70),
    ("Noman",95)
]

students.sort(key=lambda x:x[1])

print(students)

print("======Largest number using *args======")

def info(*data):
    if len(data) == 0:
        return "No data found"
    largest_num = data[0]
    for num in data:
        if num > largest_num:
            largest_num = num
        
    return largest_num
print(info(1,5,6,78,32))
    

def count(n):
    if n==0:
        return
    print(n)

    count(n-1)

count(5)

def factorial(n):
    if n==1:
        return 1
    
    return  n* factorial(n-1)
print(factorial(5))


def num():
    x=0
    print(x)

num()

print("=======global variable=======")
name = "Noman "
def show():
    print(name)

show()
print("=====Global Keyword=======")
count = 0
def show():
    global count
    count += 1
show()
print(count)

def outer():
    print("outer ")
    def inner():
        print("inner")
    inner()
outer()

print("========Employee details using **kwargs=====")
def employee_info(**data):
    print(data)
    for key , value in data.items():
        print(key, value)
employee_info(name = "Noman ", age = 22, Salary = 25000)

print("=====Student profile===========")
def student_profile(**data):
    print(data)
    for key , value in data.items():
        print(key, value)
employee_info(name = "BABA ", age = 22, Course_Fee = 35000)



print("==========Employee Payroll system===========")
print("=========Mini Project=========")

def calculate_salary(base_salary, *allowance):
    gross_Salary = base_salary
    for amount in allowance:
        gross_Salary+=amount

    return gross_Salary


def calculate_tax(salary):
    if salary >= 100000:
        tax = salary * 0.15
    elif salary >= 50000:
        tax = salary * 0.10
    else:
        tax = salary * 0.05

    return tax 

name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")

basic_salary = float(input("Enter Basic Salary: "))

gross_salary = calculate_salary(
    basic_salary,
    5000,   
    3000,   
    2000    
)

tax = calculate_tax(gross_salary)
net_salary = gross_salary - tax

print("\n====== Employee Details ======")
print("Employee Name :", name)
print("Employee ID   :", emp_id)
print("Gross Salary  :", gross_salary)
print("Tax           :", tax)
print("Net Salary    :", net_salary)

