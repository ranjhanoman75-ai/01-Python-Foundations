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