#==============================
def greet(name):
    print(name)
greet("Noman")

def greet(name="Noman"):
    print(name)
greet()
greet("guest")

#=================================
def python():
    print("Welcome to python ")
python()

#===================
def sum(a,b):
    return a + b
print(sum(3,4))
#=========================
def add(a,b,c):
    return a + b + c
result = add(3.4,4,7.9)
print(result)
#=======================
def subtract(a,b):
    return a - b
result = subtract(3,5)
print(result)
#===========================
def square(a):
    return a*a
result = square(125)
print(result)
#=====================
def cube(a):
    return a*a*a
print(cube(4))
#======================

def check(num):
    if num > 0:
        print("The number is positive ")
    elif num <0:
        print("The number is negative ")
    else:
        print("The number is zero  ")
print(check(0))