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