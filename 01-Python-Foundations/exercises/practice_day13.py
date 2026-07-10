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



    