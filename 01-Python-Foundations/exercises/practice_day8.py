tuples = (1,2,3,5)
print(tuples)


data  = ("Noman",22,"Lahore")
print(data)
name, age,city = data
print(name)
print(age)
print(city)
print((name)*10)

print("======program 3========")
t = ("Noman",22,"Jhang")
print(t[:1])
print(t[-1])

print("=====program 4====")
numbers = (1,2,3,4,5)
print(len(numbers))


print("========program 5========")
no = (23,53,52,67)
for n in no:
    print(no)
if 21 in no:
    print("found")
else:
    print("Not found")

print("======program 6========")
n = (12,42,42,52,53)
print(n.index(42))
print(n.count(42))

print("======Program 7======")
a =  ("Ali","Noman")
b = ("Mukurram","Bilal")
t= a+b
print(t)
for i in range(1,2):
    print(t)

print("=====program 8========")
names = ("Ali",22,"Jhang" )
print(names)

name, age , city  = names
print(name)
print(age)
print(city)

print("========Program 9=======Mini challange=======")
names =  ("Noman",24,"BSSE")
name, age , Degree = names
print("Name : ",name)
print("Age : ", age)
print("Degree: ", Degree)


print("==========part 2 ===Sets===========")
numbers = {1,2,2,42,53,53,53,2}
print(numbers)


name = {"Noman", "Saima","Ali"}
name.add("Bilal")
for names in name:
    print(names)
name.discard("baba")
name.remove("Ali")
name.pop()

print(name)
print(len(name))
if "Noman" in name:
    print("found")
else:
    print("not found")


print("=======program 2========")
numbers = {1,2,4}
number= {2,42,3}
print(numbers|number)
print(numbers.union(number))
