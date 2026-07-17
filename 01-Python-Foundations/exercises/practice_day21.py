print("===============Iterators=================")
print("==========With Loop==============")
numbers = [1,23,44,43,54]
for num in numbers:
    print(num,end=",")

print("=============1 program===========")
numbers = [23,42,524,635,64]
iterator = iter(numbers)
print(iterator)
print(next(iterator))
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
print("=============Program 2===============")
Tuple = (2,4,5,2,5)
iterator = iter(Tuple)
print(iterator)
while True:
    try:
        Num = next(iterator)
        print(Num)
    except StopIteration:
        break

print("===========Program 3===============")
string = "Noman Ali"
iterator = iter(string)
print(iterator)
while True:
    try:
        str = next(iterator)
        print(str)
    except StopIteration:
        break