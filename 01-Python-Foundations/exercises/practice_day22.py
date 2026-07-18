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

    
