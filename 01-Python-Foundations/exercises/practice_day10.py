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


numbers = [1,2,4,4]

try:
    print(numbers[6])
except IndexError:
    print("Index does not exist")


marks = {
    "Ali" : 56
}
try: 
    print(marks["Noman"])
except KeyError:
    print("Key does not exist")


try:
    file = open("01-Python-Foundations/exercises/test.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("File closed Successfully ")


print("====== Custom Exception ======")

class SalaryError(Exception):
    def __init__(self, salary):
        super().__init__(f"Salary too low: {salary}")

salary = 12000

try:
    if salary < 25000:
        raise SalaryError(salary)

except SalaryError as e:
    print(e)

print("========file write=====")
with open ("01-Python-Foundations/exercises/test.txt", "r") as file:
    print(file.read())

with open ("01-Python-Foundations/exercises/test.txt", "a") as file:
    file.write("Hello Ai engineer\n")
    file.write("Noman is a professional Ai engineer\n")





while True:
    print("1: Add student Record: ")
    print("2: Display Student Record: ")
    print("3:Exit program: ")
    choice = int(input("Enter your choice: (1-3)"))
    if choice == 1:
        with open ("01-Python-Foundations/exercises/student_record.txt", "a") as file:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            course = input("Enter your course: ")
            file.write(f"Name: {name}, Age: {age}, Course: {course}\n")
            print("Record added successfully!")
    elif choice == 2:
        with open ("01-Python-Foundations/exercises/student_record.txt", "r") as file:
            print(file.read())
    elif choice == 3: 
        print("Thank you for using this program!")
        break 
    else:
        print("Invalid choice! please enter choice (1-3)")
        break

