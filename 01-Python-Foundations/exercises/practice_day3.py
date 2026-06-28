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
