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
chek(0)


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

largest_no()


print("========Even or odd===========")

def Even_odd():
    num = int(input("Enter a number: "))
    if num%2==0:
        print("It is even number ")
    else:
        print("It is odd number ")

Even_odd()

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

print("=======Reversing a string========")
def reverse_string(text):
    reverse = ""
    for i in text:
        reverse = i+reverse
    return reverse
string= input("Enter a string: ")
result = reverse_string(string)
print("The reverse string is: ",result)


print("=========To check whether it is palindrome========")
def palindrome(text):
    reverse =""
    for i in text:
        reverse = i+reverse

    if text == reverse:
            print("It is palindrome ")
    else:
            print("It is not palindrome ")
string = input("Enter a string: ")
result = palindrome(string)



print("================Calculator==========")

    

def addition():
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 + num2
        print("After addition: ",result)
        

def subtraction():
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 - num2
        print("After subtracting: ",result)
        

def multiplication():
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 * num2
        print("After Multiplying: ",result)
    

def division():
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if num2 ==0:
             print("Division by zero is not allowed ")
        else:
             result = num1 / num2
             print("After division: ",result)
def exit_program():
     print("Thank you for using Calculator ")      
while True:
        print("1:Addition ")
        print("2:Subtraction ")
        print("3:Multiplication")
        print("4:Division ")
        print("5:Exit ")
        choice = int(input("Enter your choice:(1-5) "))
        if choice==1:
             addition()
        elif choice==2:
             subtraction()
        elif choice==3:
             multiplication()
        elif choice==4:
             division()
        elif choice==5:
             exit_program()
             break
        else: 
             print("Invalide choice ")


        
        



    
