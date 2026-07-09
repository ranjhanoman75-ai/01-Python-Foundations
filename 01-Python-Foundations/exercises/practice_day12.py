def greet(name):
    print("hello",name)
greet("Noman")

def student_info(name,age,course):
    print("Name: ",name)
    print("Age: ",age)
    print("Course: ",course)
student_info("Noman",22,"Agentic Ai")


def rectangle_area(length,width):
    return length*width
print(rectangle_area(23,34))

def info(name="Noman", age =22):
    print(name)
    print(age)
info()

def exponent(number,exponent=2):
    return number*exponent
print(exponent(3))

def calc(a,b):
    add = a+b
    sub = a-b
    
    return add ,sub
addition, subtraction = calc(2,4)
print(addition)
print(subtraction)

print("=========function calling another function=========")
def square(number):
    return number*number
def show_square(number):
    result = square(number)
    print(result)
show_square(4)

def add(a,b):
    """
    Returns the sum of two numbers.
    """
    return a + b
print(add.__doc__)