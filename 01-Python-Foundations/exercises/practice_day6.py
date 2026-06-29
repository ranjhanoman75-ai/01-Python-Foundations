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

def chek(num):
    if num > 0:
        print("The number is positive ")
    elif num <0:
        print("The number is negative ")
    else:
        print("The number is zero  ")
print(chek(0))


print("==========larger no.======")
def largest_no():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter the second number: "))
    if num1>num2:
        print("The largest number is: ",num1)
    elif num2>num1:
        print("The largest number is: ",num2)
    else: 
        print("Both are equals! ")

print(largest_no())


print("========Even or odd===========")

def Even_odd():
    num = int(input("Enter a number: "))
    if num%2==0:
        print("It is even number ")
    else:
        print("It is odd number ")

print(Even_odd())

print("======Factorial of number========")
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact
num = int(input("Enter a number: "))
result = factorial(num)
print("The factorial of ", num ,"is: ", result)


print("=======to count vowels in string==========")
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for i in text:
        if i in vowels:
            count+=1
    return count
string = input("Enter a string: ")
result = count_vowels(string)
print("The count of vowels in this strings are: ",result)

    
