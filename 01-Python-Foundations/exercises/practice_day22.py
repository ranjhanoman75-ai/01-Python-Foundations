print("============Day 22 =============")
print("===============Generators================")
def numbers():
    yield 1
    yield 2
    yield 3
gen = numbers()
print(next(gen))
print(next(gen))
print(next(gen))

print("===========2 program========")
def num():
    for i in range(5):
        yield  {i}
print(num())
d = num()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))

print("=========3 program=============")
def num():
    data = [2,4,52,543,6,7]
    for i in data:
        if i%2 ==0:
            print("Its even number")
            yield i 
        else:
            print("Its odd number")
            yield i

for value in num():
    print(value)


