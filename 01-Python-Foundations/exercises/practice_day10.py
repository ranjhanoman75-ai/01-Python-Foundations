age = int(input("Enter your age: "))
if age < 18:
    raise ValueError("Age must be greater than 18 ")
else:
    print("You are eligible to vote")

try:
    number =  int(input("Enter a number: "))
    number2 = int(input("Enter a number: "))
    result = number / number2
    print("Result: ",result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter valid numbers")