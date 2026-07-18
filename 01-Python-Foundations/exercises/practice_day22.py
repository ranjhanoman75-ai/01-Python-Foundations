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
for i in range(1,5):
    print(i)