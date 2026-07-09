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

print("=========Mini Project========")
def input_marks():
    marks = []
    for i in range(5):
        mark = float(input(f"Enter marks for Subject {i+1}: "))
        marks.append(mark)
    return marks


def total_marks(marks):
    return sum(marks)


def percentage(total, max_marks):
    return (total / max_marks) * 100


def grade(percent):
    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 70:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    else:
        return "F"


def display_result():
    marks = input_marks()
    total = total_marks(marks)
    max_marks = len(marks) * 100
    percent = percentage(total, max_marks)
    student_grade = grade(percent)

    print("\n----- Result -----")
    print("Marks:", marks)
    print("Total Marks:", total)
    print(f"Percentage: {percent:.2f}%")
    print("Grade:", student_grade)


display_result()
