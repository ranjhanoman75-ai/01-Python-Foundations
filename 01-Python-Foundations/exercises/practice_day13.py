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