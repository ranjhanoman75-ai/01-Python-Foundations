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
    