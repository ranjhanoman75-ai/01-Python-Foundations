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
print("============program 4============")
dict = {
    "Name": "Noman",
    "age": 33
}
iteratr = iter(dict)
print(iteratr)
while True:
    try:
        keys = next(iteratr)
        print(keys)
    except StopIteration:
        break
print("=========Program 5===========")
list = [34,53,34,74,75]
for num in list:
    print(num)
iterator = iter(list)
print(iterator)
while True:
    try:
        item  = next(iterator)
        print(item)
    except StopIteration:
        break
print("=============Program 6===============")
data= "Python"
iterator = iter(data)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
print("============Custom Iterator==========")
class Counter:
    def __init__(self):
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <=5:
            value = self.current
            self.current +=1
            return value
        else:
            raise StopIteration
counter = Counter()
for i in counter:
    print(i)

print("============ 2 Custom iterator============")
class Counter:
    def __init__(self):
        self.current = 10
    def __iter__(self):
        return self
    def __next__(self):
        for i in range(10,60):
            if self.current <=60:
                value =  self.current
                self.current +=10
                return value
            else:
                raise StopIteration
counter = Counter()
for i in counter:
    print(i)

class LetterIterator:

    def __init__(self):
        self.letters = ["A", "B", "C", "D", "E"]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index < len(self.letters):
            value = self.letters[self.index]
            self.index += 1
            return value

        raise StopIteration
letters = LetterIterator()

for letter in letters:
    print(letter)