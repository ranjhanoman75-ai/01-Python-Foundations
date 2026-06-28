age = int(input("Enter your age: "))
if age>= 18:
    print("Eligible for voting.")
else:
    print("Not eligible for voting. ")

print("===========program 2==============")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
Nationality = "Pakistani"
if age >=18 and Nationality == "Pakistani":
    print("Hello " + name + " you are eligible for voting. ")
else:
    print("Hello " + name + " you are not eligible for voting. ")

print("========Program 3=========")
num = int(input("Enter a number: "))
if num>= 0:
    print("The number is positive .")
elif num<0:
    print("The number is negative. ")
else:
    print("The number is zero.")


print("========program 4========")

num = int(input("Enter a number: "))
if num%2 ==0:
    print("The number is even. ")
else:
    print("The number is odd. ")



print("=====program 5=======")
num = int(input("Enter a number: "))
if num%3==0 and num%5==0:
    print("The number is divisible by 3 and 5.")
else: 
    print("The number is not divisible by 3 and 5. ")


print("=========program 6=======")
username = input("Enter your username: ")
password = int(input("Enter your password: "))
if username=="admin" and password ==12345:
    print("Login successfull. ")
else: 
    print("Login failed. ")


print("======program 7=======")
marks = int(input("Enter your marks: "))
if marks>= 90:
    print("Grade A ")
elif marks>=80:
    print("Grade B ")
elif marks>=70:
    print("Grade C ")
elif marks>=60:
    print("Grade D ")
elif marks<=60:
    print("Failed")
else: 
    print("Invalid marks. ")
    
